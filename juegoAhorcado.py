import random


def ahorcado():
    lista_palabras= ['francia','españa','mexico','colombia','brasil','uruguay']
    palabra= list(lista_palabras[random.randint(0,6)])
    #print(palabra) test
    a=['_']
    palabra_visual= a * len(palabra)

    for i in range(10,0,-1):
        cont=0
        print('----------------------------------------------------')
        print('           A H O R C A D O')
        print('tienes ',i,' intentos para adivinar el pais')
        print(palabra_visual)

        letra= input('escribe una letra--> ')
        for letter in palabra:
            
            if letra==letter:
                print('adivinaste una letra')
                palabra[cont]=0
                palabra_visual[cont]=letra
                break
            cont+=1
        if not'_'in palabra_visual:
            palabra_final=''.join(palabra_visual)
            print('----------------------------------------------------------------------------------------------------')
            print('            Encontraste la palabra felicidades',palabra_final.upper())
            print('----------------------------------------------------------------------------------------------------')
           

            break
    if i==1:
        print('----------------------------------------------------------------------------------------------------')
        print('           Perdiste, intentalo de nuevo')
        print('----------------------------------------------------------------------------------------------------')


if __name__ == "__main__":
    ahorcado()