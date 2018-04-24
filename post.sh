

curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "bd05b4989a7c4b53a5aeda5c56911546",
 "recipient": "42",
 "amount": 5
}' "http://localhost:5000/transactions/new"
