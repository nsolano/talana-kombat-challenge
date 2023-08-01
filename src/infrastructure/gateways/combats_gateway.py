""" Gestiona los archivos y datos de los combates """

import sys
import argparse
import os
import json

def parse_file_argument():
    """
    Parsea los argumentos de la línea de comandos para obtener el nombre del archivo JSON.

    Returns:
        str: Nombre del archivo JSON proporcionado como argumento en la terminal.
    """
    # Crear el parser de argumentos
    parser = argparse.ArgumentParser(description='Simula y narra un combate desde un archivo JSON.')
    parser.add_argument('file_name', metavar='nombre_archivo', type=str,
                        help='Nombre del archivo JSON que contiene los datos del combate.')

    # Obtener el argumento del nombre del archivo
    args = parser.parse_args()
    file_name = args.file_name

    return file_name

def get_file_path(file_name, dir_path="data/combats/"):
    """
    Obtiene la ruta completa del archivo JSON.

    Args:
        file_name (str): Nombre del archivo JSON.
        dir_path (str): Directorio donde se encuentran los archivos de combates.

    Returns:
        str: Ruta completa del archivo JSON.
    """
    file_path = os.path.join(dir_path, file_name)
    return file_path


def load_combat_from_file(file_path):
    """
    Carga los datos de un combate desde un archivo .json.

    Args:
        file_path (str): Ruta del archivo .json que contiene los datos del combate.

    Returns:
        dict: Datos del combate en formato JSON.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"El archivo {file_path} no existe.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"El archivo {file_path} no tiene un formato JSON válido.")
        sys.exit(1)
