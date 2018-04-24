

curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "234dfb7d3fb849f293a682cd41fa5e26",
 "recipient": "42",
 "amount": 1
}' "http://localhost:5000/transactions/new"
