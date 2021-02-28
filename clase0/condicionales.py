def decir_si_es_mas_grande_que_5(numero):
	res = numero > 5
	return res

def decir_si_al_dividir_no_da_resto(dividendo, divisor):
	resto = dividendo % divisor
	return resto == 0

def decir_si_es_negativo(un_numero):
	if un_numero > 0:
		res = True
	else:
		res = False
	print(res)

def decir_si_la_longitud_es_igual_a(un_nombre, un_numero):
	print(len(un_nombre) == un_numero)

def es_par(un_numero):
	resto = un_numero % 2
	return resto == 0

def devolver_valor_mas_grande(valor1, valor2):
	if valor1 > valor2:
		resultado = valor1
	else:
		resultado = valor2
	return resultado

def devolver_el_doble_si_es_par(un_numero):
	if(es_par(un_numero)):
		resultado = un_numero*2
	else:
		resultado = un_numero
	return resultado

def devolver_segun_condiciones_locas(un_numero):
	if(un_numero == 2):
		resultado = un_numero + 1
	elif un_numero <= 10:
		resultado = un_numero*2
	elif un_numero >= 20 and un_numero <= 34:
		resultado = un_numero + 5
	else:
		resultado = 0
	return resultado

def devuelve_el_doble(un_numero):
	if un_numero > 10 and un_numero < 20:
		resultado = un_numero*2
	else:
		resultado = un_numero
	return resultado

def nota(un_numero):
	if un_numero >= 4 and un_numero <= 10:
		return "Aprobado!!!"
	else:
		return "Me bocharon"

def rango(un_numero):
	if un_numero >=5 and un_numero <= 10:
		return "Está en el rango deseado"
	else:
		return "Fuera de rango"

def intervalos(numero):
	if numero < 5:
		return "Menor a 5"
	elif numero >= 10 and numero <= 20:
		return "Entre 10 y 20"
	else:
		return "Numero muy grande"