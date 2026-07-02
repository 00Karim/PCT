# from idlelib import __main__
# from operator import truediv
import tkinter
from tkinter import *
from tkinter.ttk import Treeview

BDD = [
    {
        "nombre": "Carlos Mendoza",
        "sesiones": [
            ["05-04-2026", 10.0, 45.5],
            ["12-04-2026", 12.5, 60.0],
            ["19-04-2026", 15.0, 72.3]
        ]
    },
    {
        "nombre": "Sofía Rodríguez",
        "sesiones": [
            ["02-04-2026", 8.0, 40.0],
            ["09-04-2026", 8.5, 41.2],
            ["19-04-2026", 10.0, 48.5]
        ]
    },
    {
        "nombre": "Alejandro Silva",
        "sesiones": [
            ["01-04-2026", 21.0, 110.5],
            ["15-04-2026", 21.5, 108.0]
        ]
    },
    {
        "nombre": "Mariana Costa",
        "sesiones": [
            ["04-04-2026", 5.0, 25.0],
            ["11-04-2026", 6.0, 29.5],
            ["18-04-2026", 7.5, 36.0]
        ]
    },
    {
        "nombre": "Lucas Benítez",
        "sesiones": [
            ["08-04-2026", 14.0, 65.0],
            ["22-04-2026", 16.5, 78.2]
        ]
    }
]


def registrar_atleta(nombre):
    sesiones = []  # <-- lista vacia para guardar sesiones del atleta
    BDD.append(
        {"nombre": nombre, "sesiones": sesiones})  # agregamos una lista con nombre y lista de sesiones al final de BDD


def cargar_entrenamiento(nombre, sesion):
    for j in BDD:
        if j["nombre"] == nombre:  # busca al atleta con el nombre ingresado...
            j["sesiones"].append(sesion)  # ...y le agrega su sesion de entrenamiento a la lista de sesiones.


# --- MODIFICAR SESION ---
def buscar_por_fecha(
        fecha):  # esta funcion sirve para simplificar la funcion de modificar un entrenamiento por la fecha
    lista_atletas = []
    for atleta in BDD:  # ... basicamente, el usuario ve todos los atletas con fechas parecidas y elige le que quiere modificar
        for sesion in atleta["sesiones"]:
            if sesion[0] == fecha:
                lista_atletas.append(
                    atleta)  # agregamos la posicion del atleta que tiene esa fecha en sus entrenamientos
    return lista_atletas  # devuelve todos los atletas que tienen alguna sesion con la fecha ingresada


def modificar_sesion(indice_atleta, indice_sesion, nueva_sesion):
    BDD[indice_atleta]["sesiones"][indice_sesion] = nueva_sesion
    # recibe los indices de atleta y su sesion que debe ser cambiada y la reemplaza por una nueva


# --- ELIMINAR ENTRENAMIENTOS ---
def buscar_por_nombre(nombre):
    indice_atletas = []
    for j in BDD:  # ... basicamente, el usuario ve todos los atletas con nombres parecidas y elige al que le quiere borrar los entrenamientos
        if j["nombre"] == nombre:
            indice_atletas.append(j)  # agregamos la posicion del atleta que tiene esa fecha en sus entrenamientos
    return indice_atletas  # devuelve todos los atletas que tienen nombres parecidos


def eliminar_entrenamientos(indice_atleta):
    cantidad_eliminados = len(BDD[
                                  indice_atleta].sesiones)  # guardamos el largo de la lista de sesiones del atleta que seria la cantidad de sesiones que se van a borrar
    BDD[indice_atleta].sesiones = []  # vaciamos/borramos sus sesiones
    return {"Cantida de sesiones eliminadas": cantidad_eliminados}  # FALTARIA AGREGAR EL RANGO DE FECHAS


# --- VOLUMEN TOTAL ACUMULADO ---
def volumen_total():
    vol_total = 0
    volumenes_por_atleta = []
    for atleta in BDD:
        for sesion in atleta["sesiones"]:  #
            vol_total += sesion[
                1]  # 1 es la posicion (indice) de los km en la lista sesion. Vamos sumando el km de la sesion seleccionada a lo anterior
        volumenes_por_atleta.append({"nombre": atleta["nombre"], "volumen_total": vol_total})
    return volumenes_por_atleta  # Devolvemos los volumenes para cada atleta (por nombre)


# --- RECORD DE DISTANCIA ---
def record_distancia():  # Devuelve diccionario con nombre del atleta con la sesion en km mas larga y la fecha de esa sesion
    sesion_mas_grande = 0  # hacemos que la sesion mas grande sea 0 para comparar con las sesiones de los atletas
    atletas_con_sesion_mas_grande = []  # es una lista porque puede haber mas de 1 atleta con esa distancia
    for atleta in BDD:
        for sesion in atleta["sesiones"]:
            if sesion_mas_grande < sesion[1]:  # si la sesion es mas grande:
                sesion_mas_grande = sesion[1]  # 1 - cambiamos el valor con el que comparamos
                atletas_con_sesion_mas_grande = []  # vaciamos la lista por si se habian agregado atletas antes
                atletas_con_sesion_mas_grande.append({"nombre": atleta["nombre"], "fecha": sesion[0]})
            if sesion_mas_grande == sesion[
                1]:  # si son iguales entonces lo agregamos tambien a la lista sin borrar el otro (si un atleta tiene dos sesiones iguales, se agregan ambas porque tienen fechas distintas)
                atletas_con_sesion_mas_grande.append({"nombre": atleta["nombre"], "fecha": sesion[0]})
    return (atletas_con_sesion_mas_grande)


# --- MENCION DE HONOR ---
def mencion_de_honor(umbral_km):
    atletas_por_encima_de_umbral = []
    for atleta in BDD:
        while True:
            for sesion in atleta["sesiones"]:
                if sesion[1] > umbral_km:
                    atletas_por_encima_de_umbral.append(atleta["nombre"])
                    break  # una vez que lo agregamos salimos del loop y seguimos con el siguiente atleta porque si este atleta
                    # ... tiene mas de una sesion mayor al umbral entonces se lo agregaria dos veces y seria redundante
            break  # se recorrieron todas las sesiones entonces se sale del while loop para seguir con siguiente atleta
    return (atletas_por_encima_de_umbral)


# --- CALCULAR VELOCIDAD ---
def calcular_velocidad(indice_atleta):
    velocidad_en_kmph = 0
    velocidad_en_mps = 0
    numero_sesion = 0
    registro_sesiones = []
    for sesion in BDD[indice_atleta]["sesiones"]:  # creamos el array con la informacion de la velocidad por cada sesion
        numero_sesion += 1
        velocidad_en_kmph = (sesion[1]) * 60 / sesion[2]
        velocidad_en_mps = (sesion[1] * 1000) / (sesion[2] * 60)
        registro_sesiones.append(
            {"numero_sesion": numero_sesion, "vel_kmph": velocidad_en_kmph, "vel_mps": velocidad_en_mps})
    for registro_sesion in registro_sesiones:  # calculamos el total de velocidades para despues sacar el promedio
        velocidad_en_kmph += registro_sesion["vel_kmph"]
        velocidad_en_mps += registro_sesion["vel_mps"]
    if numero_sesion != 0:  # si no tiene sesiones entonces no hacemos las divisiones asi no nos da error
        promedio_kmph = velocidad_en_kmph / numero_sesion  # sacamos los promedios con la velocidad total y la cantidad de sesiones que tiene el atleta
        promedio_mps = velocidad_en_mps / numero_sesion
    return ([registro_sesiones, promedio_kmph, promedio_mps])


# Funciones para validacion de datos

# def validar_numero_positivo(num):


if __name__ == "__main__":
    for i in BDD:
        print(i["nombre"])
    registrar_atleta("Prueba Pruebosa")
    for i in BDD:
        print(i["nombre"])


# BASE DE DATOS (estructura y elementos) (va a ser un diccionario de atletas):
#
#
#
#
#

# FUNCIONES
#   Carga de registros
#       registrarAtleta(lista, nombre_atleta) --> cargar nuevo atleta validando que no exista su nombre
#                                                 previamente
#
#       cargarEntrenamiento(lista(lista de los atletas), nombre_atleta, sesion(fecha, distancia, tiempo))
#
#
#
#   Modificacion de registros
#       buscarFecha(fecha) -->
#                         ingresa fecha y en la UI se muestran todos los atletas que tengan entrenamientos
#                         que coincidan con esa fecha. En la UI el usuario puede ingresar un numero para
#                         elegir el atleta al que le quiere modificar la fecha, luego se muestra la lista
#                         de fechas del atleta que coinciden con la ingresada y se elige una. La funcion
#                         devuelve el indice del atleta y el indice de la fecha.

#       modificarSesion(indice_atleta, indice_entrenamiento, nueva_sesion) -->
#                         Recibe el indice del atleta, el indice del entrenamiento del atleta con esa fecha y
#                         el parametro con la nueva sesion
#
#   Eliminar entrenamientos de un atleta
#       eliminarEntrenamientos(lista,nombre_atleta) --> ingresa el nombre del atleta y elimina todos los entrenamientos
#                                                       almacenados en el mismo. Ademas, devuelve un registro con la
#                                                       cantidad de entrenamientos eliminados y el rango de fechas
#
#   Visualizar reportes y estadisticas
#       mostrarAtletas() --> Muestra a los atleta en UI con su indice a la izquierda
#
#       volumenAcumulado(lista) --> suma la cantidad de km recorridos por atleta en todas las sesionres registradas,
#                                   para luego sumar el total de todos los ateltas y retornar esa sumatoria
#
#       recordDistancia(lista) --> vemos como hacerlo xd
#
#       mencionDeHonor(umbral) --> Recibe el umbral te da la lista con los nombres e indice del atleta
#
#       calcularVelocidad(indice_atleta) --> Muestra a todos los atletas en UI y te deja elegir uno para
#                                             mostrar su velocidad por sesion y su velocidad promedio km/h m/s
#
#       atletaMasVeloz(minimaDistancia) --> Mostrar cual es el atleta mas rapido que recorrio al menos la
#                                           minimaDistancia ingresada por el usuario
#
#       salirDelPrograma() --> Sale del while loop
#
# ESTRUCTURA DEL MENU
# 1. Registrar nuevo atleta [registrarAtleta()]
# 2. Cargar nuevo entrenamiento [cargarEntrenamiento()]
# 3. Buscar/Editar un entrenamiento [buscarFecha()][modificarFecha()]
# 4. Eliminar todos los entrenamientos de un atleta (generando un reporte)
# 5. Visualizar reportes y estadisticas
## 5.1 Volumen total acumulado
## 5.2 Record de distanciacc
## 5.3 Mencion de honor
## 5.4 Calcular velocidad
## 5.5 Atleta mas veloz
# 6. Salir del programa

# GRAFICOS INTERFAZ DE USUARIO
# CONFIGURACION INTERFAZ PANTALLA PRINCIPAL

def configEstiloVentanas(ventana, titulo):  # Funcion para definir el estilo inicial de todas las ventanas
    ventana.geometry("1000x1000")
    ventana.title("Proyecto Final - PCT")
    ventana.config(background="purple")

    if titulo != "":  # Si la ventana requiere un titulo, se le agrega el mismo estilo
        tituloVentana = Label(ventana, text=titulo, fg="white", bg="purple", font=("Arial", 20))
        tituloVentana.pack(side="top", pady=20)  # Apilacion de titulo de las ventanas


principal = Tk()  # Inicializacion de una instancia de la ventana principal
configEstiloVentanas(principal, "Gestor Rendimiento de Atletas")  # Seteo de la ventana del menu principal


# Funcion para ejecutar la ventana de registro de nuevo atleta, sera utilizada en el boton correspondiente
def abrirVentanaRegistro():
    ventanaRegistro = Toplevel(principal)
    configEstiloVentanas(ventanaRegistro, "Registro de nuevo atleta")

    entradaNombre = Entry(ventanaRegistro, width=30,
                          font=("Arial", 14))  # Campo de entrada para el nombre del nuevo atleta

    def obtenerDatos():  # Funcion para obtener los datos de la entrada (el nombre)
        nombre = entradaNombre.get()  # Obtengo el texto de la entrada
        if nombre != "":  # Se guardara el nuevo atleta unicamente si el campo no esta vacio
            registrar_atleta(nombre)  # Registro el nuevo atleta utilizando la funcion previamente definida
            entradaNombre.delete(0, "end")  # Borro el contenido de la entrada
            print("Atleta registrado correctamente")  # Eliminar esta y las dos lineas de abajo
            for i in BDD:
                print(i["nombre"])

    btnRegistro = Button(ventanaRegistro, text="Registro", command=obtenerDatos)

    entradaNombre.pack(side="top", pady=20)
    btnRegistro.pack(side="top", pady=20)


def abrirVentanaCargas():
    ventanaCargas = Toplevel(principal)
    configEstiloVentanas(ventanaCargas, "Carga de nueva sesion")

    # Etiquetas para identificar cada entrada
    tituloNombre = Label(ventanaCargas, text="Ingrese el nombre del atleta (ej: Erling Haaland): ", width=50,
                         fg="white", bg="purple", font=("Arial", 12))
    tituloFecha = Label(ventanaCargas, text="Ingrese la fecha de la sesion (ej: 18-12-2022): ", width=50, fg="white",
                        bg="purple", font=("Arial", 12))
    tituloDistancia = Label(ventanaCargas, text="Ingrese la distancia recorrida en km (ej: 12.5): ", fg="white",
                            bg="purple", width=50, font=("Arial", 12))
    tituloTiempo = Label(ventanaCargas, text="Ingrese el tiempo medido en minutos (ej: 150): ", fg="white", bg="purple",
                         width=50, font=("Arial", 12))

    # Entradas para una nueva sesion de entrenamiento
    entradaNombre = Entry(ventanaCargas, width=30, font=("Arial", 12))
    entradaFecha = Entry(ventanaCargas, width=30, font=("Arial", 12))
    entradaDistancia = Entry(ventanaCargas, width=30, font=("Arial", 12))
    entradaTiempo = Entry(ventanaCargas, width=30, font=("Arial", 12))

    # Apilamiento de entradas y sus titulos correspondientes
    tituloNombre.pack(side="top", pady=10)
    entradaNombre.pack(side="top", pady=5)
    tituloFecha.pack(side="top", pady=10)
    entradaFecha.pack(side="top", pady=5)
    tituloDistancia.pack(side="top", pady=10)
    entradaDistancia.pack(side="top", pady=5)
    tituloTiempo.pack(side="top", pady=10)
    entradaTiempo.pack(side="top", pady=5)

    def carga():
        sesion = []  # Declaramos una nueva lista de sesion
        # Aca habria que verificar que la entrada sea valida utilizando la funcion correspondiente
        sesion.append(entradaFecha.get())

        distancia = float(entradaDistancia.get())
        entradaTiempo.delete(0, "end")
        if distancia <= 0:  # Esta validacion y la de abajo habria que hacer una funcion para chequear ingreso de numeros positivos
            print("Distancia incorrecta")
        else:
            sesion.append(distancia)

        tiempo = float(entradaDistancia.get())
        entradaDistancia.delete(0, "end")
        if tiempo <= 0:
            print("Tiempo incorrecto")
        else:
            sesion.append(tiempo)

        nombre = entradaNombre.get()
        if nombre == "":  # Esta validacion habria que crear una funcion general para chequear ingreso de cadenas
            print("El nombre es necesario")
        else:
            cargar_entrenamiento(nombre, sesion)
            for i in BDD:  # Con este bucle buscamos las sesiones del atleta ingresado
                if i["nombre"] == nombre:
                    print(i["sesiones"])

    btnCarga = Button(ventanaCargas, text="Carga", command=carga, font=("Arial", 12))
    btnCarga.pack(side="top", pady=20)


def abrirVentanaEditarSesion():
    ventanaEdicion = Toplevel(principal)
    configEstiloVentanas(ventanaEdicion, "Modificar sesiones de entrenamiento")

    entradaFecha = Entry(ventanaEdicion, width=30,
                         font=("Arial", 12))  # Le solicitamos al usuario la fecha que desea buscar
    entradaFecha.pack(side="top", pady=5)

    tablaSesiones = Treeview(ventanaEdicion, columns=("nombre", "fecha", "distancia", "tiempo"),
                             show="headings")  # Creacion de instancia de tabla para mostrar las sesiones
    tablaSesiones.heading("#1", text="Nombre")
    tablaSesiones.heading("#2", text="Fecha")
    tablaSesiones.heading("#3", text="Distancia")
    tablaSesiones.heading("#4", text="Tiempo")
    tablaSesiones.pack(side="top", pady=5)

    def buscarAtletas():  # Funcion para mostrar en la lista los entrenamientos realizados en la fecha indicada
        fecha = entradaFecha.get()  # Capturamos el contenido del input en el momento de apretar el boton
        entradaFecha.delete(0, "end")

        listaAtletas = buscar_por_fecha(fecha)
        for atleta in listaAtletas:  # Accede a cada atleta de la lista que contiene los atletas con un entrenamiento en esa fecha
            for sesion in atleta["sesiones"]:  # Accede a cada sesion de entrenamiento
                if sesion[
                    0] == fecha:  # Compara las sesiones de cada atleta que y filtra por las que coincidan con la fecha
                    tablaSesiones.insert("", END, values=(atleta["nombre"], sesion[0], sesion[1], sesion[2]))

    def editarSesion():
        sesion = tablaSesiones.selection()

        if not sesion:  # Verifica que se haya seleccionado una sesion
            print("Error: No se selecciono ninguna sesion")
            return  # Termina la funcion aca

    btnBuscarAtletas = Button(ventanaEdicion, text="Buscar", command=buscarAtletas, font=("Arial", 12))
    btnBuscarAtletas.pack(side="top", pady=5)

    btnEditarSesion = Button(ventanaEdicion, text="Editar", command=editarSesion, font=("Arial", 12))
    btnEditarSesion.pack(side="top", pady=5)


btn1 = Button(principal, text="Registrar nuevo atleta", fg="white", bg="purple", font=("Arial", 14),
              command=abrirVentanaRegistro)
btn2 = Button(principal, text="Cargar nueva sesion entrenamiento", fg="white", bg="purple", font=("Arial", 14),
              command=abrirVentanaCargas)
btn3 = Button(principal, text="Buscar/Editar sesion entrenamiento", fg="white", bg="purple", font=("Arial", 14),
              command=abrirVentanaEditarSesion)
btn4 = Button(principal, text="Eliminar todas las sesiones de un atleta", fg="white", bg="purple", font=("Arial", 14))
btn5 = Button(principal, text="Visualizacion de reportes y estadisticas", fg="white", bg="purple", font=("Arial", 14))
btn6 = Button(principal, text="Salir del programa", fg="white", bg="purple", font=("Arial", 14))

btn1.pack(side="top", pady=10)  # Apilacion de botones de la ventana principal
btn2.pack(side="top", pady=10)
btn3.pack(side="top", pady=10)
btn4.pack(side="top", pady=10)
btn5.pack(side="top", pady=10)
btn6.pack(side="top", pady=10)

principal.mainloop()  # Ejecucion bucle principal
