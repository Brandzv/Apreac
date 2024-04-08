"""Modulo de conexión con base de datos"""
import sqlite3

try:
    conecta = sqlite3.connect("database/APREAC.db")
    cursor = conecta.cursor()

except ImportError as ie:
    print(ie)
