from typing import List
from LedgerEntryDTO import LedgerEntryDTO
from DataManagerProviders import DataManagerProviders

class DataManger:
    def __init__(self, dataMangerProviders: DataManagerProviders):
        self.__ledgerManipulator = dataMangerProviders.ledgerManipulator

    def fetchLedger(self):
        self.__ledgerManipulator\
            .appendLedger(LedgerEntryDTO('someEncryptedMetadata1'))\
            .appendLedger(LedgerEntryDTO('someEncryptedMetadata2'))\
            .appendLedger(LedgerEntryDTO('someEncryptedMetadata3'))\
            .appendLedger(LedgerEntryDTO('someEncryptedMetadata4'))\
            .printLedger()
    