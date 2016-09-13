class Usuario:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.nombre = ""
        self.admin = ""
        self.foto = ""

    def crear(self, username, password, nombre, admin, foto):
        self.username = username
        self.password = password
        self.nombre = nombre
        self.admin = admin
        self.foto = foto
