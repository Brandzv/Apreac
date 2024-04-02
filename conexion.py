"""Modulo de conexión con base de datos"""
import sqlite3

try:
    conecta = sqlite3.connect("database/apreac.db")
    print("Opened database successfully")

    conecta.close()

except ImportError as ie:
    print(ie)
