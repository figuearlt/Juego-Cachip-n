# -*- coding: utf-8 -"*-
"""

CACHIPUN

"""


"""

Random move from the machine

"""

def maquina():
    """
    Parameters: None
    
    DESCRIPTION:
    
        Determine what random answer the machine choose by 3 alternatives:
            * piedra = stone
            * papel = paper
            * scissor = tijera        
        Using random module
    """
    import random as rd
    jugada = rd.randrange(0,3)
    if jugada == 0:
        return "piedra"
    if jugada == 1:
        return "tijera"
    else:
        return "papel"


"""

Likely interactions between the machine and the player, and who would win

"""
def match(jugada):
    """
    Parameters: 
        "jugada" is the move which the player choose, within 3 alternatives:
            * "piedra"
            * "papel"
            * "tijera"
    
    DESCRIPTION:
        Scenarios where facing the machine vs the player, and when one of them win, lose or tie
    """
    python = maquina()
    print("Python jugó: ", python)
    
    if python == jugada:
        return 0
    elif python != jugada:
        if python == "piedra" and jugada =="tijera":
            return -1
        elif python == "piedra" and jugada == "papel":
            return 1
        elif python == "tijera" and jugada == "piedra":
            return 1
        elif python == "tijera" and jugada == "papel":
            return -1
        elif python == "papel" and jugada == "tijera":
            return 1
        elif python == "papel" and jugada == "piedra":
            return -1


"""

CACHIPUN function

"""

def cachipun(mejor_de=1):
    """
    Parameters:
        * mejor_de: The maximum number of times to stablish which player win. Using integer numbers
    
    DESCRIPTION:
        Using player's counter to acummulate how many times each player win. In case of tie, the counter are stay immutable.
        
        Using a "while" loop for stablish the rounds for every play.
        It'll continue as long as the result can't determine who is the player whose winnings reach the maximum possible of it, 
        such that the other can't be reach it.
        
        Depending of which player win, the counter increase on 1 unit or stay as the same if is a tie. 
        In this case, the while loop continue, mantaining this round until one player win.
        
        Finally, the winner will be the player whose "resultado" counter are greater than the other.
    """
    import math
    n_ronda = math.ceil(mejor_de/2)
    resultados = 0
    resultados_python = 0
    i=0
    while resultados < n_ronda and resultados_python < n_ronda:
        """
        Ingresar respuesta para el juego
        """
        print("Ronda # " + str(i+1))
        print("Ingrese su opción para jugar al cachipún")
        jugador = input("Las opciones serán las siguientes piedra, papel o tijera:      ").lower()
        
        """
        Aumentar o mantener el marcador del jugador o la máquina
        """
        resultado_preliminar = match(jugador)
        if resultado_preliminar == 0 :
            """
            Al existir empates, requiero poder volver a jugar la ronda hasta desempatarla
            """
            i+=1
            print("Haz empatado en esta ronda con la máquina. Sigue intentándolo")
            continue
        elif resultado_preliminar == 1:
            resultados +=1
            print("Haz ganado en esta ronda con la máquina")
        elif resultado_preliminar == (-1):
            resultados_python +=1
            print("Haz perdido en esta ronda con la máquina")
        print("---------------------------------")
        i+=1
    
    """
    Who's win?
    """
    print("Resultado final")
    
    if resultados > resultados_python:
        print("Haz ganado a la máquina")
    elif resultados < resultados_python:
        print("Haz perdido con la máquina")






