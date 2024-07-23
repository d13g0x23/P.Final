from comunidad import Comunidad
from enfermedad import Enfermedad
import numpy as np
import pandas as pd


class Simulador():

    def __init__(self):
        self.__comunidad = None
        self.__reporte = None

    def set_comunidad(self, comunidad):
        if isinstance(comunidad, Comunidad):
            self.__comunidad = comunidad
        else:
            print("Error, el objeto entregado no es una comunidad")

    def simular(self, pasos):

        # Legibilidad
        infectados = self.__comunidad.get_infectados()
        prob_contacto = self.__comunidad.get_promedio_conexion_fisica()
        prob_estrecho = self.__comunidad.get_probabilidad_conexion_fisica()
        self.reporte_diario(0)

        # Simulación
        for paso in range(1, pasos+1):
            nuevos_infectados = []

            # Determinar los contactos de cada infectado
            for infectado in infectados:

                # Determinar si existe contacto fisico
                contacto_fisico = np.random.random() <= prob_contacto
                if contacto_fisico:

                    # Determinar si es contacto estrecho o no
                    contacto_estrecho = np.random.random() <= prob_estrecho
                    if contacto_estrecho:
                        contacto = self.buscar_estrecho(infectado)
                    else:
                        contacto = self.buscar_cualquiera(infectado)

                    # Determinamos si hubo contagio o no
                    contagio = self.determinar_infeccion(infectado, contacto)
                    # Si hubo contagio, se añade a los nuevos infectados
                    if contagio:
                        nuevos_infectados.append(contacto)

                # Progresar la enfermedad en cada infectado (excepto los nuevos)
                infectado.get_enfermedad().avanzar_dias()

            # Actualizamos los infectados, susceptibles y recuperados
            self.actualizar_ciudadanos(infectados, nuevos_infectados)

            # Reportar en la terminal
            self.reporte_diario(paso)
        self.guardar_reporte()

    def buscar_estrecho(self, infectado):

        # Obtener la familia del infectado
        id_familia = infectado.get_familia()
        familia = self.__comunidad.get_ciudadanos()[id_familia]

        # Si no tiene familia, no hubo contacto
        if len(familia) == 1:
            return None

        # Si tiene familia, se saca un contacto estrecho
        else:
            contacto = np.random.choice(familia)
            while contacto == infectado:
                contacto = np.random.choice(familia)
            return contacto

    def buscar_cualquiera(self, infectado):

        # Obtenemos todos los ciudadanos, en una lista de 1 dimension
        ciudadanos = self.__comunidad.get_ciudadanos().values()
        ciudadanos_plano = [c for familia in ciudadanos for c in familia]

        # Sacamos una persona aleatoria
        contacto = np.random.choice(ciudadanos_plano)
        while contacto == infectado:
            contacto = np.random.choice(ciudadanos_plano)

        return contacto

    def determinar_infeccion(self, infectado, contacto):

        # En caso de no tener familiares no hay contagio
        if contacto is None:
            return False

        prob_infeccion = infectado.get_enfermedad().get_infeccion_probable()

        # Si es que el contacto, no tiene el virus
        if contacto.get_enfermedad() is None:
            infectar = np.random.random() <= prob_infeccion
            if infectar:
                # Se crea un nuevo virus y se contagia
                prom_pasos = infectado.get_enfermedad().get_promedio_pasos()
                nuevo_virus = Enfermedad(prob_infeccion,
                                         prom_pasos,
                                         enfermo=True)
                contacto.set_enfermedad(nuevo_virus)
                return True
        return False

    def actualizar_ciudadanos(self, infectados, nuevos_infectados):

        # Obtener la lista inicial (del dia) de gente recuperada y susceptible
        recuperados = self.__comunidad.get_recuperados()
        susceptibles = self.__comunidad.get_susceptibles()

        # Revisamos si algún enfermo se recuperó
        for infectado in infectados:
            enfermo = infectado.get_enfermedad().get_enfermo()
            if not enfermo:
                recuperados.append(infectado)

        # Se quitan los recuperados de la lista de enfermos
        for recuperado in recuperados:
            if recuperado in infectados:
                infectados.remove(recuperado)

        # Sacamos los nuevos infectados de susceptibles, y lo añadimos a
        # infectados
        for infectado in nuevos_infectados:
            susceptibles.remove(infectado)
            infectados.append(infectado)

        # Actualizamos la comunidad
        self.__comunidad.set_infectados(infectados)
        self.__comunidad.set_recuperados(recuperados)
        self.__comunidad.set_susceptibles(susceptibles)

    def reporte_diario(self, paso):
        # Contar cuantos hay de cada grupo
        n_infectados = len(self.__comunidad.get_infectados())
        n_recuperados = len(self.__comunidad.get_recuperados())
        n_susceptibles = len(self.__comunidad.get_susceptibles())

        # Guardar en reporte
        self.__reporte["Dia"].append(paso)
        self.__reporte["Susceptibles"].append(n_susceptibles)
        self.__reporte["Infectados"].append(n_infectados)
        self.__reporte["Recuperados"].append(n_recuperados)

        print(f"Dia: {paso} - Susceptibles: {n_susceptibles} - "
              f"Recuperados: {n_recuperados} - Infectados: {n_infectados}")

    # Inicializa (o reinicia) la comunidad para una nueva simulación
    def inicializar_comunidad(self):

        self.__reporte = {"Dia": [],
                          "Susceptibles": [],
                          "Infectados": [],
                          "Recuperados": []}

        # Se obtienen para mejorar legibilidad
        susceptibles = self.__comunidad.get_susceptibles()
        inf_iniciales = self.__comunidad.get_num_infectados()
        p_infeccion = self.__comunidad.get_enfermedad().get_infeccion_probable()
        pasos = self.__comunidad.get_enfermedad().get_promedio_pasos()
        infectados = []

        # c representa a un ciudadano. Se enferma a n ciudadanos iniciales
        for c in np.random.choice(susceptibles, inf_iniciales, replace=False):
            c.set_enfermedad(Enfermedad(p_infeccion, pasos, enfermo=True))
            infectados.append(c)

        # Quitar a los enfermos de la lista de susceptibles
        for infectado in infectados:
            susceptibles.remove(infectado)

        # Actualizar comunidad
        self.__comunidad.set_infectados(infectados)
        self.__comunidad.set_susceptibles(susceptibles)

    def guardar_reporte(self):
        # Convertir diccionario a dataframe
        df = pd.DataFrame(self.__reporte)
        df.to_csv("./reporte_simulacion.csv", index=False)


# Para probar mas rápido
if __name__ == "__main__":

    # Generar la comunidad y la enfermedad
    covid = Enfermedad(infeccion_probable=0.8,
                       promedio_pasos=12)
    talca = Comunidad(num_ciudadanos=1000,
                      enfermedad=covid,
                      num_infectados=20,
                      num_familias=200,
                      promedio_conexion_fisica=0.3,
                      probabilidad_conexion_fisica=0.7)
    sim = Simulador()
    sim.set_comunidad(talca)
    sim.inicializar_comunidad()
    sim.simular(60)
