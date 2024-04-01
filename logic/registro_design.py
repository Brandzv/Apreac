"""Modulo de diseño del panel registro"""

import tkinter as tk
from tkinter import ttk, Label


class RegisterDesign:
    """Clase del diseño del panel escaneo"""

    def __init__(self, body):
        frame = tk.LabelFrame(body, text="Registro",
                              font=("Helvetica", 16, "bold"))
        frame.config(bd=2)
        frame.pack(fill="x", padx=100, pady=2, ipady=5)

        self.entry_id(frame)

    def entry_id(self, frame):
        """Función que crea el entry de ID"""

        self.label_id = Label(frame, text="Ingrese o escaneé ID: ", font=(
            "Helvetica", 13))

        self.id = ttk.Entry(frame, width=18,  font=("Helvetica", 13))

        self.button_id = tk.Button(
            frame, text="Registrar", font=("Helvetica", 9))

        # Calcula el ancho total del labelFrame
        frame_width = frame.winfo_width()

        # Calcula el ancho total de los widgets (label_id, id, button_id)
        widgets_width = self.label_id.winfo_width() + self.id.winfo_width() + \
            self.button_id.winfo_width()

        # Calcula el padding izquierdo necesario para centrar los widgets
        left_padding = max((frame_width - widgets_width) // 2, 0)

        # Establece el padding para los widgets
        self.label_id.pack(padx=left_padding)
        self.id.pack(padx=left_padding)
        self.button_id.pack(padx=left_padding, pady=5)
