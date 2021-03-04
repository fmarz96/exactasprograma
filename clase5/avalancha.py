import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

# n = 4
# t = np.repeat(0, n*n)
# t = t.reshape(n, n)
# t = np.repeat(0,8*8).reshape(8,8)
# print(t)
# print(t[(2, 3)])


def crear_tablero(n):
	t = np.repeat(0,n*n).reshape(n,n)
	for i in range(0, t.shape[0], 1):
		for j in range(0, t.shape[1], 1):
			if i == 0 or i == t.shape[0]-1 or j == 0 or j == t.shape[1]-1:
				t[i][j] = -1
			else:
				t[i][j] = 0
	return t

def es_borde(tablero, coord):
	#if t[coord[0], coord[1]] == -1:
	#	return True
	#else:
	#	return False
	if coord[0] == 0 or coord[0] == tablero.shape[0]-1 or coord[1] == 0 or coord[1] == tablero.shape[1]-1:
		return True
	else:
		return False

def tirar_copo(tablero, coord):
	tablero[coord[0], coord[1]] += 1
	return tablero

def vecinos_de(tablero, coord):
	vecinos = []
	vec = []
	vec.append((coord[0]+1, coord[1]))
	vec.append((coord[0], coord[1]+1))
	vec.append((coord[0]-1, coord[1]))
	vec.append((coord[0], coord[1]-1))
	i = 0
	while i < len(vec):
		if not es_borde(tablero, vec[i]):
			vecinos.append(vec[i])
		i = i + 1
	return vecinos

def desbordar_posicion(tablero, coord):
	if tablero[coord[0], coord[1]] >= 4:
		tablero[coord[0], coord[1]] -= 4
		vecinos = vecinos_de(tablero, coord)
		i = 0
		while i < len(vecinos):
			f = vecinos[i][0]
			c = vecinos[i][1]
			tablero[f, c] += 1
			i += 1
	return tablero

def desbordar_valle(t1):
	cantidad_filas = t1.shape[0]
	cantidad_columnas = t1.shape[1]
	for i in range(1, cantidad_filas - 1):
		for j in range(1, cantidad_columnas - 1):
			if t1[i][j] >= 4:
				t1 = desbordar_posicion(t1, (i, j))
	return t1

def hay_que_desbordar(t1):
	filas = t1.shape[0]
	columnas = t1.shape[1]
	desbordes = 0
	for i in range(0, filas, 1):
		for j in range(0, columnas, 1):
			if t1[i][j] >= 4:
				desbordes += 1
	return desbordes > 0

def estabilizar(tablero):
	while hay_que_desbordar(tablero):
		tablero = desbordar_valle(tablero)
	return tablero

def paso(tablero):
	f = (tablero.shape[0]-1)//2
	c = (tablero.shape[1]-1)//2
	tablero[f, c] += 1
	tablero = estabilizar(tablero)
	return tablero

def guardar_foto(t, paso):
	dir_name = "output"
	if not os.path.exists(dir_name):
		os.mkdir(dir_name)
	ax = plt.gca()
	file_name = os.path.join(dir_name, "out{:05}.png".format(paso))
	plt.imshow(t, vmin=-1, vmax=3)
	ax.set_title("Copos tirados: {}".format(paso+1)) #titulo
	plt.savefig(file_name)

def hacer_video(cant_fotos):
	dir_name = "output"
	lista_fotos=[]
	for i in range (cant_fotos):
		file_name = os.path.join(dir_name, "out{:05}.png".format(i))
		lista_fotos.append(imageio.imread(file_name))
	video_name = os.path.join(dir_name, "avalancha.mp4")
	imageio.mimsave(video_name, lista_fotos, fps=10)
	print('Estamos trabajando en el directorio', os.getcwd())
	print('y se guardo el video:', video_name)

def probar(n, pasos=200):
	t = crear_tablero(n)
	for i in range(pasos):
		paso(t)
		guardar_foto(t, i)
		#hacer_video(pasos)
	return t

def tirar_copo_al_azar(tablero):
	f = randint(1, tablero.shape[0]-1)
	c = randint(1, tablero.shape[1]-1)
	if not es_borde(tablero[f][c]):
		tablero[f][c] += 1
	return tablero

def generar_tablero_aleatorio(n, cant_copos):
	t1 = crear_tablero(n)
	i = 1
	while i <= cant_copos:
		f = randint(1, t1.shape[0]-1)
		c = randint(1, t1.shape[1]-1)
		if not es_borde(t1[f][c]):
			t1[f][c] += 1
		i = i + 1
	return t1

# n = 8
# t = crear_tablero(8)
# print(t)

t1 = crear_tablero(9)
pasos = 200
print(probar(9, pasos))
#print(t1)

#print(es_borde(t1, (0, 1)))
#print(es_borde(t1, (8, 6)))
#print(es_borde(t1, (5, 6)))

#print(vecinos_de(t1, (1, 4)))
#print(vecinos_de(t1, (2, 5)))
#print(vecinos_de(t1, (7, 7)))