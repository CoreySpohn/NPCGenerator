import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from package.NPC.NPC import NPC

Ui_MainWindow, QtBaseClass = uic.loadUiType("package/mainwindow.ui")


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.npc = NPC([1])
        self.ui.name_button.clicked.connect(self.set_name)
        self.ui.gender_button.clicked.connect(self.set_gender)
        self.ui.race_button.clicked.connect(self.set_race)
        self.ui.age_button.clicked.connect(self.set_age)

    def set_name(self):
        self.npc.gen_name()
        self.ui.name_text.setText(self.npc.name)

    def set_gender(self):
        self.npc.gen_gender()
        self.ui.gender_text.setText(self.npc.gender)

    def set_race(self):
        self.npc.gen_race()
        self.ui.race_text.setText(self.npc.race.race)

    def set_age(self):
        self.npc.gen_age()
        self.ui.age_text.setText(str(self.npc.age))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
