import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from package.NPC import NPC

Ui_MainWindow, QtBaseClass = uic.loadUiType("package/mainwindow.ui")


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.npc = NPC()
        self.ui.name_button.clicked.connect(self.set_name)


    def set_name(self):
        name = self.npc.name
        self.ui.name_label.setText(name)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
