# TechCommerce – PROGRESS

## Sessão 2025‑05‑02 16:10 (UTC‑3)

### Concluído ✅

* **Requisitos.md** criado e revisado; commit previsto.
* **DER**: arquivo `docs/der.puml` adicionado (pronto para gerar `der.png`).
* **pyproject.toml** com dependências Poetry gerado.
* Instruções de setup de **Dockerfile**, **docker‑compose.yml** e **scripts/seed.py** fornecidas (aguardam commit).

### Próximos Passos ⏭️

1. Copiar **Dockerfile**, `docker‑compose.yml` e `scripts/seed.py` para o repo e fazer commit.
2. Executar `docker compose build && docker compose up -d db`.
3. Rodar `django-admin startproject techcommerce .` dentro do contêiner e `python manage.py migrate`.
4. Criar app `store`, definir modelos `Produto`, `Pedido`, `ItemPedido`, `Pagamento` e gerar migrações.
5. Executar `scripts/seed.py` para popular 20 produtos.
6. Configurar **Django REST Framework** e expor endpoints `/produtos` e `/pedidos` (GET/POST).
7. Escrever **pytest** básico cobrindo modelos e API, meta ≥ 80 %.
8. Escrever `demo.sh` demonstrando fluxo de compra completo.
9. Gerar `README.md` com passos de execução + screenshot do DER (`der.png`).
10. Converter `README`+diagramas em **relatório PDF** (template acadêmico).

### Dúvidas / Bloqueios ❓

* Definir se autenticação MVP será *token estático* ou *JWT* (preciso da sua escolha antes de criar endpoints protegidos).
* Confirmar se usaremos **decouple** para ler variáveis `.env` ou manter variáveis diretamente no `docker-compose.yml`.

---

*Atualize este arquivo ao final de cada sessão para manter rastreabilidade.*
