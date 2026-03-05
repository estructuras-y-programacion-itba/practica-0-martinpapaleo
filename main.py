# Tu implementacion va aqui
import random
import pandas as pd

def puntos_anotados():
    # lee y retorna tabla para anotar puntos
    puntos = pd.read_csv('generala_scoreboard.csv', index_col=0)
    return puntos

def tirar_dado():
    # simula un tiro de dado
    return random.randint(1,6)

def volcar(nro: int) -> list:
    sol = []
    for i in range(nro):
        sol.append(tirar_dado())
    return sol

def tabla_config(datos):
    
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

'''
def turno():
    return
    h
def juego():
    return
'''

def main():
    jugadores = cant_jug()
    if not jugadores:
        print('Nadie quiere jugar :(')
    else:
        tiro = volcar(2)
        tiro.sort()
        puntos = puntos_anotados()
        print(f'Cantidad de jugadores: {jugadores}\n')
        print('Tabla de Puntos: '+ '\n'*2 + f'{puntos}')
    


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()