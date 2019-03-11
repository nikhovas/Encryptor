from Cryptor import Caesar, Vigenere, Vernam
from iomanager import IOManager


cryptors = {'caesar': Caesar, 'vigenere': Vigenere, 'vernam': Vernam}


class Command:

    @staticmethod
    def encode(args):
        if args.algorithm not in cryptors:
            print("[ERROR] no such crypt: {}".format(args.algorithm))
            exit()
        if args.key is None and args.key_raw is None:
            print("[ERROR] there must be key")
            exit()
        io = IOManager(args)
        arr = cryptors[args.algorithm].encrypt(io.input_arr, io.key_arr)
        io.push(arr)

    @staticmethod
    def decode(args):
        if args.algorithm not in cryptors:
            print("[ERROR] no such crypt: {}".format(args.algorithm))
            exit()
        if args.key is None and args.key_raw is None:
            print("[ERROR] there must be key")
            exit()
        io = IOManager(args)
        arr = cryptors[args.algorithm].decrypt(io.input_arr, io.key_arr)
        io.push(arr)

    @staticmethod
    def hack(args):
        if args.algorithm not in cryptors:
            print("[ERROR] no such crypt: {}".format(args.algorithm))
            exit()
        if args.hack_tries is None:
            print("[ERROR] there must be trying number")
            exit()
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
