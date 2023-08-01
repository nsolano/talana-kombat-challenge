# Talana Kombat JRPG

Talana Kombat JRPG es un juego de lucha por turnos en el que los jugadores deben enfrentarse y reducir la energía del oponente para ganar la partida. Cada jugador tiene movimientos y golpes especiales que pueden utilizar para atacar al oponente.

Los botones que se usan son:
- (W)Arriba, (S)Abajo, (A)Izquierda, (D)Derecha, 
- (P)Puño, (K)Patada 

Golpes de nuestros personajes:
- Tonyn Stallone
```

| Combinación | Energía que quita | Nombre del movimiento |
|------------|-------------------|----------------------|
| DSD + P    | 3                 | Taladoken            |
| SD + K     | 2                 | Remuyuken            |
| P o K      | 1                 | Puño o Patada        |

```

-  Arnaldor Shuatseneguer:
```
| Combinación | Energía que quita | Nombre del movimiento |
|------------|-------------------|----------------------|
| SA + K     | 3                 | Remuyuken            |
| ASA + P    | 2                 | Taladoken            |
| P o K      | 1                 | Puño o Patada        |

```

### Información importante: 
Parte atacando el jugador que envió una combinación menor de botones (movimiento + golpes), en caso de empate, parte el con menos movimientos, si empatan de nuevo, inicia el con menos golpes, si hay empate de nuevo, inicia el player 1 (total el player 2 siempre es del hermano chico) 

La secuencia completa del combate de cada jugador se entrega de una vez (consolidada en un json) 
Cada personaje tiene 6 Puntos de energía 
- Un personaje muere cuando su energía llega a 0 y de inmediato finaliza la pelea
- Tonyn es el player 1, siempre ataca hacia la derecha (y no cambia de lado)
- Arnaldor es el player 2, siempre ataca hacia la izquierda (y no cambia de lado)
- Los personajes se atacan uno a la vez estilo JRPG, por turnos hasta que uno es derrotado, los golpes no pueden ser bloqueados, se asume que siempre son efectivos. 

Los datos llegan como un json con botones de movimiento y golpe que se correlacionan para cada jugada 

Los movimientos pueden ser un string de largo máximo 5 (puede ser vacío) 

Los golpes pueden ser un solo botón maximo (puede ser vacío) 

Se asume que el botón de golpe es justo después de la secuencia de movimiento, es decir, AADSD + P es un Taladoken (antes se movió para atrás 2 veces); DSDAA + P son movimientos más un puño 

Para este desafío: Desarrolla una solución que relata la pelea e informe el resultado final

### Por ejemplo para el siguiente json de pelea: 

```
{"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}} 
```

- Tonyn avanza y da una patada
- Arnaldor conecta un Remuyuken
- Tonyn usa un Taladoken
- Arnaldor se mueve 
- Tonyn le da un puñetazo al pobre Arnaldor
- Arnaldor conecta un Remuyuken
- Arnardold Gana la pelea y aun le queda 1 de energía

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

2. Carga el archivo de .json dentro de la carpeta `data/combats`.

3. Ejecuta el script principal para iniciar el juego.

    ```python main.py```



## Estructura del proyecto

La estructura del proyecto es la siguiente:


```
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
```

- `src/`: Contiene el código fuente de la aplicación.
- `test/`: Contiene las pruebas unitarias para el código fuente.
- `data/`: Contiene los archivos de datos necesarios para el juego.
