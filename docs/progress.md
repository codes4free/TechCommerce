# TechCommerce – PROGRESS

## Sessão 2025‑05‑02 20:10 (UTC‑3)

### Concluído ✅
- **Runtime corrigido**: Gunicorn agora usa `techcommerce.wsgi:application` ➜ endpoint `/api/token/` funcionando (access + refresh retornados).
- **Dockerfile** e **docker‑compose.yml** atualizados e commitados.
- Contêiner reconstruído (`build --no-cache`) e stack estável.
- Migrações aplicadas; usuário `admin` operacional.

### Próximos Passos ⏭️ (Sprint final)
1. **Seed de dados**
   - Executar `scripts/seed.py` (20 produtos) e confirmar via `/api/produtos/`.
2. **Endpoints restantes**
   - `POST /api/pedidos/` e `GET /api/pedidos/` – testar com JWT.
3. **Testes Pytest**
   - Cobrir modelos (subtotal, calcular_total) e APIs (produtos list, pedidos create).
   - Meta ≥ 80 % cobertura (`pytest --cov`).
4. **Demo script**
   - Finalizar `scripts/demo.sh` (token → lista produtos → cria pedido → exibe JSON).
5. **Documentação**
   - Atualizar `README.md` (setup, endpoints, exemplos `curl`).
   - Gerar `docs/der.png` com PlantUML.
   - Montar relatório PDF (template acadêmico) → subseções: Introdução, Arquitetura, DER, API, Testes, Conclusão.
6. **CI Pipeline** (GitHub Actions)
   - job: build → pytest → docker build → (opcional) push Docker Hub.

### Dúvidas / Bloqueios ❓
- Precisamos incluir lógica de pagamento (mock) antes da entrega? Ou fica para versão futura?  
- Deseja coletar métricas (Prometheus) agora ou depois?

---
*Atualize este arquivo ao final de cada sessão para manter rastreabilidade.*

services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: techcommerce
      POSTGRES_USER: tech
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  web:
    build: .
    command: >
      sh -c "python manage.py makemigrations store &&
             python manage.py migrate &&
             gunicorn techcommerce.wsgi:application -b 0.0.0.0:8000"
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      DATABASE_URL: postgres://tech:secret@db:5432/techcommerce
      SECRET_KEY: change-me
      DJANGO_SUPERUSER_USERNAME: admin
      DJANGO_SUPERUSER_EMAIL: admin@example.com
      DJANGO_SUPERUSER_PASSWORD: admin123

volumes:
  pgdata: