import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, 
                             QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, 
                             QFrame, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class TaTeTiPyQt5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tablero = [' ' for _ in range(9)]
        self.jugador = 'X'
        self.juego_activo = True
        self.puntaje_x = 0
        self.puntaje_o = 0
        
        self.setWindowTitle("🎮 Ta Te Ti - ETI Patagonia")
        self.setFixedSize(550, 650)
        self.setStyleSheet("""
            QMainWindow { background-color: #2b2b2b; color: white; }
            QPushButton { 
                background-color: #3a3a3a; 
                border: 2px solid #555; 
                border-radius: 10px; 
                color: white;
                font-size: 48px;
                font-weight: bold;
                min-height: 100px;
                min-width: 100px;
            }
            QPushButton:hover { background-color: #1f538d; border: 2px solid #4a90e2; }
            QPushButton:pressed { background-color: #0f3468; }
            QLabel { color: white; }
        """)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Título
        titulo = QLabel("🎮 TA TE TI")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Arial", 36, QFont.Bold))
        layout.addWidget(titulo)
        
        # Tablero 3x3
        tablero_frame = QFrame()
        tablero_layout = QGridLayout(tablero_frame)
        self.botones = []
        for i in range(9):
            btn = QPushButton(" ")
            btn.clicked.connect(lambda checked, pos=i: self.hacer_jugada(pos))
            tablero_layout.addWidget(btn, i//3, i%3)
            self.botones.append(btn)
        layout.addWidget(tablero_frame)
        
        # Info turno
        self.info_label = QLabel("Turno: X")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setFont(QFont("Arial", 24, QFont.Bold))
        layout.addWidget(self.info_label)
        
        # Puntaje
        self.puntaje_label = QLabel("X: 0 | O: 0")
        self.puntaje_label.setAlignment(Qt.AlignCenter)
        self.puntaje_label.setFont(QFont("Arial", 20))
        layout.addWidget(self.puntaje_label)
        
        # Botones controles
        controles_layout = QHBoxLayout()
        self.nuevo_btn = QPushButton("🔄 Nuevo Juego")
        self.nuevo_btn.clicked.connect(self.nuevo_juego)
        self.nuevo_btn.setFont(QFont("Arial", 16))
        controles_layout.addWidget(self.nuevo_btn)
        
        self.salir_btn = QPushButton("❌ Salir")
        self.salir_btn.clicked.connect(self.close)
        self.salir_btn.setFont(QFont("Arial", 16))
        controles_layout.addWidget(self.salir_btn)
        
        controles_frame = QFrame()
        controles_frame.setLayout(controles_layout)
        layout.addWidget(controles_frame)
    
    def hacer_jugada(self, pos):
        if not self.juego_activo or self.tablero[pos] != ' ':
            return
        
        self.tablero[pos] = self.jugador
        self.botones[pos].setText(self.jugador)
        
        resultado = self.verificar_ganador()
        if resultado:
            self.finalizar_juego(resultado)
            return
        
        self.cambiar_jugador()
    
    def verificar_ganador(self):
        ganadores = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for combo in ganadores:
            if (self.tablero[combo[0]] == self.tablero[combo[1]] == 
                self.tablero[combo[2]] != ' '):
                return self.tablero[combo[0]]
        if ' ' not in self.tablero:
            return 'Empate'
        return None
    
    def finalizar_juego(self, resultado):
        self.juego_activo = False
        if resultado == 'Empate':
            QMessageBox.information(self, "¡Empate!", "¡Partida empatada!")
        else:
            if resultado == 'X':
                self.puntaje_x += 1
            else:
                self.puntaje_o += 1
            QMessageBox.information(self, "¡Ganador!", f"¡Jugador {resultado} gana!")
            self.actualizar_puntaje()
        self.info_label.setText("Juego terminado")
    
    def cambiar_jugador(self):
        self.jugador = 'O' if self.jugador == 'X' else 'X'
        self.info_label.setText(f"Turno: {self.jugador}")
    
    def actualizar_puntaje(self):
        self.puntaje_label.setText(f"X: {self.puntaje_x} | O: {self.puntaje_o}")
    
    def nuevo_juego(self):
        self.tablero = [' ' for _ in range(9)]
        self.jugador = 'X'
        self.juego_activo = True
        self.info_label.setText("Turno: X")
        for btn in self.botones:
            btn.setText(" ")
    
    def closeEvent(self, event):
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = TaTeTiPyQt5()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
