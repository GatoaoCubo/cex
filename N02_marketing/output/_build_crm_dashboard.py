"""Generate GATO3 CRM Organic Dashboard with real data inlined."""
import json
import os

# Load CRM data
with open('N01_research/output/data/crm_pet_abc.json', encoding='utf-8') as f:
    data = json.load(f)

# Compact
compact = []
for d in data:
    compact.append({
        'cnpj': d.get('cnpj',''),
        'nome': d.get('nome_fantasia','') or d.get('razao_social',''),
        'seg': d.get('segmento',''),
        'sub': d.get('sub_segmento',''),
        'end': d.get('endereco',''),
        'cid': d.get('cidade',''),
        'ring': d.get('ring',''),
        'tel': d.get('telefone',''),
        'wpp': d.get('whatsapp',''),
        'email': d.get('email',''),
        'ig': d.get('instagram',''),
        'web': d.get('website',''),
        'maps': d.get('google_maps_url',''),
        'rat': d.get('google_rating',''),
        'rev': d.get('google_reviews',''),
        'porte': d.get('porte',''),
        'felino': d.get('foco_felino','false'),
        'pot': d.get('potencial_b2b',''),
        'notas': d.get('notas',''),
        'lat': d.get('lat',0),
        'lng': d.get('lng',0),
    })

js_data = 'const CRM_DATA = ' + json.dumps(compact, ensure_ascii=False, separators=(',',':')) + ';\n'

# Read template
with open('N02_marketing/output/_crm_template.html', encoding='utf-8') as f:
    template = f.read()

# Inject data
html = template.replace('/* __CRM_DATA_PLACEHOLDER__ */', js_data)

with open('N02_marketing/output/gato3_crm_organico.html', 'w', encoding='utf-8') as f:
    f.write(html)

size = os.path.getsize('N02_marketing/output/gato3_crm_organico.html')
print(f'OK: {size:,} bytes, {len(compact)} negócios embutidos')
