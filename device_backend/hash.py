import hashlib

def hash(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

print(hash("5678"))
