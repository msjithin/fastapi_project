curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/users' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "some other name",
  "last_name": "some new last name",
  "middle_name": "middle name",
  "gender": "male",
  "roles": [
    "user", "student"
  ]
}'