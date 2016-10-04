#-*- coding: latin-1 -*-

from PyQt4.QtGui import QApplication
from Main import Main

# crear la ventana

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	myapp = Main()
	myapp.show()
	with open('css/main.css' , 'r') as css:
		tema = css.read()
	app.setStyle("cleanlooks")
	app.setStyleSheet(tema)
	sys.exit(app.exec_())
