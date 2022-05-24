from DataManager import DataManger
from DataManagerProviders import DataManagerProviders

# would serve as a separate application in normal use case. For now will be run in separate thread and simulate a node
class DataManagerClient:
    def __init__(self):
        self.__dataManager = DataManger(DataManagerProviders())
    
    