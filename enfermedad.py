class Enfermedad:
    def __init__(self, infeccion_probable, promedio_pasos, enfermo=False):
        """
            infeccion_probable = Probaibilidad de infeccion de una persona (B)
            promedio_pasos = Son los DÍAS que esta CONTAGIADO o con la infección
            infeccion_estrecho = Probabilidad de infeccion a un contacto estrecho
        """
        self.__infeccion_probable = infeccion_probable # B (tasa de transmision modelo SIR)
        self.__promedio_pasos = promedio_pasos # Días que esta contagiado / Tasa de recuperación
        self.__enfermo = enfermo
        self.__contador = promedio_pasos  # Empieza a contar hacia abajo

    # gets y sets de los atributos
    def get_infeccion_probable(self):
        return self.__infeccion_probable

    def get_enfermo(self):
        return self.__enfermo

    def get_promedio_pasos(self):
        return self.__promedio_pasos

    # Método para avanzar la infección y curar, si corresponde
    def avanzar_dias(self):
        self.__contador -= 1
        if self.__contador == 0:
            self.__enfermo = False
