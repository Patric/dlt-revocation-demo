from utils.Printable import *

class LedgerEntryDTO(Printable):
    def __init__(self, encryptedMetadata: str):
        self.__encryptedMetadata = encryptedMetadata

    @property
    def encryptedMetadata(self):
        return self.__encryptedMetadata