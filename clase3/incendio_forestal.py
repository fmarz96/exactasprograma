import random
import numpy as np
import matplotlib.pyplot as plt

def generar_bosque(n):
	i = 0
	bosque = []
	while i < n:
		bosque.append(0)
		i = i + 1
	return bosque

def brotes(bosque, p):
	for i in range(len(bosque)):
		r = random.random()
		if r < p:
			bosque[i] = 1
	return bosque

# def suceso_aleatorio(p):

def cuantos(bosque, tipo_celda):
	return bosque.count(tipo_celda)
	# tot = 0
	# for i in range(0, len(bosque)):
	# 	if bosque[i] == tipo_celda:
		# 	tot += 1
	# return tot

def rayos(bosque, f):
	for i in range(0, len(bosque), 1):
		r = random.random()
		if r < f and bosque[i] == 1:
			bosque[i] = -1
	return bosque

def propagacion(bosque):
	for i in range(0, len(bosque) - 1, 1):
		if bosque[i] == -1 and bosque[i+1] == 1:
			bosque[i+1] = -1
	for j in range(len(bosque) - 1, 0, -1):
		if bosque[j] == -1 and bosque[j-1] == 1:
			bosque[j-1] = -1
	return bosque


def limpieza(bosque):
	for i in range(0, len(bosque), 1):
		if bosque[i] == -1:
			bosque[i] = 0
	return bosque

def dinamica(n, n_rep, p, f):
	bosque = generar_bosque(n)
	vivos_por_anio = []
	for i in range(1, n_rep+1, 1):
		bosque = brotes(bosque, p)
		bosque = rayos(bosque, f)
		bosque = propagacion(bosque)
		bosque = limpieza(bosque)
		vivos_por_anio.append(cuantos(bosque, 1))
	prom = np.mean(vivos_por_anio)
	return prom


b_1 = [1, 1, 1, -1, 0, 0, 0, -1, 1, 0]
print(propagacion(b_1))

b_2 = [-1, 1, 1, -1, 1, 1, 0, 0, -1, 1]
print(propagacion(b_2))

din = dinamica(10, 50, 0.9899999, 0.02)
print(din)