import numpy as np
import matplotlib.pyplot as plt

def crear_tablero(n, m):
	t = np.repeat(" ",(n+2)*(m+2)).reshape((n+2),(m+2))
	for i in range(0, t.shape[0], 1):
		for j in range(0, t.shape[1], 1):
			if i == 0 or i == t.shape[0]-1 or j == 0 or j == t.shape[1]-1:
				t[i][j] = "M"
			else:
				t[i][j] = " "
	return t

def es_borde(tablero, coord):
	if coord[0] == 0 or coord[0] == tablero.shape[0]-1 or coord[1] == 0 or coord[1] == tablero.shape[1]-1:
		return True
	else:
		return False
	#return tablero[coord[0], coord[1]] == "M"

def vecinos_de(tablero, coord):
	vecinos = []
	vec = []
	f = coord[0]
	c = coord[1]
	vec.append((f-1, c-1))
	vec.append((f-1, c))
	vec.append((f-1, c+1))
	vec.append((f, c+1))
	vec.append((f+1, c+1))
	vec.append((f+1, c))
	vec.append((f+1, c-1))
	vec.append((f, c-1))
	i = 0
	while i < len(vec):
		if not es_borde(tablero, vec[i]):
			vecinos.append(vec[i])
		i = i + 1
	return vecinos

def buscar_adyacente(tablero, coord, objetivo):
	vecinos = vecinos_de(tablero, coord)
	ady = []
	for i in range(0, len(vecinos), 1):
		f = vecinos[i][0]
		c = vecinos[i][1]
		if tablero[f][c] == objetivo:
			ady.append((f, c))
			return ady
	return ady

def mover(tablero, coord):
	#vecinos = vecinos_de(tablero, coord)
	c1 = coord[0]
	c2 = coord[1]
	#for i in range(0, len(vecinos), 1):
	#	if tablero[c1][c2] != " " and tablero[c1][c2] != "M":
	#		f = vecinos[i][0]
	#		c = vecinos[i][1]
	#		if tablero[f][c] == " ":
	#			tablero[f][c] = tablero[c1][c2]
	#			tablero[c1][c2] = " "
	#			return tablero
	objetivo = " "
	ady = buscar_adyacente(tablero, coord, objetivo)
	if len(ady) > 0 and tablero[c1][c2] != " " and tablero[c1][c2] != "M":
		x = ady[0][0]
		y = ady[0][1]
		tablero[x][y] = tablero[c1][c2]
		tablero[c1][c2] = " "
	return tablero


def alimentar(tablero, coord):
	c1 = coord[0]
	c2 = coord[1]
	if tablero[c1, c2] == "L":
		ady = buscar_adyacente(tablero, coord, "A")
		if len(ady) > 0:
			x = ady[0][0]
			y = ady[0][1]
			tablero[x][y] = "L"
			tablero[c1][c2] = " "
	return tablero
		#vecinos = vecinos_de(tablero, (c1, c2))
		#for i in range(0, len(vecinos), 1):
		#	f = vecinos[i][0]
		#	c = vecinos[i][1]
		#	if tablero[f][c] == "A":
		#		tablero[f][c] = "L"
		#		tablero[c1][c2] = " "

def reproducir(tablero, coord):
	c_x = coord[0]
	c_y = coord[1]
	if tablero[c_x][c_y] != " " and tablero[c_x][c_y] != "M":
		vecinos = vecinos_de(tablero, coord)
		ady = buscar_adyacente(tablero, coord, tablero[c_x][c_y])
		if len(ady) > 0:
			ady2 = buscar_adyacente(tablero, coord, " ")
			if len(ady2) > 0:
				f2 = ady2[0][0]
				c2 = ady2[0][1]
				tablero[f2][c2] = tablero[c_x][c_y]
	return tablero

def fase_mover(tablero):
	for i in range(1, tablero.shape[0]-1, 1):
		for j in range(1, tablero.shape[1]-1, 1):
			tablero = mover(tablero, (i, j))
	return tablero

def fase_alimentacion(tablero):
	for i in range(1, tablero.shape[0]-1, 1):
		for j in range(1, tablero.shape[1]-1, 1):
			tablero = alimentar(tablero, (i, j))
	return tablero

def fase_reproduccion(tablero):
	for i in range(1, tablero.shape[0]-1, 1):
		for j in range(1, tablero.shape[1]-1, 1):
			tablero = reproducir(tablero, (i, j))
	return tablero

def evolucionar(tablero):
	tab1 = fase_alimentacion(tablero)
	tab2 = fase_reproduccion(tab1)
	tab3 = fase_mover(tab2)
	return tab3



t = crear_tablero(3, 4)
# definimos la coordenadas de los animales
filas = [1, 2, 3, 1, 2]
columnas = [1, 1, 1, 3, 3]
animal = ["L", "A", "A", "A", "A"]
# y ahora los asignamos dentro del tablero
for i in range(0, len(animal), 1):
	t[(filas[i], columnas[i])] = animal[i]

print("Tablero original:")
print(t)
print("Tablero despues de evolucionar:")
#tab = evolucionar(t)
#print(tab)
t = evolucionar(t)
print(t)