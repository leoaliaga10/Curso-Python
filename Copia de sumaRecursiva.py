def sumarecursiva(numero):
	if numero == 0:
		return 0
	numero += sumarecursiva(numero - 1)
	return numero

if __name__ == '__main__':
	numero = int(input('Ingresa un numero: '))
	print('-----------------')
	suma = sumarecursiva(numero)
	print(suma)