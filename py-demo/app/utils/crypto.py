import json
from Crypto.Hash import SHA256

def calculateHash(data) -> str:
    if type(data) == str:
        data = bytearray(data, "utf-8")

    h = SHA256.new()
    h.update(data)
    return h.hexdigest()

def transaction_to_bytes(transaction_data: dict):
    new_transaction_data = transaction_data.copy()
    new_transaction_data["sender"] = str(transaction_data["sender"])
    new_transaction_data["receiver"] = str(transaction_data["receiver"])
    new_transaction_data["coin_id"] = str(transaction_data["coin_id"])
    return json.dumps(new_transaction_data, indent=2).encode('utf-8')