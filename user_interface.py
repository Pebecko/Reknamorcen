from PyQt5 import QtWidgets
from PyQt5 import QtGui
from main import *


def blank():
    print("Nothing here")


class Window(QtWidgets.QWidget):
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

        self.title = QtWidgets.QLabel()
        self.title.setPixmap(QtGui.QPixmap("Reknamorcen_1.png"))
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

        self.h_box_1 = QtWidgets.QHBoxLayout()
        self.h_box_1.addStretch()
        self.h_box_1.addWidget(self.label)
        self.h_box_1.addStretch()

        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addStretch()
        self.v_box.addWidget(self.title)
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

        # self.monit = app.desktop().screenGeometry()

        # self.setGeometry(0, 0, self.monit.width(), self.monit.height())
        self.setLayout(self.h_box)
        self.setWindowTitle("Reknamorcen")
        self.showFullScreen()

        self.show()

    def butt_reset(self):
        print("reseting buttons")
        self.button_1.setVisible(False)
        self.button_2.setVisible(False)
        self.button_3.setVisible(False)
        self.button_4.setVisible(False)
        self.button_5.setVisible(False)
        self.button_6.setVisible(False)

    def butt_1(self, txt, func):
        self.button_1.setVisible(True)
        self.button_1.setText(txt)
        self.func_1 = func

    def butt_2(self, txt, func):
        self.button_2.setVisible(True)
        self.button_2.setText(txt)
        self.func_2 = func

    def butt_3(self, txt, func):
        self.button_3.setVisible(True)
        self.button_3.setText(txt)
        self.func_3 = func

    def butt_4(self, txt, func):
        self.button_4.setVisible(True)
        self.button_4.setText(txt)
        self.func_4 = func

    def butt_5(self, txt, func):
        self.button_5.setVisible(True)
        self.button_5.setText(txt)
        self.func_5 = func

    def butt_6(self, txt, func):
        self.button_6.setVisible(True)
        self.button_6.setText(txt)
        self.func_6 = func

    def intro(self):
        self.showMaximized()
        self.butt_reset()

        self.label.setText("Vítejte v reknamorcenovi")

        self.butt_1("Pokračovat", self.race_sel)

    def race_sel(self):
        self.butt_reset()

        self.label.setText("Vyberte si prosím rasu")

        self.butt_1("Trpaslík", self.dwarf_char)
        self.butt_2("Člověk", self.human_char)
        self.butt_3("Elf", self.elf_char)

    def dwarf_char(self):
        self.butt_reset()

        self.label.setText("Vyberte prosím postavu")

        self.butt_1("Informace o postavách", self.dwarf_info)
        self.butt_2("Trolobijce", self.slayer_intro)
        self.butt_3("Železolamač", self.ironbreaker_intro)
        self.butt_4("Horník", self.miner_intro)
        self.butt_5("Inženýr", self.engineer_intro)
        self.butt_6("Zpět", self. race_sel)

    def dwarf_info(self):
        self.butt_reset()

        self.label.setText("O které postavě chcete něco vědět")

        self.butt_1("Trolobijce", self.slayer_info)
        self.butt_2("Železolamač", self.ironbreaker_info)
        self.butt_3("Horník", self.miner_info)
        self.butt_4("Inženýr", self.engineer_info)
        self.butt_5("Zpět", self.dwarf_char)

    def slayer_info(self):
        self.butt_reset()

        self.label.setText("{}, {}.".format(Slayer().name, Slayer().info))

        self.butt_1("Zpět", self.dwarf_info)

    def ironbreaker_info(self):
        self.butt_reset()

        self.label.setText("{}, {}.".format(Ironbreaker().name, Ironbreaker().info))

        self.butt_1("Zpět", self.dwarf_info)

    def miner_info(self):
        self.butt_reset()

        self.label.setText("{}, {}.".format(Miner().name, Miner().info))

        self.butt_1("Zpět", self.dwarf_info)

    def engineer_info(self):
        self.butt_reset()

        self.label.setText("{}, {}.".format(Engineer().name, Engineer().info))

        self.butt_1("Zpět", self.dwarf_info)

    def human_char(self):
        self.butt_reset()

        self.butt_1("Informace o postavách", self.human_info)
        self.butt_2("Gardista", self.guardsmen_intro)
        self.butt_3("Zpět", self.race_sel)

        self.label.setText("Vyberte prosím postavu")

    def human_info(self):
        self.butt_reset()

        self.label.setText("O které postavě chcete něco vědět")

        self.butt_1("Gardista", self.guardsmen_info)
        self.butt_2("Zpět", self.human_char)

    def guardsmen_info(self):
        self.butt_reset()

        self.label.setText("{}, {}.".format(Guardsman().name, Guardsman().info))

        self.butt_1("Zpět", self.human_info)

    def elf_char(self):
        self.butt_reset()

        self.butt_1("Informace o postavách", self.elf_info)
        self.butt_2("Vrah", self.assasin_intro)
        self.butt_3("Zpět", self.race_sel)

        self.label.setText("Vyberte prosím postavu")

    def elf_info(self):
        self.butt_reset()

        self.label.setText("O které postavě chcete něco vědět")

        self.butt_1("Vrah", self.assasin_info)
        self.butt_2("Zpět", self.elf_char)

    def assasin_info(self):
        self.butt_reset()

        self.label.setText("{}, {}.".format(Assasin().name, Assasin().info))

        self.butt_1("Zpět", self.elf_info)

    def slayer_intro(self):
        player = Slayer()

        self.butt_reset()

        self.label.setText("1")

    def ironbreaker_intro(self):
        player = Ironbreaker()

        self.butt_reset()

        self.label.setText("2")

    def miner_intro(self):
        player = Miner()

        self.butt_reset()

        self.label.setText("3")

    def engineer_intro(self):
        player = Engineer()

        self.butt_reset()

        self.label.setText("4")

    def guardsmen_intro(self):
        player = Guardsman()

        self.butt_reset()

        self.label.setText("5")

    def assasin_intro(self):
        player = Assasin()

        self.butt_reset()

        self.label.setText("6")


app = QtWidgets.QApplication(sys.argv)
reknamorcen = Window().intro()
sys.exit(app.exec_())
