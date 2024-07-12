from enfermedad import Enfermedad
from ciudadano import Ciudadano
import pandas as pd
import random

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
        self.__ciudadanos = {} # Diccionario para mantener a todos los ciudadanos


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

    def crear_ciudadano(self, _id, nombre, apellido, familia):
        """
        Crea un nuevo ciudadano y lo agrega a la comunidad
        """
        enfermedad = self.__enfermedad # Asigna la enfermedad definida para toda la comunidad
        ciudadano = Ciudadano(self, _id, nombre, apellido, familia, enfermedad)
        self.__susceptibles.append(ciudadano)

        # Agrupa por familia
        if familia in self.__ciudadanos:
            self.__ciudadanos[familia].append(ciudadano)
        else:
            self.__ciudadanos[familia] = [ciudadano]

        # Agrupa por ID
        self.__ciudadanos[_id] = ciudadano

        return ciudadano
    
    def cargar_ciudadanos_desde_csv(self, archivo_csv, num_familias):
        """
        Carga ciudadanos desde un archivo CSV y los agrega a la comunidad
        """
        df = pd.read_csv(archivo_csv)
        familias = [f"Familia_{i}" for i in range(1, num_familias + 1)]

        for idx, row in df.iterrows():
            if idx >= self.__num_ciudadanos:
                break
            _id = idx + 1
            nombre = row['nombre']
            apellido = row['apellido']
            familia = random.choice(familias)
            self.crear_ciudadano(_id, nombre, apellido, familia)
    
    def contagiar_en_familia(self, familia):
        """
        Intenta contagiar a todos los ciudadanos de una familia específica
        """
        ciudadanos_en_familia = self.__ciudadanos.get(familia, [])
        
        for ciudadano in ciudadanos_en_familia:
            if ciudadano.get_estado() == "S":
                if self.__probabilidad_conexion_fisica >= random.random():
                    ciudadano.infectar()
                    print(f"{ciudadano.get_nombre()} {ciudadano.get_apellido()} ha sido contagiado en la familia {familia}")

    def contagiar_por_id(self, ciudadano_id):
        """
        Intenta contagiar a un ciudadano por su ID
        """
        ciudadano = self.__ciudadanos.get(ciudadano_id)
        if ciudadano and ciudadano.get_estado() == "S":
            if self.__probabilidad_conexion_fisica >= random.random():
                ciudadano.infectar()
                print(f"{ciudadano.get_nombre()} {ciudadano.get_apellido()} ha sido contagiado por ID {ciudadano_id}")

    def determinar_contacto_estrecho(self, ciudadano1, ciudadano2):
        """
        Determina si dos ciudadanos tienen un contacto estrecho basado en promedio_pasos y prom_conexion_fisica
        """
        prom_conexion_fisica = self.get_promedio_conexion_fisica()

        if prom_conexion_fisica >= random.random():
            return True
        else:
            return False
        
    def agrupar_y_contagiar(self):
        """
        Agrupa y contagia a los ciudadanos susceptibles basado en contactos estrechos
        """
        for familia, ciudadanos in self.__ciudadanos.items():
            for ciudadano in ciudadanos:
                if ciudadano.get_estado() == "S":
                    for otro_ciudadano in ciudadanos:
                        if otro_ciudadano != ciudadano and self.determinar_contacto_estrecho(ciudadano, otro_ciudadano):
                            ciudadano.infectar()
                            print(f"{ciudadano.get_nombre()} {ciudadano.get_apellido()} ha sido contagiado en la familia {familia}")
                            break # Contagia solo a uno por ciclo

        # Contagia al azar si no hubo contacto estrecho
        for ciudadano in self.__susceptibles:
            if ciudadano.get_estado() == "S":
                if self.__probabilidad_conexion_fisica >= random.random():
                    ciudadano.infectar()
                    print(f"{ciudadano.get_nombre()} {ciudadano.get_apellido()} ha sido contagiado al azar")
