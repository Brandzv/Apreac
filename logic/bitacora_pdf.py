"""Modulo para generar PDF de bitacora de uso"""
import datetime
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from conexion import cursor


class BitacoraPDF:
    """Clase para generar PDF de bitacora de uso"""

    def generate_bitacora(self, crear_pdf):
        """Función para generar el PDF"""

        if crear_pdf:
            # Nombrar archivo
            time = datetime.datetime.now()
            date_current_time = time.strftime("%d-%m-%y_%H%M%S")
            doc = SimpleDocTemplate(
                f"BitacoraUso{date_current_time}.pdf", pagesize=landscape(letter))

            # Estilo del encabezado
            header_style = TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ])

            # Estilo del titulo
            title_style = getSampleStyleSheet()['Normal']
            title_style.fontSize = 24
            title_style.leftIndent = 170
            title_style.leading = 30

            story = []

            # Logo de la UNID
            logo_unid = './resource/LogoUnid.png'
            print_logo = Image(logo_unid, width=110,
                               height=45, hAlign='LEFT')

            title = "Bitácora de uso CTC1"
            p = Paragraph(title, title_style)

            # Crear encabezado
            header_table_data = [[print_logo, p]]
            header_table = Table(header_table_data, colWidths=[110, 570])
            header_table.setStyle(header_style)

            # Estilo de la tabla
            bitacora_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), 'gray'),
                ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), 'white'),
                ('GRID', (0, 0), (-1, -1), 1, 'black'),
            ])

            current_date = time.strftime("%d/%m/%y")
            # Crear header de la tabla
            headers = ["No.", "PC", "Fecha", "Nombre de Usuario", "Alumno/Docente",
                       "Programa", "Hora de Entrada", "Hora de Salida", "Actividad"]

            # Crear la lista de filas
            data = [headers]

            # Ejecutar consulta para obtener los datos para la tabla
            bitacora_uso = cursor.execute(
                "SELECT no, pc, fecha, nombreAlumno, rol, programa, horaEntrada, horaSalida, actividad FROM bitacoraUso WHERE fecha = ?", (current_date,))

            # Obtener los datos de la base de datos y agregarlos a la lista de filas
            for fila in bitacora_uso.fetchall():
                nombre_usuario = fila[3]
                programa = fila[5]

                # Dividir el texto en líneas de máximo 30 caracteres
                text_nombre_usuario = [nombre_usuario[i:i+30]
                                       for i in range(0, len(nombre_usuario), 30)]
                text_programa = [programa[i:i+30]
                                 for i in range(0, len(programa), 30)]

                # Convertir la tupla a una lista
                fila_data = list(fila)
                fila_data[3] = "\n".join(text_nombre_usuario)
                fila_data[5] = "\n".join(text_programa)

                # Agregar la fila modificada a la lista de datos
                data.append(fila_data)

            # Crear la tabla
            table = Table(data)
            table.setStyle(bitacora_style)

            # Agregar el encabezado y la tabla al PDF
            story.append(header_table)
            story.append(table)

            story[0].spaceAfter = 5

            doc.build(story)
