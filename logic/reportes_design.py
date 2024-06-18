"""
@Author: Brandzv
Fecha: 16/06/24
Descripción: Modulo que crea funciones para poder crear pdf con datos de una fecha no actual
"""
import tkinter as tk
from tkinter import messagebox, END
from tkcalendar import Calendar
from utility import util_window as centrar_ventana
import logic.bitacora_pdf


class ReportsDesign():
    """Clase del diseño del panel Reportes"""

    def __init__(self, body):
        # Crear LabelFrame para contener la sección de reportes
        report_frame = tk.LabelFrame(body, text="Reportes",
                                     font=("Helvetica", 16, "bold"))
        # Ancho de borde
        report_frame.config(bd=2)
        # Se expande horizontalmente
        report_frame.pack(fill="x", padx=100, pady=2, ipady=20)

        self.specific_date = None
        self.set_calendar = None
        self.entry_date = None
        self.date_window = None
        self.button_generate_pdf = None

        self.select_type(report_frame)

    def select_type(self, report_frame):
        """Función para seleccionar el tipo de reporte"""

        # label para pedir al usuario que seleccione una fecha
        lbl_date = tk.Label(
            report_frame, text="Seleccionar fecha:", font=("Helvetica", 13))

        # Campo de entrada para que el usuario introduzca a fecha
        self.entry_date = tk.Entry(report_frame, font=("Helvetica", 13))
        # Inserta el texto 'dd/mm/yyyy' en el campo de entrada
        self.entry_date.insert(0, "dd/mm/yyyy")
        # Asociar el evento de clic izquierdo del ratón con la función 'pick_date' en 'entry_date'
        self.entry_date.bind("<1>", self.pick_date)

        # botón que ejecuta la función 'create_pdf' al ser presionado
        self.button_generate_pdf = tk.Button(
            report_frame, text="Generar PDF", command=self.create_pdf, width=10, font=("Helvetica", 13))

        # Imprime los widget en el frame
        lbl_date.pack(anchor="center", pady=10)
        self.entry_date.pack(anchor="center")
        self.button_generate_pdf.pack(anchor="center", pady=5)

    def pick_date(self, event):
        """Función para seleccionar la fecha"""

        # Crea una nueva ventana como una ventana de nivel superior
        self.date_window = tk.Toplevel()
        # Establecer las dimensiones de la ventana
        w, h = 300, 270
        self.date_window.geometry(f"{w}x{h}+0+0")
        # Centrar la ventana 'date_window' en la pantalla
        centrar_ventana.centrar_ventana(self.date_window, w, h)
        self.date_window.resizable(False, False)

        # Hacer que la ventana 'date_window' sea transitoria
        self.date_window.transient()
        # Obtener el foco para la ventana
        self.date_window.focus_get()
        # Establecer la ventana 'date_window' para que capture todos los eventos
        self.date_window.grab_set()

        # Crear el widget de calendario
        self.set_calendar = Calendar(
            self.date_window, date_pattern="dd/mm/yy", font=("Helvetica", 13))

        button_submit = tk.Button(
            self.date_window, text="Seleccionar", command=self.get_date, font=("Helvetica", 13))

        self.set_calendar.pack()
        button_submit.pack(anchor="center", pady=5)

    def get_date(self):
        """Función para obtener la fecha seleccionada"""

        # Eliminar el contenido del campo de entrada 'entry_date'
        self.entry_date.delete(0, END)
        # Insertar la fecha seleccionada del calendario en el campo de entrada
        self.entry_date.insert(0, self.set_calendar.get_date())
        # Destruir la ventana emergente después de seleccionar la fecha
        self.date_window.destroy()

    def create_pdf(self):
        """Función para generar el PDF"""

        # Obtener la fecha del campo de entrada 'entry_date'
        date = self.entry_date.get()
        # Verificar si la fecha es igual al texto de ejemplo 'dd/mm/yyyy'
        if date == "dd/mm/yyyy":
            # Mostrar un mensaje de error si no se ha seleccionado una fecha válida
            messagebox.showerror(
                "Error", "Por favor, selecciona una fecha válida.")
        else:
            # Continúa con la creación del PDF si la fecha es válida
            create_bitacora_pdf = logic.bitacora_pdf.BitacoraPDF()
            create_bitacora_pdf.generate_bitacora(self, date)
