# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from src.Learning import Learning


class Ui_Dialog(object):
    def __init__(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(120, 90, 160, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.user_id = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.user_id.setObjectName("user_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.user_id)

        self.password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)

        self.cource_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cource_name.setObjectName("cource_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cource_name)

        self.setupUi(Dialog)
        self.buttonBox.accepted.connect(self.run)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setupUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "이러닝 자동 수강"))
        self.label.setText(_translate("Dialog", "학번"))
        self.label_2.setText(_translate("Dialog", "비밀번호"))
        self.label_3.setText(_translate("Dialog", "과목이름"))

    def run(self):
        ln = Learning(self.user_id.text(), self.password.text(), self.cource_name.text())
        ln.learn()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
