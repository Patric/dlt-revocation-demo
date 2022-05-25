class IdentityService:
    def __init__(self, publicKey):
        self.__publicKey = publicKey

    def getPublicKey(self):
        return self.__publicKey