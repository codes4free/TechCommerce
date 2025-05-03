## 4. demo.sh (scripts/demo.sh)
```bash
#!/usr/bin/env bash
set -euo pipefail
HOST="http://localhost:8000"
USERNAME="${USERNAME:-admin}"
PASSWORD="${PASSWORD:-admin123}"
# get token
response=$(curl -s -w "%{http_code}" -H "Content-Type: application/json" \
            -d "{\"username\":\"${USERNAME}\",\"password\":\"${PASSWORD}\"}" \
            "$HOST/api/token/")
http_code="${response: -3}"
body="${response::-3}"
if [ "$http_code" != "200" ]; then
  echo "Token request failed: HTTP $http_code – $body" >&2; exit 1;
fi
TOKEN=$(echo "$body" | jq -r '.access')

# list products
curl -s -H "Authorization: Bearer $TOKEN" "$HOST/api/produtos/?page_size=5" | jq '.results[] | {id,nome,preco}'
```

---


