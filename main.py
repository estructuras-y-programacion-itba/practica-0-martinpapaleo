# Tu implementacion va aqui
import random
import pandas as pd

puntos = pd.read_csv('generala_scoreboard.csv', index_col=0)

def tirar_dado():
    # simula un tiro de dado
    return random.randint(1,6)

def volcar(nro: int) -> list:
    sol = []
    for i in range(nro):
        sol.append(tirar_dado())
    return sol

def turno():
    return
    
def juego():
    return


def main():
    tiro = volcar(2)
    tiro.sort()
    print(tiro)
    


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()