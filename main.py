from Command import Command
import argparse
import sys


def exception_handler(exctype, value, traceback):
    if exctype == FileNotFoundError:
        print(value)
    elif exctype == KeyboardInterrupt:
        print("[ERROR] interrupted by user")
    else:
        sys.__excepthook__(exctype, value, traceback)


sys.excepthook = exception_handler


parser = argparse.ArgumentParser()
parser.add_argument('crypt', type=str, help='what to do')
parser.add_argument('algorithm', type=str, help='crypt type')
parser.add_argument('src', type=str, help='source')
parser.add_argument('dest', type=str, help='destination')
parser.add_argument('--key', type=str, help='key')
parser.add_argument('--key_raw', type=str, help='key')
parser.add_argument('--img', type=str, help='image')
parser.add_argument('--hack_tries', type=int, help='image')
parser.add_argument('--useimg', dest='useimg', action="store_true")
parser.set_defaults(useimg=False)
args = parser.parse_args()


Command.cmd_select(args)