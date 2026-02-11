#==================================================================
# PyAI_v1\main.py - ETI Patagonia - prof.martintorres@educ.ar
#==================================================================
from PyQt5.QtWidgets import QApplication
import sys

from gui.main_window import MainWindow
from core.conversation_manager import ConversationManager
from ai.groq_client import GroqClient

def main():
    app = QApplication(sys.argv)

    ai = GroqClient()
    cm = ConversationManager(ai, max_tokens=8000)

    window = MainWindow(cm)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
