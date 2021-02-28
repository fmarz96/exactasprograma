def devolver_longitud_de_un_nombre(un_nombre):
	return len(un_nombre)

def devolver_primer_elemento_de_la_lista(una_lista):
	return una_lista[0]

def devolver_segundo_elemento_del_nombre(un_nombre):
	return un_nombre[1]

def devolver_ultimo_elemento_del_nombre(un_nombre):
	return un_nombre[len(un_nombre) - 1]

def devolver_la_letra_en_posicion_del_nombre(un_nombre, posicion):
	return un_nombre[posicion]

def reemplazar_ultimo_elemento_de_la_lista(una_lista, un_elemento):
	una_lista[len(una_lista) - 1] = un_elemento
	return una_lista

def agregar_25_al_final_de_la_lista():
	lista = ["Casa", 5, "A"]
	elemento = 25
	lista.append(elemento)
	return lista

def agregar_nombre_al_final_de_la_lista(un_nombre):
	lista = ["Casa", 5, "A"]
	lista.append("" + un_nombre + "")
	return lista

def multiplicar_por_2_primer_elemento(una_lista):
	una_lista[0] = una_lista[0]*2
	return una_lista

def multiplicar_por_3_ultimo_elemento(una_lista):
	una_lista[len(una_lista) - 1] = una_lista[len(una_lista) - 1]*3
	return una_lista

def multiplicar_al_primero_y_al_ultimo_elemento(una_lista):
	una_lista = multiplicar_por_2_primer_elemento(una_lista)
	una_lista = multiplicar_por_3_ultimo_elemento(una_lista)
	return una_lista

def agregar_elemento_al_final_de_la_lista(una_lista, un_elemento):
	una_lista.append(un_elemento)
	return una_lista