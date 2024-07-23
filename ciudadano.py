class Ciudadano:
    def __init__(self, comunidad, _id, nombre,
                 apellido, familia, enfermedad=None):
        self.__comunidad = comunidad
        self.__id = _id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__familia = familia
        self.__enfermedad = enfermedad

    # gets y sets de los atributos
    def set_comunidad(self, comunidad):
        self.__comunidad = comunidad

    def get_comunidad(self):
        return self.__comunidad

    def set_id(self, _id):
        self.__id = _id

    def get_id(self):
        return self.__id

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_apellido(self):
        return self.__apellido

    def set_familia(self, familia):
        self.__familia = familia

    def get_familia(self):
        return self.__familia

    def set_enfermedad(self, enfermedad):
        self.__enfermedad = enfermedad

    def get_enfermedad(self):
        return self.__enfermedad
