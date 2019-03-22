import sys
from PyQt5 import QtWidgets, QtGui
import Design
import argparse
import os
from Command import Command
from Cryptor import *
from IOManager import IOManager
import Exceptions
import Locales


class EncryptorApp(QtWidgets.QMainWindow, Design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.executeAction.clicked.connect(lambda: execute_crypt(self))
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(script_dir + os.path.sep + 'icon.png'))


def set_src(n: int, caller: EncryptorApp, args: argparse.Namespace):
    value = str(getattr(caller, 'var' + str(n) + '_src').displayText())
    if not os.path.isfile(value):
        raise Exceptions.BadInputFileException()
    args.src = value


def set_dest(n: int, caller: EncryptorApp, args: argparse.Namespace):
    args.dest = str(getattr(caller, 'var' + str(n) + '_dest').displayText())


def set_key(n: int, caller: EncryptorApp, args: argparse.Namespace):
    key = str(getattr(caller, 'var' + str(n) + '_key').displayText())
    keyraw = str(getattr(caller, 'var' + str(n) + '_keyraw').displayText())

    if not os.path.isfile(key) and keyraw == '':
        if key == '':
            raise Exceptions.NoKeyException()
        else:
            raise Exceptions.BadKeyFileException()

    if keyraw != '':
        args.key_raw = keyraw
    else:
        args.key = key


def set_crypt_alghorithm(n: int, caller: EncryptorApp, args: argparse.Namespace):
    if n == 1:
        args.crypt = 'encode'
    elif n == 2:
        args.crypt = 'encode'
    elif n == 3:
        args.crypt = 'decode'
    elif n == 4:
        args.crypt = 'hack'
        if caller.cryptType.currentIndex() != 0:
            raise Exceptions.HackIsNotCaesarException()

    if caller.cryptType.currentIndex() == 0:
        args.algorithm = 'caesar'
    elif caller.cryptType.currentIndex() == 1:
        args.algorithm = 'vigenere'
    else:
        args.algorithm = 'vernam'


def set_img(n: int, caller: EncryptorApp, args: argparse.Namespace):
    if n == 2:
        img = str(caller.var2_img.displayText())
        if img != '':
            if not os.path.isfile(img):
                raise Exceptions.BadImageFileException()
            args.img = img
            args.useimg = True
        else:
            args.useimg = False
    elif n == 3 or n == 4:
        if getattr(caller, 'var' + str(n) + '_useImg').checkState():
            args.useimg = True
        else:
            args.useimg = False


def set_hack_tries(n: int, caller: EncryptorApp, args: argparse.Namespace):
    if n == 4:
        args.hack_tries = caller.var4_hackTries.value()


def raw_src_mode(caller: EncryptorApp):
    args = argparse.Namespace()
    raw_src = str(caller.var1_textArea.toPlainText())
    args.key_raw = str(caller.var1_keyraw.displayText())
    args.img = str(caller.var1_img.displayText())
    args.useimg = False
    args.key = None
    args.crypt = 'encode'
    args.src = os.path.realpath(__file__)
    if args.img != '':
        if not os.path.isfile(args.img):
            raise Exceptions.BadImageFileException()
        args.useimg = True
    args.dest = caller.var1_dest.displayText()
    alg = ''
    if caller.cryptType.currentIndex() == 0:
        alg = 'caesar'
    elif caller.cryptType.currentIndex() == 1:
        alg = 'vigenere'
    else:
        alg = 'vernam'
    arr = cryptors[alg].encrypt(bytearray(raw_src, sys.stdin.encoding), bytearray(args.key_raw, sys.stdin.encoding))
    io = IOManager(args)
    io.push(arr)



def execute_crypt(caller: EncryptorApp):
    additional_ckecks = [[],
                         [set_src, set_key],
                         [set_src, set_key],
                         [set_src, set_hack_tries]]
    cur_tab = caller.tabWidget.currentIndex() + 1
    if cur_tab == 1:
        raw_src_mode(caller)
    else:
        args = argparse.Namespace()
        args.key = None
        args.key_raw = None
        args.img = None
        args.hack_tries = None
        set_dest(cur_tab, caller, args)
        set_crypt_alghorithm(cur_tab, caller, args)
        set_img(cur_tab, caller, args)
        for i in additional_ckecks[cur_tab - 1]:
            i(cur_tab, caller, args)
        Command.cmd_select(args)


def exception_handler(exctype, value, traceback):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText(str(value))
    msg.setWindowTitle("Ошибка")
    msg.exec_()


if __name__ == '__main__':
    sys.excepthook = exception_handler
    Locales.locales = Locales.rus_locales
    app = QtWidgets.QApplication(sys.argv)
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'icon.png'))
    app.setApplicationName('Encryptor')
    app.setApplicationDisplayName('Encryptor')
    window = EncryptorApp()
    window.show()
    app.exec_()
