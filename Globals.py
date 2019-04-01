from enum import Enum
from Cryptor import Caesar, Vigenere, Vernam


class CryptType(Enum):
    encode = 'encode'
    decode = 'decode'
    hack = 'hack'

    def __str__(self):
        return self.value

    @staticmethod
    def list() -> tuple:
        return ('encode', 'decode', 'hack')


class CryptAlghorithm(Enum):
    caesar = 'caesar'
    vigenere = 'vigenere'
    vernam = 'vernam'

    def __str__(self):
        return self.value

    @staticmethod
    def list() -> tuple:
        return ('caesar', 'vigenere', 'vernam')

    @staticmethod
    def crypt_class(arg):
        if isinstance(arg, str):
            return {'caesar': Caesar, 'vigenere': Vigenere, 'vernam': Vernam}[arg]
        elif isinstance(arg, int):
            return (Caesar, Vigenere, Vernam)[arg]
