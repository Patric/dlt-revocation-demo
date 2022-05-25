from DHTMetadata import DHTMetadata

class DataDistributor:
    def upload(self, dataLocalPath: str):
        # do DTH stuff
        randomMockFactorToDeleteLater = dataLocalPath
        dhtPaths = ['part1', 'part2', 'part3', 'part4', 'part5', randomMockFactorToDeleteLater]
        return DHTMetadata(dhtPaths)