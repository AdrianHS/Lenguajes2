

#Buscar polimorfico para las listas: recive la lista, el nombre a buscar y devuelve el elemento encontrado o vacio
def buscar(lista,nombre):
    return list(filter(lambda x: x.nombre == nombre, lista))

#buscar para prescriciones y dosis
def buscarP(lista, id):
    return list(filter(lambda x: x.ID == id, lista))
