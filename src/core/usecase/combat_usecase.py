""" Simula el combate """


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
        return (
            self.player1
            if self.player1.should_attack_first(self.player2)
            else self.player2
        )

    def perform_attack(self, attacker, defender):
        """
        Realiza un ataque de un jugador a otro y actualiza los puntos de energía.

        Esta función simula un ataque entre dos jugadores en el juego Talana Kombat JRPG.
        Se evalúan los movimientos y golpes de ambos jugadores para determinar el daño causado
        y se actualiza la energía del jugador defensor en función de los ataques del atacante.

        Args:
            attacker (Player): El jugador atacante que realiza el ataque.
            defender (Player): El jugador defensor que recibe el ataque.

        Yields:
            tuple: Una tupla que contiene información sobre el desarrollo del ataque. Cada iteración
                   del generador devuelve una tupla con los siguientes elementos:
                    - Nombre del jugador atacante.
                    - Nombre del jugador defensor.
                    - Energía actual del jugador atacante después del ataque.
                    - Energía actual del jugador defensor después del ataque.
                    - Nombre de la técnica utilizada en el ataque.
        """
        techniques_map = {"K": ("patada", 1), "P": ("puño", 1), "": ("se mueve", 0)}

        number_attacks = max(len(attacker.attacks), len(defender.attacks)) + 1

        indexes = [x // 2 for x in range(2 * number_attacks)]

        for i in indexes:
            if attacker.energy <= 0 or defender.energy <= 0:
                break

            # Comprueba combinaciones especiales
            try:
                attacks = attacker.attacks[i]
                moves = attacker.moves[i]
            except IndexError:
                attacks, moves = "", ""
            special = attacker.special_move(moves + attacks)

            if special:
                technique_name, damage = special
            else:
                technique_name, damage = techniques_map.get(attacks)
                if moves == "" and attacks == "":
                    technique_name = "no se mueve, ni golpea"

            defender.energy -= damage

            # La energía del defensor no puede ser negativa
            defender.energy = max(0, defender.energy)

            # Intercambia el lugar del atacante y defensor en cada iteración
            attacker, defender = defender, attacker

            yield defender.name, attacker.name, defender.energy, attacker.energy, technique_name
