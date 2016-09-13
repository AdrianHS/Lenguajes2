class Prescripcion:
    def __init__(self):
        self.ID = ""
        self.usuario = ""
        self.animal = ""
        self.enfermedad = ""
        self.peso = ""
        self.dosis = ""

    def crear(self, ID, usuario, animal, enfermedad, peso, dosis):
        self.ID = ID
        self.usuario = usuario
        self.animal = animal
        self.enfermedad = enfermedad
        self.peso = peso
        self.dosis = dosis
