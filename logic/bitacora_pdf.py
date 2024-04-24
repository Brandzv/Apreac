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

            # Estilo del encabezado
            header_style = TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ])

            # Estilo del titulo
            title_style = getSampleStyleSheet()['Normal']
            title_style.fontSize = 24
            title_style.leftIndent = 170
            title_style.leading = 30

            # Crear la tabla
            headers = ["No.", "PC", "Fecha", "Nombre de Usuario", "Alumno/Docente",
                       "Programa", "Hora de Entrada", "Hora de Salida", "Actividad"]

            # Crear la lista de filas
            data = [headers]

            # Ejecutar consulta para obtener los datos para la tabla
            bitacora_uso = cursor.execute(
                "SELECT no, pc, fecha, nombreAlumno, rol, programa, horaEntrada, horaSalida, actividad FROM bitacoraUso")

            # Obtener los datos de la base de datos y agregarlos a la lista de filas
            for fila in bitacora_uso.fetchall():
                data.append(fila)

            table = Table(data)
            table.setStyle(bitacora_style)

            # Logo de la UNID
            logo_unid = './resource/LogoUnid.png'

            story = []
            print_logo = Image(logo_unid, width=110,
                               height=45, hAlign='LEFT')

            title = "Bitácora de uso CTC1"
            p = Paragraph(title, title_style)

            header_table_data = [[print_logo, p]]
            header_table = Table(header_table_data, colWidths=[110, 570])

            header_table.setStyle(header_style)

            story.append(header_table)
            story.append(table)

            story[0].spaceAfter = 5

            doc.build(story)
