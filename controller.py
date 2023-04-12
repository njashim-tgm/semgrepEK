import sys
from PyQt6.QtWidgets import QApplication
import model
import view
import app


class Controller:
    def __init__(self):
        self.model = model.MyLanguageTool()
        self.view = view.View(self)


    def reset(self) -> None:
        """
        ruft die reset-methods von den jeweiligen Klassen auf
        :return:
        """
        #self.model.reset()
        self.view.reset()

    def execute(self) -> None:
        """
        bringt das ganze Programm zum Laufen, also model und view
        und setzt auch die Werte jenachdem ein
        :return:
        """
        if self.view.get_eingabe()!="" :
            self.view.set_text_statusbar("Erkennung erfolgreich durchgeführt")
            a=self.view.get_eingabe()
            b=self.model.execute(a)
            self.view.set_ausgabe(b)

if __name__ == '__main__':
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())