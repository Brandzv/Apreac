"""Modulo de diseño del panel registro"""

import tkinter as tk
# from tkinter import ttk
from config import BODY_COLOR


class RegisterDesign:
    """Clase del diseño del panel escaneo"""

    def __init__(self, body):
        label_ctc = tk.Label(body, text="Registro",
                             bg=BODY_COLOR, font=("Helvetica", 16))
        label_ctc.pack()
