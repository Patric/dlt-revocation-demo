from DataManager import DataManger
from DataManagerProviders import *

# would serve as a separate application in normal use case. For now will be run in separate thread and simulate a node
class DataManagerClient:
    def __init__(self, publicKey: str):
        self.__dataManager = DataManger(DataManagerProviders(DataManagerProvidersEnvs(
            publicKey
        )))
        self.__publicKey = publicKey
        self.synchronize()

    def synchronize(self):
        self.__dataManager.fetchLedger()

    def printCachedLedger(self):
        self.__dataManager.printCachedLedger()

    def addData(self, dataPath: str):
        self.__dataManager.upload(dataPath)

    def getPublicKey(self):
        return self.__publicKey