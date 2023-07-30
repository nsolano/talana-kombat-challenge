""" Gestiona los datos de los combates """

import json

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
        return None
    except json.JSONDecodeError:
        print(f"El archivo {file_path} no tiene un formato JSON válido.")
        return None


def save_combat_to_file(combat_data, file_path):
    """
    Guarda los datos de un combate en un archivo .json.

    Args:
        combat_data (dict): Datos del combate en formato JSON.
        file_path (str): Ruta del archivo .json donde se guardarán los datos del combate.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(combat_data, file)
