import tkinter as tk
from tkinter import messagebox

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_info(self):
        return f"Producto: {self.nombre}\nPrecio: ${self.precio:.2f}\nCategoría: {self.categoria.nombre}"

class Cliente:
    def __init__(self, nombre, apellido, id_cliente):
        self.nombre = nombre
        self.apellido = apellido
        self.id_cliente = id_cliente

    def mostrar_info(self):
        return f"Cliente: {self.nombre} {self.apellido}\nID de Cliente: {self.id_cliente}"

class ItemOrden:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad

class Orden:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []
        self.total = 0.0

    def agregar_item(self, item):
        self.items.append(item)
        self.calcular_total()

    def calcular_total(self):
        self.total = sum(item.calcular_subtotal() for item in self.items)

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Categoría: {self.nombre}"

class Tienda:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.ordenes = []
        self.categorias = []

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def crear_orden(self, cliente):
        orden = Orden(cliente)
        self.ordenes.append(orden)
        return orden

    def mostrar_productos(self):
        info = "Productos:\n"
        for producto in self.productos:
            info += producto.mostrar_info() + "\n"
        return info

# Funciones para la interfaz gráfica
def registrar_producto():
    nombre = entry_producto_nombre.get()
    precio = float(entry_producto_precio.get())
    categoria_nombre = entry_producto_categoria.get()

    categoria = next((cat for cat in tienda.categorias if cat.nombre == categoria_nombre), None)
    if not categoria:
        categoria = Categoria(categoria_nombre)
        tienda.categorias.append(categoria)

    producto = Producto(nombre, precio, categoria)
    tienda.registrar_producto(producto)
    messagebox.showinfo("Registro de Producto", "Producto registrado con éxito")

def registrar_cliente():
    nombre = entry_cliente_nombre.get()
    apellido = entry_cliente_apellido.get()
    id_cliente = int(entry_cliente_id.get())

    cliente = Cliente(nombre, apellido, id_cliente)
    tienda.registrar_cliente(cliente)
    messagebox.showinfo("Registro de Cliente", "Cliente registrado con éxito")

def crear_orden():
    cliente_id = int(entry_orden_cliente_id.get())
    cliente = next((cli for cli in tienda.clientes if cli.id_cliente == cliente_id), None)
    if cliente:
        orden = tienda.crear_orden(cliente)
        orden_items = [ItemOrden(item[0], item[1]) for item in orden_items]
        for item in orden_items:
            orden.agregar_item(item)
        messagebox.showinfo("Creación de Orden", f"Orden creada con éxito. Total: ${orden.total:.2f}")
    else:
        messagebox.showerror("Error", "Cliente no encontrado")

def agregar_item_orden():
    producto_nombre = entry_item_producto.get()
    cantidad = int(entry_item_cantidad.get())

    producto = next((prod for prod in tienda.productos if prod.nombre == producto_nombre), None)
    if producto:
        orden_items.append((producto, cantidad))
        listbox_items.insert(tk.END, f"{producto.nombre} x {cantidad}")
    else:
        messagebox.showerror("Error", "Producto no encontrado")

def mostrar_productos():
    info = tienda.mostrar_productos()
    messagebox.showinfo("Productos", info)

# Crear la tienda
tienda = Tienda()

# Crear la ventana principal
root = tk.Tk()
root.title("Tienda")
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
canvas.create_window((0, 0), window=second_frame, anchor="nw")

def crear_label(frame, text, row, column, pady=5, padx=5, sticky="w"):
    label = tk.Label(frame, text=text, bg="#f0f0f0", font=("Helvetica", 10))
    label.grid(row=row, column=column, pady=pady, padx=padx, sticky=sticky)
    return label

def crear_entry(frame, row, column, pady=5, padx=5):
    entry = tk.Entry(frame)
    entry.grid(row=row, column=column, pady=pady, padx=padx, sticky="w")
    return entry

# Crear un frame para el registro de productos
frame_productos = tk.LabelFrame(second_frame, text="Registro de Producto", padx=10, pady=10, bg="#f0f0f0", font=("Helvetica", 12))
frame_productos.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_productos, "Nombre", 0, 0)
entry_producto_nombre = crear_entry(frame_productos, 0, 1)

crear_label(frame_productos, "Precio", 1, 0)
entry_producto_precio = crear_entry(frame_productos, 1, 1)

crear_label(frame_productos, "Categoría", 2, 0)
entry_producto_categoria = crear_entry(frame_productos, 2, 1)

tk.Button(frame_productos, text="Registrar Producto", command=registrar_producto, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=3, column=0, columnspan=2, pady=10)

# Crear un frame para el registro de clientes
frame_clientes = tk.LabelFrame(second_frame, text="Registro de Cliente", padx=10, pady=10, bg="#f0f0f0", font=("Helvetica", 12))
frame_clientes.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_clientes, "Nombre", 0, 0)
entry_cliente_nombre = crear_entry(frame_clientes, 0, 1)

crear_label(frame_clientes, "Apellido", 1, 0)
entry_cliente_apellido = crear_entry(frame_clientes, 1, 1)

crear_label(frame_clientes, "ID de Cliente", 2, 0)
entry_cliente_id = crear_entry(frame_clientes, 2, 1)

tk.Button(frame_clientes, text="Registrar Cliente", command=registrar_cliente, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=3, column=0, columnspan=2, pady=10)

# Crear un frame para crear órdenes
frame_ordenes = tk.LabelFrame(second_frame, text="Creación de Orden", padx=10, pady=10, bg="#f0f0f0", font=("Helvetica", 12))
frame_ordenes.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

crear_label(frame_ordenes, "ID de Cliente", 0, 0)
entry_orden_cliente_id = crear_entry(frame_ordenes, 0, 1)

orden_items = []
listbox_items = tk.Listbox(frame_ordenes, height=5)
listbox_items.grid(row=1, column=0, columnspan=2, pady=5)

crear_label(frame_ordenes, "Producto", 2, 0)
entry_item_producto = crear_entry(frame_ordenes, 2, 1)

crear_label(frame_ordenes, "Cantidad", 3, 0)
entry_item_cantidad = crear_entry(frame_ordenes, 3, 1)

tk.Button(frame_ordenes, text="Agregar Item", command=agregar_item_orden, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(frame_ordenes, text="Crear Orden", command=crear_orden, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=5, column=0, columnspan=2, pady=10)

# Botones adicionales
tk.Button(second_frame, text="Mostrar Productos", command=mostrar_productos, bg="#007ACC", fg="white", font=("Helvetica", 10)).grid(row=3, column=0, padx=10, pady=5, sticky="ew")

# Iniciar el bucle principal de la interfaz
root.mainloop()
