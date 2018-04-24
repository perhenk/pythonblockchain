

curl -X POST -H "Content-Type: application/json" -d '{
   "nodes":["http://localhost:5000"]
}' "http://localhost:5001/nodes/register"
