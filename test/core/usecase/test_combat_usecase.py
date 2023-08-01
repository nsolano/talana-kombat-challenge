""" Pruebas para combat_usecase.py"""

import pytest
from src.core.entity.player import Player
from src.core.usecase.combat_usecase import CombatUseCase


def test_determine_starting_player():
    """
    Prueba el método determine_starting_player() de la clase CombatUseCase.

    Esta prueba verifica si el método determine_starting_player() devuelve el nombre del
    jugador que debe atacar primero en el combate correctamente.

    """
    player1 = Player(["D", "S"], ["P", ""], 6, "Tonyn Stallone")
    player2 = Player(["AAWSD", "D", "A"], ["K", "P", ""], 6, "Arnaldor Shuatseneguer")
    combat_use_case = CombatUseCase(player1, player2)

    assert combat_use_case.determine_starting_player() == player1


def test_perform_attack():
    """
    Prueba el método perform_attack() de la clase CombatUseCase.

    Esta prueba verifica si el método perform_attack() realiza el combate entre dos jugadores
    correctamente, actualizando sus puntos de energía después de cada ataque y devolviendo
    la información sobre el desarrollo del ataque en cada iteración del generador.

    """
    player1 = Player(["DSD", "SD", "A"], ["K", "P", ""], 6, "Tonyn Stallone")
    player2 = Player(
        ["SA", "SA", "SA", "ASA", "SA"],
        ["K", "", "K", "P", "P"],
        6,
        "Arnaldor Shuatseneguer",
    )
    combat_use_case = CombatUseCase(player1, player2)

    expected_output = [
        ("Tonyn Stallone", "Arnaldor Shuatseneguer", 6, 4, "Remuyuken"),
        ("Arnaldor Shuatseneguer", "Tonyn Stallone", 4, 3, "Remuyuken"),
        ("Tonyn Stallone", "Arnaldor Shuatseneguer", 3, 3, "puño"),
        ("Arnaldor Shuatseneguer", "Tonyn Stallone", 3, 3, "se mueve"),
        ("Tonyn Stallone", "Arnaldor Shuatseneguer", 3, 3, "se mueve"),
        ("Arnaldor Shuatseneguer", "Tonyn Stallone", 3, 0, "Remuyuken"),
    ]

    result = list(combat_use_case.perform_attack(player1, player2))
    assert result == expected_output


if __name__ == "__main__":
    pytest.main()
