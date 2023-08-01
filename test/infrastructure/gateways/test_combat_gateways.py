""" Pruebas para test_combat_gateways.py """

import sys

import pytest

from src.infrastructure.gateways.combats_gateway import (get_file_path,
                                                         load_combat_from_file,
                                                         parse_file_argument)


def test_parse_file_argument():
    """
    Prueba la función parse_file_argument() de combats_gateway.

    Esta prueba verifica si la función parse_file_argument() parsea correctamente los argumentos de
    la línea de comandos y devuelve el nombre del archivo JSON proporcionado como argumento.

    """
    file_name = "combat.json"
    sys.argv = ["script.py", file_name]
    assert parse_file_argument() == file_name


def test_get_file_path():
    """
    Prueba la función get_file_path() de combats_gateway.

    Esta prueba verifica si la función get_file_path() devuelve la ruta completa del archivo JSON
    proporcionado, utilizando el directorio predeterminado de archivos de combates.

    """
    file_name = "combat.json"
    dir_path = "data/combats/"
    assert get_file_path(file_name, dir_path) == f"data/combats/{file_name}"


def test_load_combat_from_file():
    """
    Prueba la función load_combat_from_file() de combats_gateway.

    Esta prueba verifica si la función load_combat_from_file() carga correctamente los datos de
    combate desde un archivo .json y los devuelve en formato JSON.

    """
    file_path = "data/test/test_combat.json"
    assert load_combat_from_file(file_path) is not None


if __name__ == "__main__":
    pytest.main()
