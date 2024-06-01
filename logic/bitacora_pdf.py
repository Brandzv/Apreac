"""
@Author: Brandzv
Fecha: 08/05/24
Descripción: Modulo para generar un PDF de la Bitacora de uso con los registros del dia actual
"""
import datetime
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from conexion import cursor


class BitacoraPDF:
    """Clase para generar PDF de bitacora de uso"""

    def generate_bitacora(self, crear_pdf):
        """Función para generar el PDF"""

        if crear_pdf:
            # Se nombre el archivo con "BitacoraUso" "Dia/Mes/Año_Horas Minutos Segundos"
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
            # Busca el texto CTC en la bd y el dato que coincida
            # con el texto se guarda en la variable ctc
            cursor.execute(
                "SELECT usuario FROM usuarios WHERE usuario LIKE '%CTC%'")
            ctc = cursor.fetchone()
            # Titulo de la Bitacora
            title = f"Bitácora de uso {ctc[0]}"
            p = Paragraph(title, title_style)

            # Se crea el encabezado del PDF con Logo y Titulo de la bitacora de uso
            def header(canvas, doc):
                # Guarda el estado actual del canvas
                canvas.saveState()
                # Calcula las dimensiones del logo para que se ajuste al ancho y al margen superior
                w, h = print_logo.wrap(doc.width, doc.topMargin)
                # Ajusta el desplazamiento vertical del logo
                print_logo.drawOn(
                    canvas, doc.leftMargin, doc.height + doc.bottomMargin + doc.topMargin - h - 20)
                # Calcula el ancho necesario para que p se ajuste correctamente dentro del documento
                p.wrap(doc.width - doc.leftMargin -
                       doc.rightMargin, doc.topMargin)
                # Ajusta el desplazamiento vertical del titulo
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
            # Es la lista de los encabezados de la tabla
            data = [headers]

            # Se usa como filtro de fecha actual
            current_date = time.strftime("%d/%m/%y")
            # Ejecuta una consulta para obtener los datos que se imprimirán en la tabla
            bitacora_uso = cursor.execute(
                "SELECT no, pc, fecha, nombreAlumno, rol, programa, horaEntrada, horaSalida, actividad FROM bitacoraUso WHERE fecha = ?", (current_date,))

            # Lista de numeros del 1 al 20 para la columna "No."
            numbers = list(range(1, 21))
            # Lista "story" vacía
            story = []

            # Obtener los datos de la base de datos y agregarlos a la lista de filas
            for row in bitacora_uso.fetchall():
                # Se selecciona la fila 3 y 5 por que son las que pueden ser textos largos
                nombre_usuario = row[3]
                programa = row[5]

                # Divide el texto en líneas de máximo 30 caracteres
                # para que se pueda adaptar a las celdas
                text_nombre_usuario = [nombre_usuario[i:i+30]
                                       for i in range(0, len(nombre_usuario), 30)]
                #
                text_programa = [programa[i:i+30]
                                 for i in range(0, len(programa), 30)]

                # Convierte la tupla a una lista para poder formatear los textos
                # antes de imprimirlos en la tabla
                row_data = list(row)
                row_data[3] = "\n".join(text_nombre_usuario)
                row_data[5] = "\n".join(text_programa)

                # Se usa para imprimir los numero del 1 al 20 en la columna "No."
                row_data[0] = numbers[0]
                numbers.append(numbers.pop(0))
                # Agregar la fila modificada a la lista de datos
                data.append(row_data)

                # Si llega la tabla a 20 filas crea una pagina nueva
                if len(data) == 21:
                    # Vincular headers con la tabla (Se uso asi en un principio por que
                    # causaba un error usar "data" directamente, por eso lo deje asi)
                    table_data = data
                    # Crea la tabla, asigna headers y asigna ancho a las columnas
                    table = Table(table_data, colWidths=[
                        30, 40, 60, 170, 90, 80, 90, 80, 70])
                    #
                    table.setStyle(bitacora_style)
                    # Configurar el encabezado para repetirse en todas las páginas
                    table.repeatRows = 1

                    # Agregar la tabla al PDF
                    story.append(table)
                    # Ajustes adicionales (Creo que es un "Margin Bottom")
                    story[0].spaceAfter = 5

                    # Salta de pagina cuando llega a 20 filas
                    story.append(PageBreak())

                    # Limpiar la lista de filas para la siguiente página
                    data = [headers]

            # Si quedan filas sin procesar, agrega mas tablas al PDF
            if len(data) > 1:
                # Vincular headers con la tabla (Se uso asi en un principio por que
                # causaba un error usar "data" directamente, por eso lo deje asi)
                table_data = data
                # Crea la tabla, asigna headers y asigna ancho a las columnas
                table = Table(table_data, colWidths=[
                              30, 40, 60, 170, 90, 80, 90, 80, 70])
                #
                table.setStyle(bitacora_style)
                # Configurar el encabezado para repetirse en todas las páginas
                table.repeatRows = 1
                # Agregar la tabla al PDF
                story.append(table)

            # Agrega el encabezado a todas las paginas del PDF
            doc.build([p], onFirstPage=header, onLaterPages=header)
            # Construye el PDF
            doc.build(story)
