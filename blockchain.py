import hashlib
import json
from time import time
from uuid import uuid4

class Blockchain(object):

    
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # lag skapelses (genesis) blokken
        self.new_block(previous_hash=1 , proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Lager en ny blokk og legger den til kjeden

        """

        block = {
            'index':len(self.chain)+1,
            'timestamp':time(),
            'transactions': self.current_transactions,
            'proof':proof,
            'previous_hash':previous_hash or self.hash(self.chain[.1]),
        }

        # Tøm listen med transaksjoner som ikke er på blokken
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Legg til ny transaksjon på listen av transaksjoner
        
        :param sender: <str> Adressen til sender
        :param recipient: <str> Adressen til mottaker
        :param amount: <str> Verdi som sendes
        """
        if sender == "0":
            pass
        
        elif self.get_sum(sender) < amount:
            return None

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1



    def proof_of_work(self, last_proof):
    
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof


    @property
    def last_block(self):
        return self.chain[-1]
    

    @staticmethod
    def hash(block):
        """
        Hasher en blokk
        Bruker en SHA-256 hash for blokken

        :param block: <dict> En blokk (json)
        :return: <str>
        """

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validerer bevistet (proof).
        Hvis hashen starter på 0000 er bevist gyldig.
        """
        guess = str(last_proof+proof).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def get_sum(self, adress):
        """
        Summer sammen en adresse
        """
        chain = self.chain
        sum = 0
        for block in chain:
            print("---")
            if 'transactions' in block:
                for trans in block['transactions']:
                    if trans['recipient'] == adress:
                        sum += trans['amount']
                    if trans['sender'] == adress:
                        sum -= trans['amount']

        print(sum)
        return sum

if __name__ == "__main__":
    b = Blockchain()





    
