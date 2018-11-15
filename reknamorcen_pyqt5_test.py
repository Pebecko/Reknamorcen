import sys
from PyQt5 import QtWidgets


def blank():
    print("Nothing here")


class Window(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message = ""
        self.mess_1 = ""
        self.func_1 = blank
        self.mess_2 = ""
        self.func_2 = blank
        self.mess_3 = ""
        self.func_3 = blank
        self.mess_4 = ""
        self.func_4 = blank
        self.mess_5 = ""
        self.func_5 = blank
        self.mess_6 = ""
        self.func_6 = blank

        # creating widgets
        self.label = QtWidgets.QLabel(self, text=self.message)
        self.button_1 = QtWidgets.QPushButton(self, text=self.mess_1)
        self.button_1.clicked.connect(lambda: self.func_1())
        self.button_2 = QtWidgets.QPushButton(self, text=self.mess_2)
        self.button_2.clicked.connect(lambda: self.func_2())
        self.button_3 = QtWidgets.QPushButton(self, text=self.mess_3)
        self.button_3.clicked.connect(lambda: self.func_3())
        self.button_4 = QtWidgets.QPushButton(self, text=self.mess_4)
        self.button_4.clicked.connect(lambda: self.func_4())
        self.button_5 = QtWidgets.QPushButton(self, text=self.mess_5)
        self.button_5.clicked.connect(lambda: self.func_5())
        self.button_6 = QtWidgets.QPushButton(self, text=self.mess_6)
        self.button_6.clicked.connect(lambda: self.func_6())

        self.button_1.setVisible(False)
        self.button_2.setVisible(False)
        self.button_3.setVisible(False)
        self.button_4.setVisible(False)
        self.button_5.setVisible(False)
        self.button_6.setVisible(False)

        # setting layout
        self.h_box_1 = QtWidgets.QHBoxLayout()
        self.h_box_1.addStretch()
        self.h_box_1.addWidget(self.label)
        self.h_box_1.addStretch()

        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addStretch()
        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box_1)
        self.v_box.addStretch()
        self.v_box.addWidget(self.button_1)
        self.v_box.addStretch()
        self.v_box.addWidget(self.button_2)
        self.v_box.addStretch()
        self.v_box.addWidget(self.button_3)
        self.v_box.addStretch()
        self.v_box.addWidget(self.button_4)
        self.v_box.addStretch()
        self.v_box.addWidget(self.button_5)
        self.v_box.addStretch()
        self.v_box.addWidget(self.button_6)
        self.v_box.addStretch()
        self.v_box.addStretch()

        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addStretch()
        self.h_box.addLayout(self.v_box)
        self.h_box.addStretch()

        self.monit = app.desktop().screenGeometry()

        self.setGeometry(0, 0, self.monit.width() / 2, self.monit.height() / 2)
        self.setLayout(self.h_box)
        self.setWindowTitle("Reknamorcen")
        self.showMaximized()

        self.show()

    def updating(self, buttons=0, message="", mess_1="", func_1=blank, mess_2="", func_2=blank, mess_3="", func_3=blank,
                 mess_4="", func_4=blank, mess_5="", func_5=blank, mess_6="", func_6=blank):
        self.buttons = buttons
        self.message = message
        self.mess_1 = mess_1
        self.func_1 = func_1
        self.mess_2 = mess_2
        self.func_2 = func_2
        self.mess_3 = mess_3
        self.func_3 = func_3
        self.mess_4 = mess_4
        self.func_4 = func_4
        self.mess_5 = mess_5
        self.func_5 = func_5
        self.mess_6 = mess_6
        self.func_6 = func_6

        self.label.setText(self.message)

        if self.buttons > 0:
            self.bt_1_vis()
        if self.buttons > 1:
            self.bt_2_vis()
        if self.buttons > 2:
            self.bt_3_vis()
        if self.buttons > 3:
            self.bt_4_vis()
        if self.buttons > 4:
            self.bt_5_vis()
        if self.buttons > 5:
            self.bt_6_vis()
        if self.buttons > 6:
            print("No more buttons availible.")

    def bt_1_vis(self):
        if self.mess_1 != "":
            self.button_1.setVisible(True)
            self.button_1.setText(self.mess_1)

        return

    def bt_2_vis(self):
        if self.mess_2 != "":
            self.button_2.setVisible(True)
            self.button_2.setText(self.mess_2)

        return

    def bt_3_vis(self):
        if self.mess_3 != "":
            self.button_3.setVisible(True)
            self.button_3.setText(self.mess_3)

        return

    def bt_4_vis(self):
        if self.mess_4 != "":
            self.button_4.setVisible(True)
            self.button_4.setText(self.mess_4)

        return

    def bt_5_vis(self):
        if self.mess_5 != "":
            self.button_5.setVisible(True)
            self.button_5.setText(self.mess_5)

        return

    def bt_6_vis(self):
        if self.mess_6 != "":
            self.button_6.setVisible(True)
            self.button_6.setText(self.mess_6)

        return


app = QtWidgets.QApplication(sys.argv)
reknamorcen = Window()
sys.exit(app.exec_())
