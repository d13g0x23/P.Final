from enfermedad import Enfermedad # Para ocupar la tasa de recuperación (dias que esta contagiado o con la infección)

class Ciudadano:
    def __init__(self, comunidad, _id, nombre, apellido, familia, enfermedad):
        """S: suceptible
           I: infectado
           R: recuperado"""
        self.__comunidad = comunidad
        self.__id = _id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__familia = familia
        self.__enfermedad = enfermedad
        self.__estado = "S"
        self.__contador = None


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
    
    def set_estado(self, estado):
        self.__estado = estado

    def get_estado(self):
        return self.__estado
    
    def set_contador(self, contador):
        self.__contador = contador

    # Métodos para la clase ciudadano
    def iniciar_contagio(self):
        """
        Inicializa el contador de la duración del contagio con la tasa de recuperación  de la enfermedad
        """
        self.__contador = self.__enfermedad.get_tasarecuperacion() # Son los días que esta contagiado o que esta con la infección

    def duracion_contagio(self):
        """
        Simula la duración del contagio, en este caso, un contador que decrementa en 1 cada día.    
        """
        if self.__contador is not None:
            self.__contador -= 1

    def actualizar_estado(self):
        """
        Actualiza el estado del ciudadano basado en la tasa de recuperación de la enfermedad
        """
        if self.__estado == "I" and self.__contador is not None:
            self.duracion_contagio()
            if self.__contador <= 0:
                self.__estado = "R"
                self.__contador = None
    
    def infectar(self):
        """
        Cambia el estado del ciudadano de "S" a "I" y inicializa el contagio
        """
        if self.__estado == "S":
            self.__estado = "I"
            self.iniciar_contagio()