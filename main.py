# Tu implementacion va aqui
import random
import pandas as pd
from pathlib import Path
from collections import Counter

def creo_tabla():
    # lee y retorna tabla para anotar tabla_puntos
    base_dir = Path(__file__).resolve().parent
    csv_dir = base_dir / 'generala_scoreboard.csv'
    tabla_puntos = pd.read_csv(csv_dir, index_col=0)
    return tabla_puntos


def tirar_dado():
    # simula un tiro de dado
    return random.randint(1,6)

def volcar(nro: int) -> list:
    sol = []
    for i in range(nro):
        sol.append(tirar_dado())
    return sol

def tabla_config(datos, c_jug: int):
    t = 4
    j = 'Jugador'
    columns_ = []
    while c_jug < t:
        columns_.append(j+str(t))
        t -= 1
    datos = datos.drop(columns=columns_)
    return datos

def cant_jug() -> int:
    while True:
        try:
            cant = int(input('Ingrese cantidad de jugadores (1,2,3 o 4): '))
            if cant in range(5):
                return cant
            else:
                raise ValueError
        except ValueError:
            print('Respete las instrucciones previas!')

def opciones(tiro: list) -> list:
    op = []

    return op

def cant_vuelcos():
    t = 1
    tiro = volcar(5)
    tiro.sort()
    print(f'1er tiro: {tiro}')


def juego(tabla_, col_pos):
    print(tabla_.iloc[:,col_pos])
    return tabla_

def turnos(tabla_):
    for i in range(len(tabla_.index)):
        for e in range(len(tabla_.columns)):
            tabla_ = juego(tabla_, e)
            stop = input('''Ingrese "STOP": si desea finalizar el juego sin designar un ganador. 
            Esta accion es irreversible y elimina todo el progreso.''')
    return tabla_

def main():
    jugadores = cant_jug()
    if not jugadores:
        print('Nadie quiere jugar :(')
    else:
        tabla_puntos = tabla_config(creo_tabla(), jugadores)
        print('\nTabla de Puntos: '+ '\n'*2 + f'{tabla_puntos}')

    try:
        print('H')
    except:
        print('I')


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()