"""Modulo de diseño del panel Reportes"""
import tkinter as tk
# from tkinter import ttk
from config import BODY_COLOR


class ReportsDesign():
    """Clase del diseño del panel Reportes"""

    def __init__(self, body):
        label_ctc = tk.Label(body, text="Reportes",
                             bg=BODY_COLOR, font=("Helvetica", 16))
        label_ctc.pack()
