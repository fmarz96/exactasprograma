def devolver_la_suma(numero1, numero2):
	suma = numero1 + numero2
	return suma

def celsius_a_farenheit(temp_cel):
	temp_far = temp_cel*(9/5) + 32
	return temp_far

def perimetro_cuadrado(lado):
	perim = lado*4
	return perim

def area_rectangulo(lado1, lado2):
	area = lado1*lado2
	return area

def obtener_valor(precio):
	total = precio - (precio*35)/100
	return total

def es_tripla_pitagorica(cateto1, cateto2, hipotenusa):
	cuadrados_catetos = cateto1*cateto1 + cateto2*cateto2
	cuadrado_hipotenusa = hipotenusa*hipotenusa
	es_tripla = cuadrados_catetos == cuadrado_hipotenusa
	return es_tripla

suma = devolver_la_suma(3, 5)
print(suma)

temp_far = celsius_a_farenheit(40)
print(temp_far)

perim = perimetro_cuadrado(4)
print(perim)

area_rect = area_rectangulo(3, 5)
print(area_rect)

precio_con_descuento = obtener_valor(100)
print(precio_con_descuento)

es_tripla = es_tripla_pitagorica(6, 8, 10)
print(es_tripla)