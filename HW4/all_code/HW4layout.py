# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HW4_layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(944, 1160)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.controlLayout = QtWidgets.QGridLayout()
        self.controlLayout.setHorizontalSpacing(6)
        self.controlLayout.setObjectName("controlLayout")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setMinimumSize(QtCore.QSize(100, 0))
        self.label_8.setObjectName("label_8")
        self.controlLayout.addWidget(self.label_8, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setObjectName("label_3")
        self.controlLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.p2Cutoff = QtWidgets.QLineEdit(Form)
        self.p2Cutoff.setObjectName("p2Cutoff")
        self.controlLayout.addWidget(self.p2Cutoff, 1, 2, 1, 1)
        self.p3Cutoff = QtWidgets.QLineEdit(Form)
        self.p3Cutoff.setObjectName("p3Cutoff")
        self.controlLayout.addWidget(self.p3Cutoff, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setObjectName("label_4")
        self.controlLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.controlLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.controlLayout.addWidget(self.label_9, 2, 1, 1, 1)
        self.p4constantB = QtWidgets.QLineEdit(Form)
        self.p4constantB.setObjectName("p4constantB")
        self.controlLayout.addWidget(self.p4constantB, 4, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.controlLayout.addWidget(self.label_7, 4, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setObjectName("label_6")
        self.controlLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setObjectName("label_11")
        self.controlLayout.addWidget(self.label_11, 5, 1, 1, 1)
        self.p4constantK = QtWidgets.QLineEdit(Form)
        self.p4constantK.setObjectName("p4constantK")
        self.controlLayout.addWidget(self.p4constantK, 5, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setObjectName("label_12")
        self.controlLayout.addWidget(self.label_12, 5, 3, 1, 1)
        self.p4constantT = QtWidgets.QLineEdit(Form)
        self.p4constantT.setObjectName("p4constantT")
        self.controlLayout.addWidget(self.p4constantT, 5, 2, 1, 1)
        self.p4constantA = QtWidgets.QLineEdit(Form)
        self.p4constantA.setObjectName("p4constantA")
        self.controlLayout.addWidget(self.p4constantA, 4, 2, 1, 1)
        self.p3GammaH = QtWidgets.QLineEdit(Form)
        self.p3GammaH.setObjectName("p3GammaH")
        self.controlLayout.addWidget(self.p3GammaH, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.controlLayout.addWidget(self.label, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setObjectName("label_5")
        self.controlLayout.addWidget(self.label_5, 1, 3, 1, 1)
        self.p2nValue = QtWidgets.QLineEdit(Form)
        self.p2nValue.setObjectName("p2nValue")
        self.controlLayout.addWidget(self.p2nValue, 1, 4, 1, 1)
        self.p2Confirm = QtWidgets.QPushButton(Form)
        self.p2Confirm.setObjectName("p2Confirm")
        self.controlLayout.addWidget(self.p2Confirm, 1, 5, 1, 1)
        self.p3Confirm = QtWidgets.QPushButton(Form)
        self.p3Confirm.setObjectName("p3Confirm")
        self.controlLayout.addWidget(self.p3Confirm, 2, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.controlLayout.addWidget(self.label_10, 2, 3, 1, 1)
        self.p3cValue = QtWidgets.QLineEdit(Form)
        self.p3cValue.setObjectName("p3cValue")
        self.controlLayout.addWidget(self.p3cValue, 2, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAutoFillBackground(False)
        self.label_13.setObjectName("label_13")
        self.controlLayout.addWidget(self.label_13, 3, 3, 1, 1)
        self.p3GammaL = QtWidgets.QLineEdit(Form)
        self.p3GammaL.setObjectName("p3GammaL")
        self.controlLayout.addWidget(self.p3GammaL, 3, 4, 1, 1)
        self.p4Confirm = QtWidgets.QPushButton(Form)
        self.p4Confirm.setObjectName("p4Confirm")
        self.controlLayout.addWidget(self.p4Confirm, 4, 5, 1, 1)
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setMinimumSize(QtCore.QSize(310, 0))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.controlLayout.addWidget(self.label_15, 0, 6, 1, 1)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setMinimumSize(QtCore.QSize(0, 0))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.controlLayout.addWidget(self.label_16, 3, 5, 1, 1)
        self.p1Confirm = QtWidgets.QPushButton(Form)
        self.p1Confirm.setObjectName("p1Confirm")
        self.controlLayout.addWidget(self.p1Confirm, 0, 5, 1, 1)
        self.load = QtWidgets.QPushButton(Form)
        self.load.setMinimumSize(QtCore.QSize(200, 0))
        self.load.setObjectName("load")
        self.controlLayout.addWidget(self.load, 0, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setObjectName("label_14")
        self.controlLayout.addWidget(self.label_14, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.controlLayout)
        self.imageLayout = QtWidgets.QGridLayout()
        self.imageLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.imageLayout.setObjectName("imageLayout")
        self.originalImage = QtWidgets.QLabel(Form)
        self.originalImage.setMinimumSize(QtCore.QSize(300, 300))
        self.originalImage.setText("")
        self.originalImage.setObjectName("originalImage")
        self.imageLayout.addWidget(self.originalImage, 0, 0, 1, 1)
        self.modifiedImage1 = QtWidgets.QLabel(Form)
        self.modifiedImage1.setMinimumSize(QtCore.QSize(300, 300))
        self.modifiedImage1.setText("")
        self.modifiedImage1.setObjectName("modifiedImage1")
        self.imageLayout.addWidget(self.modifiedImage1, 0, 1, 1, 1)
        self.modifiedImage2 = QtWidgets.QLabel(Form)
        self.modifiedImage2.setMinimumSize(QtCore.QSize(300, 300))
        self.modifiedImage2.setText("")
        self.modifiedImage2.setObjectName("modifiedImage2")
        self.imageLayout.addWidget(self.modifiedImage2, 0, 2, 1, 1)
        self.modifiedImage3 = QtWidgets.QLabel(Form)
        self.modifiedImage3.setMinimumSize(QtCore.QSize(300, 300))
        self.modifiedImage3.setText("")
        self.modifiedImage3.setObjectName("modifiedImage3")
        self.imageLayout.addWidget(self.modifiedImage3, 1, 0, 1, 1)
        self.modifiedImage4 = QtWidgets.QLabel(Form)
        self.modifiedImage4.setMinimumSize(QtCore.QSize(300, 300))
        self.modifiedImage4.setText("")
        self.modifiedImage4.setObjectName("modifiedImage4")
        self.imageLayout.addWidget(self.modifiedImage4, 1, 1, 1, 1)
        self.modifiedImage5 = QtWidgets.QLabel(Form)
        self.modifiedImage5.setMinimumSize(QtCore.QSize(300, 300))
        self.modifiedImage5.setText("")
        self.modifiedImage5.setObjectName("modifiedImage5")
        self.imageLayout.addWidget(self.modifiedImage5, 1, 2, 1, 1)
        self.modifiedImage7 = QtWidgets.QLabel(Form)
        self.modifiedImage7.setMinimumSize(QtCore.QSize(300, 300))
        self.modifiedImage7.setText("")
        self.modifiedImage7.setObjectName("modifiedImage7")
        self.imageLayout.addWidget(self.modifiedImage7, 2, 1, 1, 1)
        self.modifiedImage6 = QtWidgets.QLabel(Form)
        self.modifiedImage6.setMinimumSize(QtCore.QSize(300, 300))
        self.modifiedImage6.setText("")
        self.modifiedImage6.setObjectName("modifiedImage6")
        self.imageLayout.addWidget(self.modifiedImage6, 2, 0, 1, 1)
        self.modifiedImage8 = QtWidgets.QLabel(Form)
        self.modifiedImage8.setMinimumSize(QtCore.QSize(300, 300))
        self.modifiedImage8.setText("")
        self.modifiedImage8.setObjectName("modifiedImage8")
        self.imageLayout.addWidget(self.modifiedImage8, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.imageLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "cutoff:"))
        self.label_3.setText(_translate("Form", "Part 2"))
        self.label_4.setText(_translate("Form", "Part 4"))
        self.label_2.setText(_translate("Form", "Part 3"))
        self.label_9.setText(_translate("Form", "cutoff:"))
        self.label_7.setText(_translate("Form", "b:"))
        self.label_6.setText(_translate("Form", "a:"))
        self.label_11.setText(_translate("Form", "T:"))
        self.label_12.setText(_translate("Form", "K:"))
        self.label.setText(_translate("Form", "gamma H:"))
        self.label_5.setText(_translate("Form", "n(Butterworth):"))
        self.p2Confirm.setText(_translate("Form", "Confirm"))
        self.p3Confirm.setText(_translate("Form", "Confirm"))
        self.label_10.setText(_translate("Form", "c:"))
        self.label_13.setText(_translate("Form", "gamma L:"))
        self.p4Confirm.setText(_translate("Form", "Confirm"))
        self.p1Confirm.setText(_translate("Form", "FFT"))
        self.load.setText(_translate("Form", "Load"))
        self.label_14.setText(_translate("Form", "Part1"))
