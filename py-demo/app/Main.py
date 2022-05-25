# patient, hospital, 3rd party,
from DataManagerClient import DataManagerClient

client1 = DataManagerClient('somePrivateKey1')
print('Client 1 public key is: %s' %(client1.getPublicKey()))
client1.addData('/some/data')
client1.printCachedLedger()

client2 = DataManagerClient('somePrivateKey2')
print('Client 2 public key is: %s' %(client2.getPublicKey()))
client2.addData('/some/data2')
client2.printCachedLedger()

