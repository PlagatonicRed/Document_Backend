import hmac, hashlib, json, base64
import os
key_file = os.path.join(os.path.dirname(__file__), 'key.txt')
def encode_jwt(payload, secret):
    try:
        header = {
            "alg": "HS256",
            "typ": "JWT"
        }

        # Encode header and payload
        def base64_url_encode(data):
            json_data = json.dumps(data).encode('utf-8')
            base64_bytes = base64.urlsafe_b64encode(json_data)
            return base64_bytes.decode('utf-8')

        encoded_header = base64_url_encode(header)
        encoded_payload = base64_url_encode(payload)

        # Create the signature
        message = f"{encoded_header}.{encoded_payload}".encode('utf-8')
        signature = hmac.new(secret.encode('utf-8'), message, hashlib.sha256).digest()

        # Convert signature to a hex string
        signature = signature.hex()

        # Create the JWT
        jwt_token = f"{encoded_header}.{encoded_payload}.{signature}"
        return jwt_token
    except Exception as e:
        return None

def decode_jwt(token, secret):
    try:

        # Split the token
        header, payload, signature_hex = token.split('.')

        # Convert the hex signature back to bytes
        signature = bytes.fromhex(signature_hex)

        # Recreate the signature to verify integrity
        message = f"{header}.{payload}".encode('utf-8')
        expected_signature = hmac.new(secret.encode('utf-8'), message, hashlib.sha256).digest()

        if expected_signature != signature:
            return None

        # Decode the payload
        decoded_payload = json.loads(base64.urlsafe_b64decode(payload + '=='))

        return decoded_payload
    except Exception as e:
        return None


def validate_jwt(jwt):
    with open(key_file, 'r') as file:
        secret_key = file.read().strip()

    jwt = decode_jwt(jwt, secret_key)
    # Authorization failed
    if jwt is None:
        print("invalid jwt")
    return jwt


def hash_sha256(data: str) -> str:
    hash_object = hashlib.sha256()

    hash_object.update(data.encode('utf-8'))

    return hash_object.hexdigest()