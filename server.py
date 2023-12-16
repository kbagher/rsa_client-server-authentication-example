from flask import Flask, request, jsonify
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    pub_key = serialization.load_pem_public_key(data['public_key'].encode())

    users[username] = {
        'public_key': pub_key,
        'challenge': None  # Placeholder for challenge
    }

    return jsonify({'status': 'success'}), 200

@app.route('/challenge', methods=['POST'])
def generate_challenge():
    username = request.json['username']
    if username not in users:
        return jsonify({'status': 'user not found'}), 404

    # Generate a random challenge
    challenge = os.urandom(32)
    users[username]['challenge'] = challenge
    return jsonify({'challenge': challenge.decode('ISO-8859-1')}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    signature = data['signature'].encode('ISO-8859-1')

    if username not in users or users[username]['challenge'] is None:
        return jsonify({'status': 'failure'}), 401

    pub_key = users[username]['public_key']
    challenge = users[username]['challenge']

    try:
        pub_key.verify(
            signature,
            challenge,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'failure'}), 401

if __name__ == '__main__':
    app.run(debug=True)
