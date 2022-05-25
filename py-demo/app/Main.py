# patient, hospital, 3rd party,
from DataManagerClient import DataManagerClient

client1 = DataManagerClient('somePrivateKey1')
print('Client 1 public key is: %s' %(client1.getPublicKey()))
client1.addData('/some/data')
client1.printCachedLedger()
