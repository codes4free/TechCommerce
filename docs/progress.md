# TechCommerce – PROGRESS

## Sessão 2025‑05‑02 16:40 (UTC‑3)

### Concluído ✅

* **Requisitos.md** criado e versionado.
* **DER** (`docs/der.puml`) pronto (gera `der.png`).
* **pyproject.toml** incluído no repo com dependências, incluindo `djangorestframework-simplejwt`.
* Decisão de autenticação: **JWT**, variáveis de ambiente mantidas no `docker-compose.yml`.
* Esboço de **Dockerfile**, **docker‑compose.yml** e `scripts/seed.py` fornecidos (aguardando commit definitivo).

### Próximos Passos ⏭️

1. Commitar Dockerfile, docker‑compose.yml e scripts/seed.py; rodar `docker compose build`.
2. Bootstrap Django (`django-admin startproject techcommerce .`) e executar `python manage.py migrate`.
3. Criar app **store**; definir modelos `Produto`, `Pedido`, `ItemPedido`, `Pagamento`; gerar migrações.
4. Executar `scripts/seed.py` para inserir 20 produtos.
5. Configurar **Django REST Framework** + SimpleJWT em `settings.py` e rotas JWT (`/api/token/`, `/api/token/refresh/`).
6. Criar serializers & viewsets DRF para `/api/produtos/` e `/api/pedidos/` com permissões adequadas.
7. Escrever **pytest** cobrindo modelos e APIs (meta 80 % cobertura).
8. Criar **demo.sh** que obtém token, lista produtos, cria pedido e exibe resposta.
9. Atualizar **README.md** com passos de execução, endpoints e captura do DER.
10. Converter README + diagramas em **relatório PDF** com template acadêmico.

### Dúvidas / Bloqueios ❓

Nenhum no momento – prosseguir com commit dos contêineres e bootstrap Django.

---

*Atualize este arquivo ao final de cada sessão para manter rastreabilidade.*
