from Crypto.Hash import SHA256

def calculateHash(data) -> str:
    if type(data) == str:
        data = bytearray(data, "utf-8")

    h = SHA256.new()
    h.update(data)
    return h.hexdigest()

def encrypt(data, publicKey) -> str:
    # use asymmetric encryption
    return calculateHash(data)