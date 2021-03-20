import random
import numpy as np

def crear_album(figus_total):
	i = 0
	album = []
	while i < figus_total:
		album.append(0)
		i = i + 1
	return album

def hay_alguno(l, e):
	contiene = False
	for i in range(0, len(l), 1):
		if l[i] == e:
			contiene = True
	return contiene

def comprar_una_figu(figus_total):
	return random.randint(0, figus_total - 1)

def cuantas_figus(figus_total):
	album = crear_album(figus_total)
	cant_figus_adquiridas = 0
	while hay_alguno(album, 0):
		num_figu = comprar_una_figu(figus_total)
		album[num_figu] = 1
		cant_figus_adquiridas = cant_figus_adquiridas + 1
	return cant_figus_adquiridas

def prom_resultados(figus_total):
	resultados = []
	for i in range(0, 5, 1):
		cant_figus = cuantas_figus(figus_total)
		resultados.append(cant_figus)
	prom = np.mean(resultados)
	return prom

def experimentar(figus_total, n_rep):
	resultados = []
	for i in range(0, n_rep, 1):
		cant_figus = cuantas_figus(figus_total)
		resultados.append(cant_figus)
	return resultados

def generar_paquete(figus_total, figus_paquete):
	paquete = []
	i = 0
	while i < figus_paquete:
		num_figu = random.randint(0, figus_total - 1)
		# if not hay_alguno(paquete, num_figu):
		paquete.append(num_figu)
		i = i + 1
	return paquete

def cuantos_paquetes(figus_total, figus_paquete):
	album = crear_album(figus_total)
	cant_paquetes = 0
	while(hay_alguno(album, 0)):
		paquete = generar_paquete(figus_total, figus_paquete)
		i = 0
		while i < len(paquete):
			num_figu = paquete[i]
			album[num_figu] = 1
			i = i + 1
		cant_paquetes = cant_paquetes + 1
	return cant_paquetes

def experimentar_con_paquetes(figus_total, figus_paquete, n_rep):
	resultados = []
	for i in range(0, n_rep, 1):
		cantidad_paquetes_comprados = cuantos_paquetes(figus_total, figus_paquete)
		resultados.append(cantidad_paquetes_comprados)
	return resultados

# r = random.random()
# print(r)
# r_int = random.randint(1, 10)
# print(r_int)
# lista = np.arange(10)
# print(lista)
# mean = np.mean(lista)
# print(mean)

# cantidad_figus = cuantas_figus(5)
# print(cantidad_figus)

# prom = prom_resultados(5)
# print(prom)

# resultados = experimentar(5, 10)
# print(resultados)

# res_mil_rep = experimentar(6, 1000)
# prom_mil_rep = np.mean(res_mil_rep)
# print(res_mil_rep)
# print(len(res_mil_rep))
# print(prom_mil_rep)

# res_670_rep = experimentar(670, 100)
# prom_670_rep = np.mean(res_670_rep)
# print(prom_670_rep)

album = crear_album(670)
print("Listo. Album creado!")

cant_paquetes = cuantos_paquetes(670, 5)
print(cant_paquetes)

exp_con_paquetes = experimentar_con_paquetes(670, 5, 100)
promedio_cant_paquetes = np.mean(exp_con_paquetes)
print(promedio_cant_paquetes)