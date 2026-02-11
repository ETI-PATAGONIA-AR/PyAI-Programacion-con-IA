import cv2
import numpy as np
from tkinter import Tk, Label, Button, Scale, HORIZONTAL, Frame, Canvas
from PIL import Image, ImageTk

class AplicacionFiltros:
    def __init__(self):
        self.root = Tk()
        self.root.title("Filtros Webcam Profesional - ETI Patagonia")
        self.root.geometry("1200x700")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(True, True)
        
        # Canvas para video (izquierda, grande)
        self.video_canvas = Canvas(self.root, bg="#000", width=900, height=650, highlightthickness=0)
        self.video_canvas.pack(side="left", padx=(10,5), pady=10, fill="both", expand=True)
        
        # Sidebar controles (derecha)
        sidebar = Frame(self.root, bg="#2d2d2d", width=280)
        sidebar.pack(side="right", padx=(5,10), pady=10, fill="y")
        sidebar.pack_propagate(False)
        
        # Título
        title = Label(sidebar, text="🎥 FILTROS", font=("Arial", 18, "bold"), fg="#00ff88", bg="#2d2d2d")
        title.pack(pady=15)
        
        # Botones filtros (estilo moderno)
        self.filtro_actual = "original"
        botones = [
            ("🟤 GRIS", "gris"),
            ("🔴 ROJO", "rojo"), 
            ("🔵 AZUL", "azul"),
            ("🟢 VERDE", "verde"),
            ("🌈 ORIGINAL", "original")
        ]
        
        for emoji_text, filtro in botones:
            btn = Button(sidebar, text=emoji_text, font=("Arial", 12, "bold"),
                        command=lambda f=filtro: self.cambiar_filtro(f),
                        bg="#4a4a4a", fg="white", activebackground="#6a6a6a",
                        relief="flat", padx=15, pady=8, height=2)
            btn.pack(fill="x", pady=3)
        
        # Separador
        Label(sidebar, text="", bg="#2d2d2d", height=1).pack(pady=15, fill="x")
        
        # Slider intensidad
        Label(sidebar, text="Intensidad", font=("Arial", 14, "bold"), fg="#00ff88", bg="#2d2d2d").pack(pady=(0,5))
        self.scale = Scale(sidebar, from_=0, to=255, orient=HORIZONTAL, length=220,
                          command=self.actualizar_intensidad, bg="#2d2d2d", fg="white",
                          highlightbackground="#2d2d2d", troughcolor="#555", borderwidth=0,
                          font=("Arial", 11))
        self.scale.set(255)
        self.scale.pack(pady=10)
        
        self.int_label = Label(sidebar, text="255", font=("Arial", 24, "bold"), fg="#ffaa00", bg="#2d2d2d")
        self.int_label.pack(pady=5)
        
        # Info
        info = Label(sidebar, text="ESC o X para cerrar", font=("Arial", 10), fg="#888", bg="#2d2d2d")
        info.pack(pady=20)
        
        # Inicializar cámara y estados
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.intensidad = 255
        
        self.photo = None
        self.actualizar_video()
        
        self.root.bind("<Escape>", lambda e: self.cerrar())
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar)

    def cambiar_filtro(self, filtro):
        self.filtro_actual = filtro

    def procesar_frame(self, frame):
        factor = self.intensidad / 255.0
        if self.filtro_actual == "gris":
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        elif self.filtro_actual == "rojo":
            b, g, r = cv2.split(frame)
            r_adj = np.clip(r.astype(float) * factor, 0, 255).astype(np.uint8)
            return cv2.merge([np.zeros_like(b), np.zeros_like(g), r_adj])
        elif self.filtro_actual == "azul":
            b, g, r = cv2.split(frame)
            b_adj = np.clip(b.astype(float) * factor, 0, 255).astype(np.uint8)
            return cv2.merge([b_adj, np.zeros_like(g), np.zeros_like(r)])
        elif self.filtro_actual == "verde":
            b, g, r = cv2.split(frame)
            g_adj = np.clip(g.astype(float) * factor, 0, 255).astype(np.uint8)
            return cv2.merge([np.zeros_like(b), g_adj, np.zeros_like(r)])
        return frame  # original

    def actualizar_video(self):
        ret, frame = self.cap.read()
        if ret:
            # Redimensionar para canvas
            h, w = frame.shape[:2]
            canvas_w, canvas_h = 900, 650
            scale = min(canvas_w/w, canvas_h/h)
            new_w, new_h = int(w*scale), int(h*scale)
            
            frame_resized = cv2.resize(frame, (new_w, new_h))
            
            # Aplicar filtro
            processed = self.procesar_frame(frame_resized)
            
            # BGR -> RGB para PIL
            rgb = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(rgb)
            self.photo = ImageTk.PhotoImage(pil_img)
            
            # Limpiar y dibujar en canvas
            self.video_canvas.delete("all")
            self.video_canvas.create_image(canvas_w//2, canvas_h//2, image=self.photo, anchor="center")
        
        self.root.after(30, self.actualizar_video)  # 30 FPS

    def actualizar_intensidad(self, val):
        self.intensidad = int(float(val))
        self.int_label.config(text=str(self.intensidad))

    def cerrar(self):
        self.cap.release()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AplicacionFiltros()
    app.run()
