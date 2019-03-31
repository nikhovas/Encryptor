from Cryptor import *
from IOManager import IOManager
import Exceptions
from Globals import cryptors, CryptType


class Command:

    @staticmethod
    def encode(**kwargs):
        if kwargs['algorithm'] not in cryptors:
            raise Exceptions.BadCryptMethodException(kwargs['algorithm'])
        if kwargs['key'] is None and kwargs['key_raw'] is None:
            raise Exceptions.NoKeyException()
        io = IOManager(**kwargs)
        arr = cryptors[kwargs['algorithm']].encrypt(io.input_arr, io.key_arr)
        io.push(arr)

    @staticmethod
    def decode(**kwargs):
        if kwargs['algorithm'] not in cryptors:
            raise Exceptions.BadCryptMethodException(kwargs['algorithm'])
        if kwargs['key'] is None and kwargs['key_raw'] is None:
            raise Exceptions.NoKeyException()
        io = IOManager(**kwargs)
        arr = cryptors[kwargs['algorithm']].decrypt(io.input_arr, io.key_arr)
        io.push(arr)

    @staticmethod
    def hack(**kwargs):
        if kwargs['algorithm'] not in cryptors:
            raise Exceptions.BadCryptMethodException(kwargs['algorithm'])
        if kwargs['hack_tries'] is None:
            raise Exceptions.HackTriesNumberException()
        io = IOManager(**kwargs)
        arr = cryptors[kwargs['algorithm']].hack(io.input_arr, kwargs['hack_tries'])
        io.push_pack(arr)

    @staticmethod
    def cmd_select(**kwargs):
        arg = kwargs['crypt']
        if arg == CryptType.encode.value:
            Command.encode(**kwargs)
        elif arg == CryptType.decode.value:
            Command.decode(**kwargs)
        elif arg == CryptType.hack.value:
            Command.hack(**kwargs)
