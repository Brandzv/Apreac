"""Modulo de diseño del panel Reportes"""
import tkinter as tk
from tkinter import ttk, messagebox


class ReportsDesign():
    """Clase del diseño del panel Reportes"""

    def __init__(self, body):
        report_frame = tk.LabelFrame(body, text="Reportes",
                                     font=("Helvetica", 16, "bold"))
        # Ancho de borde
        report_frame.config(bd=2)
        # Se expande horizontalmente
        report_frame.pack(fill="x", padx=100, pady=2, ipady=20)

        self.select_type(report_frame)

    def select_type(self, report_frame):
        """Función para seleccionar el tipo de reporte"""

        #
        lbl_report = tk.Label(report_frame, text="Selecciona el tipo de reporte:",
                              font=("Helvetica", 13))

        types_options = ["Fecha especifica", "Rango de fechas"]
        #
        self.dropdown_type = ttk.Combobox(
            report_frame, values=types_options, state="readonly", width=20, font=("Helvetica", 13))
        #
        self.dropdown_type.set("Selecciona una opción")

        button_confirm = tk.Button(report_frame, text="Confirmar", command=self.option_report,
                                   font=("Helvetica", 13))

        lbl_report.pack(anchor='center', pady=5)
        self.dropdown_type.pack(anchor='center')
        button_confirm.pack(anchor='center', pady=8)

    def option_report(self):
        """Función para generar el reporte"""

        if self.dropdown_type.get() == "Fecha especifica":
            print("Fecha especifica")

        elif self.dropdown_type.get() == "Rango de fechas":
            print("Rango de fechas")

        else:
            messagebox.showerror(
                "Error", "Por favor selecciona una opción válida")
            return
