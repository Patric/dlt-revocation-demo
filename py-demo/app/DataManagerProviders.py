from LedgerManipulator import LedgerManipulator

class DataManagerProviders:

    def __init__(self):
        self.__ledgerManipulator = LedgerManipulator()

    @property
    def ledgerManipulator(self):
        return self.__ledgerManipulator