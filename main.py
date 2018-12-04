from character_stats import *
from introduction import *



app = QtWidgets.QApplication(sys.argv)
reknamorcen = Intro().intro()
sys.exit(app.exec_())
