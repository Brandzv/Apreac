"""
Fecha: 09/05/24
Descripción: Modulo que muestra el frame para buscar alumno por ID ademas de mostrar tabla de registros
"""

import tkinter as tk
import datetime
from tkinter import ttk, messagebox
import logic.bitacora_pdf
from logic.registro_info_design import InfoDesign
from conexion import cursor


class RegisterDesign:
    """Clase del diseño del panel escaneo"""

    def __init__(self, body):
        # El panel body se usara para mostrar frame para buscar alumnos por id la tabla de registros
        body_table = body
        # Este frame se utilizará para buscar alumnos por su IDS
        frame = tk.LabelFrame(body, text="Registro",
                              font=("Helvetica", 16, "bold"))
        # Ancho de borde
        frame.config(bd=2)
        # Se expande horizontalmente
        frame.pack(fill="x", padx=100, pady=2, ipady=5)

        # Llama a los métodos
        self.register_id(frame, body_table)
        self.table_info(body_table)
        self.show_registers(body_table)

    def register_id(self, frame, body_table):
        """Función que crea el entry de ID"""

        # Etiqueta para indicar que se debe ingresar o escanear id
        self.label_id = tk.Label(
            frame, text="Ingrese o escanee ID:", font=("Helvetica", 13))

        # Entry para que el usuario ingrese el ID
        self.entry_id = ttk.Entry(frame, width=18, font=("Helvetica", 13))

        # Función para verificar si el entry contiene números válidos
        def validate_entry(search_id, body_table):
            try:
                float(search_id)
                return True
            except ValueError:
                return False

        def clic_button():
            search_id = self.entry_id.get()  # Obtiene el id del Entry
            # Verifica si el ID ingresado es válido
            if validate_entry(search_id, body_table):
                # Abre el panel de información con el ID proporcionado
                self.open_info_frame(frame, search_id, body_table)
            else:
                messagebox.showerror(
                    "Error", "Ingrese un ID válido")

        # Botón para Buscar el alumno del ID ingresado con la función "clic_button"
        self.button_id = tk.Button(
            frame, text="Buscar", command=clic_button, width=10, height=1, font=("Helvetica", 11))
        self.button_generate_pdf = tk.Button(
            frame, text="Generar PDF", command=self.create_pdf, width=10, font=("Helvetica", 11))

        # Obtiene el ancho actual del frame
        frame_width = frame.winfo_width()

        # Calcula el ancho total de los widgets (label_id, entry_id, button_id)
        widgets_width = self.label_id.winfo_width() + self.entry_id.winfo_width() + \
            self.button_id.winfo_width()

        # Calcula el padding izquierdo necesario para centrar los widgets
        left_padding = max((frame_width - widgets_width) // 2, 0)

        # Agrega padding izquierdo a "label_id" y "entry_id"
        self.label_id.pack(padx=left_padding)
        self.entry_id.pack(padx=left_padding)

        # Establece foco en el campo de entrada para que el usuario comience a escribir de inmediato
        self.entry_id.focus_set()

        # Empaqueta los botones en la misma fila y centrados horizontalmente
        self.button_id.pack(padx=left_padding, pady=5)
        self.button_generate_pdf.pack(padx=left_padding)

    def open_info_frame(self, frame, search_id, body_table):
        """Función que abre frame de información y cierra el panel de registro."""

        # Limpia el "frame" antes de entrar a InfoDesign
        self.clear_panel(frame)
        # Destruye la tabla antes de entrar a InfoDesign
        self.tree.destroy()
        # Abre el modulo "registro_info_design" y muestra la interfaz gráfica en panel
        InfoDesign(frame, search_id, body_table)

    def table_info(self, body_table):
        """Función tabla de registro bitácora"""

        # Configura el widget tree con las columnas y encabezados siguientes
        self.tree = ttk.Treeview(body_table, columns=(
            "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9"), show="headings")

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

    def show_registers(self, body_table):
        """Función mostrar registros"""

        # Borra todas las filas previamente agregadas al widget tree, lo que es útil
        # antes de volver a cargar nuevos datos en el widget tree
        self.tree.delete(*self.tree.get_children())

        # Se usa como filtro de fecha actual
        current_date = datetime.datetime.now().strftime("%d/%m/%y")

        # Seleccionar registros a mostrar y filtrar por fecha
        cursor.execute(
            "SELECT no, pc, fecha, nombreAlumno, rol, programa, horaEntrada, horaSalida, actividad FROM bitacoraUso WHERE fecha = ?", (current_date,))

        # Agrega filas al widget tree con los valores obtenidos de la consulta a la base de datos
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)

    def create_pdf(self):
        """Función para generar el PDF"""

        time = datetime.datetime.now()
        date = time.strftime("%d/%m/%y")

        create_bitacora_pdf = logic.bitacora_pdf.BitacoraPDF()
        create_bitacora_pdf.generate_bitacora(self, date)

    def clear_panel(self, panel):
        """Función que se encarga de limpiar el contenido del frame"""

        for widget in panel.winfo_children():
            widget.destroy()
