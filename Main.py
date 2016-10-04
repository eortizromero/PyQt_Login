#-*- coding: latin-1 -*-
from PyQt4.QtGui import (
	QMainWindow,
	QWidget,
	QPushButton,
	QLabel,
	QLineEdit,
	QCursor
)

from PyQt4.QtCore import Qt

class Main(QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setWindowTitle("Ventana principal")
		self.setMinimumSize(300, 400)
		self.setMaximumSize(300, 400)
		self.setObjectName('principal')
		
		self.createGUI()
		
	def createGUI(self):
		self.frame_window = QWidget(self)
		self.frame_window.setGeometry(0, 0, 300, 40)
		self.frame_window.setObjectName('frame_window')
		
		self.title_frame = QLabel(self.frame_window)
		self.title_frame.setGeometry(75 , 0, 150, 40)
		self.title_frame.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		self.title_frame.setText('Inicia Sesion')
		self.title_frame.setObjectName('title_frame')
		
		self.container = QWidget(self)
		self.container.setGeometry(0, 0, 300, 400)
		self.container.setObjectName('container')
		
		
		# buttons
		self.button_close = QPushButton(self.container)
		self.button_close.setGeometry(255, 5, 40, 30)
		self.button_close.setText('X')
		self.button_close.setObjectName('button_close')
		
		self.button_login = QPushButton(self.container)
		self.button_login.setGeometry(20, 300, 260, 40)
		self.button_login.setText('Inicia Sesion')
		self.button_login.setObjectName('button_login')
		self.button_login.setCursor(QCursor(Qt.PointingHandCursor))
		
		self.line_username = QLineEdit(self.container)
		self.line_username.setGeometry(20, 200, 260, 40)
		self.line_username.setPlaceholderText('Username')
		self.line_username.setObjectName('line_username')
		
		self.line_password = QLineEdit(self.container)
		self.line_password.setGeometry(20, 250, 260, 40)
		self.line_password.setEchoMode(QLineEdit.Password)
		self.line_password.setPlaceholderText('Password')
		self.line_password.setObjectName('line_password')
	
		# conexiones
		self.button_close.clicked.connect(self.close)
		
	def mousePressEvent(self, event):
		self.offset = event.pos()

	def mouseMoveEvent(self, event):
		x = event.globalX()
		y = event.globalY()
		x_w = self.offset.x()
		y_w = self.offset.y()
		self.move(x - x_w, y - y_w)