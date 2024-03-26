"""Se crea y configura la ventana principal"""

import tkinter as tk
from tkinter import font
from config import LEFTBAR_COLOR, BODY_COLOR, TEXT_COLOR, HOVER_COLOR, HOVER_TEXT_COLOR
from utility import util_window as centrar_ventana
from logic.registro_design import RegisterDesign
from logic.ctc_design import CtcDesign
from logic.horario_design import ScheduleDesign


class MainDesign(tk.Tk):
    """Esta clase contiene las funciones de creación y configuración de la ventana"""

    def __init__(self):
        super().__init__()
        self.config_window()
        self.panel()
        self.leftbar_menu()

    def config_window(self):
        """Función que crea y configura la ventana"""

        self.title('Registro de alumnos')
        self.iconbitmap("./resource/logo.ico")

        w, h = 840, 450

        self.geometry(f"{w}x{h}+0+0")

        centrar_ventana.centrar_ventana(self, w, h)

    def panel(self):
        """Función donde se crean los paneles"""

        self.leftbar = tk.Frame(
            self, bg=LEFTBAR_COLOR, width=200)
        self.leftbar.pack(side=tk.LEFT, fill='both', expand=False)

        self.body = tk.Frame(
            self, bg=BODY_COLOR,)
        self.body.pack(side=tk.RIGHT, fill='both', expand=True)

    def leftbar_menu(self):
        """Función de configuración gráfica de la barra lateral"""

        ancho_menu = 17
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        self.button_registro = tk.Button(self.leftbar)
        self.button_ctc = tk.Button(self.leftbar)
        self.button_horario = tk.Button(self.leftbar)

        button_content = {
            ("Registro", "   \uf02a", self.button_registro, self.open_register_panel),
            ("CTC", "   \uf390", self.button_ctc, self.open_ctc_panel),
            ("Horario", "   \uf15c", self.button_horario, self.open_schedule_panel)
        }

        for text, icon, button, comando in button_content:
            self.menu_button_config(
                button, text, icon, font_awesome, ancho_menu, alto_menu, comando)

    def menu_button_config(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        """Función de configuración de los botones en la barra lateral"""

        button.config(text=f"{icon} {text}", anchor="w", font=font_awesome, bd=0, bg=LEFTBAR_COLOR,
                      fg=TEXT_COLOR, width=ancho_menu, height=alto_menu, command=comando)
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
        RegisterDesign(self.body)

    def open_ctc_panel(self):
        """Función que abre panel de ctc y limpia los paneles y contenidos de la ventana."""
        self.clear_panel(self.body)
        CtcDesign(self.body)

    def open_schedule_panel(self):
        """Función que abre panel de horario y limpia los paneles y contenidos de la ventana."""

        self.clear_panel(self.body)
        ScheduleDesign(self.body)

    def clear_panel(self, panel):
        """Función que se encarga de limpiar el contenido del panel"""

        for widget in panel.winfo_children():
            widget.destroy()
