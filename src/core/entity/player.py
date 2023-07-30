""" Clase jugador con sus atributos """

class Player:
    """
    Representa un jugador en el juego Talana Kombat.

    Attributes:
        moves (list): Lista de movimientos realizados por el jugador.
        attacks (list): Lista de golpes realizados por el jugador.
        energy (int): Puntos de energía del jugador (de 0 a 6).
    """

    def __init__(self, moves, attacks, energy=6):
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

    def should_attack_first(self, opponent):
        """
        Determina si este jugador debe atacar primero que el oponente en el combate.

        Args:
            opponent (Player): El jugador oponente.

        Returns:
            bool: True si este jugador debe atacar primero, False en caso contrario.
        """
        if len(self.moves) != len(opponent.moves):
            return len(self.moves) < len(opponent.moves)

        player_combination_length = sum(len(move) for move in self.moves)
        opponent_combination_length = sum(len(move) for move in opponent.moves)

        if player_combination_length != opponent_combination_length:
            return player_combination_length < opponent_combination_length

        player_attack_count = len([attack for attack in self.moves if attack])
        opponent_attack_count = len([attack for attack in opponent.moves if attack])

        return player_attack_count < opponent_attack_count
