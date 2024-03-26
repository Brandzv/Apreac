"""Modulo de diseño del panel horario"""
import tkinter as tk
# from tkinter import ttk
from config import BODY_COLOR


class ScheduleDesign():
    """Clase del diseño del panel horario"""

    def __init__(self, body):
        label_report = tk.Label(body, text="Horario",
                                bg=BODY_COLOR, font=("Helvetica", 16))
        label_report.pack()
