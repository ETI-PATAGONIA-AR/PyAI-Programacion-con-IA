#==================================================================
# PyAI_v1\gui\code_highlighter.py - ETI Patagonia - prof.martintorres@educ.ar
#==================================================================

from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt5.QtCore import QRegExp

class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)

        self.keyword_format = QTextCharFormat()
        self.keyword_format.setForeground(QColor("#569CD6"))
        self.keyword_format.setFontWeight(QFont.Bold)

        keywords = [
            "def","class","import","from","return","if","elif","else",
            "for","while","try","except","with","as","lambda"
        ]
        self.rules = [(QRegExp(rf"\b{k}\b"), self.keyword_format) for k in keywords]

    def highlightBlock(self, text):
        for pattern, fmt in self.rules:
            index = pattern.indexIn(text)
            while index >= 0:
                length = pattern.matchedLength()
                self.setFormat(index, length, fmt)
                index = pattern.indexIn(text, index + length)
