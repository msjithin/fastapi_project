curl -X 'POST' \
  'http://localhost:8080/users/4/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "item 3",
  "description": "item 3 description"
}'