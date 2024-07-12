from comunidad import Comunidad
from enfermedad import Enfermedad
from ciudadano import Ciudadano

class Simulador:
    def __init__(self, enfermedad, comunidad, dias_simulacion):
        self.__enfermedad = enfermedad
        self.__comunidad = comunidad
        self.__dias_simulacion = dias_simulacion
        self.__dias_transcurridos = 0

    def get_dias_simulacion(self):
        return self.__dias_simulacion
    
    def get_dias_transcurridos(self):
        return self.__dias_transcurridos
    
    def avanzar_dia(self):
        """
        Avanza un día en la simulación:
        1. Actualiza el estado de todos los ciudadanos en la comunidad.
        2. Realiza las acciones necesarias para simular la propagación de la enfermedad.
        """
        for ciudadano in self.__comunidad.get_susceptibles():
            ciudadano.actualizar_estado()
        
        for ciudadano in self.__comunidad.get_infectados():
            ciudadano.actualizar_estado()
        
        # Realizar acciones de contagio basadas en contactos estrechos o aleatorios
        self.__comunidad.agrupar_y_contagiar()
        
        self.__dias_transcurridos += 1

    def ejecutar_simulacion(self):
        """
        Ejecuta la simulación durante el número especificado de días.
        """
        for dia in range(self.__dias_simulacion):
            self.avanzar_dia()
            print(f"Día {self.__dias_transcurridos}: Infectados {len(self.__comunidad.get_infectados())}, Recuperados {len(self.__comunidad.get_recuperados())}")
    
    def recuperar_ciudadano(self, comunidad):
        for ciudadano in comunidad:
            if ciudadano.get_estado() == "I":
                ciudadano.rescatar_ciudadano()
