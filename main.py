""" Módulo principal para el simulador de combates Talana Kombat JRPG. """

from src.infrastructure.controllers.combats_controller import (
    load_combat_from_json_file, narrate_combat)
from src.infrastructure.gateways.combats_gateway import (get_file_path,
                                                         parse_file_argument)


def main():
    """
    Función principal que simula y narra un combate cargado desde un archivo JSON.

    El script utiliza el módulo argparse para recibir el nombre del archivo JSON
    como argumento desde la línea de comandos. El archivo debe estar ubicado en
    el directorio especificado por 'dir_path'.

    Ejemplo de uso:
        python main.py nombre_archivo.json
    """
    # Directorio donde se almacenan los archivos de combates
    dir_path = "data/combats/"

    # Obtener el nombre del archivo JSON desde la línea de comandos
    file_name = parse_file_argument()

    # Obtener la ruta completa del archivo JSON
    file_path = get_file_path(file_name, dir_path)

    # Cargar el combate desde el archivo .json
    json_combat = load_combat_from_json_file(file_path)

    # Llamar al caso de uso y narrar la pelea
    narrate_combat(json_combat)


if __name__ == "__main__":
    main()
