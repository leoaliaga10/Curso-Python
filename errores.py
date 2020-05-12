def dividir(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print("¡división por cero!")
	else:
		print("el resultado es", result)
	finally:
		print("ejecutando la clausula finally")

dividir(1, 0.99999999999999999999999999999999999)