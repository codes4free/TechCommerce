## 4. demo.sh (scripts/demo.sh)
```bash
#!/usr/bin/env bash
set -euo pipefail

# --------- config ----------
HOST=${HOST:-"http://localhost:8000"}
USER=${USERNAME:-admin}
PASS=${PASSWORD:-admin123}
TIMEOUT=${TIMEOUT:-10}
# ---------------------------

command -v jq >/dev/null 2>&1 || { echo >&2 "❌ jq não encontrado. Instale jq e tente novamente."; exit 1; }

echo "🔑  Obtendo token JWT para usuário '$USER'…"
response=$(curl -sS --max-time $TIMEOUT -w "\n%{http_code}" -H "Content-Type: application/json" \
  -d "{\"username\":\"$USER\",\"password\":\"$PASS\"}" "$HOST/api/token/")
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)
if [ "$http_code" != "200" ]; then
  echo "❌ Falha ao obter token (HTTP $http_code): $body" >&2; exit 1;
fi
TOKEN=$(echo "$body" | jq -r .access)
[ -z "$TOKEN" ] && { echo "❌ Token vazio" >&2; exit 1; }

echo "📦  Listando 5 primeiros produtos…"
curl -sS --max-time $TIMEOUT -H "Authorization: Bearer $TOKEN" "$HOST/api/produtos/?page_size=5" | jq '.results[] | {id,nome,preco}'

FIRST_ID=$(curl -sS --max-time $TIMEOUT -H "Authorization: Bearer $TOKEN" "$HOST/api/produtos/?page_size=1" | jq -r .results[0].id)
[ -z "$FIRST_ID" ] && { echo "❌ Nenhum produto encontrado" >&2; exit 1; }

echo "🛒  Criando pedido com produto $FIRST_ID (qty=2)…"
order=$(curl -sS --max-time $TIMEOUT -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d "{\"itens\":[{\"produto_id\":\"$FIRST_ID\",\"quantidade\":2}]}" "$HOST/api/pedidos/")

echo "$order" | jq '{id,status,total}'
echo "✅  Pedido criado com sucesso!"
```

---


