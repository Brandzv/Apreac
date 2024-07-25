"""
Fecha: 20/07/24
Descripción: Modulo del formulario de usuarios con CRUD 
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import logic.open_panels
from utility import util_window as centrar_ventana
from conexion import get_cursor


class FormUser():
    """Clase del CRUD de la tabla usuarios"""

    def __init__(self, body):
        # Obtener el cursor de la base de datos
        conecta, cursor = get_cursor()
        # Variable para limpiar el panel
        self.refresh = body
        # LabelFrame que contiene el CRUD
        user_frame = tk.LabelFrame(body, text="Agregar Usuarios",
                                   font=("Helvetica", 16, "bold"))
        # Ancho de borde
        user_frame.config(bd=2)
        # Se expande horizontalmente
        user_frame.pack(fill="x", padx=50, pady=2, ipadx=10, ipady=5)

        # Llamada a la función del diseño del formulario
        self.form_users(user_frame, conecta, cursor)
        self.table_users(body, conecta, cursor)
        self.show_users(conecta, cursor)

    def form_users(self, user_frame, conecta, cursor):
        """Función del diseño del formulario"""

        # Ingreso de usuario
        self.text_user = tk.Label(
            user_frame, text="Usuario:", font=("Helvetica", 13))
        self.show_user = ttk.Entry(user_frame, font=("Helvetica", 13))
        # Inserta valor aleatoriamente
        user_values = ["CTC1", "CTC2"]
        self.show_user.insert(0, random.choice(user_values))

        # Ingreso de contraseña
        self.text_password = tk.Label(
            user_frame, text="Contraseña:", font=("Helvetica", 13))
        self.show_password = ttk.Entry(user_frame, font=("Helvetica", 13))

        # Configuración de botones
        self.button_back = tk.Button(
            user_frame, text="Regresar", command=self.back, font=("Helvetica", 11))
        self.button_save = tk.Button(
            user_frame, text="Guardar", command=lambda: self.save_form(conecta, cursor), font=("Helvetica", 11))

        # Posicionamiento de los elementos
        user_frame.grid_columnconfigure(0, weight=1)
        user_frame.grid_columnconfigure(0, weight=1)
        user_frame.grid_columnconfigure(1, weight=1)
        user_frame.grid_rowconfigure(0, weight=1)
        user_frame.grid_rowconfigure(1, weight=1)
        user_frame.grid_rowconfigure(2, weight=1)
        #
        self.text_user.grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.show_user.grid(row=0, column=1, padx=1, pady=2, sticky="w")
        self.text_password.grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.show_password.grid(row=1, column=1, padx=1, pady=2, sticky="w")
        self.button_back.grid(row=2, column=0, padx=2, pady=2, sticky="w")
        self.button_save.grid(row=2, column=0, columnspan=2, padx=2, pady=2)

    def table_users(self, body, conecta, cursor):
        """Función de diseño del encabezado del Treeview"""

        # Configuración de encabezados del Treeview
        self.tree = ttk.Treeview(body, columns=(
            "#1", "#2", "#3"), show="headings")

        # Nombre de los encabezados
        self.tree.heading("#1", text="No.", anchor="center")
        self.tree.heading("#2", text="Usuario", anchor="center")
        self.tree.heading("#3", text="Contraseña", anchor="center")
        # Configuración de columnas
        self.tree.column("#1", width=10, anchor="center")
        self.tree.column("#2", width=50, anchor="center")
        self.tree.column("#3", width=50, anchor="center")

        self.tree.pack(fill="both", expand=True, pady=1, padx=5)

        # Evento doble click en la tabla
        self.tree.bind(
            "<Double-1>", self.on_double_click)

    def show_users(self, conecta, cursor):
        """Función de mostrar los registros de la tabla usuarios"""

        # Limpiar tabla
        self.tree.delete(*self.tree.get_children())

        # Consulta SQL para obtener los datos de la tabla usuarios
        cursor.execute("SELECT id_usuario, usuario, contraseña FROM usuarios")
        # Insertar los datos en el Treeview
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=(
                row[0], row[1], row[2]))

    def on_double_click(self, event):
        """Función de doble click en la tabla"""

        # Obtener el cursor de la base de datos
        conecta, cursor = get_cursor()

        # Obtener el item seleccionado
        item = self.tree.selection()[0]
        values = self.tree.item(item, "values")
        self.menu_user(values, conecta, cursor)

    def menu_user(self, values, conecta, cursor):
        """Función de diseño del TopLevel para editar y eliminar"""

        self.menu_window = tk.Toplevel()
        self.menu_window.title(f"Menú de opciones de {values[1]}")
        self.menu_window.resizable(False, False)

        # Tamaño de la ventana emergente
        w, h = 320, 150
        centrar_ventana.centrar_ventana(self.menu_window, w, h)

        # Configuración del grid
        self.menu_window.grid_rowconfigure(0, weight=1)
        self.menu_window.grid_rowconfigure(1, weight=1)
        self.menu_window.grid_rowconfigure(2, weight=1)
        self.menu_window.grid_columnconfigure(0, weight=1)
        self.menu_window.grid_columnconfigure(1, weight=1)

        # Editar usuario
        self.label_edit_user = tk.Label(
            self.menu_window, text="Usuario:", font=("Helvetica", 13))
        self.entry_edit_user = ttk.Entry(
            self.menu_window, font=("Helvetica", 13))

        # Editar contraseña
        self.label_edit_password = tk.Label(
            self.menu_window, text="Contraseña:", font=("Helvetica", 13))
        self.edit_password = ttk.Entry(
            self.menu_window, font=("Helvetica", 13))

        # Crear un frame para los botones
        button_frame = tk.Frame(self.menu_window)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        # Botones para editar y eliminar
        button_edit = tk.Button(button_frame, text="Guardar",
                                command=lambda: self.edit_user(values, conecta, cursor), font=("Helvetica", 11))
        button_delete = tk.Button(button_frame, text="Eliminar",
                                  command=lambda: self.delete_user(values[0], conecta, cursor), font=("Helvetica", 11))

        # Colocar widgets en el grid
        self.label_edit_user.grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.entry_edit_user.grid(row=0, column=1, padx=5, pady=2, sticky="w")
        self.entry_edit_user.insert(0, values[1])

        self.label_edit_password.grid(
            row=1, column=0, padx=5, pady=2, sticky="e")
        self.edit_password.grid(row=1, column=1, padx=5, pady=2, sticky="w")
        self.edit_password.insert(0, values[2])

        # Colocar los botones en el frame
        button_edit.pack(side="left", padx=10)
        button_delete.pack(side="right", padx=10)

    def save_form(self, conecta, cursor):
        """Función para obtener y guardar nuevos usuarios"""

        # Obtener los valores de los campos de entrada
        user = self.show_user.get()
        password = self.show_password.get()

        if user and password:
            # Verificar si los campos no están vacíos
            cursor.execute(
                "INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)",
                (user, password))
            conecta.commit()
            self.show_users(conecta, cursor)
        else:
            # Si los campos están vacíos, mostrar mensaje de advertencia
            messagebox.showerror(
                "Advertencia", "Por favor, complete todos los campos.")

    def edit_user(self, values, conecta, cursor):
        """Función para editar los usuarios ya existentes"""

        new_user = self.entry_edit_user.get()  # Obtener el usuario actualizado
        new_password = self.edit_password.get()  # Obtener la contraseña actualizada

        if new_user and new_password:
            cursor.execute("UPDATE usuarios SET usuario = ?, contraseña = ? WHERE id_usuario = ?",
                           (new_user, new_password, values[0]))
            conecta.commit()
            self.menu_window.destroy()
            self.show_users(conecta, cursor)
        else:
            messagebox.showerror(
                "Error", "Por favor, complete todos los campos.")

    def delete_user(self, id_usuario, conecta, cursor):
        """Función para eliminar usuarios ya existentes"""

        # Mostrar mensaje de confirmación
        result = messagebox.askyesno(
            "Confirmación", "¿Está seguro de que desea eliminar este registro?")

        if result:
            cursor.execute(
                "DELETE FROM usuarios WHERE id_usuario = ?", (id_usuario,))
            conecta.commit()
            self.menu_window.destroy()
            self.show_users(conecta, cursor)

    def back(self):
        """Función para volver al panel anterior"""

        # Limpia el frame "body"
        body = self.refresh
        self.clear_panel(body)
        # Abre el panel "AddDataDesign" en frame body
        show_register_design = logic.open_panels.OpenPanel(body)
        show_register_design.show_add_panel()

    def clear_panel(self, panel):
        """Función que se encarga de limpiar el contenido del frame"""

        # Destruir todos los widgets hijos del panel
        for widget in panel.winfo_children():
            widget.destroy()
