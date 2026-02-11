#==================================================================
# PyAI_v1\gui\message_input.py - ETI Patagonia - prof.martintorres@educ.ar
#==================================================================
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTextEdit, QPushButton

class MessageInput(QWidget):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback

        self.input = QTextEdit()
        self.input.setFixedHeight(80)
        self.input.setStyleSheet("background:#1a1a1a;color:#fff;")

        send = QPushButton("Enviar")
        send.clicked.connect(self.send)

        layout = QHBoxLayout(self)
        layout.addWidget(self.input)
        layout.addWidget(send)

    def send(self):
        text = self.input.toPlainText().strip()
        if text:
            self.callback(text)
            self.input.clear()
