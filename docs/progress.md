# TechCommerce – PROGRESS

## Sessão 2025‑05‑02 17:05 (UTC‑3)

### Concluído ✅

* **Requisitos.md** criado e versionado.
* **DER** (`docs/der.puml`) pronto (gera `der.png`).
* **pyproject.toml** incluído no repo com dependências, incluindo `djangorestframework-simplejwt`.
* Decisão de autenticação: **JWT**, variáveis de ambiente mantidas no `docker-compose.yml`.
* **Dockerfile**, **docker‑compose.yml** e `scripts/seed.py` commitados e "push feito".
* `docker compose build` executado com sucesso.

### Em andamento 🔄

* Bootstrap inicial do projeto Django.

### Próximos Passos ⏭️

1. **Bootstrap Django**

   ```bash
   docker compose run --rm web django-admin startproject techcommerce .
   docker compose run --rm web python manage.py migrate
   ```
2. **Criar app store**

   ```bash
   docker compose run --rm web python manage.py startapp store
   ```
3. **Implementar modelos** em `store/models.py`:

   * `Produto`
   * `Pedido`
   * `ItemPedido`
   * `Pagamento`
4. Gerar migrações e aplicar: `python manage.py makemigrations && python manage.py migrate`.
5. **Configurar DRF + SimpleJWT** no `settings.py` e rotas `/api/token/`, `/api/token/refresh/`.
6. **Serializers & ViewSets** para `/api/produtos/` e `/api/pedidos/`.
7. Executar `scripts/seed.py` para inserir 20 produtos.
8. **Pytest** cobrindo modelos e APIs (≥ 80 % cobertura).
9. Criar `demo.sh` que obtém token, lista produtos, cria pedido completo.
10. Atualizar `README.md` e gerar relatório PDF.

### Dúvidas / Bloqueios ❓

Nenhum no momento.

---

*Atualize este arquivo ao final de cada sessão para manter rastreabilidade.*
