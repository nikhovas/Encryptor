from Cryptor import *
from IOManager import IOManager
import Exceptions


class Command:

    @staticmethod
    def encode(args):
        if args.algorithm not in cryptors:
            raise Exceptions.BadCryptMethodException(args.algorithm)
        if args.key is None and args.key_raw is None:
            raise Exceptions.NoKeyException()
        io = IOManager(args)
        arr = cryptors[args.algorithm].encrypt(io.input_arr, io.key_arr)
        io.push(arr)

    @staticmethod
    def decode(args):
        if args.algorithm not in cryptors:
            raise Exceptions.BadCryptMethodException(args.algorithm)
        if args.key is None and args.key_raw is None:
            raise Exceptions.NoKeyException()
        io = IOManager(args)
        arr = cryptors[args.algorithm].decrypt(io.input_arr, io.key_arr)
        io.push(arr)

    @staticmethod
    def hack(args):
        if args.algorithm not in cryptors:
            raise Exceptions.BadCryptMethodException(args.algorithm)
        if args.hack_tries is None:
            raise Exceptions.HackTriesNumberException()
        io = IOManager(args)
        arr = cryptors[args.algorithm].hack(io.input_arr, args.hack_tries)
        io.push_pack(arr)

    @staticmethod
    def cmd_select(args):
        arg = args.crypt
        if arg == "encode":
            Command.encode(args)
        elif arg == "decode":
            Command.decode(args)
        elif arg == "hack":
            Command.hack(args)
