import random

min_x = 10
max_x = 100
min_y = 10
max_y = 100
pos_x = random.randint(min_x, max_x)
pos_y = random.randint(min_y, max_y)
pasos_totales = 20
dt = 1000
vel_x = 10
vel_y = 10
k = 1

# vel_x * dt < max_x - min_x

salida = open("salida.xyz", "w")

def rebotar(pos, vel, minimo, maximo):
	if pos > maximo:
		vel = -vel
		pos = pos - 2*(pos - maximo)
	if pos < minimo:
		vel = -vel
		pos = pos - 2*(pos - minimo)
	return [pos, vel]

def mover_particula(pos_x, pos_y, vel_x, vel_y, dt, min_x, min_y, max_x, max_y):
	posiciones = [pos_x + vel_x*dt]
	posiciones.append(pos_y + vel_y*dt)
	eje_x = rebotar(posiciones.pop(0), vel_x, min_x, max_x)
	eje_y = rebotar(posiciones.pop(0), vel_y, min_y, max_y)
	act = []
	act.append([eje_x[0], eje_y[0]])
	act.append([eje_x[0], eje_y[1]])
	return act

def escribir_frame(archivo, pos_x, pos_y):
	print("1", file = salida)
	print(" ", file = salida)
	print("6", pos_x, pos_y, "0", file = salida)

def dist_cuadrada(x_1, y_1, x_2, y_2):
	dist = (x_2-x_1)**2 + (y_2-y_1)**2
	return dist

def calcular_fuerzas_x(pos_x,pos_y,k):
	fuerzas_x = []
	fuerzas_y = []
	for i in range(0, len(pos_x), 1):
		fza_x = 0
		fza_y = 0
		for j in range(0, len(pos_x) -1, 1):
			if i != j:
				fza_x += 4*k*(pos_x[i] - pos_x[j])/(dist**3)
				fza_y += 4*k*(pos_y[i] - pos_y[j])/(dist**3)
		fuerzas_x.append(fza_x)
		fuerzas_y.append(fza_y)
	return [fuerzas_x, fuerzas_y]

def aplicar_fuerzas(vel_x, vel_y, fzs_x, fzs_y, masas):
	for i in range(0, len(vel_x), 1):
		vel_x[i] += (fzs_x[i]/masas[i])*dt
		vel_y[i] += (fzs_y[i]/masas[i])*dt

def escribir_frame(archivo, pos_x, pos_y):
	print (nparts, file = salida)
	print (" ", file = salida)
	for i in range (nparts):
		print ("6", pos_x[i], pos_y[i], "0", file = salida)