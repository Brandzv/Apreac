import tkinter as tk
from tkinter import ttk
from config import BODY_COLOR


class CtcDesign():
    def __init__(self, body):
        label_ctc = tk.Label(body, text="Ctc",
                             bg=BODY_COLOR, font=("Helvetica", 16))
        label_ctc.pack()
