""" Pruebas para player.py"""

import pytest
from src.core.entity.player import Player


def test_should_attack_first():
    """
    Prueba el método should_attack_first() de la clase Player.

    Esta prueba verifica si el método should_attack_first() devuelve el resultado correcto
    al comparar dos instancias de la clase Player.

    """
    player1 = Player(["DSD", "SD", "P"], ["K", "P"], 6, "Tonyn Stallone")
    player2 = Player(
        ["SA", "SA", "SA", "ASA", "SA"],
        ["K", "", "K", "P", "P"],
        6,
        "Arnaldor Shuatseneguer",
    )

    assert player1.should_attack_first(player2) is True
    assert player2.should_attack_first(player1) is False


def test_special_move():
    """
    Prueba el método special_move() de la clase Player.

    Esta prueba verifica si el método special_move() devuelve los movimientos especiales
    y sus valores de energía asociados correctamente para ambos jugadores.

    """
    player1 = Player([], [], 6, "Tonyn Stallone")
    player2 = Player([], [], 6, "Arnaldor Shuatseneguer")

    # Casos de prueba para los movimientos especiales de Tonyn Stallone
    assert player1.special_move("DSDP") == ("Taladoken", 3)
    assert player1.special_move("SDK") == ("Remuyuken", 2)
    assert player1.special_move("K") is None

    # Casos de prueba para los movimientos especiales de Arnaldor Shuatseneguer
    assert player2.special_move("ASAP") == ("Taladoken", 2)
    assert player2.special_move("SAK") == ("Remuyuken", 3)
    assert player2.special_move("K") is None


if __name__ == "__main__":
    pytest.main()
