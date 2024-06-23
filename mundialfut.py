import tkinter as tk
from tkinter import messagebox
import random

class Jugador:
    def __init__(self, nombre, edad, posicion):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion

    def mostrar_info(self):
        return f"Jugador: {self.nombre}, Edad: {self.edad}, Posición: {self.posicion}"

class Equipo:
    def __init__(self, nombre, entrenador):
        self.nombre = nombre
        self.entrenador = entrenador
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_info(self):
        info = f"Equipo: {self.nombre}\nEntrenador: {self.entrenador}\nJugadores:\n"
        for jugador in self.jugadores:
            info += jugador.mostrar_info() + "\n"
        return info

class Estadio:
    def __init__(self, nombre, ciudad, capacidad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad

    def mostrar_info(self):
        return f"Estadio: {self.nombre}, Ciudad: {self.ciudad}, Capacidad: {self.capacidad}"

class Partido:
    def __init__(self, equipo_local, equipo_visitante, estadio):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.estadio = estadio
        self.resultado = None

    def jugar_partido(self):
        resultado_local = random.randint(0, 5)
        resultado_visitante = random.randint(0, 5)
        self.resultado = f"{resultado_local} - {resultado_visitante}"

    def mostrar_resultado(self):
        if self.resultado:
            return f"{self.equipo_local.nombre} {self.resultado} {self.equipo_visitante.nombre} en {self.estadio.nombre}"
        else:
            return "El partido no ha sido jugado aún"

class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def mostrar_info(self):
        info = f"Grupo: {self.nombre}\nEquipos:\n"
        for equipo in self.equipos:
            info += f"{equipo.nombre}\n"
        return info

class Mundial:
    def __init__(self):
        self.grupos = []
        self.estadios = []
        self.partidos = []

    def registrar_grupo(self, grupo):
        self.grupos.append(grupo)

    def registrar_estadio(self, estadio):
        self.estadios.append(estadio)

    def generar_fixture(self):
        for grupo in self.grupos:
            equipos = grupo.equipos
            for i in range(len(equipos)):
                for j in range(i + 1, len(equipos)):
                    estadio = random.choice(self.estadios)
                    partido = Partido(equipos[i], equipos[j], estadio)
                    self.partidos.append(partido)

    def mostrar_fixture(self):
        info = "Fixture del Mundial:\n"
        for partido in self.partidos:
            info += partido.mostrar_resultado() + "\n"
        return info

# Funciones para la interfaz gráfica
def registrar_equipo():
    nombre = entry_equipo_nombre.get()
    entrenador = entry_equipo_entrenador.get()
    equipo = Equipo(nombre, entrenador)
    mundial.registrar_equipo(equipo)
    messagebox.showinfo("Registro de Equipo", "Equipo registrado con éxito")

def agregar_jugador():
    nombre_equipo = entry_jugador_equipo.get()
    equipo = next((e for e in mundial.equipos if e.nombre == nombre_equipo), None)
    if equipo:
        nombre = entry_jugador_nombre.get()
        edad = int(entry_jugador_edad.get())
        posicion = entry_jugador_posicion.get()
        jugador = Jugador(nombre, edad, posicion)
        equipo.agregar_jugador(jugador)
        messagebox.showinfo("Registro de Jugador", "Jugador registrado con éxito")
    else:
        messagebox.showerror("Error", "Equipo no encontrado")

def registrar_estadio():
    nombre = entry_estadio_nombre.get()
    ciudad = entry_estadio_ciudad.get()
    capacidad = int(entry_estadio_capacidad.get())
    estadio = Estadio(nombre, ciudad, capacidad)
    mundial.registrar_estadio(estadio)
    messagebox.showinfo("Registro de Estadio", "Estadio registrado con éxito")

def registrar_grupo():
    nombre = entry_grupo_nombre.get()
    grupo = Grupo(nombre)
    mundial.registrar_grupo(grupo)
    messagebox.showinfo("Registro de Grupo", "Grupo registrado con éxito")

def agregar_equipo_a_grupo():
    nombre_grupo = entry_grupo_nombre_asignar.get()
    nombre_equipo = entry_grupo_equipo_asignar.get()
    grupo = next((g for g in mundial.grupos if g.nombre == nombre_grupo), None)
    equipo = next((e for e in mundial.equipos if e.nombre == nombre_equipo), None)
    if grupo and equipo:
        grupo.agregar_equipo(equipo)
        messagebox.showinfo("Asignar Equipo a Grupo", "Equipo asignado al grupo con éxito")
    else:
        messagebox.showerror("Error", "Grupo o Equipo no encontrado")

def generar_fixture():
    mundial.generar_fixture()
    messagebox.showinfo("Fixture", "Fixture generado con éxito")

def mostrar_fixture():
    info = mundial.mostrar_fixture()
    messagebox.showinfo("Fixture", info)

# Crear el mundial
mundial = Mundial()

# Crear la ventana principal
root = tk.Tk()
root.title("Mundial de Fútbol")
root.geometry("400x700")
root.configure(bg="#f0f0f0")

# Crear el canvas y el scrollbar
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(fill=tk.BOTH, expand=1)

canvas = tk.Canvas(main_frame, bg="#f0f0f0")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

second_frame = tk.Frame(canvas, bg="#f0f0f0")

canvas.create_window((0,0), window=second_frame, anchor="nw")

def crear_label(frame, text, row, column, pady=5, padx=5, sticky="w"):
    label = tk.Label(frame, text=text, bg="#f0f0f0", font=("Helvetica", 10))
    label.grid(row=row, column=column, pady=pady, padx=padx, sticky=sticky)
    return label

def crear_entry(frame, row, column, pady=5, padx=5):
    entry = tk.Entry(frame)
    entry.grid(row=row, column=column, pady=pady, padx=padx, sticky="w")
    return entry

# Crear un frame para el registro de equipos
frame_equipos = tk.LabelFrame(second_frame, text="Registro de Equipo", padx=10, pady=10, bg="#f0f0f0", font=("Helvetica", 12))
frame_equipos.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_equipos, "Nombre del Equipo", 0, 0)
entry_equipo_nombre = crear_entry(frame_equipos, 0, 1)

crear_label(frame_equipos, "Entrenador", 1, 0)
entry_equipo_entrenador = crear_entry(frame_equipos, 1, 1)

tk.Button(frame_equipos, text="Registrar Equipo", command=registrar_equipo, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=2, column=0, columnspan=2, pady=10)

# Crear un frame para agregar jugadores
frame_jugadores = tk.LabelFrame(second_frame, text="Agregar Jugador", padx=10, pady=10, bg="#f0f0f0", font=("Helvetica", 12))
frame_jugadores.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_jugadores, "Nombre del Equipo", 0, 0)
entry_jugador_equipo = crear_entry(frame_jugadores, 0, 1)

crear_label(frame_jugadores, "Nombre del Jugador", 1, 0)
entry_jugador_nombre = crear_entry(frame_jugadores, 1, 1)

crear_label(frame_jugadores, "Edad", 2, 0)
entry_jugador_edad = crear_entry(frame_jugadores, 2, 1)

crear_label(frame_jugadores, "Posición", 3, 0)
entry_jugador_posicion = crear_entry(frame_jugadores, 3, 1)

tk.Button(frame_jugadores, text="Agregar Jugador", command=agregar_jugador, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=4, column=0, columnspan=2, pady=10)

# Crear un frame para el registro de estadios
frame_estadios = tk.LabelFrame(second_frame, text="Registro de Estadio", padx=10, pady=10, bg="#f0f0f0", font=("Helvetica", 12))
frame_estadios.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_estadios, "Nombre del Estadio", 0, 0)
entry_estadio_nombre = crear_entry(frame_estadios, 0, 1)

crear_label(frame_estadios, "Ciudad", 1, 0)
entry_estadio_ciudad = crear_entry(frame_estadios, 1, 1)

crear_label(frame_estadios, "Capacidad", 2, 0)
entry_estadio_capacidad = crear_entry(frame_estadios, 2, 1)

tk.Button(frame_estadios, text="Registrar Estadio", command=registrar_estadio, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=3, column=0, columnspan=2, pady=10)

# Crear un frame para el registro de grupos
frame_grupos = tk.LabelFrame(second_frame, text="Registro de Grupo", padx=10, pady=10, bg="#f0f0f0", font=("Helvetica", 12))
frame_grupos.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_grupos, "Nombre del Grupo", 0, 0)
entry_grupo_nombre = crear_entry(frame_grupos, 0, 1)

tk.Button(frame_grupos, text="Registrar Grupo", command=registrar_grupo, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=1, column=0, columnspan=2, pady=10)

# Crear un frame para asignar equipos a grupos
frame_asignar = tk.LabelFrame(second_frame, text="Asignar Equipo a Grupo", padx=10, pady=10, bg="#f0f0f0", font=("Helvetica", 12))
frame_asignar.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_asignar, "Nombre del Grupo", 0, 0)
entry_grupo_nombre_asignar = crear_entry(frame_asignar, 0, 1)

crear_label(frame_asignar, "Nombre del Equipo", 1, 0)
entry_grupo_equipo_asignar = crear_entry(frame_asignar, 1, 1)

tk.Button(frame_asignar, text="Asignar Equipo", command=agregar_equipo_a_grupo, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=2, column=0, columnspan=2, pady=10)

# Botones adicionales
tk.Button(second_frame, text="Generar Fixture", command=generar_fixture, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=5, column=0, padx=10, pady=5, sticky="ew")
tk.Button(second_frame, text="Mostrar Fixture", command=mostrar_fixture, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=6, column=0, padx=10, pady=5, sticky="ew")

# Iniciar el bucle principal de la interfaz
root.mainloop()
