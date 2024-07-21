"""
@Author: Brandzv
Fecha: 29/05/24
Descripción: Modulo que crea y configura la ventana principal
"""

import tkinter as tk
from tkinter import font
from config import LEFTBAR_COLOR, BODY_COLOR, TEXT_COLOR, HOVER_COLOR, HOVER_TEXT_COLOR
import logic.open_panels


class MainDesign():
    """Esta clase contiene las funciones de creación y configuración de la ventana"""

    def __init__(self, body, user):
        super().__init__()
        self.body_main = body
        self.user_key = user

        self.panel()
        self.leftbar_menu()

    def panel(self):
        """Función donde se crean los paneles"""

        self.leftbar = tk.Frame(
            self.body_main, bg=LEFTBAR_COLOR, width=200)
        self.leftbar.pack(side=tk.LEFT, fill='both', expand=False)

        self.body = tk.Frame(
            self.body_main, bg=BODY_COLOR,)
        self.body.pack(side=tk.RIGHT, fill='both', expand=True)

    def leftbar_menu(self):
        """Función de configuración gráfica de la barra lateral"""

        width_menu = 17
        height_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        self.button_registro = tk.Button(self.leftbar)
        self.button_reports = tk.Button(self.leftbar)
        self.button_horario = tk.Button(self.leftbar)

        if self.user_key == "admin" or self.user_key == "Admin":
            self.button_admin = tk.Button(self.leftbar)
            self.menu_button_config(
                self.button_admin, "Agregar", " \uf044", font_awesome, width_menu, height_menu, self.open_add_panel)

        button_content = {
            ("Registro", " \uf2c2", self.button_registro, self.open_register_panel),
            ("Reportes", " \uf1c1", self.button_reports, self.open_reports_panel),
            ("Horario", " \uf784", self.button_horario, self.open_schedule_panel)
        }

        for text, icon, button, comando in button_content:
            self.menu_button_config(
                button, text, icon, font_awesome, width_menu, height_menu, comando)

    def menu_button_config(self, button, text, icon, font_awesome, width_menu, height_menu, comando):
        """Función de configuración de los botones en la barra lateral"""

        button.config(text=f"{icon} {text}", anchor="w", font=font_awesome, bd=0, bg=LEFTBAR_COLOR,
                      fg=TEXT_COLOR, width=width_menu, height=height_menu, command=comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        """Función que ejecuta el método on_enter y on_leave"""

        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        """Función hover para los botones"""

        button.config(bg=HOVER_COLOR, fg=HOVER_TEXT_COLOR)

    def on_leave(self, event, button):
        """Función que regresa el botón al estado original"""

        button.config(bg=LEFTBAR_COLOR, fg=TEXT_COLOR)

    def open_register_panel(self):
        """Función que abre panel de registro y limpia los paneles y contenidos de la ventana."""

        self.clear_panel(self.body)
        show_register_main = logic.open_panels.OpenPanel(self.body)
        show_register_main.show_register_panel()

    def open_reports_panel(self):
        """Función que abre panel de ctc y limpia los paneles y contenidos de la ventana."""

        self.clear_panel(self.body)
        show_reports_main = logic.open_panels.OpenPanel(self.body)
        show_reports_main.show_reports_panel()

    def open_schedule_panel(self):
        """Función que abre panel de horario y limpia los paneles y contenidos de la ventana."""

        self.clear_panel(self.body)
        show_schedule_main = logic.open_panels.OpenPanel(self.body)
        show_schedule_main.show_schedule_panel()

    def open_add_panel(self):
        """Función que abre panel de horario y limpia los paneles y contenidos de la ventana."""

        self.clear_panel(self.body)
        show_schedule_main = logic.open_panels.OpenPanel(self.body)
        show_schedule_main.show_add_panel()

    def clear_panel(self, panel):
        """Función que se encarga de limpiar el contenido del panel"""

        for widget in panel.winfo_children():
            widget.destroy()
