import json
import random

from operator import itemgetter
caballos = [1,1,-1,-1]
ini = [0,0,0,0]
mov = [0,0,0,0]
cab = [[0,1],[2,1],[6,-1],[8,-1]]
tab = [[0,0,0],[0,0,0],[0,0,0]]

with open('caballos.json') as file:
	data = json.load(file)

def cabs(data,cab,ini,mov):
    for t in range(len(cab)):
        for d in data:
            if d[0] == cab[t][0]:
                if (t == 0)and(ini[0] == 0) and (mov[0] == 0):
                    cab[t][0] = d[1]
                    mov[0] = 1
                    print(["Posicion de la pieza 1"]+[cab[t][0]]) 
                    tab = tablero(cab[t][0],1)
                    if (cab[t][0]) == 8:
                        ini[t] = 1
                if (t == 1)and(ini[1] == 0)and (mov[1] == 0):
                    cab[t][0] = d[1]
                    mov[1] = 1
                    print(["Posicion de la pieza 2"]+[cab[t][0]])
                    tab = tablero(cab[t][0],2)
                    if (cab[t][0]) == 6:
                        ini[t] = 1
                if (t == 2)and(ini[2] == 0)and (mov[2] == 0):
                    cab[t][0] = d[1]
                    mov[2] = 1
                    print(["Posicion de la pieza 3"]+[cab[t][0]])
                    tab = tablero(cab[t][0],3)
                    if (cab[t][0]) == 2:
                        ini[t] = 1
                if (t == 3)and(ini[3] == 0)and (mov[3] == 0):
                    cab[t][0] = d[1]
                    mov[3] = 1
                    print(["Posicion de la pieza 4"]+[cab[t][0]])
                    tab = tablero(cab[t][0],4)
                    if (cab[t][0]) == 0:
                        ini[t] = 1
    print("posicion actual")                
    for t in tab:
        print(t)
    print("Posiciones")
    

    
    if 0 in ini:
        mov = [0,0,0,0]
        tab = reseteartablero(tab)
        return cabs(data,cab,ini,mov)
    else:
        return solucion(cab)

def tablero(posicion,cab):    
    if posicion==0:
        tab[0][0] = cab
    if posicion==1:
        tab[0][1] = cab
    if posicion==2:
        tab[0][2] = cab
    if posicion==3:
        tab[1][0] = cab
    if posicion==5:
        tab[1][2] = cab
    if posicion==6:
        tab[2][0] = cab
    if posicion==7:
        tab[2][1] = cab
    if posicion==8:
        tab[2][2] = cab
    return tab

def reseteartablero(tab):
    for t in range(len(tab)):
        for r in range(len(tab[t])):
            tab[t][r] = 0
    return tab

def solucion(cab):
    print("Estado Final")
    
    for c in cab:
        print(c)
    


cabs(data,cab,ini,mov)
