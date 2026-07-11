# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.resize(504, 320)
        self.centralwidget = QWidget(vtn_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_titular = QLabel(self.centralwidget)
        self.lbl_titular.setObjectName(u"lbl_titular")
        self.lbl_titular.setGeometry(QRect(100, 50, 81, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_titular.setFont(font)
        self.lbl_codigo = QLabel(self.centralwidget)
        self.lbl_codigo.setObjectName(u"lbl_codigo")
        self.lbl_codigo.setGeometry(QRect(100, 80, 91, 31))
        self.lbl_codigo.setFont(font)
        self.txt_titular = QLineEdit(self.centralwidget)
        self.txt_titular.setObjectName(u"txt_titular")
        self.txt_titular.setGeometry(QRect(190, 60, 191, 21))
        self.txt_titular.setMaxLength(100)
        self.txt_codigo = QLineEdit(self.centralwidget)
        self.txt_codigo.setObjectName(u"txt_codigo")
        self.txt_codigo.setGeometry(QRect(190, 90, 141, 21))
        self.txt_codigo.setMaxLength(10)
        self.txt_anioapertura = QLineEdit(self.centralwidget)
        self.txt_anioapertura.setObjectName(u"txt_anioapertura")
        self.txt_anioapertura.setGeometry(QRect(190, 120, 111, 21))
        self.txt_anioapertura.setMaxLength(4)
        self.lbl_anioapertura = QLabel(self.centralwidget)
        self.lbl_anioapertura.setObjectName(u"lbl_anioapertura")
        self.lbl_anioapertura.setGeometry(QRect(40, 110, 131, 31))
        self.lbl_anioapertura.setFont(font)
        self.btn_agregar = QPushButton(self.centralwidget)
        self.btn_agregar.setObjectName(u"btn_agregar")
        self.btn_agregar.setGeometry(QRect(60, 240, 75, 23))
        self.btn_limpiar = QPushButton(self.centralwidget)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setGeometry(QRect(300, 240, 75, 23))
        self.btn_actualizar = QPushButton(self.centralwidget)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setGeometry(QRect(140, 240, 75, 23))
        self.btn_buscar = QPushButton(self.centralwidget)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setGeometry(QRect(400, 190, 75, 23))
        self.txt_email = QLineEdit(self.centralwidget)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(190, 150, 191, 21))
        self.txt_email.setMaxLength(100)
        self.txt_buscar_codigo = QLineEdit(self.centralwidget)
        self.txt_buscar_codigo.setObjectName(u"txt_buscar_codigo")
        self.txt_buscar_codigo.setGeometry(QRect(190, 190, 191, 21))
        self.txt_buscar_codigo.setMaxLength(10)
        self.lbl_buscar_codigo = QLabel(self.centralwidget)
        self.lbl_buscar_codigo.setObjectName(u"lbl_buscar_codigo")
        self.lbl_buscar_codigo.setGeometry(QRect(10, 180, 181, 31))
        self.lbl_buscar_codigo.setFont(font)
        self.btn_eliminar = QPushButton(self.centralwidget)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setGeometry(QRect(220, 240, 75, 23))
        self.lbl_identificacion = QLabel(self.centralwidget)
        self.lbl_identificacion.setObjectName(u"lbl_identificacion")
        self.lbl_identificacion.setGeometry(QRect(110, 140, 71, 41))
        self.lbl_identificacion.setFont(font)
        vtn_principal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtn_principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 504, 21))
        vtn_principal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtn_principal)
        self.statusbar.setObjectName(u"statusbar")
        vtn_principal.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txt_titular, self.txt_codigo)
        QWidget.setTabOrder(self.txt_codigo, self.txt_anioapertura)
        QWidget.setTabOrder(self.txt_anioapertura, self.txt_email)
        QWidget.setTabOrder(self.txt_email, self.txt_buscar_codigo)
        QWidget.setTabOrder(self.txt_buscar_codigo, self.btn_buscar)
        QWidget.setTabOrder(self.btn_buscar, self.btn_agregar)
        QWidget.setTabOrder(self.btn_agregar, self.btn_actualizar)
        QWidget.setTabOrder(self.btn_actualizar, self.btn_eliminar)
        QWidget.setTabOrder(self.btn_eliminar, self.btn_limpiar)

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)
    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"Sistema de Administracion de Personas", None))
        self.lbl_titular.setText(QCoreApplication.translate("vtn_principal", u"Titular:", None))
        self.lbl_codigo.setText(QCoreApplication.translate("vtn_principal", u"Codigo:", None))
        self.lbl_anioapertura.setText(QCoreApplication.translate("vtn_principal", u"A\u00f1o apertura:", None))
#if QT_CONFIG(tooltip)
        self.btn_agregar.setToolTip(QCoreApplication.translate("vtn_principal", u"Guardar los datos del titular", None))
#endif // QT_CONFIG(tooltip)
        self.btn_agregar.setText(QCoreApplication.translate("vtn_principal", u"Agregar", None))
#if QT_CONFIG(tooltip)
        self.btn_limpiar.setToolTip(QCoreApplication.translate("vtn_principal", u"Borra el formulario", None))
#endif // QT_CONFIG(tooltip)
        self.btn_limpiar.setText(QCoreApplication.translate("vtn_principal", u"Limpiar", None))
#if QT_CONFIG(tooltip)
        self.btn_actualizar.setToolTip(QCoreApplication.translate("vtn_principal", u"Guardar los datos del titular", None))
#endif // QT_CONFIG(tooltip)
        self.btn_actualizar.setText(QCoreApplication.translate("vtn_principal", u"Actualizar", None))
#if QT_CONFIG(tooltip)
        self.btn_buscar.setToolTip(QCoreApplication.translate("vtn_principal", u"Borra el formulario", None))
#endif // QT_CONFIG(tooltip)
        self.btn_buscar.setText(QCoreApplication.translate("vtn_principal", u"Buscar", None))
        self.lbl_buscar_codigo.setText(QCoreApplication.translate("vtn_principal", u"BuscarPorCodigo:", None))
#if QT_CONFIG(tooltip)
        self.btn_eliminar.setToolTip(QCoreApplication.translate("vtn_principal", u"Borra el formulario", None))
#endif // QT_CONFIG(tooltip)
        self.btn_eliminar.setText(QCoreApplication.translate("vtn_principal", u"Eliminar", None))
        self.lbl_identificacion.setText(QCoreApplication.translate("vtn_principal", u"Email:", None))
    # retranslateUi

