import random

def generar_mazos(n):
	mazos = []
	for i in range(0, n, 1):
		for l in range(0, 4, 1):
			for j in range(1, 14, 1):
				mazos.append(j)
	random.shuffle(mazos)
	return mazos

def jugar(m):
	suma_cartas = 0
	sigo = True
	while sigo:
	# while suma_cartas < 21:
		nueva_carta = m.pop(0)
		suma_cartas = suma_cartas + nueva_carta
		if suma_cartas >= 21:
			sigo = False
			break
	return suma_cartas

def jugar_varios(m, j):
	resultados = []
	for i in range(0, j, 1):
		res_jugador = jugar(m)
		resultados.append(res_jugador)
	return resultados

def ver_quien_gano(resultados):
	ganadores = []
	for i in range(0, len(resultados), 1):
		if resultados[i] == 21:
			ganadores.append(1)
		else:
			ganadores.append(0)
	return ganadores

mazo = generar_mazos(1)
print(mazo)
print(len(mazo))
# res = jugar(mazo)
# print(res)
resultados = jugar_varios(mazo, 3)
print(resultados)