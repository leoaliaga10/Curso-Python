mi_diccionario = {}
mi_diccionario['primer_elemento'] = 'hola'
mi_diccionario['segundo_elemento'] = 'adios'

calificaciones = {}
calificaciones['Algoritmos'] = 9
calificaciones['Matematicas'] = 10
calificaciones['Diseño'] = 8
calificaciones['BaseDatos'] = 10
#Iterar en llaves
for key in calificaciones.keys():
    print(key)
#Iterar en valores
for valor in calificaciones.values():
    print(valor)
#Iterar en ítems
for key, value in calificaciones.items():
    print('llave: {}, valor: {}'.format(key, value))