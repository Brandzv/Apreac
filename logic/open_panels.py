"""
@Author: Brandzv
Fecha: 29/05/24
Descripción: Modulo de conexión para abrir paneles de la ventana
"""

from logic.registro_design import RegisterDesign
from logic.reportes_design import ReportsDesign
from logic.horario_design import ScheduleDesign
from logic.agregar_datos_design import AddDataDesign
from logic.form_usuario_design import FormUser
from logic.form_alumno_design import FormStudent
from logic.form_curso_design import FormCourses


class OpenPanel:
    """Clase que abre los paneles de la ventana."""

    def __init__(self, body):
        self.body = body

    def show_register_panel(self):
        """Función que abre panel de registro y limpia los paneles y contenidos de la ventana."""

        RegisterDesign(self.body)

    def show_reports_panel(self):
        """Función que abre panel de ctc y limpia los paneles y contenidos de la ventana."""

        ReportsDesign(self.body)

    def show_schedule_panel(self):
        """Función que abre panel de horario y limpia los paneles y contenidos de la ventana."""

        ScheduleDesign(self.body)

    def show_add_panel(self):
        """Función que abre panel de admin y limpia los paneles y contenidos de la ventana."""

        AddDataDesign(self.body)

    def show_users_form(self):
        """Función que abre formulario para agregar datos en la tabla usuarios de la base de datos"""

        FormUser(self.body)

    def show_students_form(self):
        """Función que abre panel de admin y limpia los paneles y contenidos de la ventana."""

        FormStudent(self.body)

    def show_courses_form(self):
        """Función que abre panel de admin y limpia los paneles y contenidos de la ventana."""

        FormCourses(self.body)
