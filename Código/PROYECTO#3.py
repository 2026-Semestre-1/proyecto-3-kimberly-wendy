import tkinter as tk
import random
from tkinter import messagebox, scrolledtext

# ============================================#
#============== CLASE PARTIDO ================#
# ============================================#
"""
Nombre: Partido
Entrada: 2 selecciones,id_partido, equipo_1,equipo_2, fase fecha
Salida: Crea un partido nuevo
Restricciones:  Los equipos deben ser válidos y tener mínimo 11 jugadores
                Los goles inician en 0.
Objetivo: representar un partido entre dos selecciones
"""

class Partido:
    def __init__(self, id_partido, equipo_1, equipo_2, fase, fecha):
        self.id_partido = id_partido

        self.equipo_1 = equipo_1
        self.equipo_2 = equipo_2

        self.goles_equipo1 = 0
        self.goles_equipo2 = 0

        self.fase = fase
        self.fecha = fecha

        # Solo se usan cuando hay penales
        self.penales1 = 0
        self.penales2 = 0
        
        if equipo_1 == None or equipo_2 == None: #validar datos no vacios
            return
        if fase == "":
            return
        
    def simular(self):
        fuerza1 = self.equipo_1.fn_calcular_fuerza_equipo()
        fuerza2 = self.equipo_2.fn_calcular_fuerza_equipo()

        diferencia = fuerza1 - fuerza2

        if diferencia >= -15 and diferencia <= 15:
            self.goles_equipo1 = random.randint(0,4)
            self.goles_equipo2 = random.randint(0,4)

        elif diferencia > 15 and diferencia <= 30:
            self.goles_equipo1 = random.randint(1,5)
            self.goles_equipo2 = random.randint(0,4)

        elif diferencia > 30:
            self.goles_equipo1 = random.randint(2,7)
            self.goles_equipo2 = random.randint(0,3)

        elif diferencia >= -30:
            self.goles_equipo1 = random.randint(0,4)
            self.goles_equipo2 = random.randint(1,5)

        else:
            self.goles_equipo1 = random.randint(0,3)
            self.goles_equipo2 = random.randint(2,7)

        # Actualizar estadísticas de las selecciones
        self.equipo_1.fn_registrar_resultado(self.goles_equipo1,self.goles_equipo2,0,0)
        self.equipo_2.fn_registrar_resultado(self.goles_equipo2,self.goles_equipo1,0,0)
        
# Si es eliminatoria y hubo empate, ir a penales
        if self.fase != "Grupos":
            if self.goles_equipo1 == self.goles_equipo2:
                self.penales1 = random.randint(2,5)
                self.penales2 = random.randint(2,5)

                while self.penales1 == self.penales2:
                    self.penales1 = random.randint(2,5)
                    self.penales2 = random.randint(2,5)

    def generar_ganador(self):
        if self.goles_equipo1 > self.goles_equipo2:
            return self.equipo_1

        elif self.goles_equipo2 > self.goles_equipo1:
            return self.equipo_2

        else:
            if self.fase == "Grupos":
                return None
            elif self.penales1 > self.penales2:
                return self.equipo_1
            else:
                return self.equipo_2
        
    def mostrar_resultado(self):
        nombre1 = self.equipo_1.fn_nombre_del_pais()
        nombre2 = self.equipo_2.fn_nombre_del_pais()

        resultado = f"{nombre1} {self.goles_equipo1} - {self.goles_equipo2} {nombre2}"

        if self.fase != "Grupos":
            if self.goles_equipo1 == self.goles_equipo2:
                resultado += f" (Penales {self.penales1}-{self.penales2})"

        return resultado

# ============================================#
#============== CLASE GRUPO ==================#
# ============================================#
"""
Nombre: Grupo
Entrada: nombre del grupo
Salida: objeto Grupo
Restricciones: máximo 4 equipos por grupo
Objetivo: organizar selecciones en fase de grupos
    """
class Grupo:

    def __init__(self, nombre_grupo):
        self.__nombre_grupo = nombre_grupo
        self.__equipos = []
        self.__partidos = []
        

    def nombre_grupo(self):
        return self.__nombre_grupo

    def equipos(self):
        return self.__equipos

    def partidos(self):
        return self.__partidos

    def agregar_equipo(self, seleccion):
        if seleccion == None:
            return False
        if len(self.equipos) >= 4:
            return False
        self.__equipos = self.__equipos + [seleccion]
        return True


    def jugarPartidos(self):
        self.__partidos = []
        numero = 1

        for i in range(len(self.__equipos) - 1):
            for j in range(i + 1, len(self.__equipos)):
                partido = Partido(numero,self.__equipos[i],self.__equipos[j],"Grupos","")

                partido.simular()
                self.__partidos = self.__partidos + [partido]

                numero += 1

    def calcularTabla(self):
        tabla = []

        for equipo in self.__equipos:
            puntos = 0
            diferencia = equipo.fn_total_goles_favor() - equipo.fn_total_goles_contra()

            for partido in self.__partidos:
                ganador = partido.generar_ganador()

                if ganador == equipo:
                    puntos += 3

                elif ganador is None:
                    if partido.equipo_1 == equipo or partido.equipo_2 == equipo:
                        puntos += 1
            tabla = tabla + [[equipo, puntos, diferencia]]
        self.tabla = tabla
        return tabla
        
    
    def obtener_clasificados(self):
        # Calculamos la tabla primero
        tabla = self.calcularTabla()  # cada fila: [equipo, puntos, diferencia]

        cantidad = len(tabla) #contador

        for ronda in range(cantidad - 1): #recorrer varias veces
            for posicion in range(cantidad - 1 - ronda): #comparar vecinos
                equipo_actual = tabla[posicion]
                equipo_siguiente = tabla[posicion + 1]

                puntos_actual = equipo_actual[1]
                puntos_siguiente = equipo_siguiente[1]

                if puntos_actual < puntos_siguiente:  # Comparar primero por puntos
                    tabla[posicion], tabla[posicion + 1] = tabla[posicion + 1], tabla[posicion]

                # Si tienen mismos puntos, comparar diferencia de goles
                elif puntos_actual == puntos_siguiente:
                    diferencia_actual = equipo_actual[2]
                    diferencia_siguiente = equipo_siguiente[2]

                    if diferencia_actual < diferencia_siguiente:
                        tabla[posicion], tabla[posicion + 1] = tabla[posicion + 1], tabla[posicion]

        # Los dos primeros son los clasificados
        clasificados = [tabla[0][0], tabla[1][0]]
        return clasificados

    def mostrar_tabla(self):
        texto= ("=== " + self.__nombre_grupo + " ===") #titulo con nombre del grupo
            
        tabla = self.calcularTabla()#Calcular la tabla y ordenarla
        cantidad = len(tabla)

        for ronda in range(cantidad - 1):      #Ordenar la tabla por puntos y diferencia de goles
            for posicion in range(cantidad - 1 - ronda):    # Comparar equipos vecinos
                equipo_actual = tabla[posicion]
                equipo_siguiente = tabla[posicion + 1]

                puntos_actual = equipo_actual[1]
                puntos_siguiente = equipo_siguiente[1]

                if puntos_actual < puntos_siguiente:   # Ordenar por mayor cantidad de puntos
                    tabla[posicion], tabla[posicion + 1] = tabla[posicion + 1], tabla[posicion]

                elif puntos_actual == puntos_siguiente:   # Si empatan en puntos, ordenar por diferencia de goles
                    diferencia_actual = equipo_actual[2]
                    diferencia_siguiente = equipo_siguiente[2]

                    if diferencia_actual < diferencia_siguiente:
                        tabla[posicion], tabla[posicion + 1] = tabla[posicion + 1], tabla[posicion]

        # Mostrar cada equipo con su posición, puntos y diferencia
        posicion = 1
        for fila in tabla:
            equipo = fila[0]
            puntos = fila[1]
            diferencia = fila[2]
            texto += (str(posicion)+ ". "+ equipo.fn_nombre_del_pais()+ "  Pts:"+ str(puntos)+ "  DG:"+ str(diferencia)+ "\n")
            posicion += 1
        return texto

#===========================================
#==============CLASE FASE===================
#===========================================
"""
Nombre: Fase
Entradas: nombre_fase
Salidas: Crea una fase vacía,Representa una fase eliminatoria del torneo.
Restricciones: Debe existir al menos un partido.
"""
class Fase:
    def __init__(self, nombre_fase):
        self.nombre_fase = nombre_fase
        self.partidos = []

        if equipo1 == None:
            return
        if equipo2 == None:
            return

#N: registrar_juego
#E: equipo1 equipo2
#S: Agrega un partido a la fase.
#R: Los equipos deben existir.

    def registrar_juego(self, equipo1, equipo2):
        nuevo_id = len(self.partidos) + 1
        partido = Partido(nuevo_id, equipo1, equipo2, self.nombre_fase, "")

        self.partidos = self.partidos + [partido]


    def jugar_fase(self):
        for partido in self.partidos:
            partido.simular()

#N: mostrar_juegos
#Entradas:No recibe parámetros.
#S: Devuelve los resultados de todos los partidos.
#R:Los partidos deben estar simulados.

    def mostrar_juegos(self):
        texto = "=== " + self.nombre_fase + " ===\n"

        for partido in self.partidos:
            texto += partido.mostrar_resultado() + "\n"

        return texto


    def obtener_clasificados(self):
        clasificados = []

        for partido in self.partidos:
            ganador = partido.generar_ganador()
            if ganador is not None:
                clasificados = clasificados + [ganador]

        return clasificados
    
# ============================================#
#============== CLASE MUNDIAL ================#
# ============================================#
"""
Nombre: Mundial
Entradas:nombre,año
Salidas: Administra todo el torneo del mundial.
Restricciones:El nombre y el año deben ser válidos.
"""
class Mundial:
    def __init__(self, nombre, año):

        self.nombre = nombre
        self.año = año
        self.paises = []
        self.selecciones = []
        self.grupos = []
        self.fases = []
        self.campeon = None

    def registrar_pais(self, pais):
        existe = False
        
        for elemento in self.paises:
            if elemento == pais:
                existe = True
            
            if existe == False:
                self.paises = self.paises + [pais]

    def registrar_seleccion(self, seleccion):
        existe = False
        for elemento in self.selecciones:
            if elemento.fn_codigo_equipo() == seleccion.fn_codigo_equipo():
                existe = True

            if existe == False:
                self.selecciones = self.selecciones + [seleccion]

#N: crear_grupos
#E:cantidad_grupos
#S:Distribuye las selecciones en grupos.
#R:Debe existir la cantidad suficiente de selecciones.

    def crear_grupos(self, cantidad_grupos):
        self.grupos = []    # Reinicia la lista de grupos
        indice = 0

        for i in range(cantidad_grupos): # Crear cada grupo
            letra = chr(65 + i)

            grupo = Grupo("Grupo " + letra)
            cantidad = 0   

            while cantidad < 4 and indice < len(self.selecciones): # Cada grupo tendrá máximo 4 selecciones
                grupo.agregar_equipo(self.selecciones[indice])    # Agregar la selección al grupo
                indice += 1
                cantidad += 1

            self.grupos = self.grupos + [grupo]

    def jugar_fase_grupos(self):
        texto = "=========== FASE DE GRUPOS ===========\n\n"

        for grupo in self.grupos:
            grupo.jugarPartidos()
            grupo.calcularTabla()
            texto += grupo.mostrar_tabla()
            texto += "\n"

        return texto

#N:armar_fase_eliminatoria
#E:nombre_fase,clasificados
#S:Crea una nueva fase eliminatoria.
#R:Debe existir una cantidad par de equipos.

    def armar_fase_eliminatoria(self, nombre_fase, clasificados):
        fase = Fase(nombre_fase)
        i = 0

        while i < len(clasificados) - 1:
            fase.registrar_juego(clasificados[i],clasificados[i + 1])
            i += 2
        self.fases = self.fases + [fase]

        return fase

    def jugar_fase_eliminatoria(self, fase):
        fase.jugar_fase()
        return fase.obtener_clasificados()  #Retorna los equipos clasificados.

    def determinar_campeon(self): #Determina el campeón del torneo.
        clasificados = []

        for grupo in self.grupos:
            clasificados = clasificados + grupo.obtener_clasificados()

        while len(clasificados) > 1:
            if len(clasificados) == 16:
                nombre = "Octavos de Final"

            elif len(clasificados) == 8:
                nombre = "Cuartos de Final"

            elif len(clasificados) == 4:
                nombre = "Semifinales"

            else:
                nombre = "Final"

            fase = self.armar_fase_eliminatoria(nombre,clasificados)
            clasificados = self.jugar_fase_eliminatoria(fase)

        if len(clasificados) > 0:
            self.campeon = clasificados[0]

    def mostrar_tabla_general(self): # Devuelve la tabla general de todos los grupos.
        texto = "========== TABLAS DE POSICIONES ==========\n\n"

        for grupo in self.grupos:
            texto += grupo.mostrar_tabla()
            texto += "\n"
            
        return texto
    
#N: generar_reporte
#E: No recibe parámetros.
#S: Devuelve un reporte general del mundial.
#R: El torneo debe haberse ejecutado.

    def generar_reporte(self):
        texto = ""
        texto += "=====================================\n"
        texto += "      REPORTE DEL MUNDIAL\n"
        texto += "=====================================\n\n"

        texto += "Torneo: " + self.nombre + "\n" # Datos generales del torneo
        texto += "Año: " + str(self.año) + "\n\n"
        texto += self.mostrar_tabla_general()    # Agregar las tablas de todos los grupos
        texto += "\n"

        for fase in self.fases:   # Agregar los resultados de cada fase eliminatoria
            texto += fase.mostrar_juegos()
            texto += "\n"

        if self.campeon != None:  # Mostrar el campeno si ya existe
            texto += "\nCAMPEÓN DEL TORNEO\n"
            texto += self.campeon.fn_nombre_del_pais()
            texto += "\n"

        return texto






