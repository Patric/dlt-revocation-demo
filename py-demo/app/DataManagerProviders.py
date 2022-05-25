from LedgerManipulator import LedgerManipulator
from DataDistributor import DataDistributor
from IdentityService import IdentityService

class DataManagerProvidersEnvs:
    def __init__(self, publicKey):
        self.__publicKey = publicKey
    @property
    def publicKey(self):
        return self.__publicKey

class DataManagerProviders:

    def __init__(self, envs: DataManagerProvidersEnvs):
        # later change to providers to be able to DI infrastracture objects, generally rethink DI pattern
        self.__ledgerManipulator = LedgerManipulator()
        self.__dataDistributor = DataDistributor()
        self.__identityService = IdentityService(envs.publicKey)

    @property
    def ledgerManipulator(self):
        return self.__ledgerManipulator

    @property
    def dataDistributor(self):
        return self.__dataDistributor

    @property
    def identityService(self):
        return self.__identityService