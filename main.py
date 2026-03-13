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
    #elimino columnas innecesarias segun cantidad de jugadores 
    #modifico los datos tipo NaN a ''
    t = 4
    j = 'Jugador'
    columns_ = []
    while c_jug < t:
        columns_.append(j+str(t))
        t -= 1
    datos = datos.drop(columns=columns_)
    datos = datos[datos.isnull()].fillna('')
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

def quien_gano(tabla_) -> str:
    sol = None
    return sol

def opciones(tiro: list) -> list:
    op = []

    return op

def cant_vuelcos():
    t = 1
    tiro = volcar(5)
    tiro.sort()
    print(f'1er tiro: {tiro}')


def juego(tabla_, col_pos):
    print(f'''Le toca tirar a: {tabla_.columns[col_pos]}''')
    print(tabla_.iloc[1:,col_pos])
    return tabla_

def turnos(tabla_):
    # simula todos los turnos y ofrece la opcion de finalizar abruptamente luego de cualquier jugada
    for i in range(len(tabla_.index)):
        for e in range(len(tabla_.columns)):
            tabla_ = juego(tabla_, e)
            stop = input('''Ingrese "STOP": si desea finalizar el juego sin designar un ganador. 
            Esta accion es irreversible y elimina todo el progreso.\n''')
            if stop == 'STOP':
                tabla_ = None
                return tabla_
    return tabla_

def main():
    jugadores = cant_jug()
    if not jugadores:
        print('Nadie quiere jugar :(')
    else:
        tabla_puntos = tabla_config(creo_tabla(), jugadores)
        print('\nTabla de Puntos Actual: '+ '\n'*2 + f'{tabla_puntos}\n')

    if not turnos(tabla_puntos):
        print('Se decidio finalizar el juego. No hay un ganador/a. Se borraron todos los datos del juego.')
    else:
        sol = turnos(tabla_puntos)
        ganador = quien_gano(sol)
        
        print(f'''Tabla final: 
        {sol}
        El ganador/a es {ganador}, felicidades!!!

        Juego finalizado.
        ''')
        

# No cambiar a partir de aqui
if __name__ == "__main__":
    main()