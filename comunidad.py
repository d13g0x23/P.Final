from enfermedad import Enfermedad
from ciudadano import Ciudadano

class Comunidad:
    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica):
        """
            num_ciudadanos = Población de ciudadanos
            promedio_conexion_fisica = Personas que ve al día
            enfermedad = Nombre de la enfermedad :v
            num_infectados = Población de infectados iniciales
            probabilidad_conexion_fisica = Probabiidad de que se junte con más personas
            susceptibles = Lista de ciudadanos susceptibles
            infectados = Lista de ciudadanoos infectados
            recuperados = Lista de ciudadanos recuperados
        """
        self.__num_ciudadanos = num_ciudadanos # N (Población modelo SIR)
        self.__promedio_conexion_fisica = promedio_conexion_fisica 
        self.__enfermedad = enfermedad 
        self.__num_infectados = num_infectados 
        self.__probabilidad_conexion_fisica = probabilidad_conexion_fisica 
        self.__susceptibles = []
        self.__infectados = []
        self.__recuperados = []


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
    
    def set_susceptibles(self, susceptibles):
        self.__susceptibles = susceptibles

    def get_susceptibles(self):
        return self.__susceptibles
    
    def set_infectados(self, infectados):
        self.__infectados = infectados

    def get_infectados(self):
        return self.__infectados
    
    def set_recuperados(self, recuperados):
        self.__recuperados = recuperados

    def get_recuperados(self):
        return self.__recuperados

    # Métodos para la clase comunidad
    def bicho_raro(self, enfermedad): # Asigna una instancia de la clase Enfermedad al atributo self.__enfermedad
        if isinstance(enfermedad, Enfermedad):
            self.__enfermedad = enfermedad
        else:
            print("Error: El objeto no es una instancia de Enfermedad")
