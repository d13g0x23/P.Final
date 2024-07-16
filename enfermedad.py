class Enfermedad:
    def __init__(self, infeccion_probable, promedio_pasos, infeccion_estrecho):
        """
            infeccion_probable = Probaibilidad de infeccion de una persona (B)
            promedio_pasos = Son los DÍAS que esta CONTAGIADO o con la infección
            infeccion_estrecho = Probabilidad de infeccion a un contacto estrecho
        """
        self.__infeccion_probable = infeccion_probable # B (tasa de transmision modelo SIR)
        self.__promedio_pasos = promedio_pasos # Días que esta contagiado / Tasa de recuperación
        self.__infeccion_estrecho = infeccion_estrecho 

    
    # gets y sets de los atributos
    def set_infeccion_probable(self, infeccion_probable):
        self.__infeccion_probable = infeccion_probable
    
    def get_infeccion_probable(self):
        return self.__infeccion_probable
    
    def set_promedio_pasos(self, promedio_pasos):
        self.__promedio_pasos = promedio_pasos

    def get_promedio_pasos(self):
        return self.__promedio_pasos
    
    def set_infeccion_estrecho(self, infeccion_estrecho):
        self.__infeccion_estrecho = infeccion_estrecho

    def get_infeccion_estrecho(self):
        return self.__infeccion_estrecho
       