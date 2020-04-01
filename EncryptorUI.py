import sys
from PyQt5 import QtWidgets, QtGui
import Design
import os
from Command import Command
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


def default_checks(n: int, caller: EncryptorApp) -> dict:
    value = str(getattr(caller, 'var' + str(n) + '_src').displayText())
    if not os.path.isfile(value):
        raise Exceptions.BadInputFileException()
    dictionary = {'src': value,
                  'dest': str(getattr(caller, 'var' + str(n) + '_dest').displayText()),
                  'algorithm': CryptAlghorithm.list()[caller.cryptType.currentIndex()],
                  'crypt': CryptType.list()[n - 2],
                  'img': str(caller.var2_img.displayText())
                  }
    if n == 2:
        dictionary['useimg'] = dictionary['img'] != ''
    elif n == 3 or n == 4:
        dictionary['useimg'] = getattr(caller, 'var' + str(n) + '_useImg').checkState()
    return dictionary


def set_key(n: int, caller: EncryptorApp) -> dict:
    key = str(getattr(caller, 'var' + str(n) + '_key').displayText())
    keyraw = str(getattr(caller, 'var' + str(n) + '_keyraw').displayText())

    if not os.path.isfile(key) and keyraw == '':
        if key == '':
            raise Exceptions.NoKeyException()
        else:
            raise Exceptions.BadKeyFileException()

    if keyraw != '':
        return {'key_raw': keyraw}
    else:
        return {'key': key}


def set_hack_tries(n: int, caller: EncryptorApp) -> dict:
    return {'hack_tries': caller.var4_hackTries.value()}


def raw_src_mode(caller: EncryptorApp):
    kwargs = {'key_raw': str(caller.var1_keyraw.displayText()),
              'img': str(caller.var1_img.displayText()),
              'useimg': False, 'key': None, 'crypt': 'encode', 'src': os.path.realpath(__file__),
              'dest': caller.var1_dest.displayText()
              }
    raw_src = str(caller.var1_textArea.toPlainText())
    if kwargs['img'] != '':
        if not os.path.isfile(kwargs['img']):
            raise Exceptions.BadImageFileException()
        kwargs['useimg'] = True
    arr = CryptAlghorithm.crypt_class(caller.cryptType.currentIndex()).encrypt(bytearray(raw_src, sys.stdin.encoding),
                                                                               bytearray(kwargs['key_raw'],
                                                                                         sys.stdin.encoding))
    io = IOManager(**kwargs)
    io.push(arr)


def execute_crypt(caller: EncryptorApp):
    cur_tab = caller.tabWidget.currentIndex() + 1
    if cur_tab == 1:
        raw_src_mode(caller)
    else:
        kwargs = {'key': None, 'key_raw': None, 'img': None, 'hack_tries': None}
        kwargs.update(default_checks(cur_tab, caller))
        if cur_tab == 2 or cur_tab == 3:
            kwargs.update(set_key(cur_tab, caller))
        else:
            kwargs.update(set_hack_tries(cur_tab, caller))
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
