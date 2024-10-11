#pyuic6 layout.ui -o layout.py
import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        (self.ui.bussinesBox.toggled.connect(self.button_clicked))
        self.ui.firstBox.toggled.connect(self.button_clicked)
        self.ui.economicBox.toggled.connect(self.button_clicked)

        self.show()

    def button_clicked(self):
        price = 0
        if self.ui.economicBox.isChecked():
            price = 20
        elif self.ui.bussinesBox.isChecked():
            price = 150
        elif self.ui.firstBox.isChecked():
            price = 300
        else:
            price = 0
        self.ui.resultLabel.setText(f'Cena twojego lotu wynosi {price}')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())
