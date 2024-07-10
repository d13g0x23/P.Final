class Comunidad:
    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica):
        self.__num_ciudadanos = num_ciudadanos 
        self.__promedio_conexion_fisica = promedio_conexion_fisica
        self.__enfermedad = enfermedad
        self.__num_infectados = num_infectados
        self.__probabilidad_conexion_fisica = probabilidad_conexion_fisica

    # gets y sets de los atributos
    def set_num_ciudadanos(self, num_ciudadanos):
        self.__num_ciudadanos = num_ciudadanos

    def get_num_ciudadanos(self):
        return self.__num_ciudadanos
    
    def set_promedio_conexion_fisica(self, promedio_conexion_fisica):
        self.__promedio_conexion_fisica = promedio_conexion_fisica

    def get_promedio_conexion_fisica(self):
        return self.__promedio_conexion_fisica
    
    def set_enfermedad(self, enfermedad):
        self.__enfermedad = enfermedad

    def get_enfermedad(self):
        return self.__enfermedad
    
    def set_num_infectados(self, num_infectados):
        self.__num_infectados = num_infectados

    def get_num_infectados(self):
        return self.__num_infectados
    
    def set_probabilidad_conexion_fisica(self, probabilidad_conexion_fisica):
        self.__probabilidad_conexion_fisica = probabilidad_conexion_fisica

    def get_probabilidad_conexion_fisica(self):
        return self.__probabilidad_conexion_fisica
