# Talana Kombat JRPG

Talana Kombat JRPG es un juego de lucha por turnos en el que los jugadores deben enfrentarse y reducir la energía del oponente para ganar la partida. Cada jugador tiene movimientos y golpes especiales que pueden utilizar para atacar al oponente.

## Instalación

1. Clona este repositorio en tu máquina local.
```git clone https://github.com/tu_usuario/talana-kombat-challenge.git```
2. Accede al directorio del proyecto.
```cd talana-kombat-challenge```
3. Crea un entorno virtual (opcional, pero se recomienda).
```python3 -m venv .venv```
4. Activa el entorno virtual.
```source venv/bin/activate```
5. Ejecuta el comando ```pip install -r requirements.txt``` para instalar

## Cómo jugar

1. Asegúrate de estar dentro del directorio del proyecto y con el entorno virtual activado.

2. Ejecuta el script principal para iniciar el juego.
```python main.py```

3. Sigue las instrucciones en pantalla para jugar el combate.

## Estructura del proyecto

La estructura del proyecto es la siguiente:

talana_kombat/
├── src/
│ ├── core/
│ │ ├── entity/
│ │ │ └── player.py
│ │ ├── repository/
│ │ │ └── combat_repository.py
│ │ └── usecase/
│ │ └── combat_usecase.py
│ └── infrastructure/
│ ├── controllers/
│ │ └── combats_controller.py
│ └── gateways/
│ └── combats_gateway.py
├── test/
│ ├── core/
│ │ ├── entity/
│ │ │ └── test_player.py
│ │ └── usecase/
│ │ └── test_combat_usecase.py
│ └── infrastructure/
│ └── controllers/
│ └── test_combats_controller.py
└── data/
└── combats/
└── test/

- `src/`: Contiene el código fuente de la aplicación.
- `test/`: Contiene las pruebas unitarias para el código fuente.
- `data/`: Contiene los archivos de datos necesarios para el juego.
