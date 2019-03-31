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
from Globals import *


class EncryptorApp(QtWidgets.QMainWindow, Design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.executeAction.clicked.connect(lambda: execute_crypt(self))
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(script_dir + os.path.sep + 'icon.png'))


def set_src(n: int, caller: EncryptorApp, kwargs: dict):
    value = str(getattr(caller, 'var' + str(n) + '_src').displayText())
    if not os.path.isfile(value):
        raise Exceptions.BadInputFileException()
    kwargs['src'] = value


def set_dest(n: int, caller: EncryptorApp, kwargs: dict):
    kwargs['dest'] = str(getattr(caller, 'var' + str(n) + '_dest').displayText())


def set_key(n: int, caller: EncryptorApp, kwargs: dict):
    key = str(getattr(caller, 'var' + str(n) + '_key').displayText())
    keyraw = str(getattr(caller, 'var' + str(n) + '_keyraw').displayText())

    if not os.path.isfile(key) and keyraw == '':
        if key == '':
            raise Exceptions.NoKeyException()
        else:
            raise Exceptions.BadKeyFileException()

    if keyraw != '':
        kwargs['key_raw'] = keyraw
    else:
        kwargs['key'] = key


def set_crypt_alghorithm(n: int, caller: EncryptorApp, kwargs: dict):
    if n == 1:
        kwargs['crypt'] = CryptType.encode.value
    elif n == 2:
        kwargs['crypt'] = CryptType.encode.value
    elif n == 3:
        kwargs['crypt'] = CryptType.decode.value
    elif n == 4:
        kwargs['crypt'] = CryptType.hack.value
        if caller.cryptType.currentIndex() != 0:
            raise Exceptions.HackIsNotCaesarException()

    if caller.cryptType.currentIndex() == 0:
        kwargs['algorithm'] = CryptAlghorithm.caesar.value
    elif caller.cryptType.currentIndex() == 1:
        kwargs['algorithm'] = CryptAlghorithm.vigenere.value
    else:
        kwargs['algorithm'] = CryptAlghorithm.vernam.value


def set_img(n: int, caller: EncryptorApp, kwargs: dict):
    if n == 2:
        img = str(caller.var2_img.displayText())
        if img != '':
            if not os.path.isfile(img):
                raise Exceptions.BadImageFileException()
            kwargs['img'] = img
            kwargs['useimg'] = True
        else:
            kwargs['useimg'] = False
    elif n == 3 or n == 4:
        if getattr(caller, 'var' + str(n) + '_useImg').checkState():
            kwargs['useimg'] = True
        else:
            kwargs['useimg'] = False


def set_hack_tries(n: int, caller: EncryptorApp, kwargs: dict):
    if n == 4:
        kwargs['hack_tries'] = caller.var4_hackTries.value()


def raw_src_mode(caller: EncryptorApp):
    kwargs = dict()
    raw_src = str(caller.var1_textArea.toPlainText())
    kwargs['key_raw'] = str(caller.var1_keyraw.displayText())
    kwargs['img'] = str(caller.var1_img.displayText())
    kwargs['useimg'] = False
    kwargs['key'] = None
    kwargs['crypt'] = 'encode'
    kwargs['src'] = os.path.realpath(__file__)
    if kwargs['img'] != '':
        if not os.path.isfile(kwargs['img']):
            raise Exceptions.BadImageFileException()
        kwargs['useimg'] = True
    kwargs['dest'] = caller.var1_dest.displayText()
    alg = ''
    if caller.cryptType.currentIndex() == 0:
        alg = CryptAlghorithm.caesar.value
    elif caller.cryptType.currentIndex() == 1:
        alg = CryptAlghorithm.vigenere.value
    else:
        alg = CryptAlghorithm.vernam.value
    arr = cryptors[alg].encrypt(bytearray(raw_src, sys.stdin.encoding), bytearray(kwargs['key_raw'], sys.stdin.encoding))
    io = IOManager(**kwargs)
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
        kwargs = dict()
        kwargs['key'] = None
        kwargs['key_raw'] = None
        kwargs['img'] = None
        kwargs['hack_tries'] = None
        set_dest(cur_tab, caller, kwargs)
        set_crypt_alghorithm(cur_tab, caller, kwargs)
        set_img(cur_tab, caller, kwargs)
        for i in additional_ckecks[cur_tab - 1]:
            i(cur_tab, caller, kwargs)
        Command.cmd_select(**kwargs)


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
