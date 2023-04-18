import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import uic
import controller

class View(QMainWindow):
    def __init__(self, c: controller):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.setWindowTitle("My Language Tool") #windows titel
        self.set_text_statusbar("Bitte geben Sie einen Text ein!")
        self.pb_check.clicked.connect(c.execute)
        self.pb_reset.clicked.connect(c.reset)

    def reset(self)->None:
        """
        setzt alles zurück
        :return:
        """
        self.eingabe.clear()
        self.ausgabe.clear()
        self.set_text_statusbar("Bitte geben Sie einen Text ein!")

    def set_text_statusbar(self, t: str)->None:
        """
        settet die statusbar
        :param t: text für statusbar
        :return:
        """
        self.statusbar.showMessage(t)

    def get_eingabe(self)->str:
        """
        um die user eingabe zu bekommen
        :return:
        """
        return self.eingabe.toPlainText()

    def set_ausgabe(self, a):
        """
        um die ausgabe zu setzen
        :return:
        """
        self.ausgabe.setPlainText(a[0] + "\n" + a[1] + "\n" + a[2])

if __name__ == "__main__":
    app = QApplication([])
    view = View()
    view.show()
    sys.exit(app.exec())
    
exec("exec-test")
eval("eval-test")

username = input("Enter username:")
print("Username is: {}".format(username))
pickle.loads(this)
