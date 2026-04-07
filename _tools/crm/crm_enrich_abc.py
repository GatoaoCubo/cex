#!/usr/bin/env python3
"""CRM ABC Full Enrichment -- N01 Research Nucleus
Enriches existing 105 contacts + adds new ones from web research.
"""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JSON_PATH = os.path.join(BASE, "N01_research", "output", "data", "crm_pet_abc.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

idx = {d["nome_fantasia"]: i for i, d in enumerate(data)}

def enrich(name, updates):
    if name not in idx:
        return
    i = idx[name]
    for k, v in updates.items():
        if v and (not data[i].get(k) or data[i][k] in ("", "a_validar")):
            data[i][k] = v
            print(f"  ENRICHED [{i}] {name}.{k}")

def add_new(entry):
    if entry["nome_fantasia"] in idx:
        return
    data.append(entry)
    idx[entry["nome_fantasia"]] = len(data) - 1
    print(f"  ADDED: {entry['nome_fantasia']} ({entry['cidade']})")

T = {
    "cnpj": "", "razao_social": "", "nome_fantasia": "", "segmento": "", "sub_segmento": "",
    "endereco": "", "cidade": "", "ring": "1_abc", "telefone": "", "whatsapp": "", "email": "",
    "instagram": "", "website": "", "google_maps_url": "", "google_rating": "", "google_reviews": "",
    "porte": "", "foco_felino": "false", "potencial_b2b": "", "notas": ""
}

def n(nome, seg, sub, end, cidade, tel, wpp, email, ig, web, porte, foco, pot, notas):
    e = T.copy()
    e.update({"nome_fantasia": nome, "razao_social": nome, "segmento": seg, "sub_segmento": sub,
        "endereco": end, "cidade": cidade, "ring": "1_abc", "telefone": tel, "whatsapp": wpp,
        "email": email, "instagram": ig, "website": web, "porte": porte, "foco_felino": foco,
        "potencial_b2b": pot, "notas": notas})
    return e

# ===== ENRICHMENTS =====
print("=== ENRICHING EXISTING ===")

enrich("For Pet", {"telefone": "(11) 99419-9000", "whatsapp": "(11) 2786-5759",
    "endereco": "Alameda Sao Caetano, 2423", "website": "https://www.forpetsaocaetano.com.br/",
    "instagram": "@forpetsaocaetano"})
enrich("Cobasi", {"telefone": "(11) 4233-8202"})
enrich("CV Santo Andre", {"telefone": "(11) 94019-3990", "whatsapp": "(11) 93932-0960",
    "website": "https://veterinariasantoandre.com.br/", "instagram": "@veterinariasantoandre"})
enrich("VitalVet ABC", {"telefone": "(11) 4438-4655", "website": "https://www.vitalvetabc.com.br/"})
enrich("Pet Shop Pedroso", {"telefone": "(11) 94702-4713", "whatsapp": "(11) 94702-4713",
    "endereco": "Estrada do Pedroso, 943", "instagram": "@espacopet.sa"})
enrich("Cobasi Av. Estados", {"telefone": "(11) 5039-9549",
    "endereco": "Praca Eng. Roldao dos Santos Ferreira, 477"})
enrich("PETPOP SBC", {"endereco": "R. Helena Jacquey, 294 - Rudge Ramos",
    "email": "falecom@petpopsbc.com.br", "website": "https://www.petpopsbc.com.br/"})
enrich("EcoPet", {"instagram": "@ecopetcentrovet", "website": "https://ecopetonline.com.br/"})
enrich("Cao Bernardo", {"whatsapp": "(11) 94006-5777", "website": "https://caobernardo.com.br/"})
enrich("LM Bichinho", {"endereco": "R. Aura, 54 - Rudge Ramos", "website": "https://lmbichinho.com.br/"})
enrich("Pet Shop Rudge", {"endereco": "R. Dourados, 470"})

# Fix PETPOP city
if "PETPOP SBC" in idx:
    data[idx["PETPOP SBC"]]["cidade"] = "Sao Bernardo do Campo"

# ===== NEW SCS =====
print("\n=== NEW SCS ===")

add_new(n("Petlife Sao Caetano", "clinica_vet", "24h",
    "R. Amazonas, 1159 - Oswaldo Cruz", "Sao Caetano do Sul",
    "(11) 4225-1899", "(11) 95028-9537", "petlifesaocaetano@gmail.com",
    "@petlife.saocaetano", "https://petlifesaocaetano.com.br/", "epp", "false", "alto",
    "Vet 24h. Consultas, emergencias, cirurgias, oncologia, internacao."))

add_new(n("Ethicus Hospital Veterinario", "clinica_vet", "hospital_24h",
    "Estrada das Lagrimas, 1843 - Bairro Maua", "Sao Caetano do Sul",
    "(11) 4238-8505", "(11) 97445-5545", "ethicus@ethicus.com.br",
    "@ethicushospital24h", "https://ethicus.com.br/", "medio", "true", "alto",
    "Hospital 24h. Medicina Felina, Neurologia, Oncologia, Ortopedia. Referencia ABC."))

add_new(n("Oriente Clinica Veterinaria", "clinica_vet", "especialidades",
    "R. Oriente, 941 - Barcelona", "Sao Caetano do Sul",
    "(11) 4221-6880", "(11) 97277-2255", "",
    "@oriente.vet", "https://orientevet.com/", "epp", "true", "alto",
    "ESPECIALISTA EM FELINOS. Seg-Sex 9h-19h, Sab 9h-16h. Cardiologia, Oncologia, Nefrologia. MATCH GATO3."))

add_new(n("Hypolittus Vet", "clinica_vet", "especialidades",
    "Av. Vital Brasil Filho, 623 - Osvaldo Cruz", "Sao Caetano do Sul",
    "", "(11) 97090-2518", "contato@hypolittusvet.com.br",
    "@hypolittus.vet", "https://hypolittusvet.com.br/", "epp", "false", "alto",
    "Ortopedia, Fisioterapia, Oncologia, Acupuntura. Seg-Sex 9h-18h, Sab 9h-14h."))

add_new(n("Clinical Pets", "clinica_vet", "clinica_pet",
    "R. Herculano de Freitas, 417 - Fundacao", "Sao Caetano do Sul",
    "(11) 4225-1378", "(11) 99661-7999", "",
    "", "https://www.clinicalpets.com/", "epp", "true", "alto",
    "Clinica + Farmacia + Banho e Tosa + Ozonioterapia."))

add_new(n("Clinica Veterinaria Sao Caetano", "clinica_vet", "clinica",
    "Sao Caetano do Sul", "Sao Caetano do Sul",
    "", "(11) 93354-5454", "",
    "@clinvetsaocaetano", "https://clinvetsaocaetano.com.br/", "me", "false", "medio",
    "Somente agendamento via WhatsApp. Exames, Vacinas, Banho e Tosa."))

add_new(n("WeVets Sao Caetano", "clinica_vet", "hospital",
    "Sao Caetano do Sul", "Sao Caetano do Sul",
    "", "", "",
    "", "https://wevets.com.br/unidade-sao-caetano/", "medio", "false", "alto",
    "Rede de clinicas veterinarias. Unidade ABC."))

add_new(n("Pet e Co.", "pet_shop", "banho_tosa",
    "R. Oswaldo Cruz, 1580 - Santa Paula", "Sao Caetano do Sul",
    "", "(11) 97630-4312", "",
    "@petco.sp", "", "me", "false", "medio",
    "Pet shop + banho e tosa."))

add_new(n("Sao Caetano Pet Shop", "pet_shop", "local",
    "R. Nossa Senhora de Fatima, 619", "Sao Caetano do Sul",
    "(11) 4227-4637", "", "",
    "", "", "me", "false", "medio",
    "Pet shop local tradicional."))

add_new(n("Petz Sao Caetano", "pet_shop", "megaloja",
    "Fundacao", "Sao Caetano do Sul",
    "", "", "",
    "", "https://www.petz.com.br/loja/petz-carrefour-sao-caetano", "grande", "false", "alto",
    "Rede Petz, loja Carrefour Sao Caetano."))

add_new(n("S2 Pets", "pet_shop", "creche_pet",
    "Rua Amazonas, 720", "Sao Caetano do Sul",
    "", "", "",
    "@s2petss", "", "me", "false", "medio",
    "Pet shop + creche."))

add_new(n("Sao Francisco Pet Center", "hotel_pet", "hotel_daycare",
    "Sao Caetano do Sul", "Sao Caetano do Sul",
    "", "", "",
    "@saofrancisco980", "", "me", "false", "medio",
    "Hotel, DayCare, Pet Walk, Banho e Tosa. +1000m2."))

add_new(n("Woofy Pet Store", "banho_tosa", "premium",
    "Sao Caetano do Sul", "Sao Caetano do Sul",
    "", "", "",
    "@woofypetstore", "", "me", "false", "medio",
    "Sem gaiolas. Trimming e tosas especializadas."))

add_new(n("Entre Patas Day Care", "hotel_pet", "daycare",
    "Av. Presidente Kennedy, 1435", "Sao Caetano do Sul",
    "(11) 4318-3233", "(11) 99379-9852", "",
    "", "https://entrepatasdaycare.com.br/", "me", "false", "medio",
    "Daycare, Banho e Tosa, Vet, Pet Shop, Natacao. 320m2."))

add_new(n("Mon Petit Cantinho do Banho", "banho_tosa", "local",
    "R. Maceio, 811 - Barcelona", "Sao Caetano do Sul",
    "(11) 4226-1396", "(11) 96596-9858", "",
    "", "", "me", "false", "medio",
    "Banho e tosa local, bairro Barcelona."))

add_new(n("Pet Family ABC", "hotel_pet", "creche_hotel",
    "R. Marina, 1490 - Santa Maria", "Sao Caetano do Sul",
    "(11) 99519-6375", "", "",
    "", "https://petfamilyabc.com.br/", "me", "false", "medio",
    "Creche seg-sex 6:30-18:30, Hotel todos os dias. Vet incluido."))

add_new(n("Pepetos", "hotel_pet", "creche_hotel",
    "Estrada das Lagrimas, 1170 - Jardim Sao Caetano", "Sao Caetano do Sul",
    "(11) 4238-3096", "(11) 95578-3240", "",
    "", "https://pepetos.com.br/", "me", "false", "medio",
    "Creche, Hotel, Banho e Tosa, Natacao, Adestramento. Seg-Sex 7h-19h."))

add_new(n("Cao a Cao", "hotel_pet", "creche_hotel",
    "Sao Caetano do Sul", "Sao Caetano do Sul",
    "", "", "",
    "@crechecaoacao", "https://www.caoacao.com.br/", "me", "false", "medio",
    "Creche, Hotelzinho, Dogwalker, Banho e Tosa."))

add_new(n("Fuco Pet Care", "hotel_pet", "creche_hotel",
    "Bairro Santa Maria", "Sao Caetano do Sul",
    "", "(11) 94082-6070", "",
    "@fucopetcare", "", "me", "false", "medio",
    "Creche, Hotel, Banho e Tosa, Vacinas. Ambiente natureza."))

add_new(n("Regia Tinas Care", "banho_tosa", "grooming",
    "Sao Caetano do Sul", "Sao Caetano do Sul",
    "", "", "",
    "", "https://www.banhonopet.com.br/", "me", "false", "medio",
    "Groomers especializados em todas as racas."))

# ===== NEW SBC =====
print("\n=== NEW SBC ===")

add_new(n("Pronto Socorro Animal", "clinica_vet", "24h",
    "R. Secondo Modolin, 420 - Jardim Maria Cecilia", "Sao Bernardo do Campo",
    "(11) 4338-3222", "(11) 99285-3194", "",
    "", "https://prontosocorroanimal.com.br/", "epp", "false", "alto",
    "Pronto Socorro Animal 24h."))

add_new(n("Clinica Veterinaria Sao Bernardo", "clinica_vet", "clinica",
    "Sao Bernardo do Campo", "Sao Bernardo do Campo",
    "(11) 4127-1839", "(11) 4127-1839", "",
    "@vetsaobernardo", "", "epp", "false", "alto",
    "Clinica vet. Tambem: (11) 99646-0668."))

add_new(n("Sao Bernardo Saude Animal", "clinica_vet", "clinica",
    "Sao Bernardo do Campo", "Sao Bernardo do Campo",
    "(11) 3380-4421", "(11) 99191-9001", "",
    "@clinica_saobernardo", "", "epp", "false", "medio",
    "WhatsApp 99191-9001, Ligacao 99266-4390."))

add_new(n("Pet ABC", "pet_shop", "local",
    "Sao Bernardo do Campo", "Sao Bernardo do Campo",
    "", "(11) 98765-2947", "",
    "@racoesabc", "", "me", "false", "medio",
    "Pet shop + banho e tosa."))

add_new(n("Petland Rudge Ramos", "pet_shop", "franquia",
    "Av. Caminho do Mar, 2227 - Rudge Ramos", "Sao Bernardo do Campo",
    "", "", "",
    "@petlandsbc_rudgeramos", "", "medio", "false", "alto",
    "Franquia Petland premium."))

add_new(n("Cobasi SBC Faria Lima", "pet_shop", "megaloja",
    "Av. Brigadeiro Faria Lima, 1760", "Sao Bernardo do Campo",
    "(11) 4853-2220", "", "",
    "", "https://www.cobasi.com.br/lojas/cobasi-sbc-faria-lima", "grande", "false", "alto",
    "Rede Cobasi."))

add_new(n("Betpet Shop", "pet_shop", "local",
    "R. Ernesta Pelosini, 92", "Sao Bernardo do Campo",
    "(11) 4124-7057", "", "",
    "", "", "me", "false", "medio",
    "Pet shop local."))

add_new(n("Bichinho Chic", "banho_tosa", "local",
    "R. Isaac Aizemberg, 307", "Sao Bernardo do Campo",
    "(11) 4392-1313", "", "",
    "", "", "me", "false", "medio",
    "Banho e tosa."))

add_new(n("Best Pet SBC", "banho_tosa", "hotel",
    "Sao Bernardo do Campo", "Sao Bernardo do Campo",
    "", "(11) 93029-2183", "",
    "@bestpet.sbc", "", "me", "false", "medio",
    "Banho, Tosa e Hotel."))

# ===== NEW SA =====
print("\n=== NEW SA ===")

add_new(n("Hovet Dr. Vet", "clinica_vet", "24h",
    "Av. Portugal, 1680 - Jardim Bela Vista", "Santo Andre",
    "(11) 3969-7979", "(11) 94142-5536", "",
    "@drvethovet", "", "epp", "false", "alto",
    "Hospital 24h todos os dias. Tel: 3969-7979/3969-5525."))

add_new(n("Paco e Sua Turminha", "clinica_vet", "clinica",
    "Alameda Campestre, 590 - Campestre", "Santo Andre",
    "(11) 4421-6467", "(11) 98819-2753", "contato@pacoesuaturminha.com.br",
    "@pacoesuaturminha", "https://pacoesuaturminha.com.br/", "epp", "false", "alto",
    "Fundada 2007. Seg-Sab 8h-18h."))

add_new(n("Pet Shop Nemo", "pet_shop", "vet_pet",
    "Av. Queiros Filho, 553", "Santo Andre",
    "(11) 2896-7211", "", "",
    "", "", "me", "false", "medio",
    "Pet shop e veterinaria."))

add_new(n("Petz Santo Andre", "pet_shop", "megaloja",
    "Av. Ramiro Colleoni, 355 - Vila Assuncao", "Santo Andre",
    "(11) 2181-7370", "", "",
    "", "https://www.petz.com.br/loja/petz-santo-andre", "grande", "false", "alto",
    "Rede Petz."))

add_new(n("Pet Shop Mister Dog", "pet_shop", "local",
    "Estrada do Pedroso, 299", "Santo Andre",
    "", "", "",
    "", "", "me", "false", "medio",
    "Pet shop local."))

# ===== NEW DIADEMA/MAUA/RP =====
print("\n=== NEW DIADEMA/MAUA/RP ===")

add_new(n("Hospital Veterinario Rivelles", "clinica_vet", "hospital_24h",
    "Av. Alda, 384 - Parque Sete de Setembro", "Diadema",
    "(11) 4343-4126", "(11) 98944-9077", "",
    "@hospitalrivelles", "https://rivelles.com.br/", "medio", "false", "alto",
    "Hospital vet 24h. Desde 1985."))

add_new(n("Gran Pet Diadema", "pet_shop", "clinica_pet",
    "Av. Senador Vitorino Freire, 421 - Centro", "Diadema",
    "(11) 4043-2727", "(11) 98666-4655", "",
    "@granpetdiadema", "", "epp", "false", "alto",
    "Clinica + Pet Shop."))

add_new(n("Mundo Rural Pet Diadema", "pet_shop", "clinica_pet",
    "Praca Bom Jesus Piraporinha, 122 - Piraporinha", "Diadema",
    "(11) 4066-1302", "(11) 97286-5803", "",
    "", "https://www.mundoruralpet.com.br/", "epp", "false", "medio",
    "Pet shop + clinica. Clinica: (11) 94138-5172."))

add_new(n("Cobasi Diadema", "pet_shop", "megaloja",
    "Av. Presidente Kennedy, 480", "Diadema",
    "", "", "",
    "", "https://www.cobasi.com.br/lojas/cobasi-diadema", "grande", "false", "alto",
    "Rede Cobasi."))

add_new(n("Petz Diadema", "pet_shop", "megaloja",
    "Av. Fabio Eduardo Ramos Esquivel, 1100 - Centro", "Diadema",
    "(11) 2181-7352", "", "",
    "", "https://www.petz.com.br/loja/petz-diadema", "grande", "false", "alto",
    "Rede Petz."))

add_new(n("PetConsulta Diadema", "clinica_vet", "clinica_pet",
    "Campanario", "Diadema",
    "", "", "",
    "", "https://www.petconsultadiadema.com.br/", "me", "false", "medio",
    "Clinica + banho e tosa."))

add_new(n("Animavet Pet Shop", "pet_shop", "clinica_pet",
    "Av. Jose Bonifacio, 705 - Conceicao", "Diadema",
    "(11) 4056-2157", "", "",
    "", "", "me", "false", "medio",
    "Pet shop e veterinaria."))

add_new(n("Animal Mania Maua", "clinica_vet", "clinica",
    "R. Porto Feliz, 757 - Jardim Haydee", "Maua",
    "(11) 2312-8236", "(11) 95585-9443", "atendimento@animalmaniaveterinaria.com.br",
    "@clinvet_animalmaniaspmaua", "https://animalmaniaveterinaria.com.br/", "epp", "false", "medio",
    "Ter-Sex 9h-18h, Sab 9h-17h."))

add_new(n("Animale Hospital Maua", "clinica_vet", "hospital_24h",
    "R. Almirante Barroso, 114 - Vila Bocaina", "Maua",
    "(11) 4515-5535", "(11) 94669-4122", "",
    "@hovetanimale", "https://hovetanimale.com.br/", "epp", "false", "alto",
    "Hospital 24h. Clinico + Emergencial + Exames + Raio X."))

add_new(n("Pet Shop Central Maua", "pet_shop", "local",
    "R. Luis Lacava, 300", "Maua",
    "(11) 3421-9807", "", "",
    "", "", "me", "false", "medio",
    "Pet shop central."))

add_new(n("Petz Shopping Maua", "pet_shop", "megaloja",
    "Av. Gov. Mario Covas Junior, 01 - Centro", "Maua",
    "(11) 2181-7329", "", "",
    "", "https://www.petz.com.br/loja/petz-shopping-maua", "grande", "false", "alto",
    "Rede Petz."))

add_new(n("Tico Tico Vet Maua", "clinica_vet", "clinica_pet",
    "R. Alziro Vidoto, 3 - Jardim Maringa", "Maua",
    "", "(11) 93407-5752", "",
    "", "", "me", "false", "medio",
    "Clinica vet e pet shop."))

add_new(n("Pet Patas e Pelos", "pet_shop", "local",
    "Av. Presidente Castelo Branco, 1510 - Jardim Zaira", "Maua",
    "(11) 98717-3735", "", "",
    "", "", "me", "false", "medio",
    "Pet shop local."))

# ===== SUMMARY =====
cities = {}
has_phone = has_wpp = has_email = has_ig = has_web = 0
for d in data:
    c = d["cidade"]
    cities[c] = cities.get(c, 0) + 1
    if d.get("telefone") and d["telefone"] not in ("", "a_validar"): has_phone += 1
    if d.get("whatsapp") and d["whatsapp"] not in ("", "a_validar"): has_wpp += 1
    if d.get("email") and d["email"] not in ("", "a_validar"): has_email += 1
    if d.get("instagram") and d["instagram"] not in ("", "a_validar"): has_ig += 1
    if d.get("website") and d["website"] not in ("", "a_validar"): has_web += 1

print(f"\n{'='*50}")
print(f"FINAL: {len(data)} contacts")
print(f"  Phone: {has_phone}/{len(data)} ({has_phone*100//len(data)}%)")
print(f"  WhatsApp: {has_wpp}/{len(data)} ({has_wpp*100//len(data)}%)")
print(f"  Email: {has_email}/{len(data)} ({has_email*100//len(data)}%)")
print(f"  Instagram: {has_ig}/{len(data)} ({has_ig*100//len(data)}%)")
print(f"  Website: {has_web}/{len(data)} ({has_web*100//len(data)}%)")
print(f"\nBy city:")
for k, v in sorted(cities.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"\nSaved to {JSON_PATH}")
