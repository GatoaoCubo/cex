@echo off
:: CEX N05 — CRM Schema + Seed (Supabase)
:: Trabalha no repo gato-cubo-commerce

title CEX-N05-CRM-SCHEMA-SEED
set CLAUDECODE=
set CEX_NUCLEUS=N05
set CEX_ROOT=C:\Users\PC\Documents\GitHub\gato-cubo-commerce
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-20250514
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome

claude %FLAGS% %MODEL% "Voce e N05 Code Nucleus. MISSION: Criar schema Supabase para CRM e seed 509 contatos. LEIA o spec COMPLETO em C:\Users\PC\Documents\GitHub\cex\.cex\runtime\handoffs\crm_mission\SPEC_CRM_ADMIN.md. TAREFAS: 1) Criar migration SQL em supabase/migrations/ com tabela crm_contacts (schema do spec, incluir trigger updated_at, RLS policies para roles admin/vendedor/viewer, indexes). 2) Criar seed script que le o JSON de C:\Users\PC\Documents\GitHub\cex\N01_research\output\data\crm_pet_abc.json e insere os 509 contatos via INSERT. 3) Atualizar src/integrations/supabase/types.ts adicionando a interface CrmContacts. REGRAS: seguir padrao das migrations existentes. Commit ao final."
