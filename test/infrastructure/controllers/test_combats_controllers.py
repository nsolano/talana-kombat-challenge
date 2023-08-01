""" Pruebas para combats_controllers.py """

import pytest
from src.infrastructure.controllers.combats_controller import (
    load_combat_from_json_file,
    parse_json_combat,
    narrate_combat,
)


def test_load_combat_from_json_file():
    """
    Prueba la función load_combat_from_json_file() de combats_controller.

    Esta prueba verifica si la función load_combat_from_json_file() carga correctamente los datos de
    combate desde un archivo .json y los devuelve en formato JSON.

    """
    file_path = "data/test/test_combat.json"
    assert load_combat_from_json_file(file_path) is not None


def test_parse_json_combat():
    """
    Prueba la función parse_json_combat() de combats_controller.

    Esta prueba verifica si la función parse_json_combat() parsea correctamente los datos de combate
    desde el formato JSON a dos instancias de la clase Player.

    """
    json_combat = {
        "player1": {
            "movimientos": ["DSD", "S"],
            "golpes": ["P", ""],
        },
        "player2": {
            "movimientos": ["", "ASA", "DA", "AAA", "", "SA"],
            "golpes": ["P", "", "P", "K", "K", "K"],
        },
    }
    player1, player2 = parse_json_combat(json_combat)

    assert player1.name == "Tonyn Stallone"
    assert player2.name == "Arnaldor Shuatseneguer"


def test_narrate_combat(capsys):
    """
    Prueba la función narrate_combat() de combats_controller.

    Esta prueba verifica si la función narrate_combat() simula correctamente el combate y narra el
    desarrollo del mismo.

    """
    json_combat = {
        "player1": {
            "movimientos": ["DSD", "S"],
            "golpes": ["P", ""],
        },
        "player2": {
            "movimientos": ["", "ASA", "DA", "AAA", "", "SA"],
            "golpes": ["P", "", "P", "K", "K", "K"],
        },
    }
    narrate_combat(json_combat)

    captured = capsys.readouterr()
    assert "Comienza el combate:" in captured.out
    assert "Combate finalizado." in captured.out


if __name__ == "__main__":
    pytest.main()
