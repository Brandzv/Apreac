"""Modulo de centrado de ventana"""


def centrar_ventana(ventana, ventana_ancho, ventana_alto):
    """Función de calculo para centrar la ventana"""

    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    x = int((pantalla_ancho/2) - (ventana_ancho/2))
    y = int((pantalla_alto/2) - (ventana_alto/2))

    return ventana.geometry(f"{ventana_ancho}x{ventana_alto}+{x}+{y}")
