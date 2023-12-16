import requests
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Replace with your server's URL
SERVER_URL = "http://127.0.0.1:5000"

def generate_key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
    public_key = private_key.public_key()
    return private_key, public_key

def serialize_public_key(public_key):
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem.decode()

def register_user(username, public_key):
    response = requests.post(f'{SERVER_URL}/register', json={
        'username': username,
        'public_key': public_key
    })
    return response.json()

def get_challenge(username):
    response = requests.post(f'{SERVER_URL}/challenge', json={'username': username})
    return response.json()

def sign_challenge(private_key, challenge):
    signature = private_key.sign(
        challenge,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def login_user(username, signature):
    response = requests.post(f'{SERVER_URL}/login', json={
        'username': username,
        'signature': signature.decode('ISO-8859-1')
    })
    return response.json()

# Example Usage
def main():
    username = "user1"
    private_key, public_key = generate_key_pair()
    serialized_public_key = serialize_public_key(public_key)

    print("Registering user...")
    print(register_user(username, serialized_public_key))

    print("Getting challenge...")
    challenge_response = get_challenge(username)
    challenge = challenge_response['challenge'].encode('ISO-8859-1')

    print("Signing challenge...")
    signature = sign_challenge(private_key, challenge)

    print("Attempting to log in...")
    login_response = login_user(username, signature)
    print(login_response)

if __name__ == "__main__":
    main()
