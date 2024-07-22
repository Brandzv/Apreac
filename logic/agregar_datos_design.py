"""
Fecha: 07/07/24
Descripción: Modulo de diseño del panel agregar datos
"""

import tkinter as tk
import logic.open_panels


class AddDataDesign():
    """Clase del diseño de opciones para agregar datos a la base de datos"""

    def __init__(self, body):
        self.body = body

        # Crear LabelFrame para contener la sección de reportes
        self.option_frame = tk.LabelFrame(body, text="Opciones",
                                          font=("Helvetica", 16, "bold"))
        # Ancho de borde
        self.option_frame.config(bd=2)
        # Se expande horizontalmente
        self.option_frame.pack(fill="both", padx=60, pady=2, ipady=20)

        # Configurar la columna para que se expanda
        self.option_frame.grid_columnconfigure(
            0, weight=1)  # La columna 0 se expandirá
        # Configurar el comportamiento de redimensionamiento de los label
        self.update_labels()
        # Vincular el evento de redimensionamiento del frame a la función on_resize
        self.option_frame.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        """Actualiza el wraplength de los labels cuando el contenedor cambia de tamaño"""

        wraplength = self.option_frame.winfo_width(
        ) - 20  # Ajusta el valor según sea necesario
        for widget in self.option_frame.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(wraplength=wraplength)

    def update_labels(self):
        """Actualiza el contenido de los labels"""

        self.select_users(self.option_frame)
        self.select_students(self.option_frame)
        self.select_courses(self.option_frame)

    def select_users(self, option_frame):
        """Función donde se agrega widgets de la opción usuario"""

        # Crear título para la sección de usuarios
        title_users = tk.Label(option_frame, text="Seleccionar Usuario",
                               font=("Helvetica", 13, "bold"))
        # Crear descripción para la sección de usuarios con ajuste de texto y alineación a la izquierda
        text_users = tk.Label(option_frame, text='Permite la inscripción de nuevos usuarios para acceder al sistema en la tabla "Usuarios", asegurando que los datos sean almacenados correctamente.',
                              font=("Helvetica", 11), wraplength=300, anchor="w", justify="left")  # Ajusta el wraplength y alinea a la izquierda
        # Crear botón para agregar un nuevo usuario
        button_users = tk.Button(option_frame, text="Agregar Usuario",
                                 command=self.open_form_users, font=("Helvetica", 11))

        # Colocar los widgets
        title_users.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        text_users.grid(row=1, column=0, padx=10, pady=0,
                        sticky="w")
        button_users.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    def select_students(self, option_frame):
        """Función donde se agrega widgets de la opción estudiantes"""

        # Crear título para la sección de estudiantes
        title_students = tk.Label(option_frame, text="Seleccionar Estudiante",
                                  font=("Helvetica", 13, "bold"))
        # Crear descripción para la sección de estudiantes con ajuste de texto y alineación a la izquierda
        text_students = tk.Label(option_frame, text='Permite la inscripción de nuevos estudiantes en la tabla "Estudiantes" de la base de datos, asegurando que los datos sean almacenados correctamente.',
                                 font=("Helvetica", 11), wraplength=300, anchor="w", justify="left")  # Ajusta el wraplength y alinea a la izquierda
        # Crear botón para agregar un nuevo estudiante
        button_students = tk.Button(option_frame, text="Agregar Estudiante",
                                    command=self.open_form_students, font=("Helvetica", 11))

        # Colocar los widgets
        title_students.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        text_students.grid(row=4, column=0, padx=10, pady=0,
                           sticky="w")
        button_students.grid(row=5, column=0, padx=10, pady=5, sticky="w")

    def select_courses(self, option_frame):
        """Función donde se agrega widgets de la opción cursos"""

        # Crear título para la sección de cursos
        title_courses = tk.Label(option_frame, text="Seleccionar Curso",
                                 font=("Helvetica", 13, "bold"))
        # Crear descripción para la sección de cursos con ajuste de texto y alineación a la izquierda
        text_courses = tk.Label(option_frame, text='Agrega nuevos cursos al horario en la tabla "Cursos" de la base de datos, garantizando una correcta actualización y registro de la información.',
                                font=("Helvetica", 11), wraplength=300, anchor="w", justify="left")  # Ajusta el wraplength y alinea a la izquierda
        # Crear botón para agregar un nuevo curso
        button_courses = tk.Button(option_frame, text="Agregar Curso",
                                   command=self.open_form_courses, font=("Helvetica", 11))

        # Colocar los widgets
        title_courses.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        text_courses.grid(row=7, column=0, padx=10, pady=0,
                          sticky="w")  # Ajustar el sticky a "w"
        button_courses.grid(row=8, column=0, padx=10, pady=5, sticky="w")

    def open_form_users(self):
        """Función para abrir la ventana de agregar usuario"""

        self.clear_panel(self.body)
        show_users_form = logic.open_panels.OpenPanel(self.body)
        show_users_form.show_users_form()

    def open_form_students(self):
        """Función para abrir la ventana de agregar estudiante"""

        self.clear_panel(self.body)
        show_students_form = logic.open_panels.OpenPanel(self.body)
        show_students_form.show_students_form()

    def open_form_courses(self):
        """Función para abrir la ventana de agregar curso"""

        self.clear_panel(self.body)
        show_courses_form = logic.open_panels.OpenPanel(self.body)
        show_courses_form.show_courses_form()

    def clear_panel(self, panel):
        """Función que se encarga de limpiar el contenido del panel"""

        for widget in panel.winfo_children():
            widget.destroy()
