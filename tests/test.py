import json

from sicret.key_management.conditions import check_key_expiration
from sicret.key_management.keygen import create_key_with_expiration

# Example usage
private_key, public_key, metadata = create_key_with_expiration(days=30)


decoded_metatada = json.loads(metadata.decode())

decoded_metatada['expiration_date'] = '2025-01-01'

metadata = json.dumps(decoded_metatada).encode()

is_valid = check_key_expiration(metadata)


print(is_valid)