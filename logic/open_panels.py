"""
@Author: Brandzv
Fecha: 29/05/24
Descripción: Modulo de conexión para abrir paneles de la ventana
"""

from logic.registro_design import RegisterDesign
from logic.reportes_design import ReportsDesign
from logic.horario_design import ScheduleDesign


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
