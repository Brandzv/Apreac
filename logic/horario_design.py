"""
Fecha: 02/06/24
Descripción: Modulo de diseño del panel horario
"""

import tkinter as tk
from tkinter import ttk
from config import BODY_COLOR
from conexion import get_cursor


class ScheduleDesign():
    """Clase del diseño del panel horario"""

    def __init__(self, body):
        # Obtener el cursor de la base de datos
        conecta, cursor = get_cursor()
        label_schedule_text = tk.Label(body, text="Horario",
                                       bg=BODY_COLOR, font=("Helvetica", 16))
        label_schedule_text.pack()

        self.table_schedule(body, conecta, cursor)

    def table_schedule(self, body, conecta, cursor):
        """Función para crear la tabla de horario"""

        # Configura el widget tree con las columnas y encabezados siguientes
        self.tree = ttk.Treeview(body, columns=(
            "horas", "lunes", "martes", "miercoles", "jueves", "viernes"), show="headings")

        # Define cómo se mostrará el encabezado de las columnas en el widget tree
        self.tree.heading("#1", text=" ", anchor="center")
        self.tree.heading("#2", text="Lunes", anchor="center")
        self.tree.heading("#3", text="Martes", anchor="center")
        self.tree.heading("#4", text="Miércoles", anchor="center")
        self.tree.heading("#5", text="Jueves", anchor="center")
        self.tree.heading("#6", text="Viernes", anchor="center")

        # Configura ancho y alineación de las columnas
        self.tree.column("#1", width=30, anchor="center")
        self.tree.column("#2", width=50, anchor="center")
        self.tree.column("#3", width=50, anchor="center")
        self.tree.column("#4", width=50, anchor="center")
        self.tree.column("#5", width=50, anchor="center")
        self.tree.column("#6", width=50, anchor="center")

        # Ejecuta la consulta SQL para obtener los datos de la tabla "horarios"
        cursor.execute(
            "SELECT crn, docente, diaSemana, horaEntrada, horaSalida FROM horarios")
        # Obtiene los datos de la consulta
        schedule_data = cursor.fetchall()

        # Llenar la tabla con los datos
        for clase in schedule_data:
            # Desempaqueta los valores de cada clase
            crn, docente, dia_semana, hora_entrada, hora_salida = clase
            # Inserta una fila en la tabla con el rango de horas y el nombre del docente para
            # el día de la semana correspondiente
            self.tree.insert("", "end", values=(
                f"{hora_entrada} - {hora_salida}", *[docente if dia_semana == i else "-" for i in range(5)]))

        # Configura la posición de tree y el como se expande
        self.tree.pack(fill="both", expand=True, pady=5, padx=5)
