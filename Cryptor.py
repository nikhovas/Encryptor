from abc import ABC, abstractmethod
from collections import Counter
import Exceptions


class Cryptor(ABC):

    @staticmethod
    @abstractmethod
    def encrypt(byte_arr, key):
        pass

    @staticmethod
    @abstractmethod
    def decrypt(byte_arr, key):
        pass

    @staticmethod
    @abstractmethod
    def hack(byte_arr, trying_num):
        pass


class Caesar(Cryptor):

    @staticmethod
    def encrypt(byte_arr, key):
        if len(key) > 1:
            print('[CAESAR] took 2 or more symbols as key, using first one')
        key = key[0]
        return [(i + key) % 256 for i in byte_arr]

    @staticmethod
    def decrypt(byte_arr, key):
        if len(key) > 1:
            print('[CAESAR] took 2 or more symbols as key, using first one')
        key = key[0]
        return [(i - key) % 256 for i in byte_arr]

    @staticmethod
    def hack(byte_arr, trying_num):
        print('[WARNING] caesar crypt hack works only with english texts and do good results on big texts')
        res = []
        shifts = []
        for c in Counter(byte_arr).most_common(trying_num):
            popularity = c[1] / int(len(byte_arr))
            if popularity < 0.05 or popularity > 0.3:
                print('[WARNING] this is probably not a text')
            key = c[0] - ord('a')
            shifts.append(key)
            res.append([(i - key) % 256 for i in byte_arr])
        for sh in range(len(shifts)):
            print('try {}: shift: {}'.format(sh + 1, shifts[sh]))
        return res


class Vernam(Cryptor):

    @staticmethod
    def encrypt(byte_arr, key):
        data_size = len(byte_arr)
        key_size = len(key)
        return [(byte_arr[i % data_size] ^ key[i % key_size]) % 256 for i in range(data_size)]

    decrypt = encrypt

    @staticmethod
    def hack(byte_arr, trying_num):
        raise Exceptions.NoVernamHackException


class Vigenere(Cryptor):

    @staticmethod
    def encrypt(byte_arr, key):
        data_size = len(byte_arr)
        key_size = len(key)
        return [(byte_arr[i % data_size] + key[i % key_size]) % 256 for i in range(data_size)]

    @staticmethod
    def decrypt(byte_arr, key):
        data_size = len(byte_arr)
        key_size = len(key)
        return [(byte_arr[i % data_size] - key[i % key_size]) % 256 for i in range(data_size)]

    @staticmethod
    def hack(byte_arr, trying_num):
        raise Exceptions.NoVigenereHackException
