import json

def toJSONBytes(data: dict) -> bytes:
    return json.dumps(data, indent=2).encode('utf-8')

def toJSONString(data: dict) -> str:
    return json.dumps(data, indent=2)