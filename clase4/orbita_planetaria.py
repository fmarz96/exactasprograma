import numpy as np
import matplotlib.pyplot as plt
import imageio

def calcula_delta(x_sol, x_tierra):
	return x_sol - x_tierra

def calcula_distancia(pos_sol, pos_tierra):
	dist = np.sqrt(calcula_delta(pos_sol[0], pos_tierra[0])**2 + calcula_delta(pos_sol[1], pos_tierra[1])**2)
	return dist


def calcula_aceleracion(pos_sol, pos_tierra):
	G = 6.693*(10**(-11)) # Constante de gravitacion en notacion cientifica
	M = 1.98*(10**(30)) # Masa del Sol en notacion cientifica
	dist_x = calcula_delta(pos_sol[0], pos_tierra[0])
	dist_y = calcula_delta(pos_sol[1], pos_tierra[1])
	dist = calcula_distancia(pos_sol, pos_tierra)
	acel_x = (G*M/(dist**2))*(dist_x/dist)
	acel_y = (G*M/(dist**2))*(dist_y/dist)
	return [acel_x, acel_y]

def realiza_verlet(pos_anterior, pos_actual, dt):
	acel = calcula_aceleracion(pos_sol, pos_actual)
	pos_posterior = []
	pos_posterior.append(2*pos_actual[0]-pos_anterior[0]+acel[0]*dt**2)
	pos_posterior.append(2*pos_actual[1]-pos_anterior[1]+acel[1]*dt**2)
	return pos_posterior

x_lista = [-147095000000.0, -147095000000.0]
y_lista = [0.0, 2617920000.0]
dt = 60 * 60 * 24
# tiempo_total = 400
pos_sol = [0, 0]
dias = [0]
tiempo_total = 400
lista_x = []
lista_y = []
lista_aceleracion_x = []
lista_aceleracion_y = []

for i in range(1, tiempo_total-1):
	# Genero listas con las posiciones
	pos_actual = [x_lista[i], y_lista[i]]
	pos_anterior = [x_lista[i-1], y_lista[i-1]]
	# Calculo la aceleracion
	aceleracion = calcula_aceleracion(pos_sol, pos_actual)
	# Calculo la posicion futura
	pos_posterior = realiza_verlet(pos_anterior, pos_actual, dt)
	# Guardo las ultimas posiciones
	x_lista.append(pos_posterior[0])
	y_lista.append(pos_posterior[1])
	# Guardo las ultimas aceleraciones
	lista_aceleracion_x.append(aceleracion[0])
	lista_aceleracion_y.append(aceleracion[1])
	# Guardo el dia
	dias.append(i)
plt.figure()
plt.plot(x_lista, y_lista, 'grey')