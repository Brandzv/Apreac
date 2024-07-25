"""Modulo de conexión con base de datos"""

import sqlite3


def get_cursor():
    """Función para obtener un cursor de la base de datos"""

    conecta = sqlite3.connect("database/apreac.db")
    cursor = conecta.cursor()
    return conecta, cursor


def inicializar_db():
    """Función para inicializar la base de datos y crear tablas si no existen"""

    conecta, cursor = get_cursor()
    try:
        # Creación de tablas si no existen
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS "usuarios" (
            "id_usuario" INTEGER,
            "usuario" TEXT,
            "contraseña" TEXT,
            PRIMARY KEY("id_usuario" AUTOINCREMENT)
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS "alumnos" (
            "id" INTEGER,
            "idAlumno" INTEGER,
            "nombres" TEXT,
            "apellidoPaterno" TEXT,
            "apellidoMaterno" TEXT,
            "programa" TEXT,
            "rol" TEXT,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS "horarios" (
            "id" INTEGER,
            "crn" INTEGER,
            "docente" TEXT,
            "diaSemana" INTEGER,
            "horaEntrada" INTEGER,
            "horaSalida" INTEGER,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS "bitacoraUso" (
            "no" INTEGER,
            "pc" TEXT,
            "fecha" TEXT,
            "nombreAlumno" TEXT,
            "rol" TEXT,
            "programa" TEXT,
            "horaEntrada" INTEGER,
            "horaSalida" INTEGER,
            "actividad" TEXT
        );
        ''')

        # Inserta un usuario admin si no existe
        cursor.execute('''
            INSERT INTO usuarios (usuario, contraseña)
            SELECT 'admin', '1234'
            WHERE NOT EXISTS (SELECT 1 FROM usuarios WHERE usuario = 'admin')
        ''')

        # Guarda los cambios
        conecta.commit()

    except ImportError as ie:
        print(ie)

    finally:
        if conecta:
            conecta.close()
