from abc import abstractmethod

class Printable:
 
    def __str__(self):
        return str(self.__dict__)
