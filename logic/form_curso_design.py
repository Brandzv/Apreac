"""
Fecha: 23/07/24
Descripción: Modulo del formulario del horario con CRUD
"""

import tkinter as tk
from tkinter import ttk, messagebox
import logic.open_panels
from utility import util_window as centrar_ventana
from conexion import get_cursor


# Diccionario para convertir entre números y nombres de días
DAY_MAPPING = {
    'Lunes': '0', 'Martes': '1', 'Miércoles': '2', 'Jueves': '3', 'Viernes': '4',
    'Sábado': '5', 'Domingo': '6', '0': 'Lunes', '1': 'Martes', '2': 'Miércoles',
    '3': 'Jueves', '4': 'Viernes', '5': 'Sábado', '6': 'Domingo'
}


class FormCourses():
    """Clase del CRUD de la tabla cursos"""

    def __init__(self, body):
        # Obtener el cursor de la base de datos
        conecta, cursor = get_cursor()
        # Variable para limpiar el panel
        self.refresh = body
        # LabelFrame que contiene el CRUD
        schedule_frame = tk.LabelFrame(body, text="Agregar Clase",
                                       font=("Helvetica", 16, "bold"))
        # Ancho de borde
        schedule_frame.config(bd=2)
        # Se expande horizontalmente
        schedule_frame.pack(fill="x", padx=5, pady=2, ipady=5)

        # Llamada a la función del diseño del formulario
        self.form_schedule(schedule_frame, conecta, cursor)
        self.table_schedule(body)
        self.show_schedule(conecta, cursor)

    def form_schedule(self, schedule_frame, conecta, cursor):
        """Función del diseño del formulario"""

        # Ingreso del CRN
        self.text_crn = tk.Label(
            schedule_frame, text="CRN:", font=("Helvetica", 13))
        self.show_crn = ttk.Entry(schedule_frame, font=("Helvetica", 13))

        # Ingreso del docente
        self.text_teacher = tk.Label(
            schedule_frame, text="Docente:", font=("Helvetica", 13))
        self.show_teacher = ttk.Entry(schedule_frame, font=("Helvetica", 13))

        # Ingreso del dia de la semana
        self.text_course_day_week = tk.Label(
            schedule_frame, text="Dia de la semana:", font=("Helvetica", 13))
        options_day_week = ["Lunes", "Martes", "Miércoles",
                            "Jueves", "Viernes", "Sábado", "Domingo"]
        self.show_course_day_week = ttk.Combobox(
            schedule_frame, values=options_day_week, state="readonly", font=("Helvetica", 13))

        # Ingreso de la hora de entrada
        self.text_entry_time = tk.Label(
            schedule_frame, text="Hora de entrada:", font=("Helvetica", 13))
        self.show_entry_time = ttk.Entry(
            schedule_frame, font=("Helvetica", 13))

        # Ingreso de la hora de salida
        self.text_departure_time = tk.Label(
            schedule_frame, text="Hora de salida:", font=("Helvetica", 13))
        self.show_departure_time = ttk.Entry(
            schedule_frame, font=("Helvetica", 13))

        # Configuración de botones
        self.button_back = tk.Button(
            schedule_frame, text="Regresar", command=self.back, font=("Helvetica", 11))
        self.button_save = tk.Button(
            schedule_frame, text="Guardar", command=lambda: self.save_form(conecta, cursor), font=("Helvetica", 11))

        # Configuración de columnas del LabelFrame
        schedule_frame.columnconfigure(2, weight=1)
        schedule_frame.columnconfigure(4, weight=1)

        # Posicionar los widgets
        self.text_crn.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.show_crn.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        self.text_teacher.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        self.show_teacher.grid(row=1, column=4, padx=5, pady=5, sticky="ew")

        self.text_course_day_week.grid(
            row=2, column=1, padx=5, pady=5, sticky="w")
        self.show_course_day_week.grid(
            row=2, column=2, padx=5, pady=5, sticky="ew")
        self.text_entry_time.grid(
            row=2, column=3, padx=5, pady=5, sticky="w")
        self.show_entry_time.grid(
            row=2, column=4, padx=5, pady=5, sticky="ew")

        self.text_departure_time.grid(
            row=3, column=1, padx=5, pady=5, sticky="w")
        self.show_departure_time.grid(
            row=3, column=2, padx=5, pady=5, sticky="ew")

        self.button_back.grid(row=4, column=2, padx=5, pady=5, sticky="e")
        self.button_save.grid(row=4, column=3, padx=5, pady=5, sticky="w")

    def table_schedule(self, body):
        """Función de diseño del encabezado del Treeview"""

        # Configuración de encabezados del Treeview
        self.tree = ttk.Treeview(body, columns=(
            "#1", "#2", "#3", "#4", "#5"), show="headings")

        # Nombre de los encabezados
        self.tree.heading("#1", text="CRN", anchor="center")
        self.tree.heading("#2", text="Docente", anchor="center")
        self.tree.heading("#3", text="Día de la semana", anchor="center")
        self.tree.heading("#4", text="Hora de entrada", anchor="center")
        self.tree.heading("#5", text="Hora de salida", anchor="center")

        # Configuración de columnas
        self.tree.column("#1", width=50, anchor="center")
        self.tree.column("#2", width=50, anchor="center")
        self.tree.column("#3", width=50, anchor="center")
        self.tree.column("#4", width=50, anchor="center")
        self.tree.column("#5", width=50, anchor="center")

        self.tree.pack(fill="both", expand=True, pady=1, padx=5)

        # Evento doble click en la tabla
        self.tree.bind("<Double-1>", self.on_double_click)

    def show_schedule(self, conecta, cursor):
        """Función de mostrar los registros de la tabla cursos"""

        # Limpiar tabla
        self.tree.delete(*self.tree.get_children())

        # Consulta SQL para obtener los datos de la tabla cursos
        cursor.execute(
            "SELECT id, crn, docente, diaSemana, horaEntrada, horaSalida FROM horarios")
        # Insertar los datos en el Treeview
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=(
                row[1], row[2], DAY_MAPPING[str(row[3])], row[4], row[5]), iid=row[0])

    def on_double_click(self, event):
        """Función de doble click en la tabla"""

        # Obtener el cursor de la base de datos
        conecta, cursor = get_cursor()
        # Obtener el item seleccionado
        item = self.tree.selection()[0]
        values = self.tree.item(item, "values")
        self.menu_schedule(values, conecta, cursor)

    def menu_schedule(self, values, conecta, cursor):
        """Función de diseño del TopLevel para editar y eliminar"""

        self.menu_window = tk.Toplevel()
        self.menu_window.title(
            f"Menú de opciones de {values[0]}")
        self.menu_window.resizable(False, False)

        # Tamaño de la ventana emergente
        w, h = 672, 150
        centrar_ventana.centrar_ventana(self.menu_window, w, h)

        # Guardar el id del estudiante seleccionado
        self.selected_course_id = self.tree.selection()[0]

        # Editar CRN
        self.label_edit_crn = tk.Label(
            self.menu_window, text="CRN:", font=("Helvetica", 13))
        self.entry_edit_crn = ttk.Entry(
            self.menu_window, font=("Helvetica", 13))
        self.entry_edit_crn.insert(0, values[0])
        self.entry_edit_crn.focus_set()

        # Editar docente
        self.label_edit_teacher = tk.Label(
            self.menu_window, text="Docente:", font=("Helvetica", 13))
        self.entry_edit_teacher = ttk.Entry(
            self.menu_window, font=("Helvetica", 13))
        self.entry_edit_teacher.insert(0, values[1])

        # Editar dia de la semana
        self.label_edit_day_week = tk.Label(
            self.menu_window, text="Día de la semana:", font=("Helvetica", 13))
        options_day_week = ["Lunes", "Martes", "Miércoles",
                            "Jueves", "Viernes", "Sábado", "Domingo"]
        self.entry_edit_day_week = ttk.Combobox(
            self.menu_window, values=options_day_week, state="readonly", font=("Helvetica", 13))
        self.entry_edit_day_week.insert(0, values[2])

        # Editar hora de entrada
        self.label_edit_entry_time = tk.Label(
            self.menu_window, text="Hora de entrada:", font=("Helvetica", 13))
        self.entry_edit_entry_time = ttk.Entry(
            self.menu_window, font=("Helvetica", 13))
        self.entry_edit_entry_time.insert(0, values[3])

        # Editar hora de salida
        self.label_edit_departure_time = tk.Label(
            self.menu_window, text="Hora de salida:", font=("Helvetica", 13))
        self.entry_edit_departure_time = ttk.Entry(
            self.menu_window, font=("Helvetica", 13))
        self.entry_edit_departure_time.insert(0, values[4])

        # Botones
        self.button_edit_save = tk.Button(
            self.menu_window, text="Guardar", command=lambda: self.edit_schedule(conecta, cursor), font=("Helvetica", 11))
        self.button_edit_delete = tk.Button(
            self.menu_window, text="Eliminar", command=lambda: self.delete_schedule(conecta, cursor), font=("Helvetica", 11))

        # Configuración de columnas del TopLevel
        self.menu_window.columnconfigure(2, weight=1)
        self.menu_window.columnconfigure(4, weight=1)

        # Posicionar los widgets
        self.label_edit_crn.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.entry_edit_crn.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        self.label_edit_teacher.grid(
            row=1, column=3, padx=5, pady=5, sticky="w")
        self.entry_edit_teacher.grid(
            row=1, column=4, padx=5, pady=5, sticky="ew")

        self.label_edit_day_week.grid(
            row=2, column=1, padx=5, pady=5, sticky="w")
        self.entry_edit_day_week.grid(
            row=2, column=2, padx=5, pady=5, sticky="ew")
        self.label_edit_entry_time.grid(
            row=2, column=3, padx=5, pady=5, sticky="w")
        self.entry_edit_entry_time.grid(
            row=2, column=4, padx=5, pady=5, sticky="ew")

        self.label_edit_departure_time.grid(
            row=3, column=1, padx=5, pady=5, sticky="w")
        self.entry_edit_departure_time.grid(
            row=3, column=2, padx=5, pady=5, sticky="ew")

        self.button_edit_save.grid(
            row=4, column=2, padx=5, pady=5, sticky="e")
        self.button_edit_delete.grid(row=4, column=3,
                                   padx=5, pady=5, sticky="w")

    def save_form(self, conecta, cursor):
        """Función para obtener y guardar nuevos cursos"""

        # Obtener los valores de los campos de entrada
        course_crn = self.show_crn.get()
        course_teacher = self.show_teacher.get()
        course_day_week = self.show_course_day_week.get()
        course_entry_time = self.show_entry_time.get()
        course_departure_time = self.show_departure_time.get()

        if course_crn.isdigit():
            if self.isAlpha(course_teacher) and course_day_week in DAY_MAPPING and course_entry_time and course_departure_time:
                # Verificar si los campos no están vacíos
                cursor.execute(
                    "INSERT INTO horarios (crn, docente, diaSemana, horaEntrada, horaSalida) VALUES (?, ?, ?, ?, ?)",
                    (course_crn, course_teacher, DAY_MAPPING[course_day_week], course_entry_time, course_departure_time))
                conecta.commit()
                self.show_schedule(conecta, cursor)
            else:
                # Si los campos están vacíos, mostrar mensaje de advertencia
                messagebox.showwarning(
                    "Advertencia", "Por favor, complete los campos correctamente.")
        else:
            # Mostrar mensaje de advertencia si el CRN no es un número
            messagebox.showwarning(
                "Advertencia", "El campo CRN debe ser un valor numérico.")

    def edit_schedule(self, conecta, cursor):
        """Función para editar los cursos ya existentes"""

        new_course_crn = self.entry_edit_crn.get()
        new_course_teacher = self.entry_edit_teacher.get()
        new_course_day_week = self.entry_edit_day_week.get()
        new_course_entry_time = self.entry_edit_entry_time.get()
        new_course_departure_time = self.entry_edit_departure_time.get()

        if new_course_crn.isdigit():
            if self.isAlpha(new_course_teacher) and new_course_day_week in DAY_MAPPING and new_course_entry_time and new_course_departure_time:
                # Verificar si los campos no están vacíos
                cursor.execute("UPDATE horarios SET crn = ?, docente = ?, diaSemana = ?, horaEntrada = ?, horaSalida = ? WHERE id = ?",
                               (new_course_crn, new_course_teacher, DAY_MAPPING[new_course_day_week],
                                new_course_entry_time, new_course_departure_time, self.selected_course_id))
                conecta.commit()
                self.menu_window.destroy()
                self.show_schedule(conecta, cursor)
            else:
                # Si los campos están vacíos, mostrar mensaje de advertencia
                messagebox.showwarning(
                    "Advertencia", "Por favor, complete los campos correctamente.")
        else:
            # Mostrar mensaje de advertencia si el CRN no es un número
            messagebox.showwarning(
                "Advertencia", "El campo CRN debe ser un valor numérico.")

    def delete_schedule(self, conecta, cursor):
        """Función para eliminar los cursos existentes"""

        # Mostrar mensaje de confirmación
        result = messagebox.askyesno(
            "Confirmación", "¿Está seguro de que desea eliminar este registro?")

        if result:
            cursor.execute("DELETE FROM horarios WHERE id = ?",
                           (self.selected_course_id,))
            conecta.commit()
            self.menu_window.destroy()
            self.show_schedule(conecta, cursor)

    def back(self):
        """Función para volver al panel anterior"""

        # Limpia el frame "body"
        body = self.refresh
        self.clear_panel(body)
        # Abre el panel "AddDataDesign" en frame body
        show_register_design = logic.open_panels.OpenPanel(body)
        show_register_design.show_add_panel()

    def isAlpha(self, s):
        return all(c.isalpha() or c.isspace() for c in s)

    def clear_panel(self, panel):
        """Función que se encarga de limpiar el contenido del frame"""

        # Destruir todos los widgets hijos del panel
        for widget in panel.winfo_children():
            widget.destroy()
