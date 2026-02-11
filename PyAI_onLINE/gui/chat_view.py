#==================================================================
# PyAI_v1\gui\chat_view.py - ETI Patagonia - prof.martintorres@educ.ar
#==================================================================
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QPushButton
from PyQt5.QtCore import Qt
import re

DARK = """
QTextBrowser {
    background:#121212;
    color:#e6e6e6;
    border:1px solid #333;
    border-radius:6px;
    padding:8px;
    selection-background-color:#444;
}
"""

class ChatView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setSpacing(10)

    def add_message(self, role, text):
        box = QTextBrowser()
        box.setStyleSheet(DARK)
        box.setReadOnly(True)
        box.setTextInteractionFlags(Qt.TextSelectableByMouse)

        html = self.format(text)
        box.setHtml(html)

        self.layout.addWidget(box)

    def format(self, text):
        parts = re.split(r"```", text)
        html = ""
        for i, p in enumerate(parts):
            if i % 2:
                html += f"<pre>{p}</pre>"
            else:
                html += p.replace("\n", "<br>")
        return html

    def clear(self):
        while self.layout.count():
            w = self.layout.takeAt(0).widget()
            if w:
                w.deleteLater()
