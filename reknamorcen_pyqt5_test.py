import sys
from PyQt5 import QtWidgets


def blank():
    print("Nothing here")


class BaseWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message = "0"
        self.mess_1 = "1"
        self.func_1 = blank
        self.mess_2 = "2"
        self.func_2 = blank
        self.mess_3 = "3"
        self.func_3 = blank
        self.mess_4 = "4"
        self.func_4 = blank
        self.mess_5 = "5"
        self.func_5 = blank
        self.mess_6 = "6"
        self.func_6 = blank

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

        if self.bt_1_vis():
            self.button_1.setVisible(False)
        if self.bt_2_vis():
            self.button_2.setVisible(False)
        if self.bt_3_vis():
            self.button_3.setVisible(False)
        if self.bt_4_vis():
            self.button_4.setVisible(False)
        if self.bt_5_vis():
            self.button_5.setVisible(False)
        if self.bt_6_vis():
            self.button_6.setVisible(False)

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

        self.setGeometry(0, 0, self.monit.width(), self.monit.height())
        self.setLayout(self.h_box)
        self.setWindowTitle("Reknamorcen")

        self.show()

    def bt_1_vis(self):
        return True

    def bt_2_vis(self):
        return True

    def bt_3_vis(self):
        return True

    def bt_4_vis(self):
        return True

    def bt_5_vis(self):
        return True

    def bt_6_vis(self):
        return True

class OneButt(BaseWindow):
    def type(self, message="", mess_1="", func_1=blank):
        self.message = message
        self.mess_1 = mess_1
        self.func_1 = func_1

        self.label.setText(self.message)
        self.button_1.setText(self.mess_1)

    def bt_1_vis(self):
        return False


class TwoButt(BaseWindow):
    def type(self, message="", mess_1="", func_1=blank, mess_2="", func_2=blank):
        self.message = message
        self.mess_1 = mess_1
        self.func_1 = func_1
        self.mess_2 = mess_2
        self.func_2 =func_2

        self.label.setText(self.message)
        self.button_1.setText(self.mess_1)
        self.button_2.setText(self.mess_2)

    def bt_1_vis(self):
        return False

    def bt_2_vis(self):
        return False


class ThreeButt(BaseWindow):
    def bt_1_vis(self):
        return False

    def bt_2_vis(self):
        return False

    def bt_3_vis(self):
        return False

class FourButt(BaseWindow):
    def bt_1_vis(self):
        return False

    def bt_2_vis(self):
        return False

    def bt_3_vis(self):
        return False

    def bt_4_vis(self):
        return False

class FiveButt(BaseWindow):
    def bt_1_vis(self):
        return False

    def bt_2_vis(self):
        return False

    def bt_3_vis(self):
        return False

    def bt_4_vis(self):
        return False

    def bt_5_vis(self):
        return False

class SixButt(BaseWindow):
    def bt_1_vis(self):
        return False

    def bt_2_vis(self):
        return False

    def bt_3_vis(self):
        return False

    def bt_4_vis(self):
        return False

    def bt_5_vis(self):
        return False

    def bt_6_vis(self):
        return False

app = QtWidgets.QApplication(sys.argv)
reknamorcen = TwoButt().type("hello", "hi")
sys.exit(app.exec_())