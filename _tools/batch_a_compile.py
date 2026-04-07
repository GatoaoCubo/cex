#!/usr/bin/env python3
"""BATCH_A_DIRETORIOS -- compile scraped directory data into CRM JSON."""
import json
import re
from collections import Counter

# Load existing CRM for dedup
with open('N01_research/output/data/crm_pet_abc.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

existing_names = set()
for r in existing:
    n = (r.get('nome_fantasia', '') or r.get('nome', '')).lower().strip()
    if n:
        existing_names.add(n)
        existing_names.add(re.sub(r'[^a-z0-9]', '', n))

print(f"Existing names for dedup: {len(existing_names)}")


def classify_segment(name, category=''):
    nl = name.lower()
    cl = category.lower() if category else ''
    combined = nl + ' ' + cl
    if any(w in combined for w in ['hospital', 'hovet']):
        return 'hospital_24h'
    if any(w in combined for w in ['veterinar', 'vet ', 'vet.', 'clinica vet']):
        return 'clinica_vet'
    if any(w in combined for w in ['banho', 'tosa', 'grooming', 'beleza']):
        return 'banho_tosa'
    if any(w in combined for w in ['hotel', 'hospeda', 'creche']):
        return 'hotel_pet'
    if any(w in combined for w in ['adestram', 'dog walk']):
        return 'adestramento'
    if any(w in combined for w in ['avicultura', 'agro', 'rural', 'racao', 'racoes', 'racao', 'racoes']):
        return 'agropecuaria'
    if any(w in combined for w in ['ong', 'cidadania animal', 'apaa']):
        return 'ong'
    return 'pet_shop'


def is_personal_name(name):
    nl = name.lower().strip()
    if re.match(r'^\d', nl):
        return True
    blocked = [
        'samare formiga', 'miriam de souza', 'alessandro pereira giorgi',
        'debora silva de sousa', 'arnaldo joao venancio', 'izilda regina',
        'hamilton mimesse', 'suzane mayumi', 'thalia augusto', 'erick delle piaggi',
        'stephanie rodrigues', 'leonardo gomes agostinho', 'rosalina diodato',
        'marcela michilato', 'ronaldo gois barbosa', 'bruna demov', 'chen roncai',
        'ana basso', 'bruna costa ribeiro', 'arnaldo ferreira costa',
        'claudino santos rosa', 'dayane hypolito',
        'weslley alves paula', 'pedro hiroshi ruiz',
        'radyla franca', 'lucas soares delfino', 'a.g. da silva',
        'ds ultrassonografia', 'mab aiara', 'cvetpatol', 'anymedic',
        'nucleo cientifico pet', 'l.r. coelho', 'ronaldo gois',
        'm.g. macinelli', 'r. c. dos santos', 'labpets', 'l l p servicos',
        'acr vet servicos', 'mape', 'oftati', 'movida reabilitacao', 'fauna diagnostico',
        'fernanda - imaginologia', 'comercial agricola nishiyama',
        'kimimo lacos', 'cindy lacos', 'pipicao saquinhos',
    ]
    for pn in blocked:
        if pn in nl:
            return True
    return False


def compute_completeness(rec):
    score = 0
    if rec.get('nome_fantasia'):
        score += 1
    if rec.get('endereco'):
        score += 1
    if rec.get('telefone') or rec.get('whatsapp'):
        score += 1
    if rec.get('email') or rec.get('website') or rec.get('instagram'):
        score += 1
    if rec.get('google_rating'):
        score += 1
    return score


def mk(name, seg, addr, bairro, cidade, tel, fonte, **kw):
    return {
        "nome_fantasia": name,
        "segmento": seg if seg else classify_segment(name),
        "endereco": addr,
        "bairro": bairro,
        "cidade": cidade,
        "telefone": tel,
        "whatsapp": kw.get("whatsapp", ""),
        "email": kw.get("email", ""),
        "website": kw.get("website", ""),
        "instagram": kw.get("instagram", ""),
        "google_rating": kw.get("google_rating", ""),
        "fonte_descoberta": fonte,
        "completeness_score": 0,
        "data_discovery": "2026-04-04"
    }


all_records = []

# ========== TRICELEADS SCS PET SHOPS ==========
src = "triceleads:pet-shop/sao-caetano-do-sul"
for n, b in [
    ("Pesca e Bichos Comercial", "Oswaldo Cruz"),
    ("Vida de Cao & Cia", "Santa Paula"),
    ("Amigo Bicho", "Boa Vista"),
    ("Avicultura Santa Maria", "Santa Maria"),
    ("Pet & Vet", "Olimpico"),
    ("Pet Shop Sao Jose", "Olimpico"),
    ("Clinica Veterinaria Perez", "Santa Paula"),
    ("Dogs Day", "Osvaldo Cruz"),
    ("Galerinha Animal Pet Shop", "Barcelona"),
    ("Pegada do Bicho", "Santa Paula"),
    ("Dog Reis", "Nova Gerty"),
    ("Clinical Pets", "Fundacao"),
    ("Cara do Bicho Veterinaria & Pet Shop", "Sao Jose"),
    ("A. S. Martins Veterinaria e Pet Shop", "Santa Paula"),
    ("Pet Center", "Fundacao"),
    ("Pet Para Pets", "Santa Paula"),
    ("Emporion Animal Humanizado", "Osvaldo Cruz"),
]:
    all_records.append(mk(n, "", "", b, "Sao Caetano do Sul", "", src))

# ========== TRICELEADS SCS VETS ==========
src = "triceleads:veterinario/sao-caetano-do-sul"
for n, b in [
    ("Santarelli Clinica Veterinaria", "Barcelona"),
    ("Vet Planet", "Santa Paula"),
    ("De Olho no Bicho", "Santa Paula"),
    ("Pet Friend Banho & Tosa", "Santa Paula"),
    ("Animal Care", "Santa Paula"),
    ("Animalis", "Santa Paula"),
    ("M.G.S. Hospital Veterinario", "Jardim Sao Caetano"),
    ("Toca dos Bichos Servicos Veterinarios", "Ceramica"),
    ("VetNasa Sao Caetano do Sul", "Santo Antonio"),
    ("Amanimal Pet Care", "Ceramica"),
    ("Pet Stop", "Santa Maria"),
    ("Vetz For Pets", "Santa Paula"),
    ("Star Pets", "Jardim Sao Caetano"),
    ("Ethicus Hospital Veterinario", "Maua"),
    ("Clinica Veterinaria V3", "Osvaldo Cruz"),
    ("Macaw Clinica Veterinaria", "Santa Paula"),
    ("ONG SOS Cidadania Animal", "Ceramica"),
]:
    all_records.append(mk(n, "", "", b, "Sao Caetano do Sul", "", src))

# ========== TRICELEADS SBC PET SHOPS ==========
src = "triceleads:pet-shop/sao-bernardo-do-campo"
for n, b in [
    ("Cao-Fraria", "Vila Pauliceia"),
    ("4 Patas e Cia", "Pauliceia"),
    ("J.H. da Silva Avicultura", "Jardim Represa"),
    ("Pet Shop Quirino", "Terra Nova II"),
    ("Dog Show", "Assuncao"),
    ("3 Filhotes", "Taboao"),
    ("Bom Cao", "Montanhao"),
    ("Avicultura Recanto dos Animais", "Nova Petropolis"),
    ("Trakinagem Pet Shop", "Nova Petropolis"),
    ("Dogs Day SBC", "Jardim do Mar"),
    ("Animal Center", "Vila Sao Joao"),
    ("Pet Shop Amigao", "Jardim das Orquideas"),
    ("Racoes Rancho Fundo", "Santa Cruz"),
    ("Villa Pet", "Taboao"),
    ("Baby Dog", "Rudge Ramos"),
    ("L.E. Bichos Pet Shop", "Vila Pauliceia"),
    ("Pet Fanaticos", "Rudge Ramos"),
    ("Entre Bichos", "Jardim Trieste"),
    ("Avicultura e Pet Shop da Tay", "Jardim das Orquideas"),
    ("Avicultura Entre Amigos", "Ferrazopolis"),
    ("Petiscao & Cia Pet Shop", "Parque Neide"),
    ("Escova Cao", "Terra Nova II"),
    ("Nautilus", "Rudge Ramos"),
    ("Pet Shop Dr. Hato", "Baeta Neves"),
]:
    all_records.append(mk(n, "", "", b, "Sao Bernardo do Campo", "", src))

# ========== TRICELEADS RIBEIRAO PIRES VETS ==========
src = "triceleads:veterinario/ribeirao-pires"
for n, b in [
    ("Kite Veterinaria", "Parque Santa Luzia"),
    ("Clinica Veterinaria Nipon", "Santa Luzia"),
    ("Ouro Vet", "Pouso Alegre"),
    ("Acacias Servicos Veterinarios", "Centro Alto"),
    ("Patinhas e Rodas", "Vila Gomes"),
    ("Clinica Veterinaria e Pet Shop Ribeirao", "Pastoril"),
    ("Veterinaria Lulucao", "Bocaina"),
    ("Quiron Clinica Veterinaria & Pet Spa", "Pastoril"),
    ("Clinica Veterinaria Alianca", "Alianca"),
    ("Vivas Veterinaria", "Centro"),
    ("Vet House", "Ponte Seca"),
    ("KJS Clinica Veterinaria", "Centro"),
    ("Clinica Veterinaria Ferreira", "Santa Luzia"),
    ("VetClinic Saude Animal", "Centro"),
    ("Vet Pantaneiro", "Suica"),
    ("Moreirao LVet", "Represa"),
]:
    all_records.append(mk(n, "", "", b, "Ribeirao Pires", "", src))

# ========== TRICELEADS DIADEMA VETS ==========
src = "triceleads:veterinario/diadema"
for n, b in [
    ("Clinica Veterinaria Santa Marta", "Jardim Santa Rita"),
    ("Clinica Veterinaria Canin & Cat", "Centro"),
    ("Espaco Pet Feliz", "Eldorado"),
    ("UPA Vet Diadema", "Centro"),
    ("Clinica Veterinaria Projeto Jerri", "Centro"),
    ("Hospital Veterinario Diadema", "Centro"),
    ("Amigo Vet Unidade II", "Vila Nogueira"),
    ("Deixa Que Eu Cuido", "Serraria"),
    ("Shopping Animal", "Centro"),
    ("Clinica Veterinaria Mundo Rural", "Piraporinha"),
    ("Veterinaria Nosso Lar", "Casa Grande"),
    ("Mundo das Patas Servicos Veterinarios", "Centro"),
]:
    all_records.append(mk(n, "", "", b, "Diadema", "", src))

# ========== TRICELEADS MAUA VETS ==========
src = "triceleads:veterinario/maua"
for n, b in [
    ("Amor Animal", "Vila Guarani"),
    ("Casa do Cao e Gato", "Vila N. Sra. das Vitorias"),
    ("Clinica Veterinaria Bicho Amigo", "Jardim S. Jorge do Guapituba"),
    ("Clinica Veterinaria Animal Mania", "Jardim Haydee"),
    ("VetNasa Maua", "Jardim Maringa"),
    ("The Animals Home", "Sao Vicente"),
    ("Gato Q Ri", "Vila Assis Brasil"),
    ("Flocos de Mell", "Jardim Bela Vista"),
    ("Rock Vet Centro Medico Veterinario", "Jardim Itapark"),
    ("Animale Maua", "Vila Bocaina"),
    ("Verum Diagnostico Veterinario", "Vila Bocaina"),
    ("Sao Francisco de Assis Banho e Tosa", "Parque Sao Vicente"),
    ("Centro de Saude Animal Paraiso", "Jardim Haydee"),
    ("Maua Saude Animal", "Vila Ana Maria"),
    ("Smart Pet", "Vila Bocaina"),
    ("Vet Space", "Jardim Sonia Maria"),
]:
    all_records.append(mk(n, "", "", b, "Maua", "", src))

# ========== TELELISTAS DIADEMA PET SHOPS ==========
src = "telelistas:sp/diadema/pet+shop"
for n, a, b in [
    ("Tropical Pet Shop", "Avenida Da Agua Funda, 121", "Taboao"),
    ("Raca e Racao Avicultura", "Av. Antonio Sylvio Cunha Bueno, 954", "Diadema"),
    ("Mundo Magico dos Pets", "Rua Joao Theodoro Genesi, 71", "Centro"),
    ("Amicao Pet Shop", "Avenida Casa Grande, 1529", "Casa Grande"),
    ("Asa Branca Racao Pet e Acessorios", "Avenida Rotary, 146 Loja 2", "Serraria"),
    ("Atlantis Avicultura e Pet Shop", "Av. Ver. Juarez Rios de Vasconcelos, 121", "Centro"),
    ("Avicultura e Pet Shop Lumieri", "Av. Dona Ida Cerati Magrini, 397", "Piraporinha"),
    ("Avicultura Eucaliptos", "Estrada do Rufino, 545", "Serraria"),
    ("Avicultura Vila Nova Conquista", "Avenida Presidente Juscelino, 509", "Piraporinha"),
    ("Bello Dogs", "Av. Maria Candida de Oliveira, 459", "Casa Grande"),
    ("Bem-Vindo Pet", "Rua Lidia Blank, 117", "Centro"),
    ("Bichocracia", "Rua Manoel da Nobrega, 177", "Centro"),
    ("Carol Bichos & Cia Pet Shop", "Av. Dona Ruyce Ferraz Alvim, 1871 Sala 01", "Serraria"),
    ("Casa dos Pets Diadema", "Rua Raio de Sol, 28", "Piraporinha"),
    ("Casa du Pet", "Rua Maria Helena, 461", "Piraporinha"),
    ("CR Pet Nova Conquista", "Avenida Presidente Juscelino, 875", "Piraporinha"),
    ("Enimal Pet", "Rua Yamagata, 277 Conj 2", "Taboao"),
    ("Gran Pet Diadema", "Av. Senador Vitorino Freire, 421", "Centro"),
    ("Coprodi", "Rua Martim Afonso, 311", "Conceicao"),
]:
    all_records.append(mk(n, "", a, b, "Diadema", "", src))

# ========== TELELISTAS DIADEMA BANHO E TOSA ==========
src = "telelistas:sp/diadema/banho+e+tosa"
for n, a, b in [
    ("Bichos e Caprichos", "Rua Santa Cruz, 495 Lote 26-A", "Canhema"),
    ("Caobeleireiro Tosa Para Mim", "Rua Santa Marta, 306", "Taboao"),
    ("Caobeleireiro Diadema", "Rua Jose Francisco Bras, 41", "Piraporinha"),
    ("Clinica Vet Banho e Tosa Juarez", "Rua Salvador Correa de Sa, 516", "Vila Nogueira"),
    ("Pet Center Diadema Banho e Tosa", "Rua Sao Jorge, 216", "Centro"),
    ("Pet Shop Dog & Cat Diadema", "Avenida Dom Joao VI, 986", "Taboao"),
    ("Pet Shop Meu Amigao Cao & Gato", "Rua Graciosa, 528", "Centro"),
    ("Thami Vet", "R. Gen. Vicente de Paula Dale Coutinho, 60", "Centro"),
]:
    all_records.append(mk(n, "banho_tosa", a, b, "Diadema", "", src))

# ========== TELELISTAS MAUA PET SHOPS ==========
src = "telelistas:sp/maua/pet+shop"
for n, a, b in [
    ("Nutri Maua Comercial", "Avenida Barao Maua, 2796", "Maua"),
    ("Racoes e Avicultura Primavera", "Rua Das Violetas, 16", "Jardim Primavera"),
    ("Vip Pet Shop Maua", "R. Vice-Pres. Urbano Santos, 144", "Parque Sao Vicente"),
    ("Adelaide Avicultura", "Avenida Itapark, 3343", "Vila Bocaina"),
    ("Avicultura e Floricultura Schers", "Rua Rio Branco, 506 A", "Vila Augusto"),
    ("Avicultura Tomba Lata", "Rua Carlo de Campo, 204", "Vila N. Sra. das Vitorias"),
    ("Bom Pra Cachorro Equip. Banho e Tosa", "R. Pedro Eugenio Pereira, 1221", "Jardim Sao Judas"),
    ("Caomida Comercio de Racoes", "Rua Francisco da Paz, 28", "Vila Dirce"),
    ("Casa de Racao 4 Patas", "R. Gen. Hastinfilo de Moura, 160 B", "Parque Sao Vicente"),
    ("Casa de Racao Sao Francisco", "Rua Rio Branco, 2335", "Vila Bocaina"),
    ("Casa de Racoes Cat & Dog", "Rua Riachuelo, 854", "Vila N. Sra. das Vitorias"),
    ("Casa de Racoes Cristal", "R. Dr. Vicente de Carvalho Bruno, 1021", "Vila Florida"),
    ("Casa de Racoes Tico-Tico", "R. Dr. Joao Carlos Azevedo, 10", "Parque Bandeirantes"),
    ("Cla Animal Pet Shop", "Rua Dom D Patria, 575", "Maua"),
    ("Comercial Agroito", "Avenida Capitao Joao, 3714", "Maua"),
]:
    all_records.append(mk(n, "", a, b, "Maua", "", src))

# ========== GUIAMAIS SCS ==========
src = "guiamais:sao-caetano-do-sul-sp/pet-shop"
for n, a, b in [
    ("Shower Dog Pet Store", "R Major Carlos Del Prete, 1059", "Santo Antonio"),
    ("Agroshop ABC", "Av Guido Aliberti, 3051", "Maua"),
    ("Recanto Animal Pet Shop e Veterinario", "R Monte Alegre, 157", "Santo Antonio"),
    ("Petit Cao Pet Shop", "Av Dr. Augusto de Toledo, 1006", "Santa Paula"),
    ("Pet Shop Falcao", "Alameda Sao Caetano, 1570", "Santa Maria"),
    ("Pet Shop Palace Dog", "R Sao Paulo, 664", "Santo Antonio"),
    ("Micas Pet Shop", "R Amazonas 1347", "Osvaldo Cruz"),
]:
    all_records.append(mk(n, "", a, b, "Sao Caetano do Sul", "", src))

# ========== GUIAMAIS SBC ==========
src = "guiamais:sao-bernardo-do-campo-sp/pet-shop"
for n, a, b in [
    ("O Meu Bichinho Espaco Pet", "Av Wallace Simonsen, 498", "Nova Petropolis"),
    ("Canil Golden Lions", "R Xavier de Toledo, 731", "Pauliceia"),
    ("Eco Pet Clinica Veterinaria e Pet Shop", "Av Caminho do Mar, 2847", "Rudge Ramos"),
    ("Pets Brasil Estetica Animal", "R Princesa Francisca Carolina, 157", "Baeta Neves"),
    ("Banho e Tosa Se-Cao", "R Alvaro Alvim, 1349", "Pauliceia"),
    ("Caobeleireiro Studio Pet Shop", "R Mario Fongaro, 41", ""),
    ("Pet Shop Melhor Amigo", "R Borba Gato, 44", "Jordanopolis"),
]:
    all_records.append(mk(n, "", a, b, "Sao Bernardo do Campo", "", src))

# ========== GUIAMAIS SANTO ANDRE ==========
src = "guiamais:santo-andre-sp/pet-shop"
for n, a, b, t in [
    ("Pit Pet Jardim", "R das Aroeiras, 430", "Jardim", "(11) 97627-2000"),
    ("Stars Pets", "R Onze de Junho, 145", "Casa Branca", "(11) 2759-8000"),
    ("Bicho Mania SA", "Av Lino Jardim, 957", "Jardim Bela Vista", ""),
    ("Village Pet Clinica Veterinaria", "R Cel. Agenor de Camargo, 57", "Centro", ""),
    ("Pet Shop Utinga", "Pc Mario Guindani, 53", "Vila Metalurgica", ""),
    ("Clinica Veterinaria e Pet Shop Columbia", "R Columbia, 971", "Parque Nacoes", ""),
    ("Pet Shop e Veterinario Vira Lata", "Av Dr. Erasmo, 188", "Vila Assuncao", ""),
    ("KF Dogs", "R Guapore, 10", "Vila Gilda", ""),
]:
    all_records.append(mk(n, "", a, b, "Santo Andre", t, src))

# ========== INDIVIDUAL DISCOVERIES ==========
all_records.append(mk(
    "Pet & Vet Clinica Veterinaria SCS", "", "Av. Presidente Kennedy 1480", "Olimpico",
    "Sao Caetano do Sul", "(11) 4226-4910", "yelp:pet-e-vet-sao-caetano-do-sul"
))
all_records.append(mk(
    "PET LIFE Sao Caetano", "", "R. Amazonas, 1159 - Oswaldo Cruz", "Osvaldo Cruz",
    "Sao Caetano do Sul", "(11) 95028-9537", "petlifesaocaetano.com.br",
    website="https://petlifesaocaetano.com.br/", email="petlifesaocaetano@gmail.com"
))
all_records.append(mk(
    "Clinica Veterinaria ABC", "", "", "",
    "Santo Andre", "(11) 4996-4910", "instagram:@veterinaria.abc",
    instagram="@veterinaria.abc"
))
all_records.append(mk(
    "SC Pet Shop e Veterinaria", "", "Rua Ibiapava, 173", "",
    "Santo Andre", "", "econodata:CNPJ-51039192000180"
))
all_records.append(mk(
    "CEVAP - Centro Veterinario Amante dos Pets", "", "Rua Olimpia Catta Preta 567", "Centro Alto",
    "Ribeirao Pires", "(11) 97549-2141", "petlove:rede-credenciada/sp/ribeirao-pires"
))
all_records.append(mk(
    "Pet Shopping House", "", "", "",
    "Ribeirao Pires", "", "facebook:Petshoppinghousee"
))

# ========== DEDUP ==========
seen = set()
output = []
dedup_existing = 0
dedup_internal = 0

for rec in all_records:
    name = rec["nome_fantasia"]
    name_lower = name.lower().strip()
    name_simple = re.sub(r'[^a-z0-9]', '', name_lower)

    if is_personal_name(name):
        continue

    if name_lower in existing_names or name_simple in existing_names:
        dedup_existing += 1
        continue

    if name_simple in seen:
        dedup_internal += 1
        continue
    seen.add(name_simple)

    rec["completeness_score"] = compute_completeness(rec)

    if rec["nome_fantasia"] and rec["cidade"] and rec["fonte_descoberta"]:
        output.append(rec)

output.sort(key=lambda x: (x["cidade"], -x["completeness_score"], x["nome_fantasia"]))

print(f"\nTotal raw records: {len(all_records)}")
print(f"Removed (existing CRM match): {dedup_existing}")
print(f"Removed (internal dupes): {dedup_internal}")
print(f"Final new contacts: {len(output)}")
print(f"\nBy city:")
city_counts = Counter(r["cidade"] for r in output)
for city, count in sorted(city_counts.items()):
    print(f"  {city}: {count}")

seg_counts = Counter(r["segmento"] for r in output)
print(f"\nBy segment:")
for seg, count in sorted(seg_counts.items(), key=lambda x: -x[1]):
    print(f"  {seg}: {count}")

with open('N01_research/output/data/crm_batch_a_diretorios.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\nWritten to N01_research/output/data/crm_batch_a_diretorios.json")
