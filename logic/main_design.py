"""Module providing a function printing python version."""

import tkinter as tk
from config import LEFTBAR_COLOR, BODY_COLOR  # , TEXT_COLOR, HOVER_COLOR
from utility import util_window as centrar_ventana


class MainDesign(tk.Tk):
    """Class representing a person"""

    def __init__(self):
        super().__init__()
        self.config_window()

    def config_window(self):
        """Function printing python version."""

        self.title('Registro de alumnos')
        self.iconbitmap("./resource/logo.ico")

        w, h = 840, 450

        self.geometry(f"{w}x{h}+0+0")

        centrar_ventana.centrar_ventana(self, w, h)
