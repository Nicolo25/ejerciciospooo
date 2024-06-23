import tkinter as tk
from tkinter import messagebox
import datetime

class Libro:
    def __init__(self, titulo, isbn, autor, categoria):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.categoria = categoria
        self.prestado = False

    def mostrar_info(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"Libro: {self.titulo}\nISBN: {self.isbn}\nAutor: {self.autor.nombre} {self.autor.apellido}\nCategoría: {self.categoria.nombre}\nEstado: {estado}"

class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_info(self):
        return f"Autor: {self.nombre} {self.apellido}"

class Usuario:
    def __init__(self, nombre, apellido, id_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = id_usuario
        self.prestamos = []

    def mostrar_info(self):
        info = f"Usuario: {self.nombre} {self.apellido}\nID de usuario: {self.id_usuario}\nPréstamos:\n"
        for prestamo in self.prestamos:
            info += prestamo.mostrar_info() + "\n"
        return info

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion=None):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        info = f"Préstamo:\nLibro: {self.libro.titulo}\nUsuario: {self.usuario.nombre} {self.usuario.apellido}\nFecha de préstamo: {self.fecha_prestamo}\n"
        if self.fecha_devolucion:
            info += f"Fecha de devolución: {self.fecha_devolucion}\n"
        else:
            info += "Libro aún no devuelto\n"
        return info

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Categoría: {self.nombre}"

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def realizar_prestamo(self, usuario, libro):
        if libro.prestado:
            return f"El libro '{libro.titulo}' ya ha sido prestado"
        prestamo = Prestamo(libro, usuario, datetime.datetime.now())
        usuario.prestamos.append(prestamo)
        self.prestamos.append(prestamo)
        libro.prestado = True
        return f"Préstamo realizado para {usuario.nombre} {usuario.apellido} con el libro {libro.titulo}"

    def devolver_libro(self, prestamo):
        prestamo.fecha_devolucion = datetime.datetime.now()
        prestamo.libro.prestado = False
        return f"Libro {prestamo.libro.titulo} devuelto por {prestamo.usuario.nombre} {prestamo.usuario.apellido}"

    def mostrar_libros(self):
        info = "Libros disponibles:\n"
        for libro in self.libros:
            info += libro.mostrar_info() + "\n"
        return info

    def mostrar_usuarios(self):
        info = "Usuarios registrados:\n"
        for usuario in self.usuarios:
            info += usuario.mostrar_info() + "\n"
        return info

    def mostrar_libros_prestados(self):
        info = "Libros Prestados:\n"
        for prestamo in self.prestamos:
            if not prestamo.fecha_devolucion:
                info += prestamo.mostrar_info() + "\n"
        return info

# Funciones para la interfaz gráfica
def registrar_libro():
    titulo = entry_titulo.get()
    isbn = entry_isbn.get()
    autor_nombre = entry_autor_nombre.get()
    autor_apellido = entry_autor_apellido.get()
    categoria_nombre = entry_categoria.get()

    autor = Autor(autor_nombre, autor_apellido)
    categoria = Categoria(categoria_nombre)
    libro = Libro(titulo, isbn, autor, categoria)

    biblioteca.registrar_libro(libro)
    messagebox.showinfo("Registro de Libro", "Libro registrado con éxito")

def registrar_usuario():
    nombre = entry_usuario_nombre.get()
    apellido = entry_usuario_apellido.get()
    id_usuario = entry_id_usuario.get()

    usuario = Usuario(nombre, apellido, int(id_usuario))
    biblioteca.registrar_usuario(usuario)
    messagebox.showinfo("Registro de Usuario", "Usuario registrado con éxito")

def realizar_prestamo():
    id_usuario = entry_id_prestamo_usuario.get()
    titulo_libro = entry_titulo_prestamo.get()

    usuario = next((u for u in biblioteca.usuarios if u.id_usuario == int(id_usuario)), None)
    libro = next((l for l in biblioteca.libros if l.titulo == titulo_libro), None)

    if usuario and libro:
        resultado = biblioteca.realizar_prestamo(usuario, libro)
        messagebox.showinfo("Préstamo", resultado)
    elif not usuario:
        messagebox.showerror("Error", "Usuario no encontrado")
    elif not libro:
        messagebox.showerror("Error", "Libro no encontrado")

def devolver_libro():
    id_usuario = entry_id_devolucion_usuario.get()
    titulo_libro = entry_titulo_devolucion.get()

    usuario = next((u for u in biblioteca.usuarios if u.id_usuario == int(id_usuario)), None)
    if usuario:
        prestamo = next((p for p in usuario.prestamos if p.libro.titulo == titulo_libro), None)
        if prestamo:
            resultado = biblioteca.devolver_libro(prestamo)
            messagebox.showinfo("Devolución", resultado)
        else:
            messagebox.showerror("Error", "Préstamo no encontrado")
    else:
        messagebox.showerror("Error", "Usuario no encontrado")

def mostrar_libros():
    info = biblioteca.mostrar_libros()
    messagebox.showinfo("Libros Disponibles", info)

def mostrar_usuarios():
    info = biblioteca.mostrar_usuarios()
    messagebox.showinfo("Usuarios Registrados", info)

def mostrar_libros_prestados():
    info = biblioteca.mostrar_libros_prestados()
    messagebox.showinfo("Libros Prestados", info)

# Crear la biblioteca
biblioteca = Biblioteca()

# Crear la ventana principal
root = tk.Tk()
root.title("Biblioteca")
root.geometry("400x600")
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

# Crear un frame para el registro de libros
frame_libros = tk.LabelFrame(second_frame, text="Registro de Libro", padx=10, pady=10, bg="#f0f0f0", font=("Helvetica", 12))
frame_libros.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_libros, "Título", 0, 0)
entry_titulo = crear_entry(frame_libros, 0, 1)

crear_label(frame_libros, "ISBN", 1, 0)
entry_isbn = crear_entry(frame_libros, 1, 1)

crear_label(frame_libros, "Autor Nombre", 2, 0)
entry_autor_nombre = crear_entry(frame_libros, 2, 1)

crear_label(frame_libros, "Autor Apellido", 3, 0)
entry_autor_apellido = crear_entry(frame_libros, 3, 1)

crear_label(frame_libros, "Categoría", 4, 0)
entry_categoria = crear_entry(frame_libros, 4, 1)

tk.Button(frame_libros, text="Registrar Libro", command=registrar_libro, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=5, column=0, columnspan=2, pady=10)

# Crear un frame para el registro de usuarios
frame_usuarios = tk.LabelFrame(second_frame, text="Registro de Usuario", padx=10, pady=10, bg="#f0f0f0", font=("Helvetica", 12))
frame_usuarios.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_usuarios, "Nombre", 0, 0)
entry_usuario_nombre = crear_entry(frame_usuarios, 0, 1)

crear_label(frame_usuarios, "Apellido", 1, 0)
entry_usuario_apellido = crear_entry(frame_usuarios, 1, 1)

crear_label(frame_usuarios, "ID de Usuario", 2, 0)
entry_id_usuario = crear_entry(frame_usuarios, 2, 1)

tk.Button(frame_usuarios, text="Registrar Usuario", command=registrar_usuario, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=3, column=0, columnspan=2, pady=10)

# Crear un frame para realizar préstamos
frame_prestamos = tk.LabelFrame(second_frame, text="Realizar Préstamo", padx=10, pady=10, bg="#f0f0f0", font=("Helvetica", 12))
frame_prestamos.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_prestamos, "ID Usuario", 0, 0)
entry_id_prestamo_usuario = crear_entry(frame_prestamos, 0, 1)

crear_label(frame_prestamos, "Título Libro", 1, 0)
entry_titulo_prestamo = crear_entry(frame_prestamos, 1, 1)

tk.Button(frame_prestamos, text="Realizar Préstamo", command=realizar_prestamo, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=2, column=0, columnspan=2, pady=10)

# Crear un frame para devolver libros
frame_devoluciones = tk.LabelFrame(second_frame, text="Devolver Libro", padx=10, pady=10, bg="#f0f0f0", font=("Helvetica", 12))
frame_devoluciones.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_devoluciones, "ID Usuario", 0, 0)
entry_id_devolucion_usuario = crear_entry(frame_devoluciones, 0, 1)

crear_label(frame_devoluciones, "Título Libro", 1, 0)
entry_titulo_devolucion = crear_entry(frame_devoluciones, 1, 1)

tk.Button(frame_devoluciones, text="Devolver Libro", command=devolver_libro, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=2, column=0, columnspan=2, pady=10)

# Botones adicionales
tk.Button(second_frame, text="Mostrar Libros", command=mostrar_libros, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=4, column=0, padx=10, pady=5, sticky="ew")
tk.Button(second_frame, text="Mostrar Usuarios", command=mostrar_usuarios, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=5, column=0, padx=10, pady=5, sticky="ew")
tk.Button(second_frame, text="Mostrar Libros Prestados", command=mostrar_libros_prestados, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=6, column=0, padx=10, pady=5, sticky="ew")

# Iniciar el bucle principal de la interfaz
root.mainloop()
