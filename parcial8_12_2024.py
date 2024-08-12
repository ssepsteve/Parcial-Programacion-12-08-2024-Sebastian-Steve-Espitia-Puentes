'''
1.Desarrollar un programa que determine si una lista no existen elementos repetidos
2.Desarrollar un programa que determine si una lista se encuentra una cadena de caracteres
con dos o mas vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir "No existe"
3.Desarrollar un programa que dadods dos listas determine que elementos tiene la primera lista
que no tenga la segunda lista
4.Desarrollar un algoritmo que calcule el promedio de un arreglo de reales
5.Desarrollar un algorimto que determine la mediana de un arreglo de enteros, La mediaes es el numero 
que queda en la mitad del arreglo despues de ser ordenado
Mandar evidencia visual de que el programa funciona
'''



def programa1(lista:list): #True si no hay valores repetidos, false si hay valores repetidos
    for i in lista:
        listaSinI = lista
        listaSinI.remove(i)
        #listaSinI = listaSinI.pop(i)
        for j in listaSinI:
            if i == j:
                return False
            else:
                pass
        listaSinI = lista
    return True


def programa2(lista): #True si hay vocales, False si no hay vocales
    vocales = ["a","e","i","o","u"]
    contadorVocal = 0
    for i in range(len(lista)):
        for j in lista[i]:
            if j.lower() in vocales:
                contadorVocal +=1
            if contadorVocal >=2:
                return lista[i]
        else:pass
        contadorVocal = 0

    return "No existe"

def programa3(lista1,lista2):
    listaValoresNoCompartidos = []
    for i in lista1:
        if i in lista2:
            pass
        else:
            listaValoresNoCompartidos.append(i)
    for j in lista2:
        if j in lista1:
            pass
        else:
            listaValoresNoCompartidos.append(j)
    listaValoresNoCompartidos.sort()
    return listaValoresNoCompartidos


def programa4(arreglo):
    promedio = 0
    for i in arreglo:
        promedio += i
    promedio = promedio/len(arreglo)
    return promedio

def programa5(arreglo): 
    if len(arreglo)%2 != 0:
        operacionIndex = (len(arreglo)-1)/2
        mediana = arreglo[int(operacionIndex)]
    else:
        valorALaIzquierda = arreglo[int((len(arreglo)-2)/2)]
        valorALaDerecha = arreglo[int(len((arreglo))/2)]
        mediana = (valorALaIzquierda+valorALaDerecha)/2
    return mediana


if __name__ == "__main__":
    print("Programa 1")
    listaPrograma1CasoFalse = [1,2,3,4,5,6]
    print(f"Caso 1, No hay valores repetidos, Lista:{listaPrograma1CasoFalse}")
    print(f"Salida: {programa1(listaPrograma1CasoFalse)}")
    
    listaPrograma1CasoTrue = [1,2,3,3,4,5,6]
    print(f"Caso 2, Hay valores repetidos, Lista:{listaPrograma1CasoTrue}")
    print(f"Salida: {programa1(listaPrograma1CasoTrue)}")

    print("Programa 2")
    listaPrograma2CasoNoHayVocales = ["fddfgdggfdgfd","dgfggfdfd","fghddfhhfdhd"]
    print(f"Caso 1, No hay vocales, lista: {listaPrograma2CasoNoHayVocales}")
    print(f"Salida: {programa2(listaPrograma2CasoNoHayVocales)}")
    listaPrograma2CasoSiHayVocales = ["gfgfddgda","fdhddfhdfha","fdgfdgdOa"]
    print(f"Caso 2, Hay vocales, lista: {listaPrograma2CasoSiHayVocales}")
    print(f"Salida: {programa2(listaPrograma2CasoSiHayVocales)}")

    print("Programa 3")
    lista1Programa3NoHayValoresCompartidos = [1,2,3,4,5]
    lista2Programa3NoHayValoresCompartidos = [6,7,8,9,10]
    print(f"Caso 1, No hay valores compartidos, lista1: {lista1Programa3NoHayValoresCompartidos}, lista2: {lista1Programa3NoHayValoresCompartidos}")
    print(f"Salida: {programa3(lista1Programa3NoHayValoresCompartidos,lista2Programa3NoHayValoresCompartidos)}")

    lista1Programa3HayValoresCompartidos = [1,2,3,4,5]
    lista2Programa3HayValoresCompartidos = [3,6,7,8,9,10]
    print(f"Caso 2, Hay valores compartidos, lista1: {lista1Programa3HayValoresCompartidos}, lista2: {lista2Programa3HayValoresCompartidos}")
    print(f"Salida: {programa3(lista1Programa3HayValoresCompartidos,lista2Programa3HayValoresCompartidos)}")

    lista1Programa3TodosLosValoresCompartidos = [1,2,3,4,5]
    lista2Programa3TodosLosValoresCompartidos = [5,4,3,2,1]
    print(f"Caso 3, Todos los valores son compartidos, lista1: {lista1Programa3TodosLosValoresCompartidos}, lista2: {lista2Programa3TodosLosValoresCompartidos}")
    print(f"Salida: {programa3(lista1Programa3TodosLosValoresCompartidos,lista2Programa3TodosLosValoresCompartidos)}")
    
    print("Problema 4")
    arregloPrograma4 = [1,2,3,4,5,6]
    print(f"Arreglo:{arregloPrograma4}")
    print(f"Salida:{programa4(arregloPrograma4)}")

    print("Problema 5")
    
    arregloPrograma5CasoNumeroItemsImpares = [1,2,3,4,5]
    print(f"Caso 1, Numero items impares, lista {arregloPrograma5CasoNumeroItemsImpares}")
    print(f"Salida: {programa5(arregloPrograma5CasoNumeroItemsImpares)}")
    arregloPrograma5CasoNumeroItemsPares = [1,2,3,4]
    print(f"Caso 2, Numero items pares, lista {arregloPrograma5CasoNumeroItemsPares}")
    print(f"Salida: {programa5(arregloPrograma5CasoNumeroItemsPares)}")