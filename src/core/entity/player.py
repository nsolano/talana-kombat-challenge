""" Clase jugador con sus atributos """


class Player:
    """
    Representa un jugador en el juego Talana Kombat.

    Attributes:
        moves (list): Lista de movimientos realizados por el jugador.
        attacks (list): Lista de golpes realizados por el jugador.
        energy (int): Puntos de energía del jugador (de 0 a 6).
    """

    def __init__(self, moves, attacks, energy, name):
        """
        Inicializa un nuevo jugador con sus movimientos, golpes y puntos de energía.

        Args:
            moves (list): Lista de movimientos realizados por el jugador.
            attacks (list): Lista de golpes realizados por el jugador.
            energy (int): Puntos de energía del jugador (de 0 a 6).
        """
        self.moves = moves
        self.attacks = attacks
        self.energy = energy
        self.name = name

    def should_attack_first(self, opponent):
        """
        Determina si este jugador debe atacar primero que el oponente en el combate.

        Args:
            opponent (Player): El jugador oponente.

        Returns:
            bool: True si este jugador debe atacar primero, False en caso contrario.
        """
        player_moves_length = sum(len(move) for move in self.moves)
        player_attacks_length = sum(len(attack) for attack in self.attacks)
        player_combination_length = player_moves_length + player_attacks_length

        opponent_moves_length = sum(len(move) for move in opponent.moves)
        opponent_attacks_length = sum(len(attack) for attack in opponent.attacks)
        opponent_combination_length = opponent_moves_length + opponent_attacks_length

        if player_combination_length != opponent_combination_length:
            return player_combination_length < opponent_combination_length

        if player_attacks_length != opponent_attacks_length:
            return player_attacks_length < opponent_attacks_length

        if player_moves_length != opponent_moves_length:
            return player_moves_length < opponent_moves_length

        return self.name == "Tonyn Stallone"

    def special_move(self, combination):
        """
        Retorna los movimientos especiales y su energía asociada para el jugador actual.

        Args:
        combination (str): La combinación de movimientos y golpe actual del jugador.

        Returns:
        tuple or None: Una tupla que contiene el nombre del movimiento especial y su
        energía asociada, si la combinación coincide con alguno de los movimientos
        especiales del jugador. Si no se encuentra una coincidencia, devuelve None.

        """
        specials_by_player = {
            "Tonyn Stallone": {"Taladoken": ("DSDP", 3), "Remuyuken": ("SDK", 2)},
            "Arnaldor Shuatseneguer": {
                "Taladoken": ("ASAP", 2),
                "Remuyuken": ("SAK", 3),
            },
        }

        player_specials = specials_by_player.get(self.name)
        if player_specials:
            for move_name, move_combination in player_specials.items():
                if combination.endswith(move_combination[0]):
                    return move_name, move_combination[1]

        return None
