import os
import hashlib
import base64
import requests


# Generate Code Verifier for Roblox PKCE
def generate_code_verifier(length=43):
    # Generate random URL safe base64 encoded string
    random_bytes = os.urandom(32)
    code_verifier = base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip('=')
    # Ensure length is between 43 & 128
    return code_verifier[:length]

# Create the SHA-256 hash and then convert into Base64 URL encode
def generate_code_challenge(code_verifier):
    sha256_hash = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    # Base64 URL encode the hash
    code_challenge = base64.urlsafe_b64encode(sha256_hash).decode('utf-8').rstrip('=')
    return code_challenge


# Check if ROBLOX OAuth2 Token is Valid for User
def check_roblox_token(code):
    user_url = "https://apis.roblox.com/oauth/v1/userinfo"
    headers = {
        "Authorization": f"Bearer {code}"
    }


    response = requests.get(user_url, headers=headers)
    response_data = response.json()

    if response.status_code == 200:
        data = {
            'userID': response_data.get('sub'),
            'username': response_data.get('name')
        }
        # return True
        return data
    else:
        return False
    


# Tests
# code_verifier = generate_code_verifier()
# code_challenge = generate_code_challenge(code_verifier)

# print("Code Verifier:", code_verifier)
# print("Code Challenge:", code_challenge)