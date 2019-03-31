from enum import Enum
from Cryptor import Caesar, Vigenere, Vernam


class CryptType(Enum):
    encode = 'encode'
    decode = 'decode'
    hack = 'hack'

    def __str__(self):
        return self.value


class CryptAlghorithm(Enum):
    caesar = 'caesar'
    vigenere = 'vigenere'
    vernam = 'vernam'

    def __str__(self):
        return self.value


cryptors = {CryptAlghorithm.caesar.value: Caesar, CryptAlghorithm.vigenere.value: Vigenere,
            CryptAlghorithm.vernam.value: Vernam}
