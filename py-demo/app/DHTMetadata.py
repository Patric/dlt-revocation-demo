from typing import List
from unittest.util import strclass
from utils.crypto import encrypt

class DHTMetadata:
    def __init__(self, paths: List[str]):
        self.__paths = paths

    @property
    def paths(self):
        return self.__paths

    def __str__(self):
        result = ''
        for path in self.__paths:
            result += path + ','
        return result