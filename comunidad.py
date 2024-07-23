from enfermedad import Enfermedad
from ciudadano import Ciudadano
import pandas as pd
import random

class Comunidad:
    def __init__(self, num_ciudadanos, promedio_conexion_fisica,
                 enfermedad, num_infectados, num_familias,
                 probabilidad_conexion_fisica):
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
        self.__num_familias = num_familias
        self.cargar_ciudadanos_desde_csv("./nombres_apellidos.csv")

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

    def get_ciudadanos(self):
        return self.__ciudadanos

    def get_infectados(self):
        return self.__infectados

    def set_recuperados(self, recuperados):
        self.__recuperados = recuperados

    def get_recuperados(self):
        return self.__recuperados

    def crear_ciudadano(self, _id, nombre, apellido, familia):
        """
        Crea un nuevo ciudadano y lo agrega a la comunidad
        """
        # enfermedad = self.__enfermedad # Asigna la enfermedad definida para toda la comunidad
        ciudadano = Ciudadano(self, _id, nombre, apellido, familia)
        self.__susceptibles.append(ciudadano)

        # Agrupa por familia
        if familia in self.__ciudadanos:
            self.__ciudadanos[familia].append(ciudadano)
        else:
            self.__ciudadanos[familia] = [ciudadano]

        # Agrupa por ID
        # self.__ciudadanos[_id] = ciudadano

        return ciudadano

    def cargar_ciudadanos_desde_csv(self, archivo_csv):
        """
        Carga ciudadanos desde un archivo CSV y los agrega a la comunidad
        """
        self.__susceptibles = []
        self.__infectados = []
        self.__recuperados = []
        self.__ciudadanos = {}  # Diccionario para guardar los objetos tipo ciudadano
        df = pd.read_csv(archivo_csv)
        familias = [f"Familia_{i}" for i in range(1, self.__num_familias + 1)]

        for _id in range(1, self.__num_ciudadanos + 1):
            aux = df.sample()
            nombre = aux.to_numpy(str)[0][0]
            apellido = aux.to_numpy(str)[0][1]
            # apellido = row['apellido']
            familia = random.choice(familias)
            self.crear_ciudadano(_id, nombre, apellido, familia)
