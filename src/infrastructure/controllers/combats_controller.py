""" Controla la lógica para la interacción de la 
aplicación con el sistema """

from src.core.entity.player import Player
from src.core.usecase.combat_usecase import CombatUseCase
from src.infrastructure.gateways.combats_gateway import load_combat_from_file


def load_combat_from_json_file(file_path):
    """
    Carga los datos de un combate desde un archivo .json.

    Args:
        file_path (str): Ruta del archivo .json que contiene los datos del combate.

    Returns:
        dict: Datos del combate en formato JSON.
    """
    combat_data = load_combat_from_file(file_path)
    return combat_data


def parse_json_combat(json_combat):
    """
    Parsea los datos de combate desde el formato JSON a dos tuplas.

    Args:
        json_combat (dict): Datos del combate en formato JSON.

    Returns:
        tuple: Intancias de Player representando a los dos jugadores
    """
    player1_moves = json_combat["player1"]["movimientos"]
    player1_attacks = json_combat["player1"]["golpes"]
    player1 = (player1_moves, player1_attacks)
    player2_moves = json_combat["player2"]["movimientos"]
    player2_attacks = json_combat["player2"]["golpes"]
    player1 = Player(player1_moves, player1_attacks, 6, "Tonyn Stallone")
    player2 = Player(player2_moves, player2_attacks, 6, "Arnaldor Shuatseneguer")

    return player1, player2


def narrate_combat(json_combat):
    """
    Simula el combate y narra el desarrollo del mismo.

    Args:
        json_combat (dict): Datos del combate en formato JSON.
    """
    moves = {
        "Taladoken": "usa un",
        "Remuyuken": "conecta",
        "patada": "le da una",
        "puño": "le da un",
    }

    player1, player2 = parse_json_combat(json_combat)
    combat_use_case = CombatUseCase(player1, player2)

    starting_player = combat_use_case.determine_starting_player()

    print("Comienza el combate:")

    if starting_player == player1:
        combat = combat_use_case.perform_attack(starting_player, player2)
    else:
        combat = combat_use_case.perform_attack(starting_player, player1)

    for att_name, def_name, att_energy, def_energy, tec_name in combat:
        if moves.get(tec_name):
            message = (
                f"{att_name} ({att_energy}) {moves.get(tec_name)}{tec_name} "
                f"a {def_name} y le queda {def_energy} puntos de energía"
            )
        else:
            message = f"{att_name} {tec_name}"
        print(message)

    print("Combate finalizado.")

    if player1.energy <= 0:
        print(f"Gana {player2.name}")
    else:
        print(f"Gana {player1.name}")
