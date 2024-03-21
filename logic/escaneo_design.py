import tkinter as tk
from tkinter import ttk
from config import BODY_COLOR


class ScanDesign:
    def __init__(self, body):
        label_scan = tk.Label(body, text="Escaneo",
                              bg=BODY_COLOR, font=("Helvetica", 16))
        label_scan.pack()
