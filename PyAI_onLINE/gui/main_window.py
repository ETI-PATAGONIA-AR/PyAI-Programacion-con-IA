#==================================================================
# PyAI_v1\gui\main_window.py - ETI Patagonia - prof.martintorres@educ.ar
#==================================================================

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QTextEdit, QPushButton,
    QLabel, QVBoxLayout, QHBoxLayout, QComboBox
)
from PyQt5.QtCore import Qt

from tts import TTSController   # ← INTEGRACIÓN DEFINITIVA TTS


DARK_BG = "#0f0f0f"
PANEL_BG = "#1e1e1e"
TEXT_COLOR = "#e6e6e6"
ACCENT = "#10a37f"


class MainWindow(QMainWindow):
    def __init__(self, conversation_manager):
        super().__init__()

        self.cm = conversation_manager
        self.tts = TTSController()   # ← UNA SOLA INSTANCIA

        self.setWindowTitle("PyAI v1")
        self.resize(1200, 800)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout()
        central.setLayout(main_layout)
        main_layout.setContentsMargins(8, 8, 8, 8)

        # ===================== IZQUIERDA (7/8) =====================
        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout, 7)

        self.chat_box = QTextEdit()
        self.chat_box.setReadOnly(True)
        self.chat_box.setStyleSheet(
            "background:{};"
            "color:{};"
            "border:1px solid #333;"
            "padding:8px;"
            "font-size:14px;".format(PANEL_BG, TEXT_COLOR)
        )
        left_layout.addWidget(self.chat_box, 3)

        self.input_box = QTextEdit()
        self.input_box.setFixedHeight(140)
        self.input_box.setStyleSheet(
            "background:{};"
            "color:{};"
            "border:1px solid #333;"
            "padding:8px;"
            "font-size:14px;".format(PANEL_BG, TEXT_COLOR)
        )
        left_layout.addWidget(self.input_box, 1)

        # ===================== DERECHA (1/8) =====================
        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout, 1)

        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Docente", "Scripting", "Técnico"])
        self.mode_selector.setStyleSheet(
            "QComboBox {{"
            "background-color:{};"
            "color:{};"
            "padding:6px;"
            "border:1px solid #333;"
            "}}"
            "QComboBox QAbstractItemView {{"
            "background-color:{};"
            "color:{};"
            "selection-background-color:{};"
            "selection-color:#000;"
            "}}".format(PANEL_BG, TEXT_COLOR, PANEL_BG, TEXT_COLOR, ACCENT)
        )
        right_layout.addWidget(self.mode_selector)

        self.token_label = QLabel("")
        self.token_label.setAlignment(Qt.AlignCenter)
        self.token_label.setStyleSheet("color:{};font-weight:bold;".format(TEXT_COLOR))
        right_layout.addWidget(self.token_label)

        self.send_btn = QPushButton("Enviar")
        self.clear_btn = QPushButton("Limpiar")

        btn_style = (
            "QPushButton {{"
            "background-color:{};"
            "color:#000;"
            "font-weight:bold;"
            "padding:10px;"
            "border-radius:6px;"
            "}}"
            "QPushButton:hover {{"
            "background-color:#0e8f6f;"
            "}}".format(ACCENT)
        )

        self.send_btn.setStyleSheet(btn_style)
        self.clear_btn.setStyleSheet(btn_style)

        self.send_btn.clicked.connect(self.send_message)
        self.clear_btn.clicked.connect(self.clear_chat)

        right_layout.addWidget(self.send_btn)
        right_layout.addWidget(self.clear_btn)
        right_layout.addStretch()

        self.setStyleSheet("background:{};".format(DARK_BG))
        self.refresh_tokens()

    # =============================================================
    def send_message(self):
        user_text = self.input_box.toPlainText().strip()
        if not user_text:
            return

        mode = self.mode_selector.currentText()
        prompt = self._apply_mode(mode, user_text)

        response = self.cm.send(prompt)

        self.chat_box.append("Vos:\n{}\n".format(user_text))
        self.chat_box.append(
            "AI ({}):\n{}\n{}\n".format(mode, response, "-" * 60)
        )

        # ===================== TTS DEFINITIVO =====================
        if mode != "Scripting":
            self.tts.speak_ai_response(response)
        # =========================================================

        self.input_box.clear()
        self.refresh_tokens()
        self.chat_box.verticalScrollBar().setValue(
            self.chat_box.verticalScrollBar().maximum()
        )

    # =============================================================
    def clear_chat(self):
        self.chat_box.clear()
        self.cm.clear()
        self.refresh_tokens()

    # =============================================================
    def refresh_tokens(self):
        remaining = self.cm.tokens_remaining()
        self.token_label.setText("Tokens: {}".format(remaining))

        if remaining < 0:
            self.token_label.setStyleSheet("color:red;font-weight:bold;")
        else:
            self.token_label.setStyleSheet(
                "color:{};font-weight:bold;".format(TEXT_COLOR)
            )

    # =============================================================
    def _apply_mode(self, mode, text):
        if mode == "Docente":
            return "Explicá paso a paso, de forma clara y didáctica:\n\n" + text
        if mode == "Scripting":
            return "Respondé SOLO con el código completo y funcional:\n\n" + text
        if mode == "Técnico":
            return "Respondé de manera técnica, precisa y concisa:\n\n" + text
        return text
