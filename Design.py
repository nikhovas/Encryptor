from PyQt5 import QtCore, QtGui, QtWidgets
import platform
import os


class FileEdit(QtWidgets.QLineEdit):
    def __init__(self, parent):
        super(FileEdit, self).__init__(parent)

        self.setDragEnabled(True)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if (urls and urls[0].scheme() == 'file'):
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        print(urls)
        if (urls and urls[0].scheme() == 'file'):
            filepath = str(urls[0].path())[1:]
            if platform.system() in ['Darwin', 'Linux']:
                filepath = '/' + filepath
            self.setText(filepath)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Шифратор")
        MainWindow.resize(573, 344)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        MainWindow.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'icon.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")

        # raw text encrypt
        self.tab_0 = QtWidgets.QWidget()
        self.tab_0.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # text filed
        self.var1_textArea = QtWidgets.QTextEdit(self.tab_0)
        self.var1_textArea.setObjectName("var1_textArea")
        self.verticalLayout_2.addWidget(self.var1_textArea)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # key field
        self.var1_keyraw = QtWidgets.QLineEdit(self.tab_0)
        self.var1_keyraw.setObjectName("var1_keyraw")
        self.horizontalLayout_3.addWidget(self.var1_keyraw)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # image field
        self.var1_img = FileEdit(self.tab_0)
        self.var1_img.setObjectName("var1_img")
        self.horizontalLayout_4.addWidget(self.var1_img)
        # destination file field
        self.var1_dest = FileEdit(self.tab_0)
        self.var1_dest.setObjectName("var1_dest")
        self.horizontalLayout_4.addWidget(self.var1_dest)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_0, "")

        # file encrypt
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout.setObjectName("gridLayout")
        # key field
        self.var2_key = FileEdit(self.tab_1)
        self.var2_key.setObjectName("var2_key")
        self.gridLayout.addWidget(self.var2_key, 2, 0, 1, 1)
        # raw key field
        self.var2_keyraw = QtWidgets.QLineEdit(self.tab_1)
        self.var2_keyraw.setObjectName("var2_keyraw")
        self.gridLayout.addWidget(self.var2_keyraw, 3, 0, 1, 1)
        # destination file field
        self.var2_dest = FileEdit(self.tab_1)
        self.var2_dest.setObjectName("var2_dest")
        self.gridLayout.addWidget(self.var2_dest, 1, 0, 1, 1)
        # image file field
        self.var2_img = FileEdit(self.tab_1)
        self.var2_img.setObjectName("var2_img")
        self.gridLayout.addWidget(self.var2_img, 5, 0, 1, 1)
        # source file field
        self.var2_src = FileEdit(self.tab_1)
        self.var2_src.setObjectName("var2_src")
        self.gridLayout.addWidget(self.var2_src, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")

        # file decrypt
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.var3_useImg = QtWidgets.QCheckBox(self.tab_2)
        # image flag
        self.var3_useImg.setObjectName("var3_useImg")
        self.gridLayout_2.addWidget(self.var3_useImg, 4, 0, 1, 1)
        self.var3_dest = FileEdit(self.tab_2)
        # destination file field
        self.var3_dest.setObjectName("var3_src")
        self.gridLayout_2.addWidget(self.var3_dest, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 5, 0, 1, 1)
        # key file field
        self.var3_key = FileEdit(self.tab_2)
        self.var3_key.setObjectName("var3_key")
        self.gridLayout_2.addWidget(self.var3_key, 2, 0, 1, 1)
        # raw key value
        self.var3_keyraw = QtWidgets.QLineEdit(self.tab_2)
        self.var3_keyraw.setObjectName("var2_keyraw_2")
        self.gridLayout_2.addWidget(self.var3_keyraw, 3, 0, 1, 1)
        # source file field
        self.var3_src = FileEdit(self.tab_2)
        self.var3_src.setObjectName("var3_dest")
        self.gridLayout_2.addWidget(self.var3_src, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")

        # hack file
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        # image flag
        self.var4_useImg = QtWidgets.QCheckBox(self.tab_3)
        self.var4_useImg.setObjectName("var4_useImg")
        self.gridLayout_3.addWidget(self.var4_useImg, 4, 0, 1, 1)
        # destination file field
        self.var4_dest = FileEdit(self.tab_3)
        self.var4_dest.setObjectName("var4_dest")
        self.gridLayout_3.addWidget(self.var4_dest, 1, 0, 1, 1)
        # hack tries label
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)
        # source file field
        self.var4_src = FileEdit(self.tab_3)
        self.var4_src.setObjectName("var4_src")
        self.gridLayout_3.addWidget(self.var4_src, 0, 0, 1, 1)
        # hack tries field
        self.var4_hackTries = QtWidgets.QSpinBox(self.tab_3)
        self.var4_hackTries.setObjectName("var4_hackTries")
        self.var4_hackTries.setValue(7)
        self.gridLayout_3.addWidget(self.var4_hackTries, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 5, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # bottom part
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.cryptType = QtWidgets.QComboBox(self.centralwidget)
        self.cryptType.setObjectName("cryptType")
        self.cryptType.addItem("")
        self.cryptType.addItem("")
        self.cryptType.addItem("")
        self.horizontalLayout.addWidget(self.cryptType)
        self.executeAction = QtWidgets.QPushButton(self.centralwidget)
        self.executeAction.setObjectName("executeAction")
        self.horizontalLayout.addWidget(self.executeAction)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encryptor"))

        # tab 1
        self.var1_keyraw.setPlaceholderText(_translate("MainWindow", "Ключ"))
        self.var1_img.setPlaceholderText(_translate("MainWindow", "Изображение"))
        self.var1_dest.setPlaceholderText(_translate("MainWindow", "Файл для сохранения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_0), _translate("MainWindow", "Шифровать текст"))

        # tab 2
        self.var2_key.setPlaceholderText(_translate("MainWindow", "Путь к файлу ключа"))
        self.var2_keyraw.setPlaceholderText(_translate("MainWindow", "Текстовое значение ключа"))
        self.var2_dest.setPlaceholderText(_translate("MainWindow", "Путь к файлу назначения"))
        self.var2_img.setPlaceholderText(_translate("MainWindow", "Путь к картинке"))
        self.var2_src.setPlaceholderText(_translate("MainWindow", "Путь к файлу для шифровки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Шифровать файл"))

        # tab 3
        self.var3_useImg.setText(_translate("MainWindow", "Использование картинки (скенанографии)"))
        self.var3_dest.setPlaceholderText(_translate("MainWindow", "Путь назначения"))
        self.var3_key.setPlaceholderText(_translate("MainWindow", "Путь к файлу ключа"))
        self.var3_keyraw.setPlaceholderText(_translate("MainWindow", "Текстовое значение ключа"))
        self.var3_src.setPlaceholderText(_translate("MainWindow", "Путь к файлу "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Расшифровать"))

        # tab 4
        self.var4_useImg.setText(_translate("MainWindow", "Использование картинки (скенанографии)"))
        self.var4_dest.setPlaceholderText(_translate("MainWindow", "Путь назначения"))
        self.label_14.setText(_translate("MainWindow", "Количество попыток взлома"))
        self.var4_src.setPlaceholderText(_translate("MainWindow", "Путь к файлу"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Взлом"))

        # bottom
        self.cryptType.setItemText(0, _translate("MainWindow", "Цезарь"))
        self.cryptType.setItemText(1, _translate("MainWindow", "Виженер"))
        self.cryptType.setItemText(2, _translate("MainWindow", "Вернам"))
        self.executeAction.setText(_translate("MainWindow", "Выполнить"))
