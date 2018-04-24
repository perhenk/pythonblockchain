from flask import Flask, jsonify, request
import json
from uuid import uuid4

from blockchain import Blockchain

app = Flask(__name__)

# Lag en unik id hvor minet coin går til
node_identifier = str(uuid4()).replace('-','')

blockchain = Blockchain()

@app.route('/mine', methods=["GET"])
def mine():

    # Kjør Proof of work for å skaffe neste bevis
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Hent gevinsten ved å finne beviest
    # Sender 0 betyr at vi har minet en ny enhet
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # Lag en ny blokk
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """ 
    Lag en ny transaksjon
    """
    values = request.get_json()

    # Sjekk at påkrevde felter er lagt ved
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return "Mangler verdier ", 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    if index == None:
        return "Ikke nok penger i lommeboken  "
    
    response = {'message': 'Transaksjonen vil legges på blokk '+str(index)+' ', }
    return jsonify(response), 201
    

@app.route('/chain', methods=["GET"])
def full_chain():
    response =  {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response)

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return 'Feil: vennligst legg ved en liste med noder',400

    for node in nodes:
        blockchain.register_node(node)


    response = {
        'message':'Nye noder har blitt lagt til',
        'total_nodes': list(blockchain.nodes)
    }
    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message':'Vår kjede er byttet ut',
            'new_chain':blockchain.chain
        }
    else:
        response = {
            'message':'Vi beholder vår kjede',
            'chain':blockchain.chain
        }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
