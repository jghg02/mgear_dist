# MGEAR is under the terms of the MIT License

# Copyright (c) 2016 Jeremie Passerin, Miquel Campos

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Author:     Jeremie Passerin      geerem@hotmail.com  www.jeremiepasserin.com
# Author:     Miquel Campos         hello@miquel-campos.com  www.miquel-campos.com
# Date:       2016 / 10 / 10

import mgear.maya.pyqt as gqt
QtGui, QtCore, QtWidgets, wrapInstance = gqt.qt_import()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(280, 525)
        self.ikRefArray_groupBox = QtWidgets.QGroupBox(Form)
        self.ikRefArray_groupBox.setGeometry(QtCore.QRect(2, 340, 249, 175))
        self.ikRefArray_groupBox.setObjectName("ikRefArray_groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.ikRefArray_groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 231, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.ikRefArray_horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.ikRefArray_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ikRefArray_horizontalLayout.setObjectName("ikRefArray_horizontalLayout")
        self.ikRefArray_verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.ikRefArray_verticalLayout_1.setObjectName("ikRefArray_verticalLayout_1")
        self.ikRefArray_listWidget = QtWidgets.QListWidget(self.layoutWidget)
        self.ikRefArray_listWidget.setDragDropOverwriteMode(True)
        self.ikRefArray_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.ikRefArray_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ikRefArray_listWidget.setAlternatingRowColors(True)
        self.ikRefArray_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ikRefArray_listWidget.setSelectionRectVisible(False)
        self.ikRefArray_listWidget.setObjectName("ikRefArray_listWidget")
        self.ikRefArray_verticalLayout_1.addWidget(self.ikRefArray_listWidget)
        self.ikRefArray_horizontalLayout.addLayout(self.ikRefArray_verticalLayout_1)
        self.ikRefArray_verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.ikRefArray_verticalLayout_2.setObjectName("ikRefArray_verticalLayout_2")
        self.ikRefArrayAdd_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ikRefArrayAdd_pushButton.setObjectName("ikRefArrayAdd_pushButton")
        self.ikRefArray_verticalLayout_2.addWidget(self.ikRefArrayAdd_pushButton)
        self.ikRefArrayRemove_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ikRefArrayRemove_pushButton.setObjectName("ikRefArrayRemove_pushButton")
        self.ikRefArray_verticalLayout_2.addWidget(self.ikRefArrayRemove_pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ikRefArray_verticalLayout_2.addItem(spacerItem)
        self.ikRefArray_horizontalLayout.addLayout(self.ikRefArray_verticalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(1, 9, 249, 141))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 221, 121))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.joint_checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.joint_checkBox.setObjectName("joint_checkBox")
        self.verticalLayout_4.addWidget(self.joint_checkBox)
        self.uniScale_checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.uniScale_checkBox.setObjectName("uniScale_checkBox")
        self.verticalLayout_4.addWidget(self.uniScale_checkBox)
        self.neutralRotation_checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.neutralRotation_checkBox.setObjectName("neutralRotation_checkBox")
        self.verticalLayout_4.addWidget(self.neutralRotation_checkBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ctlSize_label = QtWidgets.QLabel(self.layoutWidget1)
        self.ctlSize_label.setObjectName("ctlSize_label")
        self.horizontalLayout_3.addWidget(self.ctlSize_label)
        self.ctlSize_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctlSize_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.ctlSize_doubleSpinBox.setSizePolicy(sizePolicy)
        self.ctlSize_doubleSpinBox.setWrapping(False)
        self.ctlSize_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ctlSize_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ctlSize_doubleSpinBox.setMinimum(0.01)
        self.ctlSize_doubleSpinBox.setMaximum(200.0)
        self.ctlSize_doubleSpinBox.setProperty("value", 1.0)
        self.ctlSize_doubleSpinBox.setObjectName("ctlSize_doubleSpinBox")
        self.horizontalLayout_3.addWidget(self.ctlSize_doubleSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.controlShape_label = QtWidgets.QLabel(self.layoutWidget1)
        self.controlShape_label.setText("Control Shape")
        self.controlShape_label.setObjectName("controlShape_label")
        self.horizontalLayout_2.addWidget(self.controlShape_label)
        self.controlShape_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlShape_comboBox.sizePolicy().hasHeightForWidth())
        self.controlShape_comboBox.setSizePolicy(sizePolicy)
        self.controlShape_comboBox.setObjectName("controlShape_comboBox")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.controlShape_comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.keyable_groupBox = QtWidgets.QGroupBox(Form)
        self.keyable_groupBox.setGeometry(QtCore.QRect(1, 160, 251, 171))
        self.keyable_groupBox.setObjectName("keyable_groupBox")
        self.layoutWidget2 = QtWidgets.QWidget(self.keyable_groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(9, 16, 241, 145))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.translate_pushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.translate_pushButton.setObjectName("translate_pushButton")
        self.verticalLayout.addWidget(self.translate_pushButton)
        self.tx_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.tx_checkBox.setObjectName("tx_checkBox")
        self.verticalLayout.addWidget(self.tx_checkBox)
        self.ty_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.ty_checkBox.setObjectName("ty_checkBox")
        self.verticalLayout.addWidget(self.ty_checkBox)
        self.tz_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.tz_checkBox.setObjectName("tz_checkBox")
        self.verticalLayout.addWidget(self.tz_checkBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rotate_pushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.rotate_pushButton.setObjectName("rotate_pushButton")
        self.verticalLayout_2.addWidget(self.rotate_pushButton)
        self.rx_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.rx_checkBox.setObjectName("rx_checkBox")
        self.verticalLayout_2.addWidget(self.rx_checkBox)
        self.ry_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.ry_checkBox.setObjectName("ry_checkBox")
        self.verticalLayout_2.addWidget(self.ry_checkBox)
        self.rz_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.rz_checkBox.setObjectName("rz_checkBox")
        self.verticalLayout_2.addWidget(self.rz_checkBox)
        self.ro_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.ro_checkBox.setObjectName("ro_checkBox")
        self.verticalLayout_2.addWidget(self.ro_checkBox)
        self.ro_comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.ro_comboBox.setObjectName("ro_comboBox")
        self.ro_comboBox.addItem("")
        self.ro_comboBox.addItem("")
        self.ro_comboBox.addItem("")
        self.ro_comboBox.addItem("")
        self.ro_comboBox.addItem("")
        self.ro_comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.ro_comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scale_pushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.scale_pushButton.setObjectName("scale_pushButton")
        self.verticalLayout_3.addWidget(self.scale_pushButton)
        self.sx_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.sx_checkBox.setObjectName("sx_checkBox")
        self.verticalLayout_3.addWidget(self.sx_checkBox)
        self.sy_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.sy_checkBox.setObjectName("sy_checkBox")
        self.verticalLayout_3.addWidget(self.sy_checkBox)
        self.sz_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.sz_checkBox.setObjectName("sz_checkBox")
        self.verticalLayout_3.addWidget(self.sz_checkBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.translate_pushButton, QtCore.SIGNAL("clicked()"), self.tz_checkBox.toggle)
        QtCore.QObject.connect(self.translate_pushButton, QtCore.SIGNAL("clicked()"), self.ty_checkBox.toggle)
        QtCore.QObject.connect(self.translate_pushButton, QtCore.SIGNAL("clicked()"), self.tx_checkBox.toggle)
        QtCore.QObject.connect(self.rotate_pushButton, QtCore.SIGNAL("clicked()"), self.rx_checkBox.toggle)
        QtCore.QObject.connect(self.rotate_pushButton, QtCore.SIGNAL("clicked()"), self.ry_checkBox.toggle)
        QtCore.QObject.connect(self.rotate_pushButton, QtCore.SIGNAL("clicked()"), self.rz_checkBox.toggle)
        QtCore.QObject.connect(self.rotate_pushButton, QtCore.SIGNAL("clicked()"), self.ro_checkBox.toggle)
        QtCore.QObject.connect(self.scale_pushButton, QtCore.SIGNAL("clicked()"), self.sx_checkBox.toggle)
        QtCore.QObject.connect(self.scale_pushButton, QtCore.SIGNAL("clicked()"), self.sy_checkBox.toggle)
        QtCore.QObject.connect(self.scale_pushButton, QtCore.SIGNAL("clicked()"), self.sz_checkBox.toggle)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(gqt.fakeTranslate("Form", "Form", None, -1))
        self.ikRefArray_groupBox.setTitle(gqt.fakeTranslate("Form", "IK Reference Array", None, -1))
        self.ikRefArrayAdd_pushButton.setText(gqt.fakeTranslate("Form", "<<", None, -1))
        self.ikRefArrayRemove_pushButton.setText(gqt.fakeTranslate("Form", ">>", None, -1))
        self.joint_checkBox.setText(gqt.fakeTranslate("Form", "Joint", None, -1))
        self.uniScale_checkBox.setText(gqt.fakeTranslate("Form", "Uniform Scale", None, -1))
        self.neutralRotation_checkBox.setText(gqt.fakeTranslate("Form", "World Space Orientation Align", None, -1))
        self.ctlSize_label.setText(gqt.fakeTranslate("Form", "Ctl Size", None, -1))
        self.controlShape_comboBox.setItemText(0, gqt.fakeTranslate("Form", "Arrow", None, -1))
        self.controlShape_comboBox.setItemText(1, gqt.fakeTranslate("Form", "Circle", None, -1))
        self.controlShape_comboBox.setItemText(2, gqt.fakeTranslate("Form", "Compas", None, -1))
        self.controlShape_comboBox.setItemText(3, gqt.fakeTranslate("Form", "Cross", None, -1))
        self.controlShape_comboBox.setItemText(4, gqt.fakeTranslate("Form", "Crossarrow", None, -1))
        self.controlShape_comboBox.setItemText(5, gqt.fakeTranslate("Form", "Cube", None, -1))
        self.controlShape_comboBox.setItemText(6, gqt.fakeTranslate("Form", "Cubewithpeak", None, -1))
        self.controlShape_comboBox.setItemText(7, gqt.fakeTranslate("Form", "Cylinder", None, -1))
        self.controlShape_comboBox.setItemText(8, gqt.fakeTranslate("Form", "Diamond", None, -1))
        self.controlShape_comboBox.setItemText(9, gqt.fakeTranslate("Form", "Flower", None, -1))
        self.controlShape_comboBox.setItemText(10, gqt.fakeTranslate("Form", "Null", None, -1))
        self.controlShape_comboBox.setItemText(11, gqt.fakeTranslate("Form", "Pyramid", None, -1))
        self.controlShape_comboBox.setItemText(12, gqt.fakeTranslate("Form", "Sphere", None, -1))
        self.controlShape_comboBox.setItemText(13, gqt.fakeTranslate("Form", "Square", None, -1))
        self.keyable_groupBox.setTitle(gqt.fakeTranslate("Form", "Keyable", None, -1))
        self.translate_pushButton.setText(gqt.fakeTranslate("Form", "Translate", None, -1))
        self.tx_checkBox.setText(gqt.fakeTranslate("Form", "tx", None, -1))
        self.ty_checkBox.setText(gqt.fakeTranslate("Form", "ty", None, -1))
        self.tz_checkBox.setText(gqt.fakeTranslate("Form", "tz", None, -1))
        self.rotate_pushButton.setText(gqt.fakeTranslate("Form", "Rotate", None, -1))
        self.rx_checkBox.setText(gqt.fakeTranslate("Form", "rx", None, -1))
        self.ry_checkBox.setText(gqt.fakeTranslate("Form", "ry", None, -1))
        self.rz_checkBox.setText(gqt.fakeTranslate("Form", "rz", None, -1))
        self.ro_checkBox.setText(gqt.fakeTranslate("Form", "ro", None, -1))
        self.ro_comboBox.setItemText(0, gqt.fakeTranslate("Form", "XYZ", None, -1))
        self.ro_comboBox.setItemText(1, gqt.fakeTranslate("Form", "YZX", None, -1))
        self.ro_comboBox.setItemText(2, gqt.fakeTranslate("Form", "ZXY", None, -1))
        self.ro_comboBox.setItemText(3, gqt.fakeTranslate("Form", "XZY", None, -1))
        self.ro_comboBox.setItemText(4, gqt.fakeTranslate("Form", "YXZ", None, -1))
        self.ro_comboBox.setItemText(5, gqt.fakeTranslate("Form", "ZYX", None, -1))
        self.scale_pushButton.setText(gqt.fakeTranslate("Form", "Scale", None, -1))
        self.sx_checkBox.setText(gqt.fakeTranslate("Form", "sx", None, -1))
        self.sy_checkBox.setText(gqt.fakeTranslate("Form", "sy", None, -1))
        self.sz_checkBox.setText(gqt.fakeTranslate("Form", "sz", None, -1))

