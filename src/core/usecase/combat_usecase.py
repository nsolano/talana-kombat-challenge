class CombatUseCase:
    """
    Caso de uso para simular un combate entre dos jugadores.

    Attributes:
        player1 (Player): El jugador 1.
        player2 (Player): El jugador 2.
    """

    def __init__(self, player1, player2):
        """
        Inicializa el caso de uso con los jugadores involucrados en el combate.

        Args:
            player1 (Player): El jugador 1.
            player2 (Player): El jugador 2.
        """
        self.player1 = player1
        self.player2 = player2

    def determine_starting_player(self):
        """
        Determina qué jugador debe atacar primero en el combate.

        Returns:
            str: El nombre del jugador que debe atacar primero ("player1" o "player2").
        """
        return "player1" if self.player1.should_attack_first(self.player2) else "player2"

    def perform_attack(self, attacker, defender):
        """
        Realiza un ataque de un jugador a otro y actualiza los puntos de energía.

        Args:
            attacker (Player): El jugador atacante.
            defender (Player): El jugador defensor.
        """
        
        attacker_energy, defender_energy = attacker.energy, defender.energy       

        for i, move in enumerate(attacker.moves):
            if attacker_energy <= 0 or defender_energy <= 0:
                break         

            if attacker.attacks[i]:
                # Comprobar combinaciones especiales
                if move == "DSD" and attacker.attacks[i] == "P":
                    defender_energy -= 3  # Taladoken de Tonyn Stallone
                elif move == "SD" and attacker.attacks[i] == "K":
                    defender_energy -= 2  # Remuyuken de Tonyn Stallone
                elif move == "SA" and attacker.attacks[i] == "K":
                    defender_energy -= 3  # Remuyuken de Arnaldor Shuatseneguer
                elif move == "ASA" and attacker.attacks[i] == "P":
                    defender_energy -= 2  # Taladoken de Arnaldor Shuatseneguer
                else:
                    defender_energy -= 1  # Puño o Patada

        defender.energy = max(0, defender_energy)  # La energía del defensor no puede ser negativa