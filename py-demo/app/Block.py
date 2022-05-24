import string
from utils.crypto import calculateHash
from utils.json import *
from utils.Printable import *

class Block(Printable):

    def __init__(self, idx: int, encryptedMetadata: string, previousBlockHash: string):
        self.__idx = idx
        self.__encryptedMetadata = encryptedMetadata
        self.__previousBlockHash = previousBlockHash

    @property
    def previousHash(self):
        return self.__previousBlockHash

    @property
    def getEncryptedMetadata(self):
        return self.__previousBlockHash

    @property
    def hash(self) -> str:
        return calculateHash(toJSONBytes(self.__dict__))

    