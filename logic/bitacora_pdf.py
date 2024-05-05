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

            # Logo de la UNID
            logo_unid = './resource/LogoUnid.png'
            print_logo = Image(logo_unid, width=110, height=45, hAlign='LEFT')

            # Estilo del titulo
            title_style = getSampleStyleSheet()['Title']
            title_style.fontSize = 24
            title_style.leftIndent = 130
            title_style.leading = 30
            # Titulo de la Bitacora
            title = "Bitácora de uso CTC1"
            p = Paragraph(title, title_style)

            # Crea encabezado del PDF
            def header(canvas, doc):
                # Guarda el estado actual del canvas
                canvas.saveState()
                # Calcula las dimensiones del logo para que se ajuste al ancho y al margen superior
                w, h = print_logo.wrap(doc.width, doc.topMargin)
                # Ajusta el desplazamiento vertical
                print_logo.drawOn(
                    canvas, doc.leftMargin, doc.height + doc.bottomMargin + doc.topMargin - h - 20)
                # Calcula el ancho necesario para que p se ajuste correctamente dentro del documento
                p.wrap(doc.width - doc.leftMargin -
                       doc.rightMargin, doc.topMargin)
                # Ajusta el desplazamiento vertical
                p.drawOn(canvas, doc.leftMargin + 120, doc.height +
                         doc.bottomMargin + doc.topMargin - h - 20)
                canvas.restoreState()

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

            # Crear header de la tabla
            headers = ["No.", "PC", "Fecha", "Nombre de Usuario", "Alumno/Docente",
                       "Programa", "Hora de Entrada", "Hora de Salida", "Actividad"]
            # Crear la lista de filas
            data = [headers]

            numeros = list(range(1, 21))
            # Se usa como filtro de fecha actual
            current_date = time.strftime("%d/%m/%y")
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
                #
                text_programa = [programa[i:i+30]
                                 for i in range(0, len(programa), 30)]

                # Convertir la tupla a una lista
                fila_data = list(fila)
                fila_data[3] = "\n".join(text_nombre_usuario)
                fila_data[5] = "\n".join(text_programa)

                fila_data[0] = numeros[0]
                numeros.append(numeros.pop(0))
                # Agregar la fila modificada a la lista de datos
                data.append(fila_data)

            # Vincular headers con la tabla
            table_data = data
            # Crear la tabla y asignar ancho a a las columnas
            table = Table(table_data, colWidths=[
                          30, 50, 60, 170, 90, 80, 80, 80, 70])
            table.setStyle(bitacora_style)
            # Configurar el encabezado para repetirse en todas las páginas
            table.repeatRows = 1

            story = []
            # Agregar la tabla al PDF
            story.append(table)
            # Ajustes adicionales
            story[0].spaceAfter = 5

            # Agregar el encabezado al PDF
            doc.build([p], onFirstPage=header, onLaterPages=header)
            # Construir el PDF
            doc.build(story)
