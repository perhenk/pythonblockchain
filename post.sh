

curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "50de1839f70c45cdb4e18e3590526258",
 "recipient": "42",
 "amount": 5
}' "http://localhost:5000/transactions/new"
