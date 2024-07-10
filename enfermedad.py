class Enfermedad:
    def __init__(self, infeccion_probable, promedio_pasos, infeccion_estrecho):
        """
            infeccion_probable = Probaibilidad de infeccion de una persona (B)
            promedio_pasos = Días con la infección
            infeccion_estrecho = Probabilidad de infeccion a un contacto estrecho
            tasarecuperacion = Tasa en que un ciudadano se recupera de la enfermedad
            nombre_enfermedad = Nombre de la enfermedad :v
        """
        self.__infeccion_probable = infeccion_probable 
        self.__promedio_pasos = promedio_pasos 
        self.__infeccion_estrecho = infeccion_estrecho 
        self.__tasarecuperacion = None 
        self.__nombre_enfermedad = None
    
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
    
    def set_tasarecuperacion(self, tasarecuperacion):
        self.__tasarecuperacion = tasarecuperacion

    def get_tasarecuperacion(self):
        return self.__tasarecuperacion
    
    def set_nombre_enfermedad(self, nombre_enfermedad):
        self.__nombre_enfermedad = nombre_enfermedad

    def get_nombre_enfermedad(self):
        return self.__nombre_enfermedad
