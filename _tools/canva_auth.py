# -*- coding: utf-8 -*-
"""
Canva Connect API OAuth 2.0 PKCE Authentication
Run once to get access_token, then store it.
"""
import base64
import hashlib
import http.server
import json
import os
import secrets
import subprocess
import sys
import threading
import urllib.parse
import webbrowser

try:
    import requests
except ImportError:
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "requests", "-q"],
        check=False,
    )
    import requests

# Load from .env
from pathlib import Path

env_path = Path(__file__).parent.parent / '.env'
env = {}
if env_path.exists():
    for line in env_path.read_text().splitlines():
        if '=' in line and not line.startswith('#'):
            k, v = line.split('=', 1)
            env[k.strip()] = v.strip()

CLIENT_ID = env.get('CANVA_CLIENT_ID', os.getenv('CANVA_CLIENT_ID', ''))
CLIENT_SECRET = env.get('CANVA_CLIENT_SECRET', os.getenv('CANVA_CLIENT_SECRET', ''))
REDIRECT_URI = 'http://127.0.0.1:3000/callback'
TOKEN_FILE = Path(__file__).parent.parent / '.cex' / 'brand' / 'canva_token.json'

if not CLIENT_ID or not CLIENT_SECRET:
    print("ERROR: CANVA_CLIENT_ID and CANVA_CLIENT_SECRET must be in .env")
    sys.exit(1)

# PKCE: generate code_verifier and code_challenge
code_verifier = secrets.token_urlsafe(64)[:128]
code_challenge = base64.urlsafe_b64encode(
    hashlib.sha256(code_verifier.encode()).digest()
).decode().rstrip('=')

# Scopes needed for Content Factory
SCOPES = ' '.join([
    'design:meta:read',
    'design:content:read', 
    'design:content:write',
    'design:permission:read',
    'folder:read',
    'folder:write',
    'asset:read',
    'asset:write',
    'brandtemplate:meta:read',
    'brandtemplate:content:read',
    'profile:read',
    'comment:read',
    'comment:write',
])

# Build authorization URL
auth_url = (
    "https://www.canva.com/api/oauth/authorize?"
    f"code_challenge={code_challenge}&"
    "code_challenge_method=s256&"
    f"scope={urllib.parse.quote(SCOPES)}&"
    "response_type=code&"
    f"client_id={CLIENT_ID}&"
    f"redirect_uri={urllib.parse.quote(REDIRECT_URI)}"
)

# Callback server to catch the auth code
auth_code = None
server_done = threading.Event()

class CallbackHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        
        if 'code' in params:
            auth_code = params['code'][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>CEX Canva Auth OK!</h1><p>Pode fechar esta janela.</p></body></html>')
            server_done.set()
        else:
            error = params.get('error', ['unknown'])[0]
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f'<html><body><h1>Error: {error}</h1></body></html>'.encode())
            server_done.set()
    
    def log_message(self, format, *args):
        pass  # Suppress logs

print("=" * 60)
print("CEX Canva OAuth Authentication")
print("=" * 60)
print()
print("1. Opening browser for Canva authorization...")
print("2. Authorize the CEX app when prompted")
print("3. You'll be redirected back here automatically")
print()

# Start callback server
server = http.server.HTTPServer(('localhost', 3000), CallbackHandler)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

# Open browser
webbrowser.open(auth_url)
print("Waiting for authorization... (browser should open)")
print("If not, open this URL manually:")
print(f"{auth_url[:100]}...")

# Wait for callback
server_done.wait(timeout=120)
server.shutdown()

if not auth_code:
    print("\nERROR: No authorization code received (timeout or error)")
    sys.exit(1)

print("\n[OK] Authorization code received!")
print("Exchanging for access token...")

# Exchange code for token
token_response = requests.post(
    'https://api.canva.com/rest/v1/oauth/token',
    data={
        'grant_type': 'authorization_code',
        'code': auth_code,
        'code_verifier': code_verifier,
        'redirect_uri': REDIRECT_URI,
    },
    auth=(CLIENT_ID, CLIENT_SECRET),
    headers={'Content-Type': 'application/x-www-form-urlencoded'}
)

if token_response.status_code != 200:
    print(f"ERROR: Token exchange failed: {token_response.status_code}")
    print(token_response.text)
    sys.exit(1)

token_data = token_response.json()

# Save token
TOKEN_FILE.parent.mkdir(parents=True, exist_ok=True)
TOKEN_FILE.write_text(json.dumps(token_data, indent=2))

print("\n[OK] Access token obtained!")
print(f"   Token saved to: {TOKEN_FILE}")
print(f"   Expires in: {token_data.get('expires_in', '?')} seconds")
print(f"   Scopes: {token_data.get('scope', '?')}")

# Also add to .env for MCP
access_token = token_data.get('access_token', '')
refresh_token = token_data.get('refresh_token', '')

with open(env_path, 'a', encoding="utf-8") as f:
    f.write(f"\nCANVA_ACCESS_TOKEN={access_token}\n")
    if refresh_token:
        f.write(f"CANVA_REFRESH_TOKEN={refresh_token}\n")

print("\n[OK] Tokens added to .env")
print("   Canva Connect API is ready!")
