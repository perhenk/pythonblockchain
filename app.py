from flask import Flask

from uuid import uuid4

from blockchain import Blockchain

app = Flask(__name__)

# Lag en unik id
node_identifier = str(uuid4()).replace('-','')

blockchain = Blockchain()

@app.route('/mine', methods=["GET"])
def mine():
    return "Du miner"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
