# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'products.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QSpinBox, QWidget)

class Ui_FormProduct(object):
    def setupUi(self, FormProduct):
        if not FormProduct.objectName():
            FormProduct.setObjectName(u"FormProduct")
        FormProduct.resize(400, 211)
        self.formLayout = QFormLayout(FormProduct)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(FormProduct)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.addname = QLineEdit(FormProduct)
        self.addname.setObjectName(u"addname")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.addname)

        self.label_2 = QLabel(FormProduct)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(FormProduct)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.addcat = QLineEdit(FormProduct)
        self.addcat.setObjectName(u"addcat")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.addcat)

        self.buttonBox = QDialogButtonBox(FormProduct)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.buttonBox)

        self.addprice = QSpinBox(FormProduct)
        self.addprice.setObjectName(u"addprice")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.addprice)


        self.retranslateUi(FormProduct)
        self.buttonBox.accepted.connect(FormProduct.accept)
        self.buttonBox.rejected.connect(FormProduct.reject)

        QMetaObject.connectSlotsByName(FormProduct)
    # setupUi

    def retranslateUi(self, FormProduct):
        FormProduct.setWindowTitle(QCoreApplication.translate("FormProduct", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("FormProduct", u"Nombre del producto", None))
        self.label_2.setText(QCoreApplication.translate("FormProduct", u"Precio (\u20ac )", None))
        self.label_3.setText(QCoreApplication.translate("FormProduct", u"Categoria", None))
    # retranslateUi

