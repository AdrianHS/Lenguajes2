class Dosis:
    def __init__(self):
        self.ID = ""
        self.animal = ""
        self.medicamento = ""
        self.enfermedad = ""
        self.rangoPeso = ""
        self.dosis = ""

    def crear(self, ID, animal, medicamento, enfermedad, rangoPeso, dosis):
        self.ID = ID
        self.animal = animal
        self.medicamento = medicamento
        self.enfermedad = enfermedad
        self.rangoPeso = rangoPeso
        self.dosis = dosis
