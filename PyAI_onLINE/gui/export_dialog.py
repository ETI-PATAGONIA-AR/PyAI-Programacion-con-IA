# gui/export_dialog.py

from PyQt5.QtWidgets import QMessageBox
from utils.file_utils import export_chat
import os

def export_conversation(parent, history):
    base = os.path.join(os.getcwd(), "exports")
    os.makedirs(base, exist_ok=True)

    txt, js = export_chat(history, base)

    QMessageBox.information(
        parent,
        "Exportación completa",
        f"Archivos creados:\n{txt}\n{js}"
    )
