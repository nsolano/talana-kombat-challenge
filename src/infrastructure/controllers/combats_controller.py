from src.infrastructure.gateways.combats_gateway import load_combat_from_file

# from core.usecase.combat_usecase import CombatUseCase
# from core.repository.combat_repository import CombatRepository

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
        tuple: Dos tuplas representado a los movimientols y ataques de los jugadores
    """
    player1_moves = json_combat["player1"]["movimientos"]
    player1_attacks = json_combat["player1"]["golpes"]
    player1 = (player1_moves, player1_attacks)
    player2_moves = json_combat["player2"]["movimientos"]
    player2_attacks = json_combat["player2"]["golpes"]
    player2 = (player2_moves, player2_attacks)

    return player1, player2


def narrate_combat(json_combat):
    """
    Simula el combate y narra el desarrollo del mismo.

    Args:
        json_combat (dict): Datos del combate en formato JSON.
    """
    # Implementar la lógica para simular el combate y narrar su desarrollo
    pass