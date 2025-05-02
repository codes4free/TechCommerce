# TechCommerce – Documento de Requisitos (v0.1)

> **Visão**
> Construir em 48 h um MVP de plataforma de e‑commerce voltada a demonstrações acadêmicas, focada em catálogo de produtos, carrinho, pedidos e pagamentos simulados, usando Python + Django, Postgres e pipelines CI/CD em GitHub Actions.

---

## 1 Requisitos Funcionais (RF)

| ID    | Descrição                                                                             |
| ----- | ------------------------------------------------------------------------------------- |
| RF‑01 | O usuário deve poder criar conta, autenticar‑se e terminar sessão.                    |
| RF‑02 | O sistema deve listar produtos com nome, descrição, preço e estoque.                  |
| RF‑03 | O usuário deve poder pesquisar produtos por texto.                                    |
| RF‑04 | O usuário deve poder adicionar/remover itens no carrinho.                             |
| RF‑05 | O usuário deve finalizar pedido informando endereço e forma de pagamento (simulação). |
| RF‑06 | O usuário deve consultar histórico e status de pedidos.                               |
| RF‑07 | O admin deve gerenciar produtos (CRUD) e estoque via painel.                          |
| RF‑08 | O admin deve ver relatório simples de vendas (valor total por dia).                   |

## 2 Requisitos Não Funcionais (RNF)

| ID     | Descrição                                                                       |
| ------ | ------------------------------------------------------------------------------- |
| RNF‑01 | Segurança: comunicações HTTPS, senhas com hashing BCrypt.                       |
| RNF‑02 | Performance: suportar 100 usuários simultâneos com p95 < 500 ms por requisição. |
| RNF‑03 | Disponibilidade: 99 % nas demos (contêineres reiniciáveis).                     |
| RNF‑04 | Portabilidade: deployment via Docker Compose e Kubernetes opcional.             |
| RNF‑05 | Conformidade: LGPD – armazenar dados pessoais mínimos.                          |

## 3 Regras de Negócio (RN)

1. Todo pedido deve conter pelo menos **um** item de produto em estoque.
2. O estoque de produto é decrementado somente após confirmação de pagamento (simulada).
3. O status inicial de um pedido é `Pendente`; pode evoluir para `Pago`, `Enviado`, `Concluído` ou `Cancelado`.
4. Apenas usuários com papel `Admin` podem acessar o painel administrativo.

## 4 Backlog – Histórias de Usuário MVP

| US    | História                                                                                  | Critérios de Aceitação                                                         |
| ----- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| US‑01 | Como **visitante**, quero **criar conta** para realizar compras.                          | ✅ Form de registro, ✅ validação de email único, ✅ redirecionar para login.     |
| US‑02 | Como **cliente**, quero **entrar/sair** do sistema para acessar funcionalidades privadas. | ✅ Login com email+senha, ✅ mensagem erro credenciais, ✅ botão logout funciona. |
| US‑03 | Como **cliente**, quero **ver lista de produtos** para escolher itens.                    | ✅ Rota `/produtos`, ✅ paginação 20 p/ página, ✅ preço visível.                 |
| US‑04 | Como **cliente**, quero **pesquisar** produtos por nome ou descrição.                     | ✅ Campo busca, ✅ resultados filtrados em tempo real ou submit.                 |
| US‑05 | Como **cliente**, quero **adicionar itens ao carrinho** para comprá‑los depois.           | ✅ Botão “Adicionar”, ✅ quantidades ajustáveis, ✅ subtotal correto.             |
| US‑06 | Como **cliente**, quero **finalizar pedido** informando endereço para concluir compra.    | ✅ Form checkout, ✅ ordem gravada em BD, ✅ e‑mail de confirmação (mock).        |
| US‑07 | Como **admin**, quero **cadastrar e editar produtos** para manter catálogo.               | ✅ CRUD protegido por login admin, ✅ validação de campos obrigatórios.          |
| US‑08 | Como **admin**, quero **ver relatório de vendas diárias** para acompanhar desempenho.     | ✅ Endpoint `/admin/relatorio` mostra total vendido por dia em JSON.            |

## 5 Modelo de Dados (rascunho)

Entidades principais: **Usuario, Produto, Pedido, ItemPedido, Pagamento**.

```
Usuario (id, nome, email, senha_hash, is_admin)
Produto (id, nome, descricao, preco, estoque, criado_em)
Pedido (id, usuario_id, data_criacao, status, total)
ItemPedido (id, pedido_id, produto_id, quantidade, preco_unitario)
Pagamento (id, pedido_id, data, valor, metodo, status)
```

> **Diagrama ER** será gerado em `docs/der.puml`.

## 6 Arquitetura Alvo

* **Backend**: Django 4 + Django REST Framework.
* **Banco**: Postgres 16.
* **DevOps**: GitHub Actions → Docker Hub → VPS/WSL local via Docker Compose.
* **Observabilidade**: Prometheus + Grafana (opcional para demo).

## 7 Critérios de Aceitação do MVP

* Subir ambiente completo via `docker-compose up` em ≤ 5 min.
* Executar `pytest` com 80 %+ de cobertura e zero falhas.
* Scripts de seed geram 20 produtos e 1 admin.
* Demo script (`demo.sh`) realiza fluxo completo de compra sem erros retornando HTTP 201.

## 8 Hitos & Datas

| Data/Hora (UTC‑3) | Entrega                       |
| ----------------- | ----------------------------- |
| 02‑mai 18:00      | Requisitos & DER prontos      |
| 03‑mai 03:00      | Backend básico + DB migrações |
| 03‑mai 09:00      | Testes e demo OK              |
| 03‑mai 12:00      | Relatório final PDF           |

---

\*(Gerado pela sessão ChatGPT em 02‑mai‑2025 – mantenha este arquivo atualizado a cada commit.)
