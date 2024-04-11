"""Modulo de diseño del panel registro de información"""
import tkinter as tk
import datetime
from tkinter import ttk
from conexion import cursor, conecta


class InfoDesign():
    """Clase del diseño del panel de registro de información"""

    def __init__(self, frame, search_id, body_table):
        self.body_table = body_table
        # Cambio de tamaño del frame
        frame.pack(fill="x", padx=70, pady=2, ipady=5)

        cursor.execute(
            f"SELECT id, nombres, apellidoPaterno, apellidoMaterno, programa, rol FROM alumnos WHERE ID = {search_id}")
        alumno = cursor.fetchone()

        conecta.commit()

        if alumno:
            self.id_alumno, self.nombre, self.apellido_paterno, self.apellido_materno, self.programa, self.rol = alumno
            self.student_info(frame)
            self.table_info(body_table)
            self.show_registers(body_table)

        else:
            self.lbl = tk.Label(
                frame, text="Estudiante no encontrado", font=("Helvetica", 13))
            self.lbl.pack()

    def student_info(self, frame):
        """Función mostrar información de alumno"""

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

        # Botón seleccionar actividad y pc
        self.button_select = tk.Button(
            frame, text="Selección", width=15, height=1, font=("Helvetica", 11))

        # Botón para registrar alumno
        self.button_register_student = tk.Button(
            frame, text="Registrar", command=self.save_register, width=15, height=1, font=("Helvetica", 11))

        # Posicionar información en pantalla
        self.text_nombre.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.show_nombre.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
        frame.columnconfigure(1, weight=1)
        #
        self.text_apellido_paterno.grid(
            row=1, column=2, pady=5, padx=5, sticky="w")
        self.show_apellido_paterno.grid(
            row=1, column=3, pady=5, padx=5, sticky="ew")
        frame.columnconfigure(3, weight=1)
        #
        self.text_apellido_materno.grid(
            row=2, column=0, pady=5, padx=5, sticky="w")
        self.show_apellido_materno.grid(
            row=2, column=1, pady=5, padx=5, sticky="ew")
        frame.columnconfigure(1, weight=1)
        #
        self.text_programa.grid(row=2, column=2, pady=5, padx=5, sticky="w")
        self.show_programa.grid(row=2, column=3, pady=5, padx=5, sticky="ew")
        frame.columnconfigure(3, weight=1)
        #
        self.text_rol.grid(row=3, column=0, pady=5, padx=5, sticky="w")
        self.show_rol.grid(row=3, column=1, pady=5, padx=5, sticky="ew")
        frame.columnconfigure(1, weight=1)
        #
        self.button_select.grid(row=3, column=2, columnspan=2)
        frame.columnconfigure(3, weight=1)
        #
        self.button_register_student.grid(
            row=4, columnspan=4)

    def table_info(self, body_table):
        """Función tabla de registro bitácora"""
        self.tree = ttk.Treeview(body_table, columns=(
            "numero_registro", "numero_pc", "fecha", "nombre_alumno", "rol", "programa", "hr_entrada", "hr_salida", "actividad"), show="headings")

        self.tree.heading("#1", text="No.", anchor="center")
        self.tree.heading("#2", text="PC", anchor="center")
        self.tree.heading("#3", text="Fecha", anchor="center")
        self.tree.heading("#4", text="Nombre", anchor="center")
        self.tree.heading("#5", text="Rol", anchor="center")
        self.tree.heading("#6", text="Programa", anchor="center")
        self.tree.heading("#7", text="Hora entrada", anchor="center")
        self.tree.heading("#8", text="Hora salida", anchor="center")
        self.tree.heading("#9", text="Actividad", anchor="center")

        self.tree.column("#1", width=10, anchor="center")
        self.tree.column("#2", width=10, anchor="center")
        self.tree.column("#3", width=45, anchor="center")
        self.tree.column("#4", width=50, anchor="center")
        self.tree.column("#5", width=45, anchor="center")
        self.tree.column("#6", width=50, anchor="center")
        self.tree.column("#7", width=50, anchor="center")
        self.tree.column("#8", width=50, anchor="center")
        self.tree.column("#9", width=50, anchor="center")

        self.tree.pack(fill="both", expand=True, pady=1, padx=5)

    def save_register(self):
        """Función guardar registro"""
        # Obtener la fecha y hora actual
        time = datetime.datetime.now()
        # Formatear la fecha como dd/mm/aa
        date = time.strftime("%d/%m/%y")
        # Formatear la hora como HH:MM
        hour = time.strftime("%H:%M")

        # obtiene datos a guardar
        save_nombre = self.show_nombre.get()
        save_apellido_paterno = self.show_apellido_paterno.get()
        save_apellido_amaterno = self.show_apellido_materno.get()

        nombre_completo = f"{save_nombre} {save_apellido_paterno} {save_apellido_amaterno}"

        programa = self.show_programa.get()

        rol = self.show_rol.get()

        cursor.execute(
            "INSERT INTO bitacoraUso (fecha, nombreAlumno, rol, programa, horaEntrada) VALUES (?, ?, ?, ?, ?)", (date, nombre_completo, rol, programa, hour))

        conecta.commit()

        self.show_registers(self.body_table)

    def show_registers(self, body_table):
        """Función mostrar registros"""
        self.tree.delete(*self.tree.get_children()
                         )  # Limpiar registros existentes
        cursor.execute(
            "SELECT no, pc, fecha, nombreAlumno, rol, programa, horaEntrada, horaSalida, actividad FROM bitacoraUso")
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)
