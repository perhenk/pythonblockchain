

curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "409e39f088354681886408fecdafeb69",
 "recipient": "42",
 "amount": 2
}' "http://localhost:5000/transactions/new"
