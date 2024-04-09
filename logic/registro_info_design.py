"""Modulo de diseño del panel registro de información"""
import tkinter as tk
from tkinter import ttk
from conexion import cursor


class InfoDesign():
    """Clase del diseño del panel de registro de información"""

    def __init__(self, frame, search_id, body_table):
        # Cambio de tamaño del frame
        frame.pack(fill="x", padx=70, pady=2, ipady=5)

        cursor.execute(
            f"SELECT id, nombres, apellidoPaterno, apellidoMaterno, programa, rol FROM alumnos WHERE ID = {search_id}")
        alumno = cursor.fetchone()
        cursor.close()

        if alumno:
            self.id_alumno, self.nombre, self.apellido_paterno, self.apellido_materno, self.programa, self.rol = alumno
            self.student_info(frame)
            self.table_info(body_table)

        else:
            self.lbl = tk.Label(
                frame, text="Estudiante no encontrado", font=("Helvetica", 13))
            self.lbl.pack()

    def student_info(self, frame):
        """Función mostrar información de alumno"""

        # Mostrar ID de alumno
        self.text_id = tk.Label(
            frame, text="ID:", font=("Helvetica", 13))
        self.show_id = ttk.Entry(frame, font=("Helvetica", 13))
        self.show_id.insert(0, self.id_alumno)

        # Mostrar nombre de alumno
        self.text_nombre = tk.Label(frame, text="Nombre:",
                                    font=("Helvetica", 13))
        self.show_nombre = ttk.Entry(frame, font=("Helvetica", 13))
        self.show_nombre.insert(0, self.nombre)

        # Mostrar apellido paterno
        self.text_apellido_paterno = tk.Label(frame, text="Apellido Paterno:",
                                              font=("Helvetica", 13))
        self.show_apellido_paterno = ttk.Entry(
            frame, font=("Helvetica", 13))
        self.show_apellido_paterno.insert(0, self.apellido_paterno)

        # Mostrar apellido materno
        self.text_apellido_materno = tk.Label(frame, text="Apellido Materno:",
                                              font=("Helvetica", 13))
        self.show_apellido_materno = ttk.Entry(
            frame, font=("Helvetica", 13))
        self.show_apellido_materno.insert(0, self.apellido_materno)

        # Mostrar programa
        self.text_programa = tk.Label(frame, text="Programa:",
                                      font=("Helvetica", 13))
        self.show_programa = ttk.Entry(frame, font=("Helvetica", 13))
        self.show_programa.insert(0, self.programa)

        # Mostrar rol
        self.text_rol = tk.Label(
            frame, text="Rol:", font=("Helvetica", 13))
        self.show_rol = ttk.Entry(frame, font=("Helvetica", 13))
        self.show_rol.insert(0, self.rol)

        # Botón para registrar alumno
        self.button_register_student = tk.Button(
            frame, text="Registrar", command=self.save_register, width=15, height=1, font=("Helvetica", 11))

        # Posicionar información en pantalla
        self.text_id.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.show_id.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
        frame.columnconfigure(1, weight=1)
        #
        self.text_nombre.grid(row=1, column=2, pady=5, padx=5, sticky="w")
        self.show_nombre.grid(row=1, column=3, pady=5, padx=5, sticky="ew")
        frame.columnconfigure(3, weight=1)
        #
        self.text_apellido_paterno.grid(
            row=2, column=0, pady=5, padx=5, sticky="w")
        self.show_apellido_paterno.grid(
            row=2, column=1, pady=5, padx=5, sticky="ew")
        frame.columnconfigure(1, weight=1)
        #
        self.text_apellido_materno.grid(
            row=2, column=2, pady=5, padx=5, sticky="w")
        self.show_apellido_materno.grid(
            row=2, column=3, pady=5, padx=5, sticky="ew")
        frame.columnconfigure(3, weight=1)
        #
        self.text_programa.grid(row=3, column=0, pady=5, padx=5, sticky="w")
        self.show_programa.grid(row=3, column=1, pady=5, padx=5, sticky="ew")
        frame.columnconfigure(1, weight=1)
        #
        self.text_rol.grid(row=3, column=2, pady=5, padx=5, sticky="w")
        self.show_rol.grid(row=3, column=3, pady=5, padx=5, sticky="ew")
        frame.columnconfigure(3, weight=1)
        #
        self.button_register_student.grid(
            row=4, columnspan=4)

    def table_info(self, body_table):
        """Función tabla de registro bitácora"""
        self.tree = ttk.Treeview(body_table, columns=(
            "numero_registro", "numero_pc", "fecha", "nombre_alumno", "rol", "programa", "hr_entrada", "hr_salida", "actividad"), show="headings")

        self.tree.heading("numero_registro", text="No.", anchor="center")
        self.tree.heading("numero_pc", text="PC", anchor="center")
        self.tree.heading("fecha", text="Fecha", anchor="center")
        self.tree.heading("nombre_alumno", text="Nombre", anchor="center")
        self.tree.heading("rol", text="Rol", anchor="center")
        self.tree.heading("programa", text="Programa", anchor="center")
        self.tree.heading("hr_entrada", text="Hora entrada", anchor="center")
        self.tree.heading("hr_salida", text="Hora salida", anchor="center")
        self.tree.heading("actividad", text="Actividad", anchor="center")

        self.tree.column("numero_registro", anchor="w")
        self.tree.column("numero_pc", anchor="w")
        self.tree.column("fecha", anchor="w")
        self.tree.column("nombre_alumno", anchor="w")
        self.tree.column("rol", anchor="w")
        self.tree.column("programa", anchor="w")
        self.tree.column("hr_entrada", anchor="w")
        self.tree.column("hr_salida", anchor="w")
        self.tree.column("actividad", anchor="w")

        for column in self.tree['columns']:
            self.tree.column(column, width=50,  anchor="center")
        self.tree.pack(fill="both", expand=True, pady=1, padx=5)

    def save_register(self):
        """Función guardar registro"""

    def show_registers(self):
        """Función mostrar registros"""
