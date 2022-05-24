from Block import Block
from DistributedLedgerCache import DistributedLedgerCache
from LedgerEntryDTO import LedgerEntryDTO
from utils.crypto import calculateHash

class LedgerManipulator:

    # for further use with roaming DistributedLedgerCopy
    def __init__(self, ledger: DistributedLedgerCache):
        self.__ledger = ledger

    def __init__(self):
        self.__ledger = self.__getLedgerWithGenesisBlock()

    def __getLedgerWithGenesisBlock(self):
        return DistributedLedgerCache([Block(0, None, None)])

    def appendLedger(self, ledgerEntryDTO: LedgerEntryDTO):
        #adding block logic, calcualte previous block hash, verify blockchain and stuff
        newIdx = len(self.__ledger)
        self.__ledger.append(Block(newIdx, 
                                   ledgerEntryDTO.encryptedMetadata,
                                   self.__ledger.lastBlock.hash))
        return self

    def printLedger(self):
        print(self.__ledger)
        return self


