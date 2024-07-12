from comunidad import Comunidad
from enfermedad import Enfermedad
from ciudadano import Ciudadano

class Simulador:
    def __init__(self, enfermedad, comunidad, dias_simulacion, dias_transcurridos):
        self.__enfermedad = enfermedad
        self.__comunidad = comunidad
        self.__dias_simulacion = dias_simulacion # Para mostrar en la interfaz
        self.__dias_transcurridos = 0

    def get_dias_simulacion(self):
        return self.__dias_simulacion
    
    def get_dias_transcurridos(self):
        return self.__dias_transcurridos
    
    def pasan_dias_transcurridos(self):
        self.__dias_transcurridos += 1

    def recuperar_ciudadano(self, comunidad):
        for ciudadano in comunidad:
            if ciudadano.get_estado() == "I":
                ciudadano.rescatar_ciudadano()

