@echo off
:: CEX N03 — CRM Frontend (Tabs + Table + Map)
:: Trabalha no repo gato-cubo-commerce

title CEX-N03-CRM-FRONTEND
set CLAUDECODE=
set CEX_NUCLEUS=N03
set CEX_ROOT=C:\Users\PC\Documents\GitHub\gato-cubo-commerce
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-20250514
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome

claude %FLAGS% %MODEL% "Voce e N03 Builder Nucleus. MISSION: Criar CRM Admin pages no site GATO3. LEIA o spec COMPLETO em C:\Users\PC\Documents\GitHub\cex\.cex\runtime\handoffs\crm_mission\SPEC_CRM_ADMIN.md. STACK: React+Vite+Shadcn/UI+Tailwind+Supabase+Recharts+TanStack Query. Admin existente em src/pages/admin/ com ProtectedRoute. TAREFAS: 1) Criar src/pages/admin/CRM.tsx com Shadcn Tabs (3 tabs: Dashboard, Contatos, Mapa). 2) Tab Dashboard: CRMMetrics (5 cards) + CRMCharts (Recharts bar por cidade, pie segmento). 3) Tab Contatos: ContactsTable (TanStack Table sortable+paginated) + ContactFilters (cidade/segmento/status/busca) + ContactDetail (Sheet lateral com edicao). 4) Tab Mapa: CRMMap com react-leaflet + OpenStreetMap, markers coloridos por segmento, clusters, popups com nome+tel+acoes. 5) Hooks: useCRMContacts, useCRMStats, useCRMUpdate (Supabase queries). 6) Adicionar rota /admin/crm no App.tsx dentro de ProtectedRoute. 7) Instalar: npm install react-leaflet leaflet @types/leaflet. DECISOES: Leaflet/OSM gratis. Sem kanban agora. Multi-user (roles). Visual PB minimalista GATO3. Commit ao final."
