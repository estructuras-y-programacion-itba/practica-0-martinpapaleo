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
    #simula volcar el vaso con cierta cantdidad de dados
    sol = []
    for i in range(nro):
        sol.append(tirar_dado())
    return sol

def tabla_config(datos, c_jug: int):
    #elimino columnas innecesarias segun cantidad de jugadores 
    #modifico los datos tipo NaN a str = ''
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
    # pide al usuario ingresar una cantidad de jugadores hasta que sea valida
    while True:
        try:
            cant = int(input('Ingrese cantidad de jugadores (1,2,3 o 4): '))
            if cant in range(5):
                return cant
            else:
                raise ValueError
        except ValueError:
            print('Respete las instrucciones previas!')

def cuento_verifico(tiro: list) -> int:
    #cuenta cantidad de numeros distintos que hay en el tiro
    cant_x_num = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
    for i in range(1,6):
        cant = tiro.count(i)
        cant_x_num[i] = cant
    
def sumo_puntos():
    # suma los puntos correspondientes a la tabla
    return ''

def quien_gano(tabla_) -> str:
    #al finalizar el juego, revisa la tabla e indica el ganador o si hubo empate
    sol = 'l'
    return sol


def opciones(tiro: list, nro_tiro: int) -> list:

    sol = []

    return sol

def cant_vuelcos():
    # resuelve el resultado de un turno en particular
    sol = []
    done = True
    dados = 5
    t = 0
    while t < 3 and done:
        tiro = volcar(dados)
        tiro.sort()
        print(f'Tiro nro. {t} de 3.\n{tiro}')
        sol = opciones(tiro, t)
        t += 1

    return sol


def juego(tabla_, col_pos):
    print(f'Le toca tirar a {tabla_.columns[col_pos]}\n')
    tiro_final = cant_vuelcos()
    print(tabla_.iloc[1:,col_pos])
    return tabla_

def turnos(tabla_):
    # simula todos los turnos y ofrece la opcion de finalizar abruptamente luego de cualquier jugada
    for i in range(len(tabla_.index)):
        for e in range(len(tabla_.columns)):
            tabla_ = juego(tabla_, e)
            stop = input('''Ingrese "STOP": si desea finalizar el juego sin designar un ganador.\nEsta accion es irreversible y elimina todo el progreso.\n''')
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
        #print('\nTabla de Puntos Actual: '+ '\n'*2 + f'{tabla_puntos}\n')

    if not turnos(tabla_puntos):
        print('\nSe decidio finalizar el juego. No hay un ganador/a. Se borraron todos los datos del juego.')
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