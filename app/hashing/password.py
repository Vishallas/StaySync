import hashlib

HASH_SALT =b"@/$"

def form_password(data):
    hash_form = hashlib.sha256(HASH_SALT+data.encode()+HASH_SALT).hexdigest()
    return hash_form