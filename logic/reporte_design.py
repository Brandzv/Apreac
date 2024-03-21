import tkinter as tk
from tkinter import ttk
from config import BODY_COLOR


class ReportDesign():
    def __init__(self, body):
        label_report = tk.Label(body, text="Reporte",
                                bg=BODY_COLOR, font=("Helvetica", 16))
        label_report.pack()
