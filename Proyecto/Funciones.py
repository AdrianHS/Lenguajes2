

#Buscar polimorfico para las listas: recive la lista, el nombre a buscar y devuelve el elemento encontrado o vacio
def buscar(lista,nombre):
    for element in lista:
        if element.nombre==nombre:
            return element
    return []

#Buscar temporal para prescripcion, hasta que haya polimorfismo...
def buscarP(lista,nombre):
    for element in lista:
        if element.ID==nombre:
            return element
    return []


