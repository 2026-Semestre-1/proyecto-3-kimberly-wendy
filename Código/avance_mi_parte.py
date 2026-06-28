import tkinter as tk
import random
from tkinter import messagebox, scrolledtext

# =========================================================================#
# ========CLASE PAÍS=======================================================#
# =========================================================================#


"""nombree: Class Pais
entrada: codigoFifa, nombre del pais, continente, ranking fifa
salida: diferentes funcionalidaddes dependeindo que fn klamens
retricciones: los datos deben cumplir que el ranking sea entero"""
class Pais:
    def __init__(self, codigo_fifa, nombre, continente, ranking_fifa):



        #RECOMENDACIÓN DEL TUTOR A MARTA
        
        self.__codigo_fifa  = codigo_fifa
        self.__nombre       = nombre
        self.__continente   = continente
        self.__ranking_fifa = ranking_fifa


    def fn_codigo_fifa(self):
        return self.__codigo_fifa

    def fn_nombre(self):
        return self.__nombre

    def fn_continente(self):
        return self.__continente

    def fn_ranking_fifa(self):
        return self.__ranking_fifa

    def fn_cambiar_nombre_pais(self,nuevo_nombre):
        self.__nombre=nuevo_nombre

        
        
    def fn_mostrar_datos(self):
        return (f"[{self.__codigo_fifa}] {self.__nombre} "f"| Confederación: {self.__continente} "
                f"| Ranking FIFA: {self.__ranking_fifa}")#fcailidad al guardar yllamar

    def fn_actualizar_datos(self,nombre=None,continente=None,ranking_fifa=None):
        if nombre is not None:
            self.__nombre = nombre

        if continente is not None:
            self.__continente = continente
            
        if ranking_fifa is not None:
            self.__ranking_fifa = ranking_fifa
            
    def fn_para_pasar_archivo(self):#lienea d etexto
        return f"{self.__codigo_fifa},{self.__nombre},{self.__continente},{self.__ranking_fifa}"
        




# ==========================================================================================#
#======= CLASE PERSONA  ====================================================================#
# ==========================================================================================#
  
"""nombree: Class Persona
entrada: nombre , apellido, fecha de nacimento, y nacionalidad
salida: mostar los datos
retricciones: debe ser tTXT"""                 
class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha = fecha_nacimiento
        self.__nacionalidad = nacionalidad


    def fn_mostrar_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    def fn_mostrar_nombre_persona(self):
        return self.__nombre
    def fn_mostrar_apellido_persona(self):
        return self.__apellido
    def fn_mostrar_fecha_persona(self):
        return self.__fecha
    def fn_mostrar_nacionalidad(self):
        return self.__nacionalidad
        



        
    def fn_mostrar_datos(self):

        return (f"{self.__nombre} {self.__apellido} {self.__fecha} {self.__nacionalidad}") #tiene el fin de ser más facil de guardar



# ============================================================================================#
#==== H CLASE ENTRENADOR ==================================================================#
# ==========================================================================================#

"""nombree: Class Entrenador
entrada: nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia, sistema_juego
salida: diferentes funcionalidades dependeindo que fn llamens
retricciones: los datos deben cumplir que el  que experiencia sea en años enteros """
class Entrenador(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia, sistema_juego):
        super().__init__(nombre, apellido, fecha_nacimiento, nacionalidad)
        
        self.__licencia = licencia
        self.__experiencia = experiencia
        self.__sistema_juego = sistema_juego


    def fn_licencia_entrenador(self):
        return self.__licencia
    
    def fn_experiencia_entrenador(self):
        return self.__experiencia

    def fn_juego_entrenador(self):
        return self.__sistema_juego
    
    def fn_mostrar_datos_entrenador(self):
        datos=super().fn_mostrar_datos()
        return f"{datos} {self.__licencia} {self.__experiencia} {self.__sistema_juego}"


    
    def fn_actualizar_datos(self,licencia=None,experiencia=None,sistema=None):
        if licencia is not None:
            self.__licencia = licencia

        if experiencia is not None:
            self.__experiencia = experiencia

        if sistema is not None:
            self.__sistema_juego = sistema

    def fn_calcular_factor_entrenador(self):
        valor= self.__experiencia*4
        if valor>100:
            return 100
        return valor

    #no se si ace falta

    


# ==========================================================================================#
#======= H CLASE FUTBOLISTA ================================================================#
# ==========================================================================================#

"""nombree: Class Futbolista
entrada: self, nombre, apellido, fecha_nacimiento,nacionalidad,
 dorsal, posicion, velocidad, estratega, dominio_balon ,fuerza
salida: diferentes funcionalidades dependeindo que fn llamens
retricciones: los datos deben cumplir que el  que experiencia sea en años enteros  y el dorsal"""
class Futbolista(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento,nacionalidad,
                 dorsal, posicion, velocidad=None, estratega=None, dominio_balon=None, fuerza=None):
        
        super().__init__( nombre, apellido, fecha_nacimiento, nacionalidad)

        self.__dorsal = dorsal
        self.__posicion = posicion
        
        #se uraran durante el torneo
        self.__total_tarjetas_amarrillas =0
        self.__total_tarjetas_rojas = 0
        self.__goles = 0
        self.__asistencias = 0

        
        self.__velocidad     = velocidad     if velocidad     is not None else random.randint(1, 25)#porsi no asignan nada c++
        self.__estratega     = estratega     if estratega     is not None else random.randint(1, 25)
        self.__dominio_balon = dominio_balon if dominio_balon is not None else random.randint(1, 25)
        self.__fuerza_sub    = fuerza        if fuerza        is not None else random.randint(1, 25)
        
    def fn_puntaje_individual(self):
        return ( self.__velocidad +self.__estratega +self.__dominio_balon +self.__fuerza_sub )
    def fn_dorsal(self):
        return self.__dorsal
    def fn_posicion(self):
        return self.__posicion
    
    def fn_goles(self):
        return self.__goles
    def fn_asistencias(self):
        return self.__asistencias
    def fn_tarjetas_amarrillas(self):
        return self.__total_tarjetas_amarrillas
    def fn_tarjetas_rojas(self):
        return self.__total_tarjetas_rojas

    def fn_velocidad(self):
        return self.__velocidad
    def fn_estratega(self):
        return self.__estratega

    def fn_dominio_balon(self):
        return self.__dominio_balon

    def fn_fuerza_sub(self):
        return self.__fuerza_sub


    def actualizar_datos(self,dorsal=None, posicion=None, velocidad=None, estratega=None, dominio_balon=None, fuerza=None):
        

        if dorsal        is not None:
            self.__dorsal        = dorsal
        if posicion      is not None:
            self.__posicion      = posicion
        if velocidad     is not None:
            self.__velocidad     = velocidad
        if estratega     is not None:
            self.__estratega     = estratega
        if dominio_balon is not None:
            self.__dominio_balon = dominio_balon
        if fuerza        is not None:
            self.__fuerza_sub    = fuerza

    def fn_registrar_gol(self):
        self.__goles+=1

    def fn_registrar_asistencia(self):
        self.__asistencias+=1
    def fn_registrar_tarjeta(self,tipo):
        if tipo=="amarilla":
            self.__total_tarjetas_amarrillas +=1

        if tipo== "roja":
            self.__total_tarjetas_rojas+=1

            



    
    def fn_mostrar_datos_futbolista(self):
        datos_persona = super().fn_mostrar_datos()
        return (f"#{self.__dorsal} {datos_persona} "
                f"| Posicion: {self.__posicion} "
                f"| Puntaje: {self.fn_puntaje_individual()} "
                f"| Goles: {self.__goles} Asist: {self.__asistencias} "
                f"| Amarillas: {self.__total_tarjetas_amarrillas} "
                f"Rojas: {self.__total_tarjetas_rojas}")#orden
    

    
        
# ============================================#
#===========   CLASE SELECCION  ==============#
# ============================================#
"""nombree: Class Selección
entrada: codigo del país y el equipoi
salida: diferentes funcionalidades dependeindo que fn llamens
retricciones: deebn ser TXT"""               
class Seleccion:
    MAXIMO_JUGADORES=23
    MINIMO_JUGADORES=11
    def __init__(self,codigoEquipo,pais ):
        

        self.__codigo_equipo = codigoEquipo
        self.__pais = pais
        self.__jugadores=[]
        self.__cantidad_jugadores=0

        self.__entrenador= None
        
        self.__total_goles_favor = 0
        self.__total_goles_contra = 0
        self.__total_tarjetas_amarrillas = 0
        self.__total_tarjetas_rojas = 0
        self.__fuerza_equipo = 0
        
    def fn_codigo_equipo(self):
        return self.__codigo_equipo
    
    def fn_pais(self):
        return self.__pais
    
    def fn_entrenador(self):
        return self.__entrenador
    
    def fn_jugadores(self):
        return list(self.__jugadores)
    
    def fn_cantidad_jugadores(self):
        return self.__cantidad_jugadores
    
    def fn_nombre_del_pais(self):
        return self.__pais.fn_nombre()#clase pais
    
    def fn_total_tarjetas_amarillas(self):
        return  self.__total_tarjetas_amarrillas
    
    def fn_total_tarjetas_rojas(self):
        return  self.__total_tarjetas_rojas
    
    def fn_total_goles_favor(self):
        return self.__total_goles_favor
    
    def fn_total_goles_contra(self):
        return self.__total_goles_contra

    def fn_fuerza_equipo(self):
        return self.__fuerza_equipo

    
    def fn_mostrar_datos(self):
        if self.__entrenador is not None:
            nombre_dt = self.__entrenador.fn_mostrar_nombre_completo()
        else:
            nombre_dt = "Sin asignar"

        lineas = [
            f"=== Selección: {self.__pais.fn_nombre()} [{self.__codigo_equipo}] ===",
            f"Entrenador: {nombre_dt}",
            f"Fuerza del equipo: {self.__fuerza_equipo:.1f}",
            f"Jugadores convocados ({self.__cantidad_jugadores}):"
        ]

        for jugador in self.__jugadores:
            lineas = lineas + ["  " + jugador.fn_mostrar_nombre_completo()]

        return "\n".join(lineas)


    
    def fn_agregar_jugador(self,futbolista):
        if self.__cantidad_jugadores >= self.MAXIMO_JUGADORES:
            return False

        self.__jugadores = self.__jugadores + [futbolista]
        self.__cantidad_jugadores += 1
        self.__recalcular_fuerza()#creo despues
        return True


    def fn_eliminar_jugador(self,dorsal):
        lista_nueva=[]
        encontrado=False

        for jugador in self.__jugadores:
            if jugador.fn_dorsal()==dorsal and not encontrado:
                encontrado=True
            else:
                lista_nueva= lista_nueva+[jugador]


        if encontrado:#si es verda
            self.__jugadores=lista_nueva
            self.__cantidad_jugadores-=1
            self.__recalcular_fuerza()#funcion despues definire

    def fn_asignar_entrenador(self,entrenador):
        self.__entrenador=entrenador
        self.__recalcular_fuerza()

    def fn_registrar_resultado(self,goles_favor,goles_contra,tarjetas_amarrillas,tarjetas_rojas):
        
        self.__total_goles_favor += goles_favor
        self.__total_goles_contra += goles_contra
        self.__total_tarjetas_amarrillas +=tarjetas_amarrillas
        self.__total_tarjetas_rojas+=tarjetas_rojas


    def __recalcular_fuerza(self):
        copia=list(self.__jugadores)
        total= self.__cantidad_jugadores
        pasada=0

        while pasada< total-1:
            posicion=0
            while posicion< total-1-pasada:
                puntaje_actual =copia[posicion].fn_puntaje_individual()#Futbolista
                puntaje_siguiente=copia[posicion+1].fn_puntaje_individual()
                if puntaje_actual<puntaje_siguiente:
                    copia[posicion],copia[posicion + 1] = copia[posicion + 1], copia[posicion]

                posicion+=1
            pasada+=1

        cuantos_titulares = 11 if total >= 11 else total
        suma_puntajes=0
        actual=0
        while actual<cuantos_titulares:
            suma_puntajes+= copia[actual].fn_puntaje_individual()
            actual+=1

        promedio_titulares = suma_puntajes / cuantos_titulares if cuantos_titulares > 0 else 0

        if self.__entrenador is not None:
            factor_entrenador= self.__entrenador.fn_calcular_factor_entrenador()#en cllas entrenador ya s ecaulta se mamnda nuero
        else:
            factor_entrenador=0

        ranking_bruto=self.__pais.fn_ranking_fifa()

        factor_ranking= 100-ranking_bruto
        if factor_ranking<0:
            factor_ranking=0
        self.__fuerza_equipo=((promedio_titulares * 0.6) +(factor_entrenador  * 0.25) +(factor_ranking * 0.15))
        #ya se calculo dout

    def fn_calcular_fuerza_equipo(self):
        self.__recalcular_fuerza()
        return self.__fuerza_equipo
    
    def fn_valida_para_jugar(self):
        tiene_entrenador  =self.__entrenador is not None #funcionan igaul qu el if estoy usando modo c++
        tiene_once =self.__cantidad_jugadores >= self.MINIMO_JUGADORES
        return tiene_entrenador and tiene_once
    
        


