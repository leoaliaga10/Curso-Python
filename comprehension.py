pares = []

for num in range(1,31):
    if num % 2 == 0:
        pares.append(num)

print (pares)

pares2 = [num for num in range(1,31) if num % 2 == 0]

print (pares2)

cuadrados = {}
for num in range(1,11):
	cuadrados[num] = num**2

print (cuadrados)

cuadrados2 = {num: num**2 for num in range(1,11) }

print (cuadrados2)