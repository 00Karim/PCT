# from idlelib import __main__
# from operator import truediv
import tkinter
from customtkinter import *
from tkinter import *
from tkinter.ttk import Treeview
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
def buscar_por_fecha(fecha):  # esta funcion sirve para simplificar la funcion de modificar un entrenamiento por la fecha
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
    cantidad_eliminados = len(BDD[indice_atleta].sesiones)  # guardamos el largo de la lista de sesiones del atleta que seria la cantidad de sesiones que se van a borrar
    BDD[indice_atleta].sesiones = []  # vaciamos/borramos sus sesiones
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

print(validar_fecha("18-12-2022")) #TODO: Borrar los chequeos de numeros y fechas
print(validar_numero_positivo(19))
print(validar_numero_positivo(-20))
print(validar_texto(" "))

#if __name__ == "__main__":
#    for i in BDD:
#        print(i["nombre"])
#    registrar_atleta("Prueba Pruebosa")
#    for i in BDD:
#        print(i["nombre"])

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
    configEstiloVentanas(ventanaRegistro, "500x200" , "Registro de nuevo atleta")
    contenedor = Frame(ventanaRegistro, bg="purple") #Definimos el contenedor para que entry y boton queden en linea
    desc = Label(ventanaRegistro, text="Ingrese el nombre del atleta que desea registrar: ",
                 bg= "purple", fg="white", width=50,
                 wraplength=400, font=("Arial", 20))
    entradaNombre = Entry(contenedor, width=30, font=("Arial", 14))  # Campo de entrada para el nombre del nuevo atleta

    def obtenerDatos():  # Funcion para obtener los datos de la entrada (el nombre)
        nombre = entradaNombre.get()  # Obtengo el texto de la entrada
        if validar_texto(nombre):  # Chequeo que el nombre sea valido
            registrar_atleta(nombre)  # Registro el nuevo atleta utilizando la funcion previamente definida
            entradaNombre.delete(0, "end")  # Borro el contenido de la entrada
            ventanaExitoError("Atleta registrado correctamente.", ventanaRegistro)
        else:
            ventanaExitoError("Error: No se ha ingresado un nombre valido, vuelva a intentar.", ventanaRegistro)
    btnRegistro = Button(contenedor, text="Registro", command=obtenerDatos)

    desc.pack(side="top", pady=10)
    contenedor.pack(pady=10)
    entradaNombre.pack(side="left", padx=10)
    btnRegistro.pack(side="left", padx=10)

#Funcion para abrir la ventana de carga de nueva sesion de entrenamiento
def abrirVentanaCargas():
    ventanaCargas = Toplevel(principal)
    configEstiloVentanas(ventanaCargas, "500x500" , "Carga de nueva sesion")

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
        nombre = entradaNombre.get()
        fecha = entradaFecha.get()
        print(fecha)
        print(validar_fecha(fecha))
        distancia = entradaDistancia.get()
        tiempo = entradaTiempo.get()

        #En cada bucle if, validamos si los datos ingresados son validos
        if validar_texto(nombre): #TODO: Crear validacion de atleta en la base de datos
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


    btnCarga = Button(ventanaCargas, text="Cargar sesion", command=carga, font=("Arial", 12))
    btnCarga.pack(side="top", pady=20)

#Funcion para abrir la ventana de busqueda y edicion de una sesion de entrenamiento
def abrirVentanaEditarSesion():
    ventanaEdicion = Toplevel(principal)
    configEstiloVentanas(ventanaEdicion, "900x500", "Modificar sesiones de entrenamiento")

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
        entradaFecha.delete(0, "end") #Borramos el entry de fecha

        listaAtletas = buscar_por_fecha(fecha) #Utilizamos la funcion definida previamente
        for atleta in listaAtletas:  # Accede a cada atleta de la lista que contiene los atletas con un entrenamiento en esa fecha
            for sesion in atleta["sesiones"]:  # Accede a cada sesion de entrenamiento
                if sesion[0] == fecha:  # Compara las sesiones de cada atleta que y filtra por las que coincidan con la fecha
                    for f in tablaSesiones.get_children(): #Bucle for para eliminar los datos que hayan en la tabla previamente
                        tablaSesiones.delete(f)
                    tablaSesiones.insert("", END, values=(atleta["nombre"], sesion[0], sesion[1], sesion[2]))

    def editarSesion():
        seleccion = tablaSesiones.selection() #Devuelve un array con la posicion del la fila seleccionada

        if not seleccion:  # Verifica que se haya seleccionado una sesion
            print("Error: No se selecciono ninguna sesion")
            return  # Termina la funcion aca

        sesion = tablaSesiones.item(seleccion[0], "values") #Guardamos los datos de la fila seleccionada

        #Ejecutamos una nueva ventana estilo pop up para editar la sesion que elegimos
        ventanaEditarSesion = Toplevel(ventanaEdicion)
        configEstiloVentanas(ventanaEditarSesion, "500x500", "Editar sesion")

        # Etiquetas para identificar cada entrada
        tituloDistancia = Label(ventanaEditarSesion, text="Ingrese la distancia recorrida en km (ej: 12.5): ", fg="white", bg="purple", width=50, font=("Arial", 12))
        tituloTiempo = Label(ventanaEditarSesion, text="Ingrese el tiempo medido en minutos (ej: 150): ", fg="white", bg="purple", width=50, font=("Arial", 12))

        # Entradas para una nueva sesion de entrenamiento
        entradaDistancia = Entry(ventanaEditarSesion, width=30, font=("Arial", 12))
        entradaTiempo = Entry(ventanaEditarSesion, width=30, font=("Arial", 12))

        # Apilamiento de entradas y sus titulos correspondientes
        tituloDistancia.pack(side="top", pady=10)
        entradaDistancia.pack(side="top", pady=5)
        tituloTiempo.pack(side="top", pady=10)
        entradaTiempo.pack(side="top", pady=5)

        # Boton de editar TODO: Editar la funcion de modificar sesion, que funcione sin indices
        btnEditar = Button(ventanaEditarSesion, text="Editar", command=lambda: modificar_sesion(sesion[0], sesion[1], [entradaDistancia.get(), entradaTiempo.get()]), font=("Arial", 12))
        btnEditar.pack(side="top", pady=5)


    btnBuscarAtletas = Button(ventanaEdicion, text="Buscar", command=buscarAtletas, font=("Arial", 12))
    btnBuscarAtletas.pack(side="top", pady=5)

    btnEditarSesion = Button(ventanaEdicion, text="Editar", command=editarSesion, font=("Arial", 12))
    btnEditarSesion.pack(side="top", pady=5)

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
        eliminar_entrenamientos(indice) #TODO: No funciona, la funcion buscar por nombre no devuelve un indice sino un diccionario

    btnEliminar = Button(ventanaEliminacion, text="Eliminar sesiones", fg="white", bg="purple", font=("Arial", 16),
              command=eliminarSesion)

    btnEliminar.pack(side="top", pady=5)

#Funcion que despliega un menu donde se pueden obtener los reportes y estadisticas buscados
def abrirVentanaReportes():
    ventanaReportes = Toplevel(principal)
    configEstiloVentanas(ventanaReportes, "400x500","Reportes y estadisticas")

    #Configuraremos los botones para acceder a cada visualizacion solicitada
    #Reporte volumen total
    def abrirVolumen():
        ventanaVolumenes = Toplevel(ventanaReportes)
        configEstiloVentanas(ventanaVolumenes, "500x500", "Volumen de distancia por atleta")
        tabla = Treeview(ventanaVolumenes, columns=("nombre", "volumen_total"),
                             show="headings")  # Creacion de instancia de tabla para mostrar las sesiones
        tabla.heading("#1", text="Nombre")
        tabla.heading("#2", text="Voluemn Total")
        tabla.pack(side="top", pady=5)
        listaVolumenes = volumen_total()
        for atleta in listaVolumenes:
            tabla.insert("", END, values=(atleta["nombre"], atleta["volumen_total"]))

    #Reporte de records de distancia
    def abrirRecordDistancia():
        ventanaDistancias = Toplevel(ventanaReportes)
        configEstiloVentanas(ventanaDistancias, "500x500", "Atletas con el record de distancia recorrida")
        tabla = Treeview(ventanaDistancias, columns=("nombre", "fecha"),
                         show="headings")  # Creacion de instancia de tabla para mostrar las sesiones
        tabla.heading("#1", text="Nombre")
        tabla.heading("#2", text="Fecha")
        tabla.pack(side="top", pady=5)
        listaRecord = record_distancia()
        for atleta in listaRecord:
            tabla.insert("", END, values=(atleta["nombre"], atleta["fecha"]))

    #Reporte de mencion de honor (atletas con sesiones mayores a un umbral)
    def abrirMencionHonor():
        ventanaHonor = Toplevel(ventanaReportes)
        configEstiloVentanas(ventanaHonor, "500x500", "Mencion de Honor")

        titulo = Label(ventanaHonor, text="Ingrese el umbral que desea definir en km: ", fg="white", bg="purple", width=50, font=("Arial", 12))
        umbral = Entry(ventanaHonor, width=20, font=("Arial", 12))
        titulo.pack(side="top", pady=5)
        umbral.pack(side="top", pady=5)

        lista = Listbox(ventanaHonor, height=15, width=50)
        lista.pack(side="top", pady=5)

        def buscarMencion():
            umbral_km = umbral.get()
            listaMencion = mencion_de_honor(float(umbral_km))
            for atleta in listaMencion:
                lista.insert(END, atleta)

        btnBuscar = Button(ventanaHonor, text="Buscar", command=buscarMencion)
        btnBuscar.pack(side="top", pady=5)


    btnVolumen = Button(ventanaReportes, text="Volumen", command=abrirVolumen)
    btnVolumen.pack(side="top", pady=10)
    btnRecord = Button(ventanaReportes, text="Record Distancia", command=abrirRecordDistancia)
    btnRecord.pack(side="top", pady=10)
    btnMencion = Button(ventanaReportes, text="Mencion de Honor", command=abrirMencionHonor)
    btnMencion.pack(side="top", pady=10)

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
