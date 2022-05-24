from Block import Block
from typing import List

# create a simple model DTO that can be converted to a json file and sent back and forth
class DistributedLedgerCache():
    
    def __init__(self, blockchain: List[Block]):
        self.__blockchain = blockchain

    @property
    def lastBlock(self):
        return self.__blockchain[len(self.__blockchain) - 1]

    def append(self, block: Block):
        self.__blockchain.append(block)

    def __len__(self):
        return len(self.__blockchain)

    def __str__(self):
        result = ''
        for block in self.__blockchain:
            result += block.__str__() + '\n'
        return result