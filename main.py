"""
@Author: Brandzv
Fecha: 09/05/24
Descripción: Modulo de ejecución del sistema de acceso
"""

from logic.login_design import Login
from conexion import inicializar_db


def main():
    # Inicializa la base de datos
    inicializar_db()

    # Inicia la ventana de login
    root = Login()
    root.mainloop()


if __name__ == "__main__":
    main()
