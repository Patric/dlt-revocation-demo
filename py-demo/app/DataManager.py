from LedgerEntryDTO import LedgerEntryDTO
from DataManagerProviders import DataManagerProviders
from DHTMetadata import DHTMetadata
from utils.crypto import encrypt

class DataManger:
    def __init__(self, dataMangerProviders: DataManagerProviders):
        self.__ledgerManipulator = dataMangerProviders.ledgerManipulator
        self.__dataDistributor = dataMangerProviders.dataDistributor
        self.__identityService = dataMangerProviders.identityService

    def fetchLedger(self):
        # infrastracture layer will be added

        # mock
        self.__ledgerManipulator\
            .appendLedger(LedgerEntryDTO('someEncryptedMetadata1'))\
            .appendLedger(LedgerEntryDTO('someEncryptedMetadata2'))\
            .appendLedger(LedgerEntryDTO('someEncryptedMetadata3'))\
            .appendLedger(LedgerEntryDTO('someEncryptedMetadata4'))\
    
    def printCachedLedger(self):
        self.__ledgerManipulator.printLedger()
    
    def upload(self, dataPath: str):
        # add basic validation of the data
        metadata = self.__distribute(dataPath)
        ledgerEntry = LedgerEntryDTO(self.__encryptMetadata(metadata))
        self.__ledgerManipulator.appendLedger(ledgerEntry)

    def __distribute(self, dataPath: str) -> DHTMetadata:
        distributedHashTableMetadata = self.__dataDistributor.upload(dataPath)
        return distributedHashTableMetadata

    def __encryptMetadata(self, metadata: DHTMetadata):
        return encrypt(metadata.__str__(), self.__identityService.getPublicKey())
