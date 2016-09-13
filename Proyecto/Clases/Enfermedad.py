class Enfermedad:
    def __init__(self):
        self.nombre=""
        self.descripcion=""
        self.foto=""

    def crear(self,nombre,descripcion,foto):
        self.nombre = nombre
        self.descripcion = descripcion
        self.foto = foto
