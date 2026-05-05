import tkinter as tk
from tkinter import ttk

def incrementar_barra():
    valor = barra_progreso["value"]
    if valor < 100:
        barra_progreso["value"] = valor + 10
        actualizar_porcentaje()