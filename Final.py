# from idlelib import __main__
# from operator import truediv
import tkinter
from operator import truediv

from customtkinter import *
from tkinter import *
from tkinter.ttk import Treeview, Style
from datetime import datetime #Libreria utilizada para validar las fechas

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
            ["01-04-2026", 21.5, 110.5],
            ["15-04-2026", 21.5, 108.0]
        ]
    },
    {
        "nombre": "Mariana Costa",
        "sesiones": [
            ["04-04-2026", 21.5, 25.0],
            ["11-04-2026", 6.0, 29.5],
            ["18-04-2026", 7.5, 36.0]
        ]
    },
{
        "nombre": "Karim Benzema",
        "sesiones": [
            ["18-12-2022", 5.0, 25.0],
            ["11-04-2026", 6.0, 29.5],
            ["18-04-2026", 7.5, 36.0]
        ]
    },
    {
        "nombre": "Lucas Benitez",
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
def buscar_por_fecha(fecha):  # esta funcion sirve para simplificar la funcion de modificar un entrenamiento por la fecha
    lista_atletas = []
    for atleta in BDD:  # ... basicamente, el usuario ve todos los atletas con fechas parecidas y elige le que quiere modificar
        for sesion in atleta["sesiones"]:
            if sesion[0] == fecha:
                lista_atletas.append(atleta)  # agregamos al atleta que tiene esa fecha en sus entrenamientos
    return (lista_atletas)# devuelve todos los atletas que tienen alguna sesion con la fecha ingresada


def modificar_sesion(nombre_atleta, sesion_vieja, nueva_sesion):
    for atleta in BDD:
        if atleta["nombre"] == nombre_atleta:
            # enumerate() devuelve la posición (i) y el elemento (sesion) al mismo tiempo.
            # lo usamos para saber exactamente qué índice de la lista tenemos que modificar.
            for i, sesion in enumerate(atleta["sesiones"]):
                if sesion[0] == sesion_vieja[0] and sesion[1] == sesion_vieja[1] and sesion[2] == sesion_vieja[2]:
                    atleta["sesiones"][i] = nueva_sesion # modificamos la sesion correspondiente del atleta correspondiente
    # recibe los indices de atleta y su sesion que debe ser cambiada y la reemplaza por una nueva


# --- ELIMINAR ENTRENAMIENTOS ---
def buscar_por_nombre(nombre):
    indice_atletas = []
    for j in BDD:  # ... basicamente, el usuario ve todos los atletas con nombres parecidas y elige al que le quiere borrar los entrenamientos
        if j["nombre"] == nombre:
            indice_atletas.append(j)  # agregamos la posicion del atleta que tiene esa fecha en sus entrenamientos
    return indice_atletas  # devuelve todos los atletas que tienen nombres parecidos


def eliminar_entrenamientos(nombre): #TODO: Hacer que funcione sin indice
    for i, atleta in enumerate(BDD):
        if atleta["nombre"] == nombre:
            cantidad_eliminados = len(BDD[i]["sesiones"])  # guardamos el largo de la lista de sesiones del atleta que seria la cantidad de sesiones que se van a borrar
            atleta["sesiones"] = []  # vaciamos/borramos sus sesiones
    return {"Cantida de sesiones eliminadas": cantidad_eliminados}  # FALTARIA AGREGAR EL RANGO DE FECHAS


# --- VOLUMEN TOTAL ACUMULADO ---
def volumen_total():
    volumenes_por_atleta = []
    for atleta in BDD:
        vol_total = 0
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
            elif sesion_mas_grande == sesion[1]:  # si son iguales entonces lo agregamos tambien a la lista sin borrar el otro (si un atleta tiene dos sesiones iguales, se agregan ambas porque tienen fechas distintas)
                atletas_con_sesion_mas_grande.append({"nombre": atleta["nombre"], "fecha": sesion[0]})
    return (atletas_con_sesion_mas_grande)

# --- MENCION DE HONOR ---
def mencion_de_honor(umbral_km): #TODO: Revisar por que solo muestra los nombres sin apellido (chequearlo con la terminal)
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
def calcular_velocidad(nombre_atleta):

    indice_atleta = 0

    # determinamos el indice del atleta con el nombre ingresado para usarlo mas adelante
    for i, atleta in enumerate(BDD):
        if atleta["nombre"] == nombre_atleta:
            indice_atleta = i
            break # detenemos el loop porque ya se encontro al atleta

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

def atleta_mas_veloz(umbral_km):

    atletas_en_umbral = []

    for atleta in BDD:
        sesiones_en_umbral = []
        for sesion in atleta["sesiones"]:
            if sesion[1] > umbral_km:
                sesiones_en_umbral.append(sesion)
        if len(sesiones_en_umbral) > 0: # si el atleta tiene sesiones por encima del umbral, aniadimos su nobmre y sesiones por encima del umbral a la lista
            atletas_en_umbral.append({"nombre": atleta["nombre"], "sesiones_en_umbral": sesiones_en_umbral})
        sesiones_en_umbral = [] # vaciamos la lista para seguir con el siguiente atleta

    velocidad_atletas = []

    # para los atletas y sus sesion dentro de umbral, definimos la velocidad para cada sesion y la
    # asociamos a su nombre en otro diccionario
    for atleta in atletas_en_umbral:
        for sesion in atleta["sesiones_en_umbral"]:
            velocidad_sesion_kmph = (sesion[1]) * 60 / sesion[2]
            velocidad_atletas.append({"nombre": atleta["nombre"], "velocidad": velocidad_sesion_kmph})

    atleta_mas_rapido = {"nombre": "", "velocidad": 0}

    # recorremos el diccionario de atletas y velocidad de sus sesiones buscando la mas rapida en ese umbral

    for atleta in velocidad_atletas:
        if atleta["velocidad"] > atleta_mas_rapido["velocidad"]:
            atleta_mas_rapido["nombre"] = atleta["nombre"]
            atleta_mas_rapido["velocidad"] = atleta["velocidad"]

    return atleta_mas_rapido



# --- FUNCIONES DE VALIDACION DE DATOS ---

def validar_fecha(fecha):
    try:
        fecha = datetime.strptime(fecha, "%d-%m-%Y") #Utilizando la libreria datetime, comprobamos que la fecha sea valida
        dia_actual = datetime.now() #Obtenemos la fecha actual
        if fecha <= dia_actual: #Comprobamos que la fecha ingresada no sea mayor a la actual
            return True
        else:
            return False
    except ValueError:
        return False

def validar_numero_positivo(num):
    try:
        num = int(num) #Intentamos convertir el numero ingresado a entero
        if num >= 0: #Compruebo que sea mayor o igual a 0
            return True
        else:
            return False
    except ValueError:
        return False #Se ingreso un tipo de dato que no se puede converir a entero (string, bool, etc)

def validar_texto(texto):
        #Con replace, eliminamos los espacios para que quede una unica cadena, ej: leo messi = leomessi
        #Con isalpha, comprobamos si son letras, cualquier otro tipo devolvera false
        return texto.replace(" ", "").isalpha()


#--- GRAFICOS INTERFAZ DE USUARIO ---

#Funcion para configurar ventanas de forma generica, objeto ventana y resolucion son requeridos,
#el titulo es opcional.
def configEstiloVentanas(ventana, resolucion , titulo):  # Funcion para definir el estilo inicial de todas las ventanas
    ventana.geometry(resolucion)
    ventana.title("Proyecto Final - PCT")
    ventana.config(background="purple")

    if titulo != "":  # Si la ventana requiere un titulo, se le agrega el mismo estilo
        tituloVentana = Label(ventana, text=titulo, wraplength=500 , fg="white", bg="purple", font=("Arial", 28))
        tituloVentana.pack(side="top", pady=20)  # Apilacion de titulo de las ventanas

def configBotonMenu(ventana, texto, comando):
    btn = CTkButton(ventana, text=texto, font=("Segoe UI", 20),
                command=comando, fg_color="#45098F",bg_color="purple",
                border_width=1,
                border_color="white",
                corner_radius=6,
                height=40)
    return btn

principal = CTk()  # Inicializacion de una instancia de la ventana principal
configEstiloVentanas(principal, "500x500", "Gestor Rendimiento de Atletas")  # Seteo de la ventana del menu principal

#--- VENTANAS DE EXITO O ERROR ---
def ventanaExitoError(mensaje, ventana):
    ventanaExitoError = Toplevel(ventana)
    configEstiloVentanas(ventanaExitoError,"600x350", "")
    descripcion = CTkLabel(ventanaExitoError, text=mensaje, wraplength=400, font=("Segoe UI", 22))
    btnCerrar = configBotonMenu(ventanaExitoError, "Cerrar", ventanaExitoError.destroy)
    descripcion.pack(pady=20)
    btnCerrar.pack(pady=20)

#Todas las funciones listadas debajo son llamadas por sus correspondientes botones en el menu principal

# Funcion para abrir la ventana de registro nuevo atleta
def abrirVentanaRegistro():
    #principal.withdraw()
    ventanaRegistro = Toplevel(principal)
    configEstiloVentanas(ventanaRegistro, "500x300" , "Registro de nuevo atleta")
    contenedor = Frame(ventanaRegistro, bg="purple") #Definimos el contenedor para que entry y boton queden en linea
    desc = Label(ventanaRegistro, text="Ingrese el nombre del atleta que desea registrar: ",
                 bg= "purple", fg="white", width=50,
                 wraplength=400, font=("Arial", 20))
    entradaNombre = Entry(contenedor, width=20, font=("Arial", 20))  # Campo de entrada para el nombre del nuevo atleta

    def obtenerDatos():  # Funcion para obtener los datos de la entrada (el nombre)
        nombre = entradaNombre.get()  # Obtengo el texto de la entrada
        if validar_texto(nombre):  # Chequeo que el nombre sea valido
            registrar_atleta(nombre)  # Registro el nuevo atleta utilizando la funcion previamente definida
            entradaNombre.delete(0, "end")  # Borro el contenido de la entrada
            ventanaExitoError("Atleta registrado correctamente.", ventanaRegistro)
        else:
            ventanaExitoError("Error: No se ha ingresado un nombre valido, vuelva a intentar.", ventanaRegistro)
    btnRegistro = configBotonMenu(contenedor, "Registro", obtenerDatos)

    desc.pack(side="top", pady=10)
    contenedor.pack(pady=10)
    entradaNombre.pack(side="left", padx=10)
    btnRegistro.pack(side="left", padx=10)

#Funcion para abrir la ventana de carga de nueva sesion de entrenamiento
def abrirVentanaCargas():
    ventanaCargas = Toplevel(principal)
    configEstiloVentanas(ventanaCargas, "600x600" , "Carga de nueva sesion")

    # Etiquetas para identificar cada entrada
    tituloNombre = Label(ventanaCargas, text="Ingrese el nombre del atleta (ej: Erling Haaland): ", width=50,
                         fg="white", bg="purple", font=("Arial", 18))
    tituloFecha = Label(ventanaCargas, text="Ingrese la fecha de la sesion (ej: 18-12-2022): ", width=50, fg="white",
                        bg="purple", font=("Arial", 18))
    tituloDistancia = Label(ventanaCargas, text="Ingrese la distancia recorrida en km (ej: 12.5): ", fg="white",
                            bg="purple", width=50, font=("Arial", 18))
    tituloTiempo = Label(ventanaCargas, text="Ingrese el tiempo medido en minutos (ej: 150): ", fg="white", bg="purple",
                         width=50, font=("Arial", 18))

    # Entradas para una nueva sesion de entrenamiento
    entradaNombre = Entry(ventanaCargas, width=30, font=("Arial", 18))
    entradaFecha = Entry(ventanaCargas, width=30, font=("Arial", 18))
    entradaDistancia = Entry(ventanaCargas, width=30, font=("Arial", 18))
    entradaTiempo = Entry(ventanaCargas, width=30, font=("Arial", 18))

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
        nombre = entradaNombre.get()
        fecha = entradaFecha.get()
        distancia = entradaDistancia.get()
        tiempo = entradaTiempo.get()

        #En cada bucle if, validamos si los datos ingresados son validos
        if validar_texto(nombre):
            if validar_fecha(fecha):
                sesion.append(fecha) #Como se ingreso una fecha valida, se agrega al array sesion
                if validar_numero_positivo(distancia):
                    sesion.append(float(distancia))
                    if validar_numero_positivo(tiempo):
                        sesion.append(float(tiempo))
                        cargar_entrenamiento(nombre, sesion) #Como todos son validos, cargamos la sesion
                        entradaNombre.delete(0, "end") #Borramos todas las entradas para despejarlas
                        entradaFecha.delete(0, "end")
                        entradaDistancia.delete(0, "end")
                        entradaTiempo.delete(0, "end")
                        ventanaExitoError("La sesion de entrenamiento se ha cargado con exito.", ventanaCargas)
                    else:
                        ventanaExitoError("Se ha ingresado un tiempo invalido, vuelva a intentar.", ventanaCargas)
                else:
                    ventanaExitoError("Se ha ingresado una distancia invalida, vuelva a intentar.", ventanaCargas)
            else:
                ventanaExitoError("Se ha ingresado una fecha invalida, vuelva a intentar.", ventanaCargas)
        else:
            ventanaExitoError("Se ha ingresado un nombre invalido, vuelva a intentar.", ventanaCargas)

    btnCarga = configBotonMenu(ventanaCargas, "Cargar sesion", carga)
    btnCarga.pack(side="top", pady=20)

#Funcion para abrir la ventana de busqueda y edicion de una sesion de entrenamiento
def abrirVentanaEditarSesion():
    ventanaEdicion = Toplevel(principal)
    configEstiloVentanas(ventanaEdicion, "900x800", "Modificar sesiones de entrenamiento")

    entradaFecha = Entry(ventanaEdicion, width=30,
                                        font=("Arial", 18))  # Le solicitamos al usuario la fecha que desea buscar
    entradaFecha.pack(side="top", pady=5)

    # Estilizamos la tabla
    estilo = Style()
    estilo.theme_use("default") #Utilizado por incompatibilidades con windows
    estilo.configure("Treeview", background="#9D6AE6", foreground="white", fieldbackground="#9D6AE6",
                     rowheight=40, borderwidth=0, font=("Arial", 18)) #Configuramos el estilo de las columnas
    estilo.configure("Treeview.Heading", background="#45098F", foreground="white",
                        borderwidth=0, font=("Arial", 22)) #Configuramos el estilo de los encabezados

    tablaSesiones = Treeview(ventanaEdicion, columns=("nombre", "fecha", "distancia", "tiempo"),
                             show="headings")  # Creacion de instancia de tabla para mostrar las sesiones
    tablaSesiones.heading("#1", text="Nombre")
    tablaSesiones.heading("#2", text="Fecha")
    tablaSesiones.heading("#3", text="Distancia")
    tablaSesiones.heading("#4", text="Tiempo")
    tablaSesiones.pack(side="top", pady=10)


    def buscarAtletas():  # Funcion para mostrar en la lista los entrenamientos realizados en la fecha indicada
        fecha = entradaFecha.get()  # Capturamos el contenido del input en el momento de apretar el boton
        entradaFecha.delete(0, "end") #Borramos el entry de fecha

        if validar_fecha(fecha):
            listaAtletas = buscar_por_fecha(fecha)  # Utilizamos la funcion definida previamente
            tablaSesiones.delete(*tablaSesiones.get_children()) #Borramos lo que haya en la tabla al momento de cargarla
            for atleta in listaAtletas:  # Accede a cada atleta de la lista que contiene los atletas con un entrenamiento en esa fecha
                for sesion in atleta["sesiones"]:  # Accede a cada sesion de entrenamiento
                    if sesion[
                        0] == fecha:  # Compara las sesiones de cada atleta que y filtra por las que coincidan con la fecha
                        tablaSesiones.insert("", END, values=(atleta["nombre"], sesion[0], sesion[1], sesion[2]))
        else:
            ventanaExitoError("Error: Ingrese una fecha valida y vuelva a intentarlo", ventanaEdicion)

    def editarSesion():
        seleccion = tablaSesiones.selection() #Guarda un array con la fila seleccionada

        if not seleccion:  # Verifica que se haya seleccionado una sesion en la lista
            ventanaExitoError("Error: No se selecciono ninguna sesion", ventanaEdicion)
            return  # Termina la funcion aca

        sesion = tablaSesiones.item(seleccion[0], "values") #Guardamos los datos de la fila seleccionada

        #Ejecutamos una nueva ventana estilo pop up para editar la sesion que elegimos
        ventanaEditarSesion = Toplevel(ventanaEdicion)
        configEstiloVentanas(ventanaEditarSesion, "600x400", "Editar sesion")

        # Etiquetas para identificar cada entrada
        tituloDistancia = Label(ventanaEditarSesion, text="Ingrese la distancia recorrida en km (ej: 12.5): ", fg="white", bg="purple", width=50, font=("Arial", 18))
        tituloTiempo = Label(ventanaEditarSesion, text="Ingrese el tiempo medido en minutos (ej: 150): ", fg="white", bg="purple", width=50, font=("Arial", 18))

        # Entradas para una nueva sesion de entrenamiento
        entradaDistancia = Entry(ventanaEditarSesion, width=30, font=("Arial", 18))
        entradaTiempo = Entry(ventanaEditarSesion, width=30, font=("Arial", 18))

        # Apilamiento de entradas y sus titulos correspondientes
        tituloDistancia.pack(side="top", pady=10)
        entradaDistancia.pack(side="top", pady=5)
        tituloTiempo.pack(side="top", pady=10)
        entradaTiempo.pack(side="top", pady=5)

        def ejecucionEdicion(sesion):
            if validar_numero_positivo(entradaDistancia.get()) and validar_numero_positivo(entradaTiempo.get()):
                nombre=sesion[0] #Almacenamos el nombre en la lista de la sesion indicada
                viejaSesion = [sesion[1], float(sesion[2]), float(sesion[3])] #Guardamos los datos de la sesion indicada
                nuevaSesion = [sesion[1],float(entradaDistancia.get()), float(entradaTiempo.get())] #Guardamos los datos tomados en los entry
                modificar_sesion(nombre, viejaSesion, nuevaSesion)
                ventanaExitoError("Se ha modificado correctamente la sesion de entrenamiento.", ventanaEditarSesion)
            else:
                ventanaExitoError("Ha ingresado una distancia o un tiempo invalido, vuelva a intentarlo.", ventanaEditarSesion)

        # Boton de editar
        btnEditar = configBotonMenu(ventanaEditarSesion, "Editar", lambda:ejecucionEdicion(sesion))
        btnEditar.pack(side="top", pady=10)

    contenedor = Frame(ventanaEdicion, bg="purple")  # Definimos el contenedor para que los botones queden alineados
    btnBuscarAtletas = configBotonMenu(contenedor, "Buscar", buscarAtletas)
    btnEditarSesion = configBotonMenu(contenedor, "Editar", editarSesion)

    contenedor.pack(pady=10)
    btnBuscarAtletas.pack(side="left", padx=10)
    btnEditarSesion.pack(side="left", padx=10)

#Funcion para abrir la ventana donde se puede eliminar todos los entrenamientos de un atleta
def abrirVentanaEliminarSesion():
    ventanaEliminacion = Toplevel(principal)
    configEstiloVentanas(ventanaEliminacion, "Eliminar sesion")

    titulo = Label(ventanaEliminacion, text="Ingrese el nombre del atleta que desea eliminar sus sesiones: ",
                   fg="white", bg="purple", font=("Arial", 12))
    nombre = Entry(ventanaEliminacion)
    titulo.pack(side="top", pady=10)
    nombre.pack(side="top", pady=5)

    def eliminarSesion():
        indice = buscar_por_nombre(nombre.get())
        print(indice)
        eliminar_entrenamientos(indice)

    btnEliminar = Button(ventanaEliminacion, text="Eliminar sesiones", fg="white", bg="purple", font=("Arial", 16),
              command=eliminarSesion)

    btnEliminar.pack(side="top", pady=5)

#Funcion que despliega un menu donde se pueden obtener los reportes y estadisticas buscados
def abrirVentanaReportes():
    ventanaReportes = Toplevel(principal)
    configEstiloVentanas(ventanaReportes, "500x550","Reportes y estadisticas")

    #Configuraremos los botones para acceder a cada visualizacion solicitada
    #Reporte volumen total
    def abrirVolumen():
        ventanaVolumenes = Toplevel(ventanaReportes)
        configEstiloVentanas(ventanaVolumenes, "500x700", "Volumen de distancia por atleta")

        # Estilizamos la tabla
        estilo = Style()
        estilo.theme_use("default")  # Utilizado por incompatibilidades con windows
        estilo.configure("Treeview", background="#9D6AE6", foreground="white", fieldbackground="#9D6AE6",
                         rowheight=40, borderwidth=0, font=("Arial", 18))  # Configuramos el estilo de las columnas
        estilo.configure("Treeview.Heading", background="#45098F", foreground="white",
                         borderwidth=0, font=("Arial", 22))  # Configuramos el estilo de los encabezados

        tabla = Treeview(ventanaVolumenes, columns=("nombre", "volumen_total"),
                             show="headings")  # Creacion de instancia de tabla para mostrar las sesiones
        tabla.heading("#1", text="Nombre")
        tabla.heading("#2", text="Voluemen Total")
        tabla.pack(side="top", pady=5)

        listaVolumenes = volumen_total() #Obtenemos el listado de volumen utilizando la funcion correspondiente
        for atleta in listaVolumenes:
            tabla.insert("", END, values=(atleta["nombre"], atleta["volumen_total"]))

        btnCerrar = configBotonMenu(ventanaVolumenes, "Cerrar", ventanaVolumenes.destroy)
        btnCerrar.pack(pady=20)

    #Reporte de records de distancia
    def abrirRecordDistancia():
        ventanaDistancias = Toplevel(ventanaReportes)
        configEstiloVentanas(ventanaDistancias, "500x700", "Atletas con el record de distancia recorrida")
        tabla = Treeview(ventanaDistancias, columns=("nombre", "fecha"),
                         show="headings")  # Creacion de instancia de tabla para mostrar las sesiones
        tabla.heading("#1", text="Nombre")
        tabla.heading("#2", text="Fecha")
        tabla.pack(side="top", pady=5)
        listaRecord = record_distancia()
        for atleta in listaRecord:
            tabla.insert("", END, values=(atleta["nombre"], atleta["fecha"]))

        btnCerrar = configBotonMenu(ventanaDistancias, "Cerrar", ventanaDistancias.destroy)
        btnCerrar.pack(pady=20)

    #Reporte de mencion de honor (atletas con sesiones mayores a un umbral)
    def abrirMencionHonor():
        ventanaHonor = Toplevel(ventanaReportes)
        configEstiloVentanas(ventanaHonor, "550x700", "Mencion de Honor")

        # Estilizamos la tabla
        estilo = Style()
        estilo.theme_use("default")  # Utilizado por incompatibilidades con windows
        estilo.configure("Treeview", background="#9D6AE6", foreground="white", fieldbackground="#9D6AE6",
                         rowheight=40, borderwidth=0, font=("Arial", 18))  # Configuramos el estilo de las columnas
        estilo.configure("Treeview.Heading", background="#45098F", foreground="white",
                         borderwidth=0, font=("Arial", 22))  # Configuramos el estilo de los encabezados

        tabla = Treeview(ventanaHonor, columns="nombre",
                         show="headings")  # Creacion de instancia de tabla para mostrar las sesiones
        tabla.heading("#1", text="Nombre")
        tabla.column("#1", width=400)
        tabla.pack(side="top", pady=5)

        def buscarMencion():
            umbral_km = umbral.get()
            if validar_numero_positivo(umbral_km):
                listaMencion = mencion_de_honor(float(umbral_km))
                tabla.delete(*tabla.get_children()) #Borramos lo que habia previamente
                for atleta in listaMencion:
                    tabla.insert("", END, value=atleta)
            else:
                ventanaExitoError("Ha ingresado un umbral invalido, vuelva a intentar.", ventanaHonor)

        contenedor = Frame(ventanaHonor, bg="purple")
        btnBuscar = configBotonMenu(contenedor, "Buscar", buscarMencion)
        titulo = Label(ventanaHonor, text="Ingrese el umbral que desea definir en km: ", fg="white", bg="purple",
                       width=50, font=("Arial", 18))
        umbral = Entry(contenedor, width=20, font=("Arial", 20))

        titulo.pack(side="top", pady=10)
        contenedor.pack(pady=10)
        umbral.pack(side="left", padx=10)
        btnBuscar.pack(side="left", padx=5)

    def abrirCalcularVel():
        ventanaCalcular = Toplevel(ventanaReportes)
        configEstiloVentanas(ventanaCalcular, "700x700", "Calcular velocidad")

        titulo = Label(ventanaCalcular, text="Ingrese el nombre del atleta que quiere calcular sus sesiones: ",
                       fg="white",
                       bg="purple",
                       width=50, font=("Arial", 18))
        nombreEntrada = Entry(ventanaCalcular, width=20, font=("Arial", 20))

        titulo.pack(pady=10)
        nombreEntrada.pack(pady=5)

        # Estilizamos la tabla
        estilo = Style()
        estilo.theme_use("default")  # Utilizado por incompatibilidades con windows
        estilo.configure("Treeview", background="#9D6AE6", foreground="white", fieldbackground="#9D6AE6",
                         rowheight=30, borderwidth=0, font=("Arial", 18))  # Configuramos el estilo de las columnas
        estilo.configure("Treeview.Heading", background="#45098F", foreground="white",
                         borderwidth=0, font=("Arial", 22))  # Configuramos el estilo de los encabezados

        tabla = Treeview(ventanaCalcular, columns=("km/h", "m/s"),
                         show="headings")  # Creacion de instancia de tabla para mostrar las sesiones
        tabla.heading("#1", text="Km/h")
        tabla.heading("#2", text="m/s")
        tabla.pack(side="top", pady=10)

        def calcularSesiones():
            nombre = nombreEntrada.get()
            if validar_texto(nombre):
                listaSesiones = calcular_velocidad(nombre)
                tabla.delete(*tabla.get_children())  # Borramos lo que habia previamente
                for sesion in listaSesiones[0]:
                    tabla.insert("", END, values=(sesion["vel_kmph"], sesion["vel_mps"]))
            else:
                ventanaExitoError("Error: Ha ingresado un nombre invalido, vuelva a intentarlo.", ventanaCalcular)

        def obtenerPromedio():
            nombre = nombreEntrada.get()
            if validar_texto(nombre):
                ventanaPromedio = Toplevel(ventanaCalcular)
                configEstiloVentanas(ventanaPromedio, "550x300", "Calculo de velocidad promedio")

                registro = calcular_velocidad(nombre)
                nombreL = Label(ventanaPromedio, text=f"Nombre: {nombre}", fg="white", bg="purple", width=50, font=("Arial", 18))
                promedio_kmh = Label(ventanaPromedio, text=f"Promedio en km/h: {registro[1]}", fg="white", bg="purple", width=50, font=("Arial", 18))
                promedio_ms = Label(ventanaPromedio, text=f"Promedio en m/s: {registro[2]}", fg="white", bg="purple", width=50, font=("Arial", 18))

                nombreL.pack(pady=10)
                promedio_kmh.pack(side="top", pady=10)
                promedio_ms.pack(side="top", pady=10)
            else:
                ventanaExitoError("Error: Ha ingresado un nombre invalido, vuelva a intentarlo.", ventanaCalcular)

        contenedor = Frame(ventanaCalcular, bg="purple")
        btnCalcular = configBotonMenu(contenedor, "Obtener velocidades", calcularSesiones)
        btnPromedio = configBotonMenu(contenedor, "Obtener promedio", obtenerPromedio)

        contenedor.pack(pady=10)
        btnCalcular.pack(side="left", padx=5)
        btnPromedio.pack(side="left", padx=5)

    def abrirAtletaVeloz():
        ventanaAtleta = Toplevel(ventanaReportes)
        configEstiloVentanas(ventanaAtleta, "600x300", "Obtener atleta mas veloz")

        def obtenerVeloz(num):
            if validar_numero_positivo(num):
                ventanaVeloz = Toplevel(ventanaAtleta)
                configEstiloVentanas(ventanaVeloz, "550x300", "Atleta mas veloz encontrado")

                atleta = atleta_mas_veloz(num)
                nombreL = Label(ventanaVeloz, text=f"Nombre: {atleta["nombre"]}", fg="white", bg="purple", width=50,
                                font=("Arial", 18))
                velocidad = Label(ventanaVeloz, text=f"Velocidad: {atleta["velocidad"]}", fg="white", bg="purple",
                                     width=50, font=("Arial", 18))
                nombreL.pack(pady=10)
                velocidad.pack(pady=10)
            else:
                ventanaExitoError("Error: Ha ingresado un minimo invalido, vuelva a intentarlo.", ventanaAtleta)

        contenedor = Frame(ventanaAtleta, bg="purple")
        titulo = Label(ventanaAtleta, text="Ingrese el umbral que desea definir en km: ", fg="white", bg="purple",
                       width=50, font=("Arial", 18))
        umbral = Entry(contenedor, width=20, font=("Arial", 20))
        btnBuscar = configBotonMenu(contenedor, "Buscar", lambda: obtenerVeloz(float(umbral.get())))

        titulo.pack(side="top", pady=10)
        contenedor.pack(pady=10)
        umbral.pack(side="left", padx=10)
        btnBuscar.pack(side="left", padx=5)


    btnVolumen = configBotonMenu(ventanaReportes, "Volumen total acumulado", abrirVolumen)
    btnVolumen.pack(side="top", pady=10)
    btnRecord = configBotonMenu(ventanaReportes, "Record de distancia", abrirRecordDistancia)
    btnRecord.pack(side="top", pady=10)
    btnMencion = configBotonMenu(ventanaReportes, "Mencion de Honor", abrirMencionHonor)
    btnMencion.pack(side="top", pady=10)
    btnCalculo = configBotonMenu(ventanaReportes, "Calcular velocidad", abrirCalcularVel)
    btnCalculo.pack(side="top", pady=10)
    btnVeloz = configBotonMenu(ventanaReportes, "Atleta mas veloz", abrirAtletaVeloz)
    btnVeloz.pack(side="top", pady=10)

#Funcion que cierra el menu principal
def cerrarMenu():
    principal.destroy()

#BOTONES DEL MENU PRINCIPAL
btn1 = configBotonMenu(principal, "Registrar nuevo atleta", abrirVentanaRegistro)
btn2 = configBotonMenu(principal, "Cargar nueva sesion de entrenamiento", abrirVentanaCargas)
btn3 = configBotonMenu(principal, "Buscar/Editar sesion de entrenamiento", abrirVentanaEditarSesion)
btn4 = configBotonMenu(principal, "Eliminar todas las sesiones de un atleta", abrirVentanaEliminarSesion)
btn5 = configBotonMenu(principal, "Visualizacion de reportes y estadisticas", abrirVentanaReportes)
btn6 = configBotonMenu(principal, "Salir del programa", cerrarMenu)

btn1.pack(side="top", pady=10)  # Apilacion de botones de la ventana principal
btn2.pack(side="top", pady=10)
btn3.pack(side="top", pady=10)
btn4.pack(side="top", pady=10)
btn5.pack(side="top", pady=10)
btn6.pack(side="top", pady=10)

principal.mainloop()  # Ejecucion bucle principal
