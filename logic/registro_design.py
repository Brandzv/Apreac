"""Modulo de diseño del panel registro"""

import tkinter as tk
from tkinter import ttk
from logic.registro_info_design import InfoDesign


class RegisterDesign:
    """Clase del diseño del panel escaneo"""

    def __init__(self, body):
        body_table = body
        frame = tk.LabelFrame(body, text="Registro",
                              font=("Helvetica", 16, "bold"))
        frame.config(bd=2)
        frame.pack(fill="x", padx=100, pady=2, ipady=5)

        self.register_id(frame, body_table)

    def register_id(self, frame, body_table):
        """Función que crea el entry de ID"""

        self.label_id = tk.Label(
            frame, text="Ingrese o escaneé ID:", font=("Helvetica", 13))

        self.entry_id = ttk.Entry(frame, width=18, font=("Helvetica", 13))

        # Función para verificar si el entry contiene números válidos
        def validar_entry(search_id, body_table):
            try:
                float(search_id)
                return True
            except ValueError:
                return False

        def clic_button():
            search_id = self.entry_id.get()  # Obtiene el id del Entry
            if validar_entry(search_id, body_table):
                self.open_info_frame(frame, search_id, body_table)
            else:
                print("Por favor, ingresa números válidos en el Entry.")

        self.button_id = tk.Button(
            frame, text="Registrar", command=clic_button, width=10, height=1, font=("Helvetica", 9))

        frame_width = frame.winfo_width()

        # Calcula el ancho total de los widgets (label_id, entry_id, button_id)
        widgets_width = self.label_id.winfo_width() + self.entry_id.winfo_width() + \
            self.button_id.winfo_width()

        # Calcula el padding izquierdo necesario para centrar los widgets
        left_padding = max((frame_width - widgets_width) // 2, 0)

        self.label_id.pack(padx=left_padding)
        self.entry_id.pack(padx=left_padding)
        self.entry_id.focus_set()
        self.button_id.pack(padx=left_padding, pady=5)

    def open_info_frame(self, frame, search_id, body_table):
        """Función que abre frame de información y cierra el panel de registro."""
        self.clear_panel(frame)
        InfoDesign(frame, search_id, body_table)

    def clear_panel(self, panel):
        """Función que se encarga de limpiar el contenido del frame"""
        for widget in panel.winfo_children():
            widget.destroy()
