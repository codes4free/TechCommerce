# =========================
# demo.sh (novo arquivo raiz)
# =========================
#!/usr/bin/env bash
set -e

HOST="http://localhost:8000"
USERNAME="admin"
PASSWORD="admin123"

# obter token
TOKEN=$(curl -s -X POST "$HOST/api/token/" -H "Content-Type: application/json" -d "{\"username\":\"$USERNAME\",\"password\":\"$PASSWORD\"}" | jq -r .access)

echo "Token: $TOKEN"

# listar produtos
curl -H "Authorization: Bearer $TOKEN" "$HOST/api/produtos/"

# criar pedido simples (1º produto, quantidade 2)
FIRST_ID=$(curl -s -H "Authorization: Bearer $TOKEN" "$HOST/api/produtos/?page_size=1" | jq -r .results[0].id)

curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
     -d "{\"itens\":[{\"produto_id\":\"$FIRST_ID\",\"quantidade\":2}] }" \
     "$HOST/api/pedidos/"

echo -e "\nPedido criado!"
echo "Raw token response:" $(curl -s -X POST "$HOST/api/token/" -H "Content-Type: application/json" -d "{\"username\":\"$USERNAME\",\"password\":\"$PASSWORD\"}")