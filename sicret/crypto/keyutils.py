import base64
import json
from datetime import datetime, timedelta

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def generate_keys(key_size=2048):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
    public_key = private_key.public_key()

    public_key_serialized = serialize(public_key)
    private_key_serialized = serialize(private_key, is_private=True)

    return private_key_serialized.decode("utf-8"), public_key_serialized.decode("utf-8")


def serialize(key, is_private=False):
    if is_private:
        return key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
    else:
        return key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )


def encrypt_data(public_key_str, message):
    """
    Encrypts the message using the provided public key string.
    """
    public_key = serialization.load_pem_public_key(public_key_str.encode("utf-8"))

    encrypted = public_key.encrypt(
        message.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    # Return the encrypted data encoded in Base64
    return base64.b64encode(encrypted).decode("utf-8")


def decrypt_data(private_key_str, encrypted_message):
    """
    Decrypts the encrypted message using the provided private key string.
    """
    private_key = serialization.load_pem_private_key(
        private_key_str.encode("utf-8"), password=None
    )

    decrypted = private_key.decrypt(
        base64.b64decode(encrypted_message),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    return decrypted.decode("utf-8")
