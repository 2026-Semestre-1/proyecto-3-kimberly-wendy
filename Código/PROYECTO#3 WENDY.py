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


# Nombre: fn_codigo_fifa
# Entradas: Ninguna.
# Salidas: Devuelve el código FIFA del país.
# Restricciones: El objeto debe estar inicializado.
    def fn_codigo_fifa(self):
        return self.__codigo_fifa






# Nombre: fn_nombre
# Entradas: Ninguna.
# Salidas: Devuelve el nombre del país.
# Restricciones: El objeto debe estar inicializado.  

    def fn_nombre(self):
        return self.__nombre




# Nombre: fn_ranking_fifa
# Entradas: Ninguna.
# Salidas: Devuelve el ranking FIFA del país.
# Restricciones: El objeto debe estar inicializado.   

    def fn_continente(self):
        return self.__continente





# Nombre: fn_ranking_fifa
# Entradas: Ninguna.
# Salidas: Devuelve el ranking FIFA del país.
# Restricciones: El objeto debe estar inicializado.
    



    def fn_ranking_fifa(self):
        return self.__ranking_fifa

# Nombre: fn_cambiar_nombre_pais
# Entradas: nuevo_nombre (cadena de texto).
# Salidas: Actualiza el nombre del país.
# Restricciones: El nuevo nombre no debe estar vacío.

    def fn_cambiar_nombre_pais(self,nuevo_nombre):
        self.__nombre=nuevo_nombre





# Nombre: fn_mostrar_datos
# Entradas: Ninguna.
# Salidas: Devuelve una cadena con los datos del país.
# Restricciones: El objeto debe contener información válida.        
        
    def fn_mostrar_datos(self):
        return (f"[{self.__codigo_fifa}] {self.__nombre} "f"| Confederación: {self.__continente} "
                f"| Ranking FIFA: {self.__ranking_fifa}")#fcailidad al guardar yllamar




# Nombre: fn_actualizar_datos
# Entradas: nombre, continente y ranking_fifa.
# Salidas: Actualiza los datos del país.
# Restricciones: El ranking debe ser un entero válido.


    def fn_actualizar_datos(self,nombre=None,continente=None,ranking_fifa=None):
        if nombre is not None:
            self.__nombre = nombre

        if continente is not None:
            self.__continente = continente
            
        if ranking_fifa is not None:
            self.__ranking_fifa = ranking_fifa

            

# Nombre: fn_para_pasar_archivo
# Entradas: Ninguna.
# Salidas: Devuelve una línea de texto lista para guardar en un archivo.
# Restricciones: Los datos del país deben estar inicializados.           
            
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
# Nombre: fn_mostrar_nombre_completo
# Entradas: Ninguna.
# Salidas: Devuelve el nombre completo de la persona.
# Restricciones: El objeto debe estar inicializado.

    def fn_mostrar_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"


# Nombre: fn_mostrar_nombre_persona
# Entradas: Ninguna.
# Salidas: Devuelve el nombre de la persona.
# Restricciones: El objeto debe estar inicializado.


    def fn_mostrar_nombre_persona(self):
        return self.__nombre


# Nombre: fn_mostrar_apellido_persona
# Entradas: Ninguna.
# Salidas: Devuelve el apellido de la persona.
# Restricciones: El objeto debe estar inicializado.
    def fn_mostrar_apellido_persona(self):
        return self.__apellido


# Nombre: fn_mostrar_fecha_persona
# Entradas: Ninguna.
# Salidas: Devuelve la fecha de nacimiento.
# Restricciones: El objeto debe estar inicializado.
    def fn_mostrar_fecha_persona(self):
        return self.__fecha



# Nombre: fn_mostrar_nacionalidad
# Entradas: Ninguna.
# Salidas: Devuelve la nacionalidad.
# Restricciones: El objeto debe estar inicializado.
    def fn_mostrar_nacionalidad(self):
        return self.__nacionalidad




        
# Nombre: fn_mostrar_datos
# Entradas: Ninguna.
# Salidas: Devuelve una cadena con todos los datos de la persona.
# Restricciones: Los datos deben existir.
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



# Nombre: fn_licencia_entrenador
# Entradas: Ninguna.
# Salidas: Devuelve la licencia del entrenador.
# Restricciones: El objeto debe estar inicializado.


    def fn_licencia_entrenador(self):
        return self.__licencia


# Nombre: fn_experiencia_entrenador
# Entradas: Ninguna.
# Salidas: Devuelve los años de experiencia.
# Restricciones: El objeto debe estar inicializado.

    def fn_experiencia_entrenador(self):
        return self.__experiencia


# Nombre: fn_juego_entrenador
# Entradas: Ninguna.
# Salidas: Devuelve el sistema de juego del entrenador.
# Restricciones: El objeto debe estar inicializado.

    def fn_juego_entrenador(self):
        return self.__sistema_juego


# Nombre: fn_mostrar_datos_entrenador
# Entradas: Ninguna.
# Salidas: Devuelve una cadena con toda la información del entrenador.
# Restricciones: Los datos deben existir.    
    def fn_mostrar_datos_entrenador(self):
        datos=super().fn_mostrar_datos()
        return f"{datos} {self.__licencia} {self.__experiencia} {self.__sistema_juego}"



# Nombre: fn_actualizar_datos
# Entradas: licencia (texto), experiencia (entero), sistema (texto).
# Salidas: Actualiza los datos del entrenador.
# Restricciones: La experiencia debe ser un entero válido.

    
    def fn_actualizar_datos(self,licencia=None,experiencia=None,sistema=None):
        if licencia is not None:
            self.__licencia = licencia

        if experiencia is not None:
            self.__experiencia = experiencia

        if sistema is not None:
            self.__sistema_juego = sistema


            
# Nombre: fn_calcular_factor_entrenador
# Entradas: Ninguna.
# Salidas: Devuelve el factor del entrenador según su experiencia.
# Restricciones: La experiencia debe ser mayor o igual a cero.
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

# Nombre: fn_puntaje_individual
# Entradas: Ninguna.
# Salidas: Devuelve el puntaje total del jugador.
# Restricciones: Los atributos deben estar inicializados.

        
    def fn_puntaje_individual(self):
        return ( self.__velocidad +self.__estratega +self.__dominio_balon +self.__fuerza_sub )

# Nombre: fn_dorsal
# Entradas: Ninguna.
# Salidas: Devuelve el dorsal del jugador.
# Restricciones: El objeto debe estar inicializado.
    def fn_dorsal(self):
        return self.__dorsal


# Nombre: fn_posicion
# Entradas: Ninguna.
# Salidas: Devuelve la posición del jugador.
# Restricciones: El objeto debe estar inicializado.

    def fn_posicion(self):
        return self.__posicion


# Nombre: fn_goles
# Entradas: Ninguna.
# Salidas: Devuelve la cantidad de goles.
# Restricciones: El objeto debe estar inicializado.
    def fn_goles(self):
        return self.__goles


# Nombre: fn_asistencias
# Entradas: Ninguna.
# Salidas: Devuelve la cantidad de asistencias.
# Restricciones: El objeto debe estar inicializado.
    def fn_asistencias(self):
        return self.__asistencias


# Nombre: fn_tarjetas_amarrillas
# Entradas: Ninguna.
# Salidas: Devuelve la cantidad de tarjetas amarillas.
# Restricciones: El objeto debe estar inicializado.
    def fn_tarjetas_amarrillas(self):
        return self.__total_tarjetas_amarrillas


# Nombre: fn_tarjetas_rojas
# Entradas: Ninguna.
# Salidas: Devuelve la cantidad de tarjetas rojas.
# Restricciones: El objeto debe estar inicializado.
    def fn_tarjetas_rojas(self):
        return self.__total_tarjetas_rojas


# Nombre: fn_velocidad
# Entradas: Ninguna.
# Salidas: Devuelve la velocidad del jugador.
# Restricciones: El objeto debe estar inicializado.
    def fn_velocidad(self):
        return self.__velocidad

# Nombre: fn_estratega
# Entradas: Ninguna.
# Salidas: Devuelve el atributo estratega.
# Restricciones: El objeto debe estar inicializado.
    def fn_estratega(self):
        return self.__estratega


# Nombre: fn_dominio_balon
# Entradas: Ninguna.
# Salidas: Devuelve el dominio de balón.
# Restricciones: El objeto debe estar inicializado.

    def fn_dominio_balon(self):
        return self.__dominio_balon

# Nombre: fn_fuerza_sub
# Entradas: Ninguna.
# Salidas: Devuelve el atributo fuerza.
# Restricciones: El objeto debe estar inicializado.

    def fn_fuerza_sub(self):
        return self.__fuerza_sub

# Nombre: actualizar_datos
# Entradas: dorsal (entero), posicion (texto), velocidad (entero), estratega (entero), dominio_balon (entero), fuerza (entero).
# Salidas: Actualiza los datos del futbolista.
# Restricciones: Los valores deben ser válidos.

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


# Nombre: fn_registrar_gol
# Entradas: Ninguna.
# Salidas: Incrementa en uno la cantidad de goles.
# Restricciones: El objeto debe estar inicializado.

    def fn_registrar_gol(self):
        self.__goles+=1

        
# Nombre: fn_registrar_asistencia
# Entradas: Ninguna.
# Salidas: Incrementa en uno la cantidad de asistencias.
# Restricciones: El objeto debe estar inicializado.
    def fn_registrar_asistencia(self):
        self.__asistencias+=1


# Nombre: fn_registrar_tarjeta
# Entradas: tipo (texto).
# Salidas: Registra una tarjeta amarilla o roja.
# Restricciones: El tipo debe ser "amarilla" o "roja".
    def fn_registrar_tarjeta(self,tipo):
        if tipo=="amarilla":
            self.__total_tarjetas_amarrillas +=1

        if tipo== "roja":
            self.__total_tarjetas_rojas+=1

            


# Nombre: fn_mostrar_datos_futbolista
# Entradas: Ninguna.
# Salidas: Devuelve una cadena con toda la información del futbolista.
# Restricciones: Los datos del jugador deben existir.
    
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

# Nombre: fn_codigo_equipo
# Entradas: Ninguna.
# Salidas: Devuelve el código de la selección.
# Restricciones: El objeto debe estar inicializado.
        
    def fn_codigo_equipo(self):
        return self.__codigo_equipo


    
# Nombre: fn_pais
# Entradas: Ninguna.
# Salidas: Devuelve el objeto País asociado.
# Restricciones: El objeto debe estar inicializado.    
    def fn_pais(self):
        return self.__pais


# Nombre: fn_entrenador
# Entradas: Ninguna.
# Salidas: Devuelve el entrenador asignado.
# Restricciones: El objeto debe estar inicializado.

    def fn_entrenador(self):
        return self.__entrenador

    
# Nombre: fn_jugadores
# Entradas: Ninguna.
# Salidas: Devuelve la lista de jugadores.
# Restricciones: El objeto debe estar inicializado.
    def fn_jugadores(self):
        return list(self.__jugadores)


# Nombre: fn_cantidad_jugadores
# Entradas: Ninguna.
# Salidas: Devuelve la cantidad de jugadores registrados.
# Restricciones: El objeto debe estar inicializado.
    def fn_cantidad_jugadores(self):
        return self.__cantidad_jugadores


# Nombre: fn_nombre_del_pais
# Entradas: Ninguna.
# Salidas: Devuelve el nombre del país de la selección.
# Restricciones: Debe existir un país asociado.   
    def fn_nombre_del_pais(self):
        return self.__pais.fn_nombre()#clase pais


# Nombre: fn_total_tarjetas_amarillas
# Entradas: Ninguna.
# Salidas: Devuelve el total de tarjetas amarillas.
# Restricciones: El objeto debe estar inicializado.
    def fn_total_tarjetas_amarillas(self):
        return  self.__total_tarjetas_amarrillas


# Nombre: fn_total_tarjetas_rojas
# Entradas: Ninguna.
# Salidas: Devuelve el total de tarjetas rojas.
# Restricciones: El objeto debe estar inicializado.
    def fn_total_tarjetas_rojas(self):
        return  self.__total_tarjetas_rojas



# Nombre: fn_total_goles_favor
# Entradas: Ninguna.
# Salidas: Devuelve los goles a favor.
# Restricciones: El objeto debe estar inicializado.  
    def fn_total_goles_favor(self):
        return self.__total_goles_favor



# Nombre: fn_total_goles_contra
# Entradas: Ninguna.
# Salidas: Devuelve los goles en contra.
# Restricciones: El objeto debe estar inicializado.
    def fn_total_goles_contra(self):
        return self.__total_goles_contra


# Nombre: fn_fuerza_equipo
# Entradas: Ninguna.
# Salidas: Devuelve la fuerza del equipo.
# Restricciones: El objeto debe estar inicializado.
    def fn_fuerza_equipo(self):
        return self.__fuerza_equipo



# Nombre: fn_mostrar_datos
# Entradas: Ninguna.
# Salidas: Devuelve una cadena con la información de la selección.
# Restricciones: Deben existir los datos de la selección.
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


# Nombre: fn_agregar_jugador
# Entradas: futbolista (objeto Futbolista).
# Salidas: Agrega un jugador a la selección.
# Restricciones: La selección no debe superar los 23 jugadores.
    
    def fn_agregar_jugador(self,futbolista):
        if self.__cantidad_jugadores >= self.MAXIMO_JUGADORES:
            return False

        self.__jugadores = self.__jugadores + [futbolista]
        self.__cantidad_jugadores += 1
        self.__recalcular_fuerza()#creo despues
        return True

# Nombre: fn_eliminar_jugador
# Entradas: dorsal (entero).
# Salidas: Elimina un jugador de la selección.
# Restricciones: El dorsal debe existir.
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


# Nombre: fn_asignar_entrenador
# Entradas: entrenador (objeto Entrenador).
# Salidas: Asigna un entrenador a la selección.
# Restricciones: El entrenador debe existir.
    def fn_asignar_entrenador(self,entrenador):
        self.__entrenador=entrenador
        self.__recalcular_fuerza()


        
# Nombre: fn_registrar_resultado
# Entradas: goles_favor (entero), goles_contra (entero), tarjetas_amarrillas (entero), tarjetas_rojas (entero).
# Salidas: Actualiza las estadísticas de la selección.
# Restricciones: Todos los valores deben ser enteros.
    def fn_registrar_resultado(self,goles_favor,goles_contra,tarjetas_amarrillas,tarjetas_rojas):
        
        self.__total_goles_favor += goles_favor
        self.__total_goles_contra += goles_contra
        self.__total_tarjetas_amarrillas +=tarjetas_amarrillas
        self.__total_tarjetas_rojas+=tarjetas_rojas

# Nombre: __recalcular_fuerza
# Entradas: Ninguna.
# Salidas: Recalcula la fuerza de la selección.
# Restricciones: Deben existir jugadores registrados.
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

        
# Nombre: fn_calcular_fuerza_equipo
# Entradas: Ninguna.
# Salidas: Devuelve la fuerza actual de la selección.
# Restricciones: El objeto debe estar inicializado.
    def fn_calcular_fuerza_equipo(self):
        self.__recalcular_fuerza()
        return self.__fuerza_equipo


# Nombre: fn_valida_para_jugar
# Entradas: Ninguna.
# Salidas: Indica si la selección puede participar.
# Restricciones: Debe tener entrenador y al menos 11 jugadores.
    def fn_valida_para_jugar(self):
        tiene_entrenador  =self.__entrenador is not None #funcionan igaul qu el if estoy usando modo c++
        tiene_once =self.__cantidad_jugadores >= self.MINIMO_JUGADORES
        return tiene_entrenador and tiene_once
    
        




# ============================================#
#============== CLASE PARTIDO ================#
# ============================================#
""" Nombre: Partido
 Entradas: Id del partido, dos selecciones, la fase y la fecha.
 Salidas: Crea un objeto encargado de representar un partido del mundial.
 Restricciones: Las selecciones deben existir y pertenecer al mundial."""

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


# Nombre: simular
# Entradas: Ninguna.
# Salidas: Simula el resultado del partido.
# Restricciones: Ambos equipos deben estar preparados para jugar.
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

                    
# Nombre: generar_ganador
# Entradas: Ninguna.
# Salidas: Devuelve el equipo ganador o None si hay empate en grupos.
# Restricciones: El partido debe haber sido simulado.

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


# Nombre: mostrar_resultado
# Entradas: Ninguna.
# Salidas: Devuelve una cadena con el marcador del partido.
# Restricciones: El partido debe haber sido simulado.
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
""" Nombre: Grupo
 Entradas: Nombre del grupo.
 Salidas: Crea un grupo donde se almacenan las selecciones y los partidos.
 Restricciones: Un grupo solo puede contener un máximo de cuatro selecciones."""

class Grupo:

    def __init__(self, nombre_grupo):
        self.__nombre_grupo = nombre_grupo
        self.__equipos = []
        self.__partidos = []
        
# Nombre: nombre_grupo
# Entradas: Ninguna.
# Salidas: Devuelve el nombre del grupo.
# Restricciones: El objeto debe estar inicializado.
    def nombre_grupo(self):
        return self.__nombre_grupo

# Nombre: equipos
# Entradas: Ninguna.
# Salidas: Devuelve la lista de equipos.
# Restricciones: El objeto debe estar inicializado.


    def equipos(self):
        return self.__equipos


    
# Nombre: partidos
# Entradas: Ninguna.
# Salidas: Devuelve la lista de partidos.
# Restricciones: El objeto debe estar inicializado.
    def partidos(self):
        return self.__partidos



# Nombre: agregar_equipo
# Entradas: seleccion (objeto Selección).
# Salidas: Agrega una selección al grupo.
# Restricciones: El grupo puede tener máximo cuatro selecciones.
    def agregar_equipo(self, seleccion):
        if len(self.__equipos) >= 4:
            return False
        self.__equipos = self.__equipos + [seleccion]
        return True

# Nombre: jugarPartidos
# Entradas: Ninguna.
# Salidas: Simula todos los partidos del grupo.
# Restricciones: Deben existir al menos dos selecciones.
    def jugarPartidos(self):
        self.__partidos = []
        numero = 1

        for i in range(len(self.__equipos) - 1):
            for j in range(i + 1, len(self.__equipos)):
                partido = Partido(numero,self.__equipos[i],self.__equipos[j],"Grupos","")

                partido.simular()
                self.__partidos = self.__partidos + [partido]

                numero += 1

                
# Nombre: calcularTabla
# Entradas: Ninguna.
# Salidas: Calcula la tabla de posiciones.
# Restricciones: Los partidos deben haber sido jugados.
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
        
# Nombre: obtener_clasificados
# Entradas: Ninguna.
# Salidas: Devuelve las dos selecciones clasificadas.
# Restricciones: La tabla debe estar calculada.    
    def obtener_clasificados(self):
        
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



# Nombre: mostrar_tabla
# Entradas: Ninguna.
# Salidas: Devuelve una cadena con la tabla de posiciones.
# Restricciones: Debe existir al menos una selección.
    def mostrar_tabla(self):
        texto= ("=== " + self.__nombre_grupo + " ===") #titulo con nombre del grupo
            
        tabla = self.calcularTabla()# Calcular la tabla y ordenarla
        cantidad = len(tabla)

        for ronda in range(cantidad - 1):      # Ordenamiento
            for posicion in range(cantidad - 1 - ronda):
                equipo_actual = tabla[posicion]
                equipo_siguiente = tabla[posicion + 1]

                puntos_actual = equipo_actual[1]
                puntos_siguiente = equipo_siguiente[1]

                if puntos_actual < puntos_siguiente:
                    tabla[posicion], tabla[posicion + 1] = tabla[posicion + 1], tabla[posicion]

                elif puntos_actual == puntos_siguiente:
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

    
""" Nombre: Fase
 Entradas: Nombre de la fase eliminatoria.
 Salidas: Crea una fase que almacena los partidos correspondientes.
 Restricciones: El nombre de la fase no debe estar vacío."""

class Fase:
    def __init__(self, nombre_fase):
        self.nombre_fase = nombre_fase
        self.partidos = []


# Nombre: registrar_juego
# Entradas: equipo1 (Selección), equipo2 (Selección).
# Salidas: Registra un partido de la fase.
# Restricciones: Ambos equipos deben existir.

    def registrar_juego(self, equipo1, equipo2):
        nuevo_id = len(self.partidos) + 1
        partido = Partido(nuevo_id, equipo1, equipo2, self.nombre_fase, "")

        self.partidos = self.partidos + [partido]



# Nombre: jugar_fase
# Entradas: Ninguna.
# Salidas: Simula todos los partidos de la fase.
# Restricciones: Deben existir partidos registrados.
    def jugar_fase(self):
        for partido in self.partidos:
            partido.simular()


# Nombre: mostrar_juegos
# Entradas: Ninguna.
# Salidas: Devuelve una cadena con los resultados de la fase.
# Restricciones: Los partidos deben haberse registrado.
    def mostrar_juegos(self):
        texto = "=== " + self.nombre_fase + " ===\n"

        for partido in self.partidos:
            texto += partido.mostrar_resultado() + "\n"

        return texto


# Nombre: obtener_clasificados
# Entradas: Ninguna.
# Salidas: Devuelve los equipos clasificados a la siguiente fase.
# Restricciones: Los partidos deben haber sido simulados.
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
""" Nombre: Mundial
 Entradas: Nombre del torneo y año.
 Salidas: Crea un objeto que administra todo el desarrollo del mundial.
 Restricciones: Debe existir un nombre y un año válido para el torneo."""

class Mundial:
    def __init__(self, nombre, año):

        self.nombre = nombre
        self.año = año
        self.paises = []
        self.selecciones = []
        self.grupos = []
        self.fases = []
        self.campeon = None

        
# Nombre: registrar_pais
# Entradas: pais (objeto Pais).
# Salidas: Agrega un país al mundial.
# Restricciones: El país no debe estar registrado previamente.
    def registrar_pais(self, pais):
        if pais not in self.paises:
            self.paises = self.paises + [pais]

            
# Nombre: registrar_seleccion
# Entradas: seleccion (objeto Seleccion).
# Salidas: Agrega una selección al mundial.
# Restricciones: La selección no debe estar registrada previamente.
    def registrar_seleccion(self, seleccion):
        if seleccion not in self.selecciones:
            self.selecciones = self.selecciones + [seleccion]

# Nombre: crear_grupos
# Entradas: cantidad_grupos (entero).
# Salidas: Crea los grupos del mundial y distribuye las selecciones.
# Restricciones: Debe existir una cantidad suficiente de selecciones.
    def crear_grupos(self, cantidad_grupos):
        self.grupos = []
        indice = 0

        for i in range(cantidad_grupos):
            letra = chr(65 + i)

            grupo = Grupo("Grupo " + letra)
            cantidad = 0

            while cantidad < 4 and indice < len(self.selecciones):
                grupo.agregar_equipo(self.selecciones[indice])
                indice += 1
                cantidad += 1

            self.grupos = self.grupos + [grupo]

            
# Nombre: jugar_fase_grupos
# Entradas: Ninguna.
# Salidas: Simula todos los partidos de la fase de grupos y devuelve los resultados.
# Restricciones: Los grupos deben haber sido creados.
    def jugar_fase_grupos(self):
        texto = "=========== FASE DE GRUPOS ===========\n\n"

        for grupo in self.grupos:
            grupo.jugarPartidos()
            grupo.calcularTabla()
            texto += grupo.mostrar_tabla()
            texto += "\n"

        return texto


# Nombre: armar_fase_eliminatoria
# Entradas: nombre_fase (texto), clasificados (lista de Seleccion).
# Salidas: Crea una fase eliminatoria y registra los enfrentamientos.
# Restricciones: La lista debe contener un número par de selecciones.
    def armar_fase_eliminatoria(self, nombre_fase, clasificados):
        fase = Fase(nombre_fase)
        i = 0

        while i < len(clasificados) - 1:
            fase.registrar_juego(clasificados[i],clasificados[i + 1])
            i += 2
        self.fases = self.fases + [fase]

        return fase



    
# Nombre: jugar_fase_eliminatoria
# Entradas: fase (objeto Fase).
# Salidas: Simula la fase eliminatoria y devuelve los equipos clasificados.
# Restricciones: La fase debe contener partidos registrados.
    def jugar_fase_eliminatoria(self, fase):
        fase.jugar_fase()
        return fase.obtener_clasificados()


# Nombre: determinar_campeon
# Entradas: Ninguna.
# Salidas: Determina la selección campeona del mundial.
# Restricciones: La fase de grupos debe haber finalizado.
    def determinar_campeon(self):
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



# Nombre: mostrar_tabla_general
# Entradas: Ninguna.
# Salidas: Devuelve las tablas de posiciones de todos los grupos.
# Restricciones: Deben existir grupos registrados.
    def mostrar_tabla_general(self):
        texto = "========== TABLAS DE POSICIONES ==========\n\n"

        for grupo in self.grupos:
            texto += grupo.mostrar_tabla()
            texto += "\n"
            
        return texto

    
# Nombre: generar_reporte
# Entradas: Ninguna.
# Salidas: Genera un reporte completo del mundial cpn tablas, fases y campeón.
# Restricciones: Debe existir información del torneo para generar el reporte.
    def generar_reporte(self):
        texto = ""
        texto += "=====================================\n"
        texto += "      REPORTE DEL MUNDIAL\n"
        texto += "=====================================\n\n"

        texto += "Torneo: " + self.nombre + "\n"
        texto += "Año: " + str(self.año) + "\n\n"
        texto += self.mostrar_tabla_general()
        texto += "\n"

        for fase in self.fases:
            texto += fase.mostrar_juegos()
            texto += "\n"

        if self.campeon != None:
            texto += "\nCAMPEÓN DEL TORNEO\n"
            texto += self.campeon.fn_nombre_del_pais()
            texto += "\n"

        return texto




















# ==========================================================================#
#======================= CLASE INTERFAZ GRAFICA ============================#
# ==========================================================================#
"""nombre: Interfaz_grafica
entarda:la ventana principal
salida: sus diferentesramificaciones den la ventaan flotante
retricciones: no detroy"""
class Interfaz_Grafica:
    # Colores del tema
    COLOR_FONDO       = "#0d1b2a"
    COLOR_PANEL       = "#1b2a3b"
    COLOR_ACENTO      = "#1db954"
    COLOR_ACENTO2     = "#e94560"
    COLOR_TEXTO       = "#ffffff"
    COLOR_SUBTEXTO    = "#a0aec0"
    COLOR_BOTON       = "#1e3a5f"
    COLOR_BOTON_HOVER = "#2a5080"

    def __init__(self, ventana_madre):
        
        self.__ventana = ventana_madre
        self.__ventana.title("Mundial FIFA 2026 🌎⚽")
        self.__ventana.geometry("900x620")
        self.__ventana.configure(bg=self.COLOR_FONDO)
        self.__ventana.resizable(False, False)

        self.__mundial = Mundial("Mundial FIFA 2026", 2026)
        self.__fase_actual_idx = 0  # controla que fase eliminatoria se juega siguemte

        self.__mostrar_inicio()#pa llamar mi inicio de pantalla

    ########################################################
    #  UTILIDADES GENERALES                                             
    # #####################################################


# Nombre: __limpiar
# Entradas: Ninguna.
# Salidas: Elimina todos los componentes de la ventana actual.
# Restricciones: La ventana debe estar inicializada.
    def __limpiar(self):
        
        for widget in self.__ventana.winfo_children():
            widget.destroy()

# Nombre: __barra_nav
# Entradas: titulo (texto).
# Salidas: Muestra la barra de navegación con el título de la pantalla.
# Restricciones: El título no debe estar vacío.
    def __barra_nav(self, titulo):
        
        barra = tk.Frame(self.__ventana, bg="#0a3d62", pady=8)#los codigos fueron preguntados a IA
        barra.pack(fill="x")
        
        tk.Label(barra, text="⚽ MUNDIAL FIFA 2026", bg="#0a3d62",
                 fg=self.COLOR_ACENTO, font=("Arial", 11, "bold")).pack(side="left", padx=12)
        
        tk.Label(barra, text=titulo, bg="#0a3d62",
                 fg=self.COLOR_TEXTO, font=("Arial", 11)).pack(side="left", padx=6)
        
        tk.Button(barra, text="🏠 Inicio", command=self.__mostrar_inicio,
                  bg=self.COLOR_BOTON, fg=self.COLOR_TEXTO, relief="flat",
                  font=("Arial", 9), padx=8, cursor="hand2").pack(side="right", padx=8)


# Nombre: __boton
# Entradas: padre (contenedor), texto (texto), comando (función), color (texto, opcional), ancho (entero).
# Salidas: Crea y devuelve un botón con el estilo de la aplicación.
# Restricciones: El contenedor debe existir y el comando debe ser válido.
    def __boton(self, padre, texto, comando, color=None, ancho=28):
        
        c = color if color else self.COLOR_BOTON#formato c++
        
        return tk.Button(padre, text=texto, command=comando,
                         bg=c, fg=self.COLOR_TEXTO, relief="flat",#que e torne plano
                         font=("Arial", 11), width=ancho, pady=7,
                         activebackground=self.COLOR_BOTON_HOVER,#cuando pase mause que se torne
                         activeforeground=self.COLOR_TEXTO, cursor="hand2")#activite se busco ayuda como mostar para cuando esta activo



# Nombre: __label
# Entradas: padre (contenedor), texto (texto), bold (booleano), color (texto, opcional).
# Salidas: Crea y devuelve una etiqueta.
# Restricciones: El contenedor debe existir.
    def __label(self, padre, texto, bold=False, color=None):
        
        fuente = ("Arial", 10, "bold") if bold else ("Arial", 10)
        c = color if color else self.COLOR_TEXTO
        return tk.Label(padre, text=texto, bg=self.COLOR_PANEL,


                        fg=c, font=fuente)
# Nombre: __entry
# Entradas: padre (contenedor).
# Salidas: Crea y devuelve un campo de texto.
# Restricciones: El contenedor debe existir.
    def __entry(self, padre):
       
        return tk.Entry(padre, bg="#2d3748", fg=self.COLOR_TEXTO,
                        insertbackground=self.COLOR_TEXTO,


                        relief="flat", font=("Arial", 10), width=28)
# Nombre: __area_texto
# Entradas: padre (contenedor), alto (entero).
# Salidas: Crea y devuelve un área de texto con barra de desplazamiento.
# Restricciones: El contenedor debe existir.
    def __area_texto(self, padre, alto=18):
       
        caja = scrolledtext.ScrolledText(padre, wrap=tk.WORD,
                                         font=("Courier", 9),
                                         bg="#0f2035", fg=self.COLOR_TEXTO,
                                         insertbackground=self.COLOR_TEXTO,
                                         height=alto, relief="flat")
        return caja


# Nombre: __escribir_texto
# Entradas: caja (área de texto), texto (cadena).
# Salidas: Muestra el texto recibido dentro del área de texto.
# Restricciones: El área de texto debe existir.
    def __escribir_texto(self, caja, texto):
        
        caja.config(state="normal")
        caja.delete("1.0", tk.END)
        caja.insert(tk.END, texto)
        caja.config(state="disabled")

        
# Nombre: __frame_panel
# Entradas: padre (contenedor, opcional).
# Salidas: Crea y devuelve un panel con el diseño de la aplicación.
# Restricciones: Si se proporciona un contenedor, este debe existir.
    def __frame_panel(self, padre=None):
       
        # Objetivo: crear frame con color de panel del tema
        p = padre if padre else self.__ventana
        return tk.Frame(p, bg=self.COLOR_PANEL)

# ==================================================== #
#==============PANTALLA PRINCIPAL  =====================                                                
#=====================================================#

    def __mostrar_inicio(self):
       
        self.__limpiar()#limpiar la pantalal antes de gyernera
        self.__fase_actual_idx = 0#codigo

        cabeza = tk.Frame(self.__ventana, bg=self.COLOR_FONDO)
        cabeza.pack(fill="x", pady=(20, 0))
        
        tk.Label(cabeza, text="🌎  MUNDIAL FIFA 2026  🌎",
                 bg=self.COLOR_FONDO, fg=self.COLOR_ACENTO,
                 font=("Arial", 22, "bold")).pack()
        tk.Label(cabeza, text="Simulador Oficial del Torneo",
                 bg=self.COLOR_FONDO, fg=self.COLOR_SUBTEXTO,
                 font=("Arial", 11)).pack(pady=(2, 16))

        contenedor = tk.Frame(self.__ventana, bg=self.COLOR_FONDO)
        contenedor.pack(expand=True)

        opciones = [
            (" 🌍  Administrar Países y Selecciones",  self.__pantalla_paises),
            (" 👤  Administrar Entrenadores y Jugadores", self.__pantalla_personas),
            (" 🔩  Configurar Mundial (Grupos)",        self.__pantalla_configurar),
            (" ▶️️  Jugar Mundial",                      self.__pantalla_jugar),
            (" 📊  Estadísticas / Rankings",            self.__pantalla_estadisticas),
            (" ❎ Salir",                               self.__ventana.quit),
        ]

        for texto, cmd in opciones:
            self.__boton(contenedor, texto, cmd, ancho=38).pack(pady=5)#mostar en cascada

    # ======================================= #
    #  PANTALLA: PAÍSES Y SELECCIONES                                      
    # ========================================== #

    def __pantalla_paises(self):
        
        self.__limpiar()
        self.__barra_nav("› Países y Selecciones")

        cuerpo = tk.Frame(self.__ventana, bg=self.COLOR_FONDO)
        cuerpo.pack(fill="both", expand=True, padx=16, pady=10)

        # Columna izquierda,formularios 
        izq = self.__frame_panel(cuerpo)#lamo mi funcion frame
        izq.pack(side="left", fill="y", padx=(0, 10), pady=4)

       
        tk.Label(izq, text="➕ Registrar País", bg=self.COLOR_PANEL, # Formulario País
                 fg=self.COLOR_ACENTO, font=("Arial", 11, "bold")).grid(
                 row=0, column=0, columnspan=2, pady=(10, 6), padx=10)

        campos_pais = ["Código FIFA", "Nombre", "Continente", "Ranking FIFA"]#mis Label
        self.__ep = []
        for i, c in enumerate(campos_pais):#recorro y optendo de unanel indice para luego  dnadodirid
            self.__label(izq, c + ":").grid(row=i+1, column=0, sticky="e", padx=8, pady=3)
            e = self.__entry(izq)#recurro
            e.grid(row=i+1, column=1, padx=8, pady=3)
            self.__ep = self.__ep + [e]

        self.__boton(izq, "Guardar País", self.__guardar_pais, ancho=22).grid(
            row=5, column=0, columnspan=2, pady=8)#solo 2 saltos pafa represnetar letras

        tk.Frame(izq, bg=self.COLOR_SUBTEXTO, height=1).grid(
            row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=4)#que lado pego y alinbeo mi witget

        # Formulario Selección
        tk.Label(izq, text="🟩️ Crear Selección", bg=self.COLOR_PANEL,
                 fg=self.COLOR_ACENTO, font=("Arial", 11, "bold")).grid(
                 row=7, column=0, columnspan=2, pady=(6, 4), padx=10)

        self.__label(izq, "Código Equipo:").grid(row=8, column=0, sticky="e", padx=8, pady=3)
        self.__e_cod_sel = self.__entry(izq)
        self.__e_cod_sel.grid(row=8, column=1, padx=8, pady=3)

        self.__label(izq, "País (código FIFA):").grid(row=9, column=0, sticky="e", padx=8, pady=3)
        self.__e_pais_sel = self.__entry(izq)
        self.__e_pais_sel.grid(row=9, column=1, padx=8, pady=3)

        self.__boton(izq, "Crear Selección", self.__guardar_seleccion, ancho=22).grid(
            row=10, column=0, columnspan=2, pady=8)

        # Columna derecha
        der = tk.Frame(self.__ventana, bg=self.COLOR_FONDO)
        der.pack(side="left", fill="both", expand=True, pady=4)

        tk.Label(der, text="📋 Países y Selecciones registrados",
                 bg=self.COLOR_FONDO, fg=self.COLOR_TEXTO,
                 font=("Arial", 10, "bold")).pack(anchor="w")

        self.__txt_paises = self.__area_texto(der, alto=24)
        self.__txt_paises.pack(fill="both", expand=True)
        self.__actualizar_lista_paises()

        
# Nombre: __guardar_pais
# Entradas: Ninguna.
# Salidas: Registra un nuevo país con los datos ingresados por el usuario.
# Restricciones: Todos los campos deben estar completos y el ranking debe estar entre 1 y 200.
    def __guardar_pais(self):
        
        try:
            codigo   = self.__ep[0].get().strip().upper()#almaceno entrys del formulraionquedaravlamfifa
            nombre   = self.__ep[1].get().strip()
            conf     = self.__ep[2].get().strip()
            ranking  = int(self.__ep[3].get().strip())

            if codigo == "" or nombre == "" or conf == "":#verificaciones pa más facil
                messagebox.showwarning("Campo vacío", "Todos los campos son obligatorios.")
                return
            if ranking < 1 or ranking > 200:
                messagebox.showwarning("Ranking inválido", "El ranking debe estar entre 1 y 200.")
                return

            # verificar que no exista ya ese código
            for p in self.__mundial.paises:
                if p.fn_codigo_fifa() == codigo:
                    messagebox.showwarning("Duplicado", f"Ya existe un país con código {codigo}.")
                    return

            pais = Pais(codigo, nombre, conf, ranking)
            self.__mundial.registrar_pais(pais)

            for e in self.__ep:
                e.delete(0, tk.END)

            self.__actualizar_lista_paises()
            messagebox.showinfo("☑️ Éxito", f"País '{nombre}' registrado correctamente.")
        except ValueError:
            messagebox.showerror("Error", "El ranking FIFA debe ser un número entero.")

    def __guardar_seleccion(self):
        
        codigo = self.__e_cod_sel.get().strip().upper()
        cod_pais = self.__e_pais_sel.get().strip().upper()

        if codigo == "" or cod_pais == "":
            messagebox.showwarning("Campo vacío", "Todos los campos son obligatorios.")#aviso
            return

        
        pais_encontrado = None# buscaDOR DEL PAIS el país
        for p in self.__mundial.paises:
            if p.fn_codigo_fifa() == cod_pais:
                pais_encontrado = p

        if pais_encontrado is None:
            messagebox.showerror("Error", f"No existe un país con código '{cod_pais}'.")#formato de error
            return

        
        for s in self.__mundial.selecciones:# verificar que no exista ya esa selección
            if s.fn_codigo_equipo() == codigo:
                messagebox.showwarning("Duplicado", f"Ya existe una selección con código {codigo}.")
                return

        sel = Seleccion(codigo, pais_encontrado)
        self.__mundial.registrar_seleccion(sel)

        self.__e_cod_sel.delete(0, tk.END)
        self.__e_pais_sel.delete(0, tk.END)
        self.__actualizar_lista_paises()
        messagebox.showinfo("☑ Éxito", f"Selección '{codigo}' creada correctamente.")

    def __actualizar_lista_paises(self):
        
        texto = "=== PAÍSES REGISTRADOS ===\n"
        for p in self.__mundial.paises:
            texto = texto + p.fn_mostrar_datos() + "\n"

        texto = texto + "\n=== SELECCIONES REGISTRADAS ===\n"
        for s in self.__mundial.selecciones:
            texto = texto + s.fn_mostrar_datos() + "\n" + "-"*40 + "\n"

        self.__escribir_texto(self.__txt_paises, texto)

    # ================================================ #
    #  PANTALLA: ENTRENADORES Y JUGADORES                                  
    # ########################################################### #

    def __pantalla_personas(self):
        
        self.__limpiar()
        self.__barra_nav("› Entrenadores y Jugadores")

        nb = tk.Frame(self.__ventana, bg=self.COLOR_FONDO)
        nb.pack(fill="x", padx=16, pady=(8, 0))

        self.__frame_entrenador = tk.Frame(self.__ventana, bg=self.COLOR_FONDO)
        self.__frame_jugador    = tk.Frame(self.__ventana, bg=self.COLOR_FONDO)

        def mostrar_entrenador():
            self.__frame_jugador.pack_forget()
            self.__frame_entrenador.pack(fill="both", expand=True, padx=16, pady=6)

        def mostrar_jugador():
            self.__frame_entrenador.pack_forget()
            self.__frame_jugador.pack(fill="both", expand=True, padx=16, pady=6)

        self.__boton(nb, "👕 Entrenadores", mostrar_entrenador, ancho=18).pack(side="left", padx=4)
        self.__boton(nb, "🥅 Jugadores",    mostrar_jugador,    ancho=18).pack(side="left", padx=4)

        self.__construir_form_entrenador()
        self.__construir_form_jugador()
        mostrar_entrenador()

    def __construir_form_entrenador(self):
        
        f = self.__frame_entrenador

        izq = self.__frame_panel(f)#llamarlo conlos tados delmentrenador
        izq.pack(side="left", fill="y", padx=(0, 10))

        tk.Label(izq, text="➕ Registrar Entrenador", bg=self.COLOR_PANEL,
                 fg=self.COLOR_ACENTO, font=("Arial", 11, "bold")).grid(
                 row=0, column=0, columnspan=2, pady=(10,6), padx=10)

        campos = ["Nombre", "Apellido", "Fecha Nac. (DD/MM/AAAA)",
                  "Nacionalidad", "Licencia", "Experiencia (años)", "Sistema de Juego"]
        self.__ee = []
        #nuemro con indivce
        for i, c in enumerate(campos):
            self.__label(izq, c + ":").grid(row=i+1, column=0, sticky="e", padx=8, pady=2)
            e = self.__entry(izq)
            e.grid(row=i+1, column=1, padx=8, pady=2)
            self.__ee = self.__ee + [e]

        self.__label(izq, "Selección (código):").grid(row=8, column=0, sticky="e", padx=8, pady=2)
        self.__e_sel_dt = self.__entry(izq)
        self.__e_sel_dt.grid(row=8, column=1, padx=8, pady=2)

        self.__boton(izq, "Asignar Entrenador", self.__guardar_entrenador, ancho=22).grid(
            row=9, column=0, columnspan=2, pady=8)

        der = tk.Frame(f, bg=self.COLOR_FONDO)
        der.pack(side="left", fill="both", expand=True)
        tk.Label(der, text="📋 Selecciones y sus entrenadores",
                 bg=self.COLOR_FONDO, fg=self.COLOR_TEXTO,
                 font=("Arial", 10, "bold")).pack(anchor="w")
        
        self.__txt_dt = self.__area_texto(der, alto=22)
        self.__txt_dt.pack(fill="both", expand=True)
        self.__refrescar_txt_dt()
 
    def __refrescar_txt_dt(self):#pa rederfcar los datos o dt aap simplifical
       
        texto = ""
        for s in self.__mundial.selecciones:
            dt = s.fn_entrenador()
            nombre_dt = dt.fn_mostrar_nombre_completo() if dt is not None else "Sin entrenador"
            texto = texto + f"[{s.fn_codigo_equipo()}] {s.fn_nombre_del_pais()} → DT: {nombre_dt}\n"
        self.__escribir_texto(self.__txt_dt, texto if texto != "" else "No hay selecciones registradas.")

    def __guardar_entrenador(self):
        
        try:#pal frameoLabel
            nombre   = self.__ee[0].get().strip()
            apellido = self.__ee[1].get().strip()
            fecha    = self.__ee[2].get().strip()
            nac      = self.__ee[3].get().strip()
            lic      = self.__ee[4].get().strip()
            exp      = int(self.__ee[5].get().strip())
            sistema  = self.__ee[6].get().strip()
            cod_sel  = self.__e_sel_dt.get().strip().upper()

            if nombre == "" or apellido == "" or fecha == "" or nac == "" or lic == "" or sistema == "" or cod_sel == "":
                messagebox.showwarning("Campo vacío", "Todos los campos son obligatorios.")
                return
            if exp < 0:
                messagebox.showwarning("Valor inválido", "La experiencia no puede ser negativa.")
                return

            sel = None
            for s in self.__mundial.selecciones:
                if s.fn_codigo_equipo() == cod_sel:
                    sel = s

            if sel is None:
                messagebox.showerror("Error", f"No existe la selección '{cod_sel}'.")
                return

            dt = Entrenador(nombre, apellido, fecha, nac, lic, exp, sistema)
            sel.fn_asignar_entrenador(dt)

            for e in self.__ee:
                e.delete(0, tk.END)
            self.__e_sel_dt.delete(0, tk.END)

            self.__refrescar_txt_dt()
            messagebox.showinfo(" ☑️ Éxito", f"Entrenador '{nombre} {apellido}' asignado a {cod_sel}.")
        except ValueError:
            messagebox.showerror("Error", "La experiencia debe ser un número entero.")

    def __construir_form_jugador(self):
        
        f = self.__frame_jugador

        izq = self.__frame_panel(f)
        izq.pack(side="left", fill="y", padx=(0, 10))

        tk.Label(izq, text="➕ Registrar Jugador", bg=self.COLOR_PANEL,
                 fg=self.COLOR_ACENTO, font=("Arial", 11, "bold")).grid(
                 row=0, column=0, columnspan=2, pady=(10,6), padx=10)

        campos = ["Nombre", "Apellido", "Fecha Nac. (DD/MM/AAAA)",
                  "Nacionalidad", "Dorsal (1-99)", "Posición",
                  "Velocidad (1-25)", "Estratega (1-25)",
                  "Dominio Balón (1-25)", "Fuerza (1-25)"]
        self.__ej = []
        
        for i, c in enumerate(campos):
            self.__label(izq, c + ":").grid(row=i+1, column=0, sticky="e", padx=8, pady=2)
            e = self.__entry(izq)
            e.grid(row=i+1, column=1, padx=8, pady=2)
            self.__ej = self.__ej + [e]

        self.__label(izq, "Selección (código):").grid(row=11, column=0, sticky="e", padx=8, pady=2)
        
        self.__e_sel_jug = self.__entry(izq)
        self.__e_sel_jug.grid(row=11, column=1, padx=8, pady=2)

        self.__boton(izq, "Agregar Jugador", self.__guardar_jugador, ancho=22).grid(
            row=12, column=0, columnspan=2, pady=4)
        
        self.__boton(izq, "Eliminar Jugador", self.__eliminar_jugador,
                     color=self.COLOR_ACENTO2, ancho=22).grid(
            row=13, column=0, columnspan=2, pady=4)

        der = tk.Frame(f, bg=self.COLOR_FONDO)
        der.pack(side="left", fill="both", expand=True)
        tk.Label(der, text="📋 Jugadores por selección",
                 bg=self.COLOR_FONDO, fg=self.COLOR_TEXTO,
                 font=("Arial", 10, "bold")).pack(anchor="w")
        self.__txt_jug = self.__area_texto(der, alto=26)
        self.__txt_jug.pack(fill="both", expand=True)
        self.__refrescar_txt_jugadores()

    def __guardar_jugador(self):
       
        try:#casso pa dato futbolista
            nombre   = self.__ej[0].get().strip()
            apellido = self.__ej[1].get().strip()
            fecha    = self.__ej[2].get().strip()
            nac      = self.__ej[3].get().strip()
            dorsal   = int(self.__ej[4].get().strip())
            posicion = self.__ej[5].get().strip()
            vel      = int(self.__ej[6].get().strip()) if self.__ej[6].get().strip() != "" else None
            est      = int(self.__ej[7].get().strip()) if self.__ej[7].get().strip() != "" else None
            dom      = int(self.__ej[8].get().strip()) if self.__ej[8].get().strip() != "" else None
            fue      = int(self.__ej[9].get().strip()) if self.__ej[9].get().strip() != "" else None
            cod_sel  = self.__e_sel_jug.get().strip().upper()

            if nombre == "" or apellido == "" or fecha == "" or nac == "" or posicion == "" or cod_sel == "":
                messagebox.showwarning("Campo vacío", "Nombre, apellido, fecha, nacionalidad, posición y selección son obligatorios.")
                return
            if dorsal < 1 or dorsal > 99:
                messagebox.showwarning("Dorsal inválido", "El dorsal debe estar entre 1 y 99.")
                return

            for v in [vel, est, dom, fue]:
                if v is not None and (v < 1 or v > 25):
                    messagebox.showwarning("Atributo inválido", "Velocidad, estratega, dominio y fuerza deben estar entre 1 y 25.")
                    return

            sel = None
            for s in self.__mundial.selecciones:
                if s.fn_codigo_equipo() == cod_sel:
                    sel = s

            if sel is None:
                messagebox.showerror("Error", f"No existe la selección '{cod_sel}'.")
                return

            jugador = Futbolista(nombre, apellido, fecha, nac, dorsal, posicion, vel, est, dom, fue)#pa kllamr mis adatos ainicise
            resultado = sel.fn_agregar_jugador(jugador)

            if not resultado:
                messagebox.showwarning("Límite", f"La selección '{cod_sel}' ya tiene el máximo de 23 jugadores.")
                return

            for e in self.__ej:
                e.delete(0, tk.END)
            self.__e_sel_jug.delete(0, tk.END)

            self.__refrescar_txt_jugadores()
            messagebox.showinfo("☑️ Éxito", f"Jugador '{nombre} {apellido}' agregado a {cod_sel}.")
        except ValueError:
            messagebox.showerror("Error", "Dorsal y atributos deben ser números enteros.")

    def __eliminar_jugador(self):
        
        try:
            dorsal  = int(self.__ej[4].get().strip())
            cod_sel = self.__e_sel_jug.get().strip().upper()

            if cod_sel == "":
                messagebox.showwarning("Campo vacío", "Ingrese el código de la selección.")
                return

            sel = None
            for s in self.__mundial.selecciones:
                if s.fn_codigo_equipo() == cod_sel:
                    sel = s

            if sel is None:
                messagebox.showerror("Error", f"No existe la selección '{cod_sel}'.")
                return

            sel.fn_eliminar_jugador(dorsal)
            self.__refrescar_txt_jugadores()
            messagebox.showinfo("☑️", f"Jugador dorsal #{dorsal} eliminado de {cod_sel} (si existía).")
        except ValueError:
            messagebox.showerror("Error", "El dorsal debe ser un número entero.")

    def __refrescar_txt_jugadores(self):
        
        texto = ""
        for s in self.__mundial.selecciones:
            texto = texto + f"\n🥅 [{s.fn_codigo_equipo()}] {s.fn_nombre_del_pais()} — {s.fn_cantidad_jugadores()} jugadores\n"
            for j in s.fn_jugadores():
                texto = texto + f"   #{j.fn_dorsal()} {j.fn_mostrar_nombre_completo()} | {j.fn_posicion()} | Puntaje: {j.fn_puntaje_individual()}\n"
        self.__escribir_texto(self.__txt_jug, texto if texto != "" else "No hay selecciones registradas.")

    # ==================================================================
    #  PANTALLA: CONFIGURAR MUNDIAL                                        
    # ================================================================#

    def __pantalla_configurar(self):
        
        self.__limpiar()
        self.__barra_nav("› Configurar Mundial")

        cuerpo = tk.Frame(self.__ventana, bg=self.COLOR_FONDO)
        cuerpo.pack(fill="both", expand=True, padx=20, pady=10)

        panel = self.__frame_panel(cuerpo)
        panel.pack(side="left", fill="y", padx=(0, 14))

        tk.Label(panel, text="️ Crear Grupos", bg=self.COLOR_PANEL,
                 fg=self.COLOR_ACENTO, font=("Arial", 12, "bold")).pack(pady=(12, 6), padx=16)

        tk.Label(panel, text=f"Selecciones registradas: {len(self.__mundial.selecciones)}",
                 bg=self.COLOR_PANEL, fg=self.COLOR_SUBTEXTO,
                 font=("Arial", 10)).pack(pady=2, padx=16)

        tk.Label(panel, text="Cantidad de grupos (mín. 2):",
                 bg=self.COLOR_PANEL, fg=self.COLOR_TEXTO,
                 font=("Arial", 10)).pack(pady=(10, 2), padx=16)

        self.__e_grupos = tk.Entry(panel, bg="#2d3748", fg=self.COLOR_TEXTO,
                                   insertbackground=self.COLOR_TEXTO,
                                   relief="flat", font=("Arial", 11), width=10)
        self.__e_grupos.pack(pady=4, padx=16)

        self.__boton(panel, "Crear Grupos", self.__crear_grupos, ancho=20).pack(pady=10, padx=16)

        der = tk.Frame(cuerpo, bg=self.COLOR_FONDO)
        der.pack(side="left", fill="both", expand=True)
        tk.Label(der, text="📋 Grupos formados",
                 bg=self.COLOR_FONDO, fg=self.COLOR_TEXTO,
                 font=("Arial", 10, "bold")).pack(anchor="w")
        self.__txt_grupos = self.__area_texto(der, alto=26)
        self.__txt_grupos.pack(fill="both", expand=True)
        self.__mostrar_grupos_actuales()

    def __crear_grupos(self):
        
        try:
            cantidad = int(self.__e_grupos.get().strip())
            if cantidad < 2:
                messagebox.showwarning("Inválido", "Debe haber al menos 2 grupos.")
                return
            if len(self.__mundial.selecciones) < cantidad * 2:
                messagebox.showwarning("Pocas selecciones",
                    f"Se necesitan al menos {cantidad * 2} selecciones para {cantidad} grupos.")
                return

            self.__mundial.crear_grupos(cantidad)
            self.__mostrar_grupos_actuales()
            messagebox.showinfo("☑️ Éxito", f"{cantidad} grupos creados correctamente.")
        except ValueError:
            messagebox.showerror("Error", "La cantidad de grupos debe ser un número entero.")

    def __mostrar_grupos_actuales(self):
       
        if self.__mundial.grupos == []:
            self.__escribir_texto(self.__txt_grupos, "Aún no se han creado grupos.")
            return
        texto = ""
        for g in self.__mundial.grupos:
            texto = texto + f"\n{'='*30}\n  {g.nombre_grupo()}\n{'='*30}\n"
            for eq in g.equipos():
                texto = texto + f"  • {eq.fn_nombre_del_pais()} [{eq.fn_codigo_equipo()}] — Fuerza: {eq.fn_fuerza_equipo():.1f}\n"
        self.__escribir_texto(self.__txt_grupos, texto)

    # =================================================================#
    #  PANTALLA JUGAR MUNDIAL                                             
    #==================================================================#

    def __pantalla_jugar(self):
        
        self.__limpiar()
        self.__barra_nav("› Jugar Mundial")

        if self.__mundial.grupos == []:
            tk.Label(self.__ventana, text="⚠️️Debes configurar los grupos primero.",
                     bg=self.COLOR_FONDO, fg=self.COLOR_ACENTO2,
                     font=("Arial", 12)).pack(expand=True)
            return

        cuerpo = tk.Frame(self.__ventana, bg=self.COLOR_FONDO)
        cuerpo.pack(fill="both", expand=True, padx=16, pady=8)

        panel = self.__frame_panel(cuerpo)
        panel.pack(side="left", fill="y", padx=(0, 12))

        tk.Label(panel, text="▶️ Fases del Torneo", bg=self.COLOR_PANEL,
                 fg=self.COLOR_ACENTO, font=("Arial", 11, "bold")).pack(pady=(12, 8), padx=14)

        self.__boton(panel, "1️🟩 Simular Fase de Grupos",
                     self.__simular_grupos, ancho=26).pack(pady=5, padx=10)
        self.__boton(panel, "2️🟩 Siguiente Fase Eliminatoria",
                     self.__siguiente_fase, ancho=26).pack(pady=5, padx=10)
        self.__boton(panel, "🏆  Ver Campeón",
                     self.__mostrar_campeon, ancho=26).pack(pady=5, padx=10)

        der = tk.Frame(cuerpo, bg=self.COLOR_FONDO)
        der.pack(side="left", fill="both", expand=True)
        tk.Label(der, text=" 📋 Resultados",
                 bg=self.COLOR_FONDO, fg=self.COLOR_TEXTO,
                 font=("Arial", 10, "bold")).pack(anchor="w")
        self.__txt_juego = self.__area_texto(der, alto=26)
        self.__txt_juego.pack(fill="both", expand=True)

    def __simular_grupos(self):
        
        invalidas = ""
        for g in self.__mundial.grupos:
            for eq in g.equipos():
                if not eq.fn_valida_para_jugar():
                    invalidas = invalidas + f"  • {eq.fn_nombre_del_pais()} (necesita entrenador y al menos 11 jugadores)\n"

        if invalidas != "":
            messagebox.showwarning("Selecciones incompletas",
                "Las siguientes selecciones no están listas:\n" + invalidas)
            return

        resultado = self.__mundial.jugar_fase_grupos()
        self.__fase_actual_idx = 0
        self.__escribir_texto(self.__txt_juego, resultado)

    def __siguiente_fase(self):
        
        nombres_fases = ["Dieciseisavos de Final", "Octavos de Final",
                         "Cuartos de Final", "Semifinales", "Final"]

        
        if self.__fase_actual_idx == 0:# Obtener clasificados actuales
            clasificados = []
            for g in self.__mundial.grupos:
                clasificados = clasificados + g.obtener_clasificados()
        else:
            if self.__fase_actual_idx - 1 < len(self.__mundial.fases):
                clasificados = self.__mundial.fases[self.__fase_actual_idx - 1].obtener_clasificados()
            else:
                messagebox.showinfo("Torneo terminado", "Ya se jugó la Final. Ver campeón.")
                return

        if len(clasificados) < 2:
            messagebox.showinfo("Fin", "No hay suficientes equipos clasificados.")
            return

       
        if len(clasificados) == 32: # elegir nombre de fase según cantidad de clasificados
            nombre = "Dieciseisavos de Final"
        elif len(clasificados) == 16:
            nombre = "Octavos de Final"
        elif len(clasificados) == 8:
            nombre = "Cuartos de Final"
        elif len(clasificados) == 4:
            nombre = "Semifinales"
        elif len(clasificados) == 2:
            nombre = "Final"
        else:
            nombre = nombres_fases[self.__fase_actual_idx] if self.__fase_actual_idx < len(nombres_fases) else "Fase Eliminatoria"

        fase = self.__mundial.armar_fase_eliminatoria(nombre, clasificados)
        self.__mundial.jugar_fase_eliminatoria(fase)
        self.__fase_actual_idx += 1

        texto = fase.mostrar_juegos()

       
        if nombre == "Final": # Si fue la final, asignar campeón
            ganadores = fase.obtener_clasificados()
            if ganadores != []:
                self.__mundial.campeon = ganadores[0]
                texto = texto + f"\n🏆 ¡CAMPEÓN DEL MUNDIAL FIFA 2026!\n 🥇 {self.__mundial.campeon.fn_nombre_del_pais()} 🥇\n"

        self.__escribir_texto(self.__txt_juego, texto)

    def __mostrar_campeon(self):
        
        if self.__mundial.campeon is None:
            messagebox.showinfo("Sin campeón", "Aún no se ha determinado el campeón. Juega todas las fases primero.")
            return
        messagebox.showinfo(
            "🏆 CAMPEÓN MUNDIAL FIFA 2026 🏆",
            f"\n🥇  {self.__mundial.campeon.fn_nombre_del_pais()}  🥇\n\n¡Felicitaciones al Campeón del Mundo!"
        )

    # =======================================================#
    #  PANTALLA: ESTADÍSTICAS Y RANKINGS                                  
    # ========================================================#

    def __pantalla_estadisticas(self):
        
        self.__limpiar()
        self.__barra_nav("› Estadísticas / Rankings")

        cuerpo = tk.Frame(self.__ventana, bg=self.COLOR_FONDO)
        cuerpo.pack(fill="both", expand=True, padx=16, pady=8)

        panel = self.__frame_panel(cuerpo)
        panel.pack(side="left", fill="y", padx=(0, 12))

        tk.Label(panel, text="📊 Ver Estadísticas", bg=self.COLOR_PANEL,
                 fg=self.COLOR_ACENTO, font=("Arial", 11, "bold")).pack(pady=(12, 8), padx=14)

        self.__boton(panel, "🥅 Ranking Goleadores",      self.__stat_goleadores, ancho=24).pack(pady=5, padx=10)
        self.__boton(panel, "🏅 Ranking Selecciones",     self.__stat_selecciones, ancho=24).pack(pady=5, padx=10)
        self.__boton(panel, "🪪 Más Tarjetas",            self.__stat_tarjetas,   ancho=24).pack(pady=5, padx=10)
        self.__boton(panel, "📋 Guardar Archivos .txt",   self.__guardar_archivos, ancho=24).pack(pady=5, padx=10)

        der = tk.Frame(cuerpo, bg=self.COLOR_FONDO)
        der.pack(side="left", fill="both", expand=True)
        tk.Label(der, text="📄 Resultados",
                 bg=self.COLOR_FONDO, fg=self.COLOR_TEXTO,
                 font=("Arial", 10, "bold")).pack(anchor="w")
        self.__txt_stats = self.__area_texto(der, alto=26)
        self.__txt_stats.pack(fill="both", expand=True)

    def __stat_goleadores(self):
        
        todos = []
        for s in self.__mundial.selecciones:
            for j in s.fn_jugadores():
                todos = todos + [(j, s.fn_nombre_del_pais())]

        
        n = len(todos)
        for i in range(n - 1):# ordenar por goles en descendente
            for k in range(n - 1 - i):
                if todos[k][0].fn_goles() < todos[k+1][0].fn_goles():
                    todos[k], todos[k+1] = todos[k+1], todos[k]

        texto = "=== 🏆 RANKING DE GOLEADORES ===\n\n"
        pos = 1
        for jugador, pais in todos:
            if jugador.fn_goles() > 0:
                texto = texto + f"{pos}. {jugador.fn_mostrar_nombre_completo()} ({pais}) — {jugador.fn_goles()} goles\n"
                pos += 1

        if pos == 1:
            texto = texto + "Aún no hay goles registrados."

        self.__escribir_texto(self.__txt_stats, texto)

    def __stat_selecciones(self):
        
        sels = list(self.__mundial.selecciones)
        n = len(sels)
        for i in range(n - 1):
            for k in range(n - 1 - i):
                gf_a = sels[k].fn_total_goles_favor()
                gf_b = sels[k+1].fn_total_goles_favor()
                dif_a = sels[k].fn_total_goles_favor() - sels[k].fn_total_goles_contra()
                dif_b = sels[k+1].fn_total_goles_favor() - sels[k+1].fn_total_goles_contra()
                if gf_a < gf_b or (gf_a == gf_b and dif_a < dif_b):
                    sels[k], sels[k+1] = sels[k+1], sels[k]

        texto = "=== 🏅 RANKING DE SELECCIONES ===\n\n"
        pos = 1
        for s in sels:
            dif = s.fn_total_goles_favor() - s.fn_total_goles_contra()
            texto = texto + (f"{pos}. {s.fn_nombre_del_pais()} [{s.fn_codigo_equipo()}] "
                             f"— GF: {s.fn_total_goles_favor()} GC: {s.fn_total_goles_contra()} DG: {dif} "
                             f"| Fuerza: {s.fn_fuerza_equipo():.1f}\n")
            pos += 1

        if self.__mundial.campeon is not None:
            texto = texto + f"\n🏆 Campeón: {self.__mundial.campeon.fn_nombre_del_pais()}"

        self.__escribir_texto(self.__txt_stats, texto)

    def __stat_tarjetas(self):
        
        sels = list(self.__mundial.selecciones)

        # ordenar por tarjetas amarillas
        n = len(sels)
        for i in range(n - 1):
            for k in range(n - 1 - i):
                if sels[k].fn_total_tarjetas_amarillas() < sels[k+1].fn_total_tarjetas_amarillas():
                    sels[k], sels[k+1] = sels[k+1], sels[k]

        texto = "=== 🪪 TARJETAS AMARILLAS ===\n"
        for s in sels:
            texto = texto + f"  {s.fn_nombre_del_pais()}: {s.fn_total_tarjetas_amarillas()} amarillas\n"

        # ordenar por rojas
        for i in range(n - 1):
            for k in range(n - 1 - i):
                if sels[k].fn_total_tarjetas_rojas() < sels[k+1].fn_total_tarjetas_rojas():
                    sels[k], sels[k+1] = sels[k+1], sels[k]

        texto = texto + "\n=== 🪪 TARJETAS ROJAS ===\n"
        for s in sels:
            texto = texto + f"  {s.fn_nombre_del_pais()}: {s.fn_total_tarjetas_rojas()} rojas\n"

        self.__escribir_texto(self.__txt_stats, texto)

    # =====================================================#
    #   GUARDAR ARCHIVOS TXT                                 
    # ==================================================== #

    def __guardar_archivos(self):
        
        self.__guardar_paises_txt()
        self.__guardar_selecciones_txt()
        self.__guardar_jugadores_txt()
        self.__guardar_partidos_txt()
        self.__guardar_ranking_goleadores_txt()
        self.__guardar_ranking_selecciones_txt()
        messagebox.showinfo("📋 Guardado", "Todos los archivos .txt fueron guardados correctamente.")

    def __guardar_paises_txt(self):
        
        archivo = open("paises.txt", "w", encoding="utf-8")
        for p in self.__mundial.paises:
            archivo.write(p.fn_para_pasar_archivo() + "\n")
        archivo.close()

    def __guardar_selecciones_txt(self):
       
        archivo = open("selecciones.txt", "w", encoding="utf-8")
        for s in self.__mundial.selecciones:
            dt = s.fn_entrenador()
            nombre_dt = dt.fn_mostrar_nombre_completo() if dt is not None else "Sin entrenador"
            linea = f"{s.fn_codigo_equipo()},{s.fn_nombre_del_pais()},{nombre_dt},{s.fn_fuerza_equipo():.2f}\n"
            archivo.write(linea)
        archivo.close()

    def __guardar_jugadores_txt(self):
       
        archivo = open("jugadores.txt", "w", encoding="utf-8")
        for s in self.__mundial.selecciones:
            for j in s.fn_jugadores():
                linea = f"{s.fn_codigo_equipo()},{j.fn_dorsal()},{j.fn_mostrar_nombre_completo()},{j.fn_posicion()},{j.fn_puntaje_individual()},{j.fn_goles()},{j.fn_asistencias()}\n"
                archivo.write(linea)
        archivo.close()

    def __guardar_partidos_txt(self):
        
        archivo = open("partidos.txt", "w", encoding="utf-8")
        for g in self.__mundial.grupos:
            for p in g.partidos():
                linea = f"Grupos,{p.equipo_1.fn_nombre_del_pais()},{p.goles_equipo1},{p.equipo_2.fn_nombre_del_pais()},{p.goles_equipo2}\n"
                archivo.write(linea)
        for fase in self.__mundial.fases:
            for p in fase.partidos:
                linea = f"{fase.nombre_fase},{p.equipo_1.fn_nombre_del_pais()},{p.goles_equipo1},{p.equipo_2.fn_nombre_del_pais()},{p.goles_equipo2}"
                if p.penales1 != 0 or p.penales2 != 0:
                    linea = linea + f",Penales:{p.penales1}-{p.penales2}"
                archivo.write(linea + "\n")
        archivo.close()

    def __guardar_ranking_goleadores_txt(self):
        
        todos = []
        for s in self.__mundial.selecciones:
            for j in s.fn_jugadores():
                todos = todos + [(j, s.fn_nombre_del_pais())]

        n = len(todos)
        for i in range(n - 1):
            for k in range(n - 1 - i):
                if todos[k][0].fn_goles() < todos[k+1][0].fn_goles():
                    todos[k], todos[k+1] = todos[k+1], todos[k]

        archivo = open("ranking_goleadores.txt", "w", encoding="utf-8")
        archivo.write("Pos,Jugador,Seleccion,Goles\n")
        pos = 1
        for j, pais in todos:
            archivo.write(f"{pos},{j.fn_mostrar_nombre_completo()},{pais},{j.fn_goles()}\n")
            pos += 1
        archivo.close()

    def __guardar_ranking_selecciones_txt(self):
        
        sels = list(self.__mundial.selecciones)#lpo ha guardad
        n = len(sels)
        for i in range(n - 1):
            for k in range(n - 1 - i):
                gf_a = sels[k].fn_total_goles_favor()
                gf_b = sels[k+1].fn_total_goles_favor()
                dif_a = sels[k].fn_total_goles_favor() - sels[k].fn_total_goles_contra()
                dif_b = sels[k+1].fn_total_goles_favor() - sels[k+1].fn_total_goles_contra()
                if gf_a < gf_b or (gf_a == gf_b and dif_a < dif_b):
                    sels[k], sels[k+1] = sels[k+1], sels[k]

        archivo = open("ranking_selecciones.txt", "w", encoding="utf-8")
        archivo.write("Pos,Seleccion,GolesFavor,GolesContra,DiferenciaGoles\n")
        pos = 1
        for s in sels:
            dif = s.fn_total_goles_favor() - s.fn_total_goles_contra()
            archivo.write(f"{pos},{s.fn_nombre_del_pais()},{s.fn_total_goles_favor()},{s.fn_total_goles_contra()},{dif}\n")
            pos += 1
        archivo.close()


# ===================== INICIO =====================
if __name__ == "__main__":
    ventana = tk.Tk()
    app = Interfaz_Grafica(ventana)
