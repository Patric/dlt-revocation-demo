# patient, hospital, 3rd party,
from LedgerManipulator import LedgerManipulator
from LedgerEntryDTO import LedgerEntryDTO


LedgerManipulator()\
    .appendLedger(LedgerEntryDTO('someEncryptedMetadata1'))\
    .appendLedger(LedgerEntryDTO('someEncryptedMetadata2'))\
    .appendLedger(LedgerEntryDTO('someEncryptedMetadata3'))\
    .appendLedger(LedgerEntryDTO('someEncryptedMetadata4'))\
    .printLedger()
