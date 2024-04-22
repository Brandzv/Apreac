"""Modulo para generar PDF de bitacora de uso"""
import datetime
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
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

            # Por si se ocupa centrar algo
            w, h = letter

            # Obtener los datos de la base de datos
            bitacora_uso = cursor.execute(
                "SELECT no, pc, fecha, nombreAlumno, rol, programa, horaEntrada, horaSalida, actividad FROM bitacoraUso")
            headers = ["No.", "PC", "Fecha", "Nombre de Usuario", "Alumno/Docente",
                       "Programa", "Hora de Entrada", "Hora de Salida", "Actividad"]

            data = [headers]  # Encabezados

            # Obtener los datos de la base de datos y agregarlos a la lista de filas
            for fila in bitacora_uso.fetchall():
                data.append(fila)

            style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), 'gray'),
                ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), 'white'),
                ('GRID', (0, 0), (-1, -1), 1, 'black')
            ])

            table = Table(data)
            table.setStyle(style)

            # Logo de la UNID
            logo_unid = './resource/LogoUnid.png'

            story = [Image(logo_unid, width=110, height=45,
                           hAlign='LEFT'), table]
            story[0].spaceAfter = 10

            # Construir el PDF
            doc.build(story)
