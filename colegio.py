import tkinter as tk
from tkinter import ttk, messagebox

# Definición de clases (mismas que en el código anterior)

class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.asignaturas = []

    def mostrar_info(self):
        asignaturas = ', '.join(asignatura.nombre for asignatura in self.asignaturas)
        return f"Profesor: {self.nombre} {self.apellido}\nAsignaturas: {asignaturas}"

class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante
        self.cursos = []

    def mostrar_info(self):
        cursos = ', '.join(curso.nombre for curso in self.cursos)
        return f"Estudiante: {self.nombre} {self.apellido}\nID: {self.id_estudiante}\nCursos: {cursos}"

class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    def mostrar_info(self):
        return f"Asignatura: {self.nombre}\nProfesor: {self.profesor.nombre} {self.profesor.apellido}"

class Evaluacion:
    def __init__(self, curso, estudiante, nota):
        self.curso = curso
        self.estudiante = estudiante
        self.nota = nota

    def mostrar_info(self):
        return f"Evaluación:\nCurso: {self.curso.nombre}\nEstudiante: {self.estudiante.nombre} {self.estudiante.apellido}\nNota: {self.nota}"

class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def mostrar_info(self):
        return f"Horario: {self.dia} de {self.hora_inicio} a {self.hora_fin}"

class Curso:
    def __init__(self, nombre, profesor, horario):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
        self.horario = horario

    def mostrar_info(self):
        estudiantes = ', '.join(estudiante.nombre for estudiante in self.estudiantes)
        return f"Curso: {self.nombre}\nProfesor: {self.profesor.nombre} {self.profesor.apellido}\nHorario: {self.horario.mostrar_info()}\nEstudiantes: {estudiantes}"

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.cursos.append(self)

# Biblioteca de Cursos
class SistemaAcademico:
    def __init__(self):
        self.cursos = []
        self.profesores = []
        self.estudiantes = []
        self.asignaturas = []
        self.evaluaciones = []

    def registrar_curso(self, curso):
        self.cursos.append(curso)

    def registrar_profesor(self, profesor):
        self.profesores.append(profesor)

    def registrar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def registrar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def registrar_evaluacion(self, evaluacion):
        self.evaluaciones.append(evaluacion)

    def mostrar_cursos(self):
        info = "Cursos:\n"
        for curso in self.cursos:
            info += curso.mostrar_info() + "\n"
        return info

    def mostrar_profesores(self):
        info = "Profesores:\n"
        for profesor in self.profesores:
            info += profesor.mostrar_info() + "\n"
        return info

    def mostrar_estudiantes(self):
        info = "Estudiantes:\n"
        for estudiante in self.estudiantes:
            info += estudiante.mostrar_info() + "\n"
        return info

# Funciones para la interfaz gráfica
def registrar_curso():
    nombre = entry_curso_nombre.get()
    profesor_nombre = entry_profesor_nombre.get()
    profesor_apellido = entry_profesor_apellido.get()
    dia = entry_horario_dia.get()
    hora_inicio = entry_horario_inicio.get()
    hora_fin = entry_horario_fin.get()

    profesor = next((p for p in sistema.profesores if p.nombre == profesor_nombre and p.apellido == profesor_apellido), None)
    if not profesor:
        profesor = Profesor(profesor_nombre, profesor_apellido)
        sistema.registrar_profesor(profesor)

    horario = Horario(dia, hora_inicio, hora_fin)
    curso = Curso(nombre, profesor, horario)
    sistema.registrar_curso(curso)
    messagebox.showinfo("Registro de Curso", "Curso registrado con éxito")

def registrar_profesor():
    nombre = entry_profesor_nombre.get()
    apellido = entry_profesor_apellido.get()

    profesor = Profesor(nombre, apellido)
    sistema.registrar_profesor(profesor)
    messagebox.showinfo("Registro de Profesor", "Profesor registrado con éxito")

def registrar_estudiante():
    nombre = entry_estudiante_nombre.get()
    apellido = entry_estudiante_apellido.get()
    id_estudiante = entry_id_estudiante.get()

    estudiante = Estudiante(nombre, apellido, int(id_estudiante))
    sistema.registrar_estudiante(estudiante)
    messagebox.showinfo("Registro de Estudiante", "Estudiante registrado con éxito")

def registrar_asignatura():
    nombre = entry_asignatura_nombre.get()
    profesor_nombre = entry_profesor_asignatura_nombre.get()
    profesor_apellido = entry_profesor_asignatura_apellido.get()

    profesor = next((p for p in sistema.profesores if p.nombre == profesor_nombre and p.apellido == profesor_apellido), None)
    if not profesor:
        messagebox.showerror("Error", "Profesor no encontrado")
        return

    asignatura = Asignatura(nombre, profesor)
    profesor.asignaturas.append(asignatura)
    sistema.registrar_asignatura(asignatura)
    messagebox.showinfo("Registro de Asignatura", "Asignatura registrada con éxito")

def registrar_evaluacion():
    curso_nombre = entry_evaluacion_curso.get()
    estudiante_id = entry_evaluacion_estudiante.get()
    nota = entry_evaluacion_nota.get()

    curso = next((c for c in sistema.cursos if c.nombre == curso_nombre), None)
    if not curso:
        messagebox.showerror("Error", "Curso no encontrado")
        return

    estudiante = next((e for e in sistema.estudiantes if e.id_estudiante == int(estudiante_id)), None)
    if not estudiante:
        messagebox.showerror("Error", "Estudiante no encontrado")
        return

    evaluacion = Evaluacion(curso, estudiante, nota)
    sistema.registrar_evaluacion(evaluacion)
    messagebox.showinfo("Registro de Evaluación", "Evaluación registrada con éxito")

def mostrar_cursos():
    info = sistema.mostrar_cursos()
    messagebox.showinfo("Cursos", info)

def mostrar_profesores():
    info = sistema.mostrar_profesores()
    messagebox.showinfo("Profesores", info)

def mostrar_estudiantes():
    info = sistema.mostrar_estudiantes()
    messagebox.showinfo("Estudiantes", info)

# Crear el sistema académico
sistema = SistemaAcademico()

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema Académico")
root.geometry("600x800")

# Estilo
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#007ACC", foreground="white", font=("Helvetica", 10))
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 10))
style.configure("TFrame", background="#f0f0f0")

# Crear el canvas y el scrollbar
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

canvas = tk.Canvas(main_frame, bg="#f0f0f0")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

second_frame = ttk.Frame(canvas)
canvas.create_window((0,0), window=second_frame, anchor="nw")

def crear_label(frame, text, row, column, pady=5, padx=5, sticky="w"):
    label = ttk.Label(frame, text=text)
    label.grid(row=row, column=column, pady=pady, padx=padx, sticky=sticky)
    return label

def crear_entry(frame, row, column, pady=5, padx=5):
    entry = ttk.Entry(frame)
    entry.grid(row=row, column=column, pady=pady, padx=padx, sticky="w")
    return entry

# Crear un frame para el registro de cursos
frame_cursos = ttk.LabelFrame(second_frame, text="Registro de Curso", padding=(10, 10))
frame_cursos.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_cursos, "Nombre del Curso", 0, 0)
entry_curso_nombre = crear_entry(frame_cursos, 0, 1)

crear_label(frame_cursos, "Profesor Nombre", 1, 0)
entry_profesor_nombre = crear_entry(frame_cursos, 1, 1)

crear_label(frame_cursos, "Profesor Apellido", 2, 0)
entry_profesor_apellido = crear_entry(frame_cursos, 2, 1)

crear_label(frame_cursos, "Horario Día", 3, 0)
entry_horario_dia = crear_entry(frame_cursos, 3, 1)

crear_label(frame_cursos, "Horario Inicio", 4, 0)
entry_horario_inicio = crear_entry(frame_cursos, 4, 1)

crear_label(frame_cursos, "Horario Fin", 5, 0)
entry_horario_fin = crear_entry(frame_cursos, 5, 1)

ttk.Button(frame_cursos, text="Registrar Curso", command=registrar_curso).grid(row=6, column=0, columnspan=2, pady=10)

# Crear un frame para el registro de profesores
frame_profesores = ttk.LabelFrame(second_frame, text="Registro de Profesor", padding=(10, 10))
frame_profesores.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_profesores, "Nombre", 0, 0)
entry_profesor_nombre = crear_entry(frame_profesores, 0, 1)

crear_label(frame_profesores, "Apellido", 1, 0)
entry_profesor_apellido = crear_entry(frame_profesores, 1, 1)

ttk.Button(frame_profesores, text="Registrar Profesor", command=registrar_profesor).grid(row=2, column=0, columnspan=2, pady=10)

# Crear un frame para el registro de estudiantes
frame_estudiantes = ttk.LabelFrame(second_frame, text="Registro de Estudiante", padding=(10, 10))
frame_estudiantes.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_estudiantes, "Nombre", 0, 0)
entry_estudiante_nombre = crear_entry(frame_estudiantes, 0, 1)

crear_label(frame_estudiantes, "Apellido", 1, 0)
entry_estudiante_apellido = crear_entry(frame_estudiantes, 1, 1)

crear_label(frame_estudiantes, "ID de Estudiante", 2, 0)
entry_id_estudiante = crear_entry(frame_estudiantes, 2, 1)

ttk.Button(frame_estudiantes, text="Registrar Estudiante", command=registrar_estudiante).grid(row=3, column=0, columnspan=2, pady=10)

# Crear un frame para el registro de asignaturas
frame_asignaturas = ttk.LabelFrame(second_frame, text="Registro de Asignatura", padding=(10, 10))
frame_asignaturas.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_asignaturas, "Nombre de la Asignatura", 0, 0)
entry_asignatura_nombre = crear_entry(frame_asignaturas, 0, 1)

crear_label(frame_asignaturas, "Profesor Nombre", 1, 0)
entry_profesor_asignatura_nombre = crear_entry(frame_asignaturas, 1, 1)

crear_label(frame_asignaturas, "Profesor Apellido", 2, 0)
entry_profesor_asignatura_apellido = crear_entry(frame_asignaturas, 2, 1)

ttk.Button(frame_asignaturas, text="Registrar Asignatura", command=registrar_asignatura).grid(row=3, column=0, columnspan=2, pady=10)

# Crear un frame para el registro de evaluaciones
frame_evaluaciones = ttk.LabelFrame(second_frame, text="Registro de Evaluación", padding=(10, 10))
frame_evaluaciones.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_evaluaciones, "Curso", 0, 0)
entry_evaluacion_curso = crear_entry(frame_evaluaciones, 0, 1)

crear_label(frame_evaluaciones, "Estudiante ID", 1, 0)
entry_evaluacion_estudiante = crear_entry(frame_evaluaciones, 1, 1)

crear_label(frame_evaluaciones, "Nota", 2, 0)
entry_evaluacion_nota = crear_entry(frame_evaluaciones, 2, 1)

ttk.Button(frame_evaluaciones, text="Registrar Evaluación", command=registrar_evaluacion).grid(row=3, column=0, columnspan=2, pady=10)

# Botones adicionales
ttk.Button(second_frame, text="Mostrar Cursos", command=mostrar_cursos).grid(row=5, column=0, padx=10, pady=5, sticky="ew")
ttk.Button(second_frame, text="Mostrar Profesores", command=mostrar_profesores).grid(row=6, column=0, padx=10, pady=5, sticky="ew")
ttk.Button(second_frame, text="Mostrar Estudiantes", command=mostrar_estudiantes).grid(row=7, column=0, padx=10, pady=5, sticky="ew")

# Iniciar el bucle principal de la interfaz
root.mainloop()
