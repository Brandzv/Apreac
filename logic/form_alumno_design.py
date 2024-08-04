"""
Fecha: 20/07/24
Descripción: Modulo del formulario de alumnos con CRUD
"""

import tkinter as tk
from tkinter import ttk, messagebox
import logic.open_panels
from utility import util_window as centrar_ventana
from conexion import get_cursor


class FormStudent():
    """Clase del CRUD de la tabla alumnos"""

    def __init__(self, body):
        # Obtener el cursor de la base de datos
        conecta, cursor = get_cursor()
        # Variable para limpiar el panel
        self.refresh = body
        # LabelFrame que contiene el CRUD
        student_frame = tk.LabelFrame(body, text="Agregar Alumnos",
                                      font=("Helvetica", 16, "bold"))
        # Ancho de borde
        student_frame.config(bd=2)
        # Se expande horizontalmente
        student_frame.pack(fill="x", padx=5, pady=2, ipady=5)

        # Llamada a la función del diseño del formulario
        self.form_students(student_frame, conecta, cursor)
        self.table_students(body)
        self.show_students(conecta, cursor)

    def form_students(self, student_frame, conecta, cursor):
        """Función del diseño del formulario"""

        # Ingreso de id
        self.text_id = tk.Label(
            student_frame, text="ID:", font=("Helvetica", 13))
        self.show_id = ttk.Entry(student_frame, font=("Helvetica", 13))

        # Ingreso de nombre
        self.text_name = tk.Label(
            student_frame, text="Nombre:", font=("Helvetica", 13))
        self.show_name = ttk.Entry(student_frame, font=("Helvetica", 13))

        # Ingreso de apellido paterno
        self.text_father_surname = tk.Label(
            student_frame, text="Apellido paterno:", font=("Helvetica", 13))
        self.show_father_surname = ttk.Entry(
            student_frame, font=("Helvetica", 13))

        # Ingreso de apellido materno
        self.text_mother_surname = tk.Label(
            student_frame, text="Apellido materno:", font=("Helvetica", 13))
        self.show_mother_surname = ttk.Entry(
            student_frame, font=("Helvetica", 13))

        # Ingreso de programa
        self.text_career = tk.Label(
            student_frame, text="Programa:", font=("Helvetica", 13))
        self.show_career = ttk.Entry(student_frame, font=("Helvetica", 13))

        # Ingreso de rol
        self.text_role = tk.Label(
            student_frame, text="Rol:", font=("Helvetica", 13))
        self.show_role = ttk.Entry(student_frame, font=("Helvetica", 13))

        # Configuración de botones
        self.button_back = tk.Button(
            student_frame, text="Regresar", command=self.back, font=("Helvetica", 11))
        self.button_save = tk.Button(
            student_frame, text="Guardar", command=lambda: self.save_form(conecta, cursor), font=("Helvetica", 11))

        # Configuración de columnas del LabelFrame
        student_frame.columnconfigure(2, weight=1)
        student_frame.columnconfigure(4, weight=1)

        # Posicionar los widgets
        self.text_id.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.show_id.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        self.text_name.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        self.show_name.grid(row=1, column=4, padx=5, pady=5, sticky="ew")

        self.text_father_surname.grid(
            row=2, column=1, padx=5, pady=5, sticky="w")
        self.show_father_surname.grid(
            row=2, column=2, padx=5, pady=5, sticky="ew")
        self.text_mother_surname.grid(
            row=2, column=3, padx=5, pady=5, sticky="w")
        self.show_mother_surname.grid(
            row=2, column=4, padx=5, pady=5, sticky="ew")

        self.text_career.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.show_career.grid(row=3, column=2, padx=5, pady=5, sticky="ew")
        self.text_role.grid(row=3, column=3, padx=5, pady=5, sticky="w")
        self.show_role.grid(row=3, column=4, padx=5, pady=5, sticky="ew")

        self.button_back.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.button_save.grid(row=4, column=1, columnspan=4,
                              padx=5, pady=5, ipadx=25)

    def table_students(self, body):
        """Función de diseño del encabezado del Treeview"""

        # Configuración de encabezados del Treeview
        self.tree = ttk.Treeview(body, columns=(
            "#1", "#2", "#3", "#4", "#5", "#6", "#7"), show="headings")

        # Nombre de los encabezados
        self.tree.heading("#1", text="No.", anchor="center")
        self.tree.heading("#2", text="ID", anchor="center")
        self.tree.heading("#3", text="Nombre", anchor="center")
        self.tree.heading("#4", text="Apellido paterno", anchor="center")
        self.tree.heading("#5", text="Apellido materno", anchor="center")
        self.tree.heading("#6", text="Programa", anchor="center")
        self.tree.heading("#7", text="Rol", anchor="center")
        # Configuración de columnas
        self.tree.column("#1", width=10, anchor="center")
        self.tree.column("#2", width=50, anchor="center")
        self.tree.column("#3", width=50, anchor="center")
        self.tree.column("#4", width=50, anchor="center")
        self.tree.column("#5", width=50, anchor="center")
        self.tree.column("#6", width=50, anchor="center")
        self.tree.column("#7", width=50, anchor="center")

        self.tree.pack(fill="both", expand=True, pady=1, padx=5)

        # Evento doble click en la tabla
        self.tree.bind("<Double-1>", self.on_double_click)

    def show_students(self, conecta, cursor):
        """Función de mostrar los registros de la tabla alumnos"""

        # Limpiar tabla
        self.tree.delete(*self.tree.get_children())

        # Consulta SQL para obtener los datos de la tabla alumnos
        cursor.execute(
            "SELECT id, idAlumno, nombres, apellidoPaterno, apellidoMaterno, programa, rol FROM alumnos")
        # Insertar los datos en el Treeview
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    def on_double_click(self, event):
        """Función de doble click en la tabla"""

        # Obtener el cursor de la base de datos
        conecta, cursor = get_cursor()
        # Obtener el item seleccionado
        item = self.tree.selection()[0]
        values = self.tree.item(item, "values")
        self.menu_student(values, conecta, cursor)

    def menu_student(self, values, conecta, cursor):
        """Función de diseño del TopLevel para editar y eliminar"""

        self.menu_window = tk.Toplevel()
        self.menu_window.title(
            f"Menú de opciones de {values[2]} {values[3]} {values[4]}")
        self.menu_window.resizable(False, False)

        # Tamaño de la ventana emergente
        w, h = 672, 150
        centrar_ventana.centrar_ventana(self.menu_window, w, h)

        # Guardar el id del estudiante seleccionado
        self.selected_student_id = values[0]

        # Editar id
        self.label_edit_id = tk.Label(
            self.menu_window, text="ID:", font=("Helvetica", 13))
        self.entry_edit_id = ttk.Entry(
            self.menu_window, font=("Helvetica", 13))
        self.entry_edit_id.insert(0, values[1])
        self.entry_edit_id.focus_set()

        # Editar nombre
        self.label_edit_name = tk.Label(
            self.menu_window, text="Nombre:", font=("Helvetica", 13))
        self.entry_edit_name = ttk.Entry(
            self.menu_window, font=("Helvetica", 13))
        self.entry_edit_name.insert(0, values[2])

        # Editar apellido paterno
        self.label_edit_father_surname = tk.Label(
            self.menu_window, text="Apellido paterno:", font=("Helvetica", 13))
        self.entry_edit_father_surname = ttk.Entry(
            self.menu_window, font=("Helvetica", 13))
        self.entry_edit_father_surname.insert(0, values[3])

        # Editar apellido materno
        self.label_edit_mother_surname = tk.Label(
            self.menu_window, text="Apellido materno:", font=("Helvetica", 13))
        self.entry_edit_mother_surname = ttk.Entry(
            self.menu_window, font=("Helvetica", 13))
        self.entry_edit_mother_surname.insert(0, values[4])

        # Editar programa
        self.label_edit_career = tk.Label(
            self.menu_window, text="Programa:", font=("Helvetica", 13))
        self.entry_edit_career = ttk.Entry(
            self.menu_window, font=("Helvetica", 13))
        self.entry_edit_career.insert(0, values[5])

        # Editar rol
        self.label_edit_role = tk.Label(
            self.menu_window, text="Rol:", font=("Helvetica", 13))
        self.entry_edit_role = ttk.Entry(
            self.menu_window, font=("Helvetica", 13))
        self.entry_edit_role.insert(0, values[6])

        # Crear un frame para los botones
        button_frame = tk.Frame(self.menu_window)
        button_frame.grid(row=3, column=0, columnspan=4, pady=10)

        # Botones para editar y eliminar
        button_edit = tk.Button(
            button_frame, text="Guardar", command=lambda: self.edit_student(conecta, cursor), font=("Helvetica", 11))
        button_delete = tk.Button(
            button_frame, text="Eliminar", command=lambda: self.delete_student(conecta, cursor), font=("Helvetica", 11))

        # Colocar widgets en el grid
        self.label_edit_id.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_edit_id.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.label_edit_name.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_edit_name.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        self.label_edit_father_surname.grid(
            row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_edit_father_surname.grid(
            row=1, column=1, padx=5, pady=5, sticky="ew")

        self.label_edit_mother_surname.grid(
            row=1, column=2, padx=5, pady=5, sticky="w")
        self.entry_edit_mother_surname.grid(
            row=1, column=3, padx=5, pady=5, sticky="ew")

        self.label_edit_career.grid(
            row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_edit_career.grid(
            row=2, column=1, padx=5, pady=5, sticky="ew")

        self.label_edit_role.grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.entry_edit_role.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

        # Colocar los botones en el frame
        button_edit.pack(side="left", padx=10)
        button_delete.pack(side="right", padx=10)

    def save_form(self, conecta, cursor):
        """Función para obtener y guardar nuevos alumnos"""

        # Obtener los valores de los campos de entrada
        student_id = self.show_id.get()
        student_name = self.show_name.get()
        father_surname = self.show_father_surname.get()
        mother_surname = self.show_mother_surname.get()
        career = self.show_career.get()
        role = self.show_role.get()

        if student_id.isdigit():
            if self.isAlpha(student_name) and self.isAlpha(father_surname) and self.isAlpha(mother_surname) and career and role.isalpha():
                # Verificar si los campos no están vacíos
                cursor.execute(
                    "INSERT INTO alumnos (idAlumno, nombres, apellidoPaterno, apellidoMaterno, programa, rol) VALUES (?, ?, ?, ?, ?, ?)", (student_id, student_name, father_surname, mother_surname, career, role))
                conecta.commit()

                self.show_id.delete(0, tk.END)
                self.show_name.delete(0, tk.END)
                self.show_father_surname.delete(0, tk.END)
                self.show_mother_surname.delete(0, tk.END)
                self.show_career.delete(0, tk.END)
                self.show_role.delete(0, tk.END)

                self.show_students(conecta, cursor)
            else:
                # Si los campos están vacíos, mostrar mensaje de advertencia
                messagebox.showwarning(
                    "Advertencia", "Por favor, complete los campos correctamente.")
        else:
            # Mostrar mensaje de advertencia si el ID no es un número
            messagebox.showwarning(
                "Advertencia", "El campo ID debe ser un valor numérico.")

    def edit_student(self, conecta, cursor):
        """Función para editar los alumnos ya existentes"""

        new_student_id = self.entry_edit_id.get()
        new_student_name = self.entry_edit_name.get()
        new_father_surname = self.entry_edit_father_surname.get()
        new_mother_surname = self.entry_edit_mother_surname.get()
        new_career = self.entry_edit_career.get()
        new_role = self.entry_edit_role.get()

        if new_student_id.isdigit():
            if self.isAlpha(new_student_name) and self.isAlpha(new_father_surname) and self.isAlpha(new_mother_surname) and new_career and new_role.isalpha():
                # Verificar si los campos no están vacíos
                cursor.execute("UPDATE alumnos SET idAlumno = ?, nombres = ?, apellidoPaterno = ?, apellidoMaterno = ?, programa = ?, rol = ? WHERE id = ?",
                               (new_student_id, new_student_name, new_father_surname,
                                new_mother_surname, new_career, new_role, self.selected_student_id))
                conecta.commit()
                self.menu_window.destroy()
                self.show_students(conecta, cursor)
            else:
                # Si los campos están vacíos, mostrar mensaje de advertencia
                messagebox.showwarning(
                    "Advertencia", "Por favor, complete los campos correctamente.")
        else:
            # Mostrar mensaje de advertencia si el ID no es un número
            messagebox.showwarning(
                "Advertencia", "El campo ID debe ser un valor numérico.")

    def delete_student(self, conecta, cursor):
        """Función para eliminar alumnos ya existentes"""

        # Mostrar mensaje de confirmación
        result = messagebox.askyesno(
            "Confirmación", "¿Está seguro de que desea eliminar este registro?")

        if result:
            cursor.execute(
                "DELETE FROM alumnos WHERE id = ?", (self.selected_student_id,))
            conecta.commit()
            self.menu_window.destroy()
            self.show_students(conecta, cursor)

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
