---
id: n02_kc_email_html_responsive
kind: knowledge_card
pillar: P01
title: Email HTML Responsive
domain: N02_marketing / Email
tags: [email, html, responsive, mjml, react-email, dark-mode, mso, inline-css]
quality: 9.0
source: react.email, caniemail.com, mjml.io
created: 2026-04-01
---

# KC: Email HTML Responsive

## Core Mental Model

Email is NOT a browser. Render engines: Outlook (Word/MSHTML), Gmail (strips `<head>`),
Apple Mail (WebKit), Yahoo (old Gecko). Design for the worst (Outlook) first.
Max-width: **600px**. Always inline CSS. Test in Litmus or Email on Acid.

---

## Table Layout (Outlook-safe foundation)

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <!--[if mso]>
  <noscript><xml><o:OfficeDocumentSettings>
    <o:PixelsPerInch>96</o:PixelsPerInch>
  </o:OfficeDocumentSettings></xml></noscript>
  <![endif]-->
  <style>
    /* Reset */
    body, table, td, p, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
    table, td { border-collapse: collapse !important; mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
    img { border: 0; line-height: 100%; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; }

    /* Responsive */
    @media only screen and (max-width: 600px) {
      .wrapper { width: 100% !important; }
      .column { display: block !important; width: 100% !important; }
      .hide-mobile { display: none !important; }
      .show-mobile { display: block !important; }
    }
  </style>
</head>
<body style="margin:0; padding:0; background-color:#f4f4f4;">

  <!-- Outer wrapper -->
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>
      <td align="center" style="padding: 40px 20px;">

        <!-- Email container: max 600px -->
        <table role="presentation" class="wrapper" width="600" cellpadding="0" cellspacing="0" border="0"
               style="max-width:600px; background:#ffffff;">
          <tr>
            <td style="padding: 32px 40px; font-family: Arial, sans-serif; font-size: 16px; color: #333333;">
              <!-- content here -->
            </td>
          </tr>
        </table>

      </td>
    </tr>
  </table>
</body>
</html>
```

---

## Inline CSS Rules

Gmail strips `<head>` styles. **Always inline critical CSS.**

```html
<!-- Safe inline properties -->
<p style="
  font-family: Arial, Helvetica, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: #333333;
  margin: 0 0 16px 0;
  padding: 0;
">Text</p>

<a href="https://example.com" style="
  display: inline-block;
  padding: 12px 24px;
  background-color: #007bff;
  color: #ffffff !important;
  font-family: Arial, sans-serif;
  font-size: 16px;
  font-weight: bold;
  text-decoration: none;
  border-radius: 4px;
">CTA Button</a>
```

**Inlining tools**: `juice` (npm), `premailer` (Ruby), React Email (built-in).

---

## MSO (Microsoft Office) Conditional Comments

```html
<!-- Outlook-only table fix for multi-column -->
<!--[if mso]>
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td width="280" valign="top">
<![endif]-->
<div style="display:inline-block; width:280px; vertical-align:top;">
  <!-- Left column content -->
</div>
<!--[if mso]>
    </td>
    <td width="280" valign="top">
<![endif]-->
<div style="display:inline-block; width:280px; vertical-align:top;">
  <!-- Right column content -->
</div>
<!--[if mso]>
    </td>
  </tr>
</table>
<![endif]-->

<!-- Outlook button fix (VML) -->
<!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"
  href="https://example.com" style="height:48px; v-text-anchor:middle; width:200px;"
  arcsize="8%" strokecolor="#007bff" fillcolor="#007bff">
  <w:anchorlock/>
  <center style="color:#ffffff; font-family:sans-serif; font-size:16px; font-weight:bold;">
    Clique Aqui
  </center>
</v:roundrect>
<![endif]-->
<![if !mso]>
<a href="https://example.com" style="...">Clique Aqui</a>
<![endif]>
```

---

## Fluid-Hybrid Layout

Works in Gmail (no media query support) AND Outlook.

```html
<!-- Two columns that stack on mobile via inline-block trick -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td align="center">
      <!-- Ghost table for Outlook -->
      <!--[if mso]><table><tr><td width="280"><![endif]-->
      <div style="display:inline-block; width:100%; max-width:280px; vertical-align:top;">
        <!-- Column 1 -->
      </div>
      <!--[if mso]></td><td width="280"><![endif]-->
      <div style="display:inline-block; width:100%; max-width:280px; vertical-align:top;">
        <!-- Column 2 -->
      </div>
      <!--[if mso]></td></tr></table><![endif]-->
    </td>
  </tr>
</table>
```

---

## Dark Mode Email

```css
/* In <head> style block */
@media (prefers-color-scheme: dark) {
  body, .email-body { background-color: #1a1a2e !important; }
  .email-container { background-color: #16213e !important; }
  p, h1, h2, h3, li { color: #e0e0e0 !important; }
  a { color: #7eb3ff !important; }
  .btn { background-color: #0066cc !important; }
}

/* Gmail dark mode (data-ogsc) */
[data-ogsc] body { background-color: #1a1a2e !important; }
[data-ogsc] .email-container { background-color: #16213e !important; }
[data-ogsc] p { color: #e0e0e0 !important; }
```

**Images for dark mode:**
```html
<!-- Show/hide different images for dark mode -->
<img src="logo-light.png" class="light-mode-img" alt="Logo"
     style="display:block;" width="150" />
<img src="logo-dark.png" class="dark-mode-img" alt="Logo"
     style="display:none;" width="150" />
```
```css
@media (prefers-color-scheme: dark) {
  .light-mode-img { display: none !important; }
  .dark-mode-img { display: block !important; }
}
```

---

## Client Support Matrix (2025)

| Feature | Gmail | Apple Mail | Outlook | Yahoo |
|---|---|---|---|---|
| `<head>` styles | Strip | Full | Partial | Partial |
| Media queries | No | Yes | No | Yes |
| CSS variables | No | Yes | No | No |
| Flexbox | No | Yes | No | Partial |
| CSS Grid | No | Yes | No | No |
| `border-radius` | Yes | Yes | No (VML) | Yes |
| `background-image` | Yes | Yes | No | Yes |
| Web fonts | No | Yes | No | No |
| Dark mode | `data-ogsc` | `prefers-color-scheme` | Limited | No |
| SVG | No | Yes | No | No |

**Key rule**: Use tables + inline CSS for 99% compatibility. Enhance progressively.

---

## MJML

Declarative markup compiled to cross-client HTML.

```xml
<mjml>
  <mj-head>
    <mj-attributes>
      <mj-all font-family="Arial, sans-serif" />
      <mj-text font-size="16px" color="#333333" line-height="1.5" />
    </mj-attributes>
    <mj-style>
      .custom-link { color: #007bff !important; }
    </mj-style>
  </mj-head>

  <mj-body background-color="#f4f4f4">
    <mj-section background-color="#ffffff" padding="32px 40px">
      <mj-column>
        <mj-image src="https://cdn.example.com/logo.png" width="150px" alt="Logo" />
        <mj-text font-size="24px" font-weight="bold" padding-top="24px">
          Titulo do Email
        </mj-text>
        <mj-text>
          Corpo do email com <strong>negrito</strong> e
          <a href="https://example.com" class="custom-link">link</a>.
        </mj-text>
        <mj-button background-color="#007bff" href="https://example.com"
                   padding="12px 24px" font-size="16px">
          Clique Aqui
        </mj-button>
      </mj-column>
    </mj-section>
  </mj-body>
</mjml>
```

**CLI**: `npx mjml input.mjml -o output.html`

---

## React Email

Component-based, TypeScript-first, outputs email-compatible HTML.

```tsx
import {
  Html, Head, Body, Container, Section, Text, Button, Img, Hr, Preview
} from '@react-email/components';

export default function WelcomeEmail({ name }: { name: string }) {
  return (
    <Html lang="pt">
      <Head />
      <Preview>Bem-vindo ao CODEXA, {name}!</Preview>
      <Body style={{ backgroundColor: '#f4f4f4', fontFamily: 'Arial, sans-serif' }}>
        <Container style={{ maxWidth: '600px', margin: '40px auto', backgroundColor: '#fff', padding: '40px' }}>

          <Img src="https://cdn.example.com/logo.png" width={150} alt="Logo" />

          <Text style={{ fontSize: '24px', fontWeight: 'bold', color: '#333' }}>
            Ola, {name}!
          </Text>

          <Text style={{ fontSize: '16px', lineHeight: '1.5', color: '#555' }}>
            Seu cadastro foi confirmado. Acesse sua conta agora.
          </Text>

          <Button
            href="https://app.example.com/login"
            style={{
              backgroundColor: '#007bff',
              color: '#ffffff',
              padding: '12px 24px',
              borderRadius: '4px',
              fontSize: '16px',
              fontWeight: 'bold',
              textDecoration: 'none',
            }}
          >
            Acessar Conta
          </Button>

          <Hr style={{ margin: '32px 0', borderColor: '#e0e0e0' }} />

          <Text style={{ fontSize: '12px', color: '#999', textAlign: 'center' }}>
            Voce recebeu este email pois se cadastrou em example.com.
            <a href="https://example.com/unsubscribe" style={{ color: '#999' }}>
              Descadastrar
            </a>
          </Text>
        </Container>
      </Body>
    </Html>
  );
}
```

**Preview server**: `npx react-email dev`
**Render to string**: 
```ts
import { render } from '@react-email/render';
const html = render(<WelcomeEmail name="Joao" />);
```

---

## Checklist

- [ ] Max-width 600px container
- [ ] All CSS inlined (use juice/React Email)
- [ ] MSO conditional comments for multi-column
- [ ] VML button fallback for Outlook
- [ ] Dark mode `@media prefers-color-scheme` styles
- [ ] `role="presentation"` on layout tables
- [ ] Images: explicit width/height attributes
- [ ] Web font fallback stack (Arial/Helvetica)
- [ ] Preview text in `<head>`
- [ ] Tested in Gmail + Apple Mail + Outlook
- [ ] Unsubscribe link (legal requirement BR: LGPD)
- [ ] `lang` attribute on `<html>`
