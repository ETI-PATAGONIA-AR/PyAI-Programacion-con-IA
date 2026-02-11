import tkinter as tk
from tkinter import messagebox

class CalculadoraOhm:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora de la ley de Ohm")

        # Campos de entrada
        self.tension_label = tk.Label(self.ventana, text="Tensión (V):")
        self.tension_label.grid(row=0, column=0)
        self.tension_entry = tk.Entry(self.ventana)
        self.tension_entry.grid(row=0, column=1)

        self.corriente_label = tk.Label(self.ventana, text="Corriente (I):")
        self.corriente_label.grid(row=1, column=0)
        self.corriente_entry = tk.Entry(self.ventana)
        self.corriente_entry.grid(row=1, column=1)

        self.resistencia_label = tk.Label(self.ventana, text="Resistencia (R):")
        self.resistencia_label.grid(row=2, column=0)
        self.resistencia_entry = tk.Entry(self.ventana)
        self.resistencia_entry.grid(row=2, column=1)

        self.potencia_label = tk.Label(self.ventana, text="Potencia (P):")
        self.potencia_label.grid(row=3, column=0)
        self.potencia_entry = tk.Entry(self.ventana)
        self.potencia_entry.grid(row=3, column=1)

        # Botón de calcular
        self.calcular_button = tk.Button(self.ventana, text="CALCULAR", command=self.calcular)
        self.calcular_button.grid(row=4, column=0)

        # Botón de limpiar
        self.limpiar_button = tk.Button(self.ventana, text="LIMPIAR", command=self.limpiar)
        self.limpiar_button.grid(row=4, column=1)

        # Campos de salida
        self.tension_salida_label = tk.Label(self.ventana, text="Tensión (V):")
        self.tension_salida_label.grid(row=5, column=0)
        self.tension_salida = tk.Label(self.ventana, text="")
        self.tension_salida.grid(row=5, column=1)

        self.corriente_salida_label = tk.Label(self.ventana, text="Corriente (I):")
        self.corriente_salida_label.grid(row=6, column=0)
        self.corriente_salida = tk.Label(self.ventana, text="")
        self.corriente_salida.grid(row=6, column=1)

        self.resistencia_salida_label = tk.Label(self.ventana, text="Resistencia (R):")
        self.resistencia_salida_label.grid(row=7, column=0)
        self.resistencia_salida = tk.Label(self.ventana, text="")
        self.resistencia_salida.grid(row=7, column=1)

        self.potencia_salida_label = tk.Label(self.ventana, text="Potencia (P):")
        self.potencia_salida_label.grid(row=8, column=0)
        self.potencia_salida = tk.Label(self.ventana, text="")
        self.potencia_salida.grid(row=8, column=1)

        # Fórmulas
        self.formulas_label = tk.Label(self.ventana, text="Fórmulas:")
        self.formulas_label.grid(row=9, column=0, columnspan=2)
        self.formulas_text = tk.Text(self.ventana, height=10, width=40)
        self.formulas_text.grid(row=10, column=0, columnspan=2)

    def calcular(self):
        try:
            tension = float(self.tension_entry.get()) if self.tension_entry.get() else None
            corriente = float(self.corriente_entry.get()) if self.corriente_entry.get() else None
            resistencia = float(self.resistencia_entry.get()) if self.resistencia_entry.get() else None
            potencia = float(self.potencia_entry.get()) if self.potencia_entry.get() else None

            formulas = ""

            if tension and corriente:
                resistencia = tension / corriente
                potencia = tension * corriente
                formulas += "R = V / I\nP = V * I\n"
            elif tension and resistencia:
                corriente = tension / resistencia
                potencia = tension * corriente
                formulas += "I = V / R\nP = V * I\n"
            elif tension and potencia:
                resistencia = tension ** 2 / potencia
                corriente = potencia / tension
                formulas += "R = V^2 / P\nI = P / V\n"
            elif corriente and resistencia:
                tension = corriente * resistencia
                potencia = corriente ** 2 * resistencia
                formulas += "V = I * R\nP = I^2 * R\n"
            elif corriente and potencia:
                resistencia = potencia / corriente ** 2
                tension = potencia / corriente
                formulas += "R = P / I^2\nV = P / I\n"
            elif resistencia and potencia:
                corriente = (potencia / resistencia) ** 0.5
                tension = corriente * resistencia
                formulas += "I = sqrt(P / R)\nV = I * R\n"

            self.tension_salida.config(text=str(round(tension, 2)) if tension else "")
            self.corriente_salida.config(text=str(round(corriente, 2)) if corriente else "")
            self.resistencia_salida.config(text=str(round(resistencia, 2)) if resistencia else "")
            self.potencia_salida.config(text=str(round(potencia, 2)) if potencia else "")

            self.formulas_text.delete(1.0, tk.END)
            self.formulas_text.insert(tk.END, formulas)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos")

    def limpiar(self):
        self.tension_entry.delete(0, tk.END)
        self.corriente_entry.delete(0, tk.END)
        self.resistencia_entry.delete(0, tk.END)
        self.potencia_entry.delete(0, tk.END)
        self.tension_salida.config(text="")
        self.corriente_salida.config(text="")
        self.resistencia_salida.config(text="")
        self.potencia_salida.config(text="")
        self.formulas_text.delete(1.0, tk.END)

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    calculadora = CalculadoraOhm()
    calculadora.run()
