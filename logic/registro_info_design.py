"""
@Author: Brandzv
Fecha: 09/05/24
Descripción: Modulo que muestra el panel registro de información de los alumnos
"""
import tkinter as tk
import datetime
from tkinter import ttk, messagebox
import logic.open_panels
import logic.bitacora_pdf
from conexion import cursor, conecta


class InfoDesign():
    """Clase del diseño del panel de registro de información"""

    def __init__(self, frame, search_id, body_table):
        # Cambio de tamaño del frame
        frame.pack(fill="x", padx=70, pady=2, ipady=5)

        # Se usara para refrescar la tabla al guardar los registros
        self.refresh = body_table

        # Se selecciona los datos necesarios para mostrar en los input
        cursor.execute(
            f"SELECT id, nombres, apellidoPaterno, apellidoMaterno, programa, rol FROM alumnos WHERE ID = {search_id}")
        alumno = cursor.fetchone()

        # Guarda los cambios
        conecta.commit()

        # Verifica si existe un alumno con la ID ingresada
        if alumno:
            # Si existe alumno con la ID entonces se desempaquetara los valores del alumno
            # en las siguientes variables
            self.id_alumno, self.nombre, self.apellido_paterno, self.apellido_materno, self.programa, self.rol = alumno
            # Se llaman los métodos
            self.student_info(frame)
            self.table_info(body_table)
            self.show_registers(body_table)
        else:
            # En caso de que no exista alumno con la ID ingresada se mostrara el siguiente texto
            self.lbl = tk.Label(
                frame, text="Estudiante no encontrado", font=("Helvetica", 13))
            self.lbl.pack()

    def student_info(self, frame):
        """Función mostrar información de alumno"""

        # Mostrar información de alumno
        self.text_nombre = tk.Label(frame, text="Nombre:",
                                    font=("Helvetica", 13))
        self.show_nombre = ttk.Entry(frame, font=("Helvetica", 13))
        self.show_nombre.insert(0, self.nombre)
        #
        self.text_apellido_paterno = tk.Label(frame, text="Apellido Paterno:",
                                              font=("Helvetica", 13))
        self.show_apellido_paterno = ttk.Entry(
            frame, font=("Helvetica", 13))
        self.show_apellido_paterno.insert(0, self.apellido_paterno)
        #
        self.text_apellido_materno = tk.Label(frame, text="Apellido Materno:",
                                              font=("Helvetica", 13))
        self.show_apellido_materno = ttk.Entry(
            frame, font=("Helvetica", 13))
        self.show_apellido_materno.insert(0, self.apellido_materno)
        #
        self.text_programa = tk.Label(frame, text="Programa:",
                                      font=("Helvetica", 13))
        self.show_programa = ttk.Entry(frame, font=("Helvetica", 13))
        self.show_programa.insert(0, self.programa)
        #
        self.text_rol = tk.Label(
            frame, text="Rol:", font=("Helvetica", 13))
        self.show_rol = ttk.Entry(frame, font=("Helvetica", 13))
        self.show_rol.insert(0, self.rol)

        # Dropdown seleccionar actividades
        options_activity = ["Clase", "Tarea"]
        self.dropdown_activity = ttk.Combobox(
            frame, values=options_activity, state="readonly")
        self.dropdown_activity.current(0)
        # Dropdown seleccionar pc
        options_pc = [str(i) for i in range(1, 31)]
        self.dropdown_pc = ttk.Combobox(
            frame, values=options_pc, state="readonly")
        self.dropdown_pc.set("Selección PC")

        # Botón para volver a buscar id
        self.button_recover_id = tk.Button(
            frame, text="Atrás", command=self.recover_id, width=6, font=("Helvetica", 11))
        # Botón para registrar alumno
        self.button_register_student = tk.Button(
            frame, text="Registrar", command=self.save_register, width=15, font=("Helvetica", 11))
        # Botón para generar PDF
        self.button_generate_pdf = tk.Button(
            frame, text="Generar PDF", command=self.create_pdf, width=15, font=("Helvetica", 11))

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
        self.dropdown_activity.grid(row=3, column=2, pady=5, padx=5)
        #
        self.dropdown_pc.grid(row=3, column=3, pady=5, padx=5)
        #
        self.button_recover_id.grid(
            row=4, column=0, pady=5, padx=5, sticky="w")
        #
        self.button_register_student.grid(row=4, column=1, padx=5)
        #
        self.button_generate_pdf.grid(row=4, column=2)

    def table_info(self, body_table):
        """Función tabla de registro bitácora"""

        # Configura el widget tree con las columnas y encabezados siguientes
        self.tree = ttk.Treeview(body_table, columns=(
            "numero_registro", "numero_pc", "fecha", "nombre_alumno", "rol", "programa", "hr_entrada", "hr_salida", "actividad"), show="headings")

        # Define cómo se mostrará el encabezado de las columnas en el widget tree
        self.tree.heading("#1", text="No.", anchor="center")
        self.tree.heading("#2", text="PC", anchor="center")
        self.tree.heading("#3", text="Fecha", anchor="center")
        self.tree.heading("#4", text="Nombre", anchor="center")
        self.tree.heading("#5", text="Rol", anchor="center")
        self.tree.heading("#6", text="Programa", anchor="center")
        self.tree.heading("#7", text="Hora entrada", anchor="center")
        self.tree.heading("#8", text="Hora salida", anchor="center")
        self.tree.heading("#9", text="Actividad", anchor="center")

        # Configura ancho y alineación de las columnas
        self.tree.column("#1", width=10, anchor="center")
        self.tree.column("#2", width=10, anchor="center")
        self.tree.column("#3", width=45, anchor="center")
        self.tree.column("#4", width=50, anchor="center")
        self.tree.column("#5", width=45, anchor="center")
        self.tree.column("#6", width=50, anchor="center")
        self.tree.column("#7", width=50, anchor="center")
        self.tree.column("#8", width=50, anchor="center")
        self.tree.column("#9", width=50, anchor="center")

        # Configura la posición de tree y el como se expande
        self.tree.pack(fill="both", expand=True, pady=1, padx=5)

    def save_register(self):
        """Función guardar registro"""

        # Obtener valores de los campos
        pc_seleccionado = self.dropdown_pc.get()
        save_nombre = self.show_nombre.get()
        save_apellido_paterno = self.show_apellido_paterno.get()
        save_apellido_materno = self.show_apellido_materno.get()
        programa = self.show_programa.get()
        rol = self.show_rol.get()
        actividad = self.dropdown_activity.get()

        # Se usa para obligar tener en regla todos los campos
        if pc_seleccionado and save_nombre and save_apellido_paterno and save_apellido_materno and programa and rol and actividad:

            # Asegura de que se haya seleccionado una PC
            if pc_seleccionado != "Selección PC":

                # Campo "no" en bd bitacoraUso
                cursor.execute(
                    "SELECT no FROM bitacoraUso ORDER BY ROWID DESC LIMIT 1")
                result = cursor.fetchone()
                # Checa cual es el ultimo numero de la columna "No." para seguir desde el numero
                # donde se quedo en la numeración de los registros
                if result:
                    last_number = result[0]
                else:
                    last_number = 0
                #
                counter = last_number + 1
                if counter > 20:
                    counter = 1

                # Campo "pc" en bd bitacoraUso
                pc_uso = f"PC{pc_seleccionado}"

                # Campo "fecha" en bd bitacoraUso
                time = datetime.datetime.now()
                #
                date = time.strftime("%d/%m/%y")

                # Campo "hora" en bd bitacoraUso
                hour = time.strftime("%H:%M")

                # Campo "nombreAlumno" en bd bitacoraUso
                nombre_completo = f"{save_nombre} {save_apellido_paterno} {save_apellido_materno}"

                # Guarda los datos obtenidos en la tabla "bitacoraUso"
                cursor.execute(
                    "INSERT INTO bitacoraUso (no, pc, fecha, nombreAlumno, rol, programa, horaEntrada, actividad) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (counter, pc_uso, date, nombre_completo, rol, programa, hour, actividad))

                conecta.commit()

                # Limpia el frame "body"
                body = self.refresh
                self.clear_panel(body)
                # Abre el panel "register_design" en frame body
                show_register_design = logic.open_panels.OpenPanel(body)
                show_register_design.show_register_panel()

            else:
                messagebox.showerror(
                    "Error", "Por favor, selecciona una PC")
        else:
            messagebox.showerror(
                "Error", "Por favor, completa todos los campos")

        # Refresca la tabla cuando se guarda un registro
        # ? self.show_registers(self.refresh) <--- Por si se llega a utilizar en el futuro

    def show_registers(self, body_table):
        """Función mostrar registros"""

        # Borra todas las filas previamente agregadas al widget tree, lo que es útil
        # antes de volver a cargar nuevos datos en el widget tree
        self.tree.delete(*self.tree.get_children())

        # Se usa como filtro de fecha actual
        fecha_actual = datetime.datetime.now().strftime("%d/%m/%y")

        # Seleccionar registros a mostrar y filtrar por fecha
        cursor.execute(
            "SELECT no, pc, fecha, nombreAlumno, rol, programa, horaEntrada, horaSalida, actividad FROM bitacoraUso WHERE fecha = ?", (fecha_actual,))

        # Agrega filas al widget tree con los valores obtenidos de la consulta a la base de datos
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)

    def recover_id(self):
        """Función recuperar id"""

        # Limpia el frame "body"
        body = self.refresh
        self.clear_panel(body)
        # Abre el panel "register_design" en frame body
        show_register_design = logic.open_panels.OpenPanel(body)
        show_register_design.show_register_panel()

    def create_pdf(self):
        """Función para generar el PDF"""
        create_bitacora_pdf = logic.bitacora_pdf.BitacoraPDF()
        create_bitacora_pdf.generate_bitacora(self)

    def clear_panel(self, panel):
        """Función que se encarga de limpiar el contenido del frame"""
        for widget in panel.winfo_children():
            widget.destroy()
