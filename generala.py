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

def cant_jug() -> int:
    # pide al usuario ingresar una cantidad de jugadores hasta que sea valida
    while True:
        try:
            cant = int(input('Ingrese cantidad de jugadores (1,2,3 o 4): \n'))
            if cant in range(5):
                return cant
            else:
                raise ValueError
        except ValueError:
            print('Respete las instrucciones previas!\n')

def tirar_dado():
    # simula un tiro de dado
    return random.randint(1,6)

def volcar(nro: int) -> list:
    # simula volcar el vaso con cierta cantdidad de dados
    sol = []
    for i in range(nro):
        sol.append(tirar_dado())
    return sol

def tabla_config(datos, c_jug: int):
    # elimina columnas innecesarias segun cantidad de jugadores 
    # elimina filas innecesarias para todas las columnas: Subtotal y Bonus
    # modifica los datos tipo NaN a str = ''
    nro_tiro = 4
    j = 'Jugador'
    columns_ = []
    while c_jug < nro_tiro:
        columns_.append(j+str(nro_tiro))
        nro_tiro -= 1
    datos = datos.drop(columns=columns_)
    datos = datos[datos.isnull()].fillna('')
    datos = datos.drop(['Subtotal', 'Bonus'])
    return datos

def valido_eleccion():
    #pide y valida seleccion al usuario
    print(1)
    return None

def es_gene(tiro: dict) -> bool:
    for i in tiro:
        if tiro[i] == 5:
            return True
    return False

def es_poker(tiro):
    for i in tiro:
        if tiro[i] == 4:
            return True
    return False

def es_full(tiro):
    for i in tiro:
        if tiro[i] == 3:
            for e in tiro:
                    if tiro[e] == 2:
                        return True
    return False

def es_esc(tiro):
    tiro = list(tiro)
    print('h')

def opciones(tiro: dict, nro_tiro: int) -> list:
    # muestra opciones para sumar puntos disponibles, 
    puntos = 0
    gene_real = False
    for i in tiro:
        if es_gene(tiro):
            puntos += 50
            if nro_tiro == 1:
                puntos += 30
                gene_real = True
                return puntos, gene_real
        elif es_poker(tiro):
            puntos += 40
            if nro_tiro == 1:
                puntos += 5
        elif es_full(tiro):
            print('A')
        else:
            print('A')
            
    return puntos, gene_real

def cuento_dados(tiro: list) -> dict:
    # retorna dict con cantidad de numeros distintos que hay en el tiro
    cant_x_num = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
    for i in range(1,6):
        cant = tiro.count(i)
        cant_x_num[i] = cant
    return cant_x_num

def sumo_puntos(tabla, tiro: list, nro_tiro: int) -> int:
    # suma los puntos correspondientes a la tabla
    return ''

def quien_gano(tabla_) -> str:
    # al finalizar el juego, revisa la tabla e indica el ganador o si hubo empate
    sol = 'l'
    return sol

def fijo_dados(tiro_: list, nro_tiro) -> list:
    # valida y retorna lista con los dados que el jugador desea fijar
    sol = []
    tiro = tiro_
    while True:
        try:
            sol.append(int(input('Ingrese los numeros que desea fijar de su tiro sin espacios, si desea tirar todos los dados nuevamente, ingrese 0')))
            if sol[0] == 0:
                return sol
            if len(sol > len(tiro)):
                raise ValueError
            for i in str(sol):
                if int(i) not in tiro:
                    raise ValueError
                else:
                    tiro.remove(int(i))
                    sol.append(i)
            return sol.sort()
        except ValueError:
            print('Respete las instrucciones previas!')
    return sol
    
def cant_vuelcos(tabla_, col_pos):
    # anota el resultado de un turno en la tabla de puntos
    turno = True
    dados = 5
    nro_tiro = 1
    sol = []
    while nro_tiro <= 3 and turno:
        tiro = volcar(dados - len(sol))
        tiro.sort()
        print(f'Tiro nro. {nro_tiro} de 3: \n{tiro}')
        sol = fijo_dados(tiro, nro_tiro)
        nro_tiro += 1
    cant_x_num = cuento_dados(tiro)
    return tabla_

def juego(tabla_, col_pos):
    # indica a quien le toca tirar y muestra su tabla de puntos
    # llama a funciones que resuelven anotar los puntos del turno actual
    print(f'''\nTabla de Puntos: \n{tabla_}\n
    Le toca tirar a {tabla_.columns[col_pos]}\n''')
    cant_vuelcos(tabla_, col_pos)
    return tabla_

def turnos(tabla_):
    # simula todos los turnos y ofrece la opcion de finalizar abruptamente luego de cualquier jugada
    for i in range(len(tabla_.index) - 1): # se resta uno porque la fila 'Total' no se incluye, se calcula automaticamente por otra funcion.
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