mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]


#Eliminando duplicados cambiando la lista a conjunto y a lista nuevamente.
mi_conjunto = set(mi_lista)
mi_lista_conjunto = list(mi_conjunto)
print (mi_lista_conjunto)

#Eliminando duplicados solo utilizando listas

mi_nueva_lista = []

for numero in mi_lista:
    if numero not in mi_nueva_lista:
        mi_nueva_lista.append(numero)
print (mi_nueva_lista)        


#Ordenando la lista utilizando sort con funcion()

def ordenar_lista():
    mi_nueva_lista.sort()
    print(mi_nueva_lista)

ordenar_lista()


#Sin funcion

mi_nueva_lista.sort()
print(mi_nueva_lista)

