"""
@Author: Brandzv
Fecha: 29/05/24
Descripción: Login del sistema de acceso
"""

import tkinter as tk
from tkinter import messagebox
from utility import util_window as centrar_ventana
from logic.main_design import MainDesign
from conexion import cursor


class Login(tk.Tk):
    """Clase donde se estructura la ventana login"""

    def __init__(self):
        super().__init__()
        self.config_login()
        self.panel()
        self.top_text()
        self.data_login()

    def config_login(self):
        """Función que crea y configura la ventana"""

        self.title('Login')
        self.iconbitmap("./resource/logo.ico")

        w, h = 840, 450

        self.geometry(f"{w}x{h}+0+0")

        centrar_ventana.centrar_ventana(self, w, h)

    def panel(self):
        """Función que crea los paneles del login"""
        self.top_login = tk.Frame(self)
        self.top_login.pack(side="top", fill="both", expand=True)

        self.bottom_login = tk.Frame(self)
        self.bottom_login.pack(side="bottom", fill="both", expand=True)

        self.body_login = tk.Frame(self.bottom_login, width=420)
        self.body_login.pack(side="top")

        self.top_login.columnconfigure(0, weight=1)
        self.bottom_login.columnconfigure(1, weight=1)

    def top_text(self):
        """Función que crea la estructura del login"""
        self.text = tk.Label(self.top_login, text="Login",
                             font=("Arial", 30, "bold"))
        self.text.pack(side="bottom", pady=20)

    def data_login(self):
        """Función que obtiene los datos del login"""
        self.label_user = tk.Label(
            self.body_login, text="Usuario:", font=("Arial", 13))
        #
        self.entry_user = tk.Entry(
            self.body_login, bd=1, width=14, font=("Arial", 13))

        self.label_password = tk.Label(self.body_login, text="Contraseña:",
                                       font=("Arial", 13))
        #
        self.entry_password = tk.Entry(self.body_login, bd=1, width=14,
                                       font=("Arial", 13), show="*")
        #
        self.button_login = tk.Button(
            self.body_login, text="Iniciar sesión", font=("Arial", 13), command=self.access)

        self.label_user.grid(row=0, column=0, padx=5, pady=10, sticky="w")
        #
        self.entry_user.grid(row=0, column=1, padx=5, pady=10)
        self.entry_user.focus_set()
        #
        self.label_password.grid(row=1, column=0, padx=5, pady=10, sticky="w")
        #
        self.entry_password.grid(row=1, column=1, padx=5, pady=10)
        #
        self.button_login.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def access(self):
        """Función que obtiene los datos del login"""
        user = self.entry_user.get()
        password = self.entry_password.get()

        cursor.execute(
            "SELECT usuario, contraseña FROM usuarios WHERE usuario = ? AND contraseña = ?", (user, password))

        # Obtener resultados
        valid_access = cursor.fetchone()

        if valid_access:
            if user == "admin" or user == "Admin":
                self.title('Registro de alumnos')
                body = self
                self.clear_panel(self)
                MainDesign(body)
            else:
                messagebox.showinfo(
                    "Información", "Bienvenido al sistema de usuario")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            self.entry_user.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)

    def clear_panel(self, panel):
        """Función que se encarga de limpiar el contenido del panel"""

        for widget in panel.winfo_children():
            widget.destroy()
