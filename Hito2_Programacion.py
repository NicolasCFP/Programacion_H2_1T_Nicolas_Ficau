clientes = {} # Lista de clientes
pedidos = {} # Lista de pedidos 
productos = { #Libreria de productos
    1: {"nombre": "Manzanas", "precio": 1.0},# Manzanas y su precio
    2: {"nombre": "Limones", "precio": 2.0},# Limones y su precio
    3: {"nombre": "Peras", "precio": 3.50},# Peras y su precio
    4: {"nombre": "Sandias", "precio": 4.0},# Sandias y su precio
    5: {"nombre": "Naranjas", "precio": 2.50}# Naranjas y su precio
    }

contador_pedidos = 0 # Contador de los pedidos

def registrar_cliente(): # Definicion para registrar el cliente
    print("--Registro del cliente--") # Titulo del registro
    nombre = input("Ingrese su nombre:") # Input para ingresar el nombre 
    if nombre in clientes: # Si nombre esta dentro de clientes
        print("Este cliente ya está registrado.") # Le diremos al ususario que este usuario ya esta registrado
        return
    apellido = input("Ingrese su apellido:")# Le pediremos que ingrese el apellido, si el usuario no esta registrado
    telefono = input("Ingrese su número de teléfono:")# Le pediremos al usuario que ingrese su numero de telefono

    clientes[nombre] = {  # Usar la variable global clientes
        "nombre": nombre,# Variable nombre
        "apellido": apellido,# Variable apellido
        "telefono": telefono# Variable telefono
    }

    print("¡Registro completado con éxito!")# Le diremos al usuario que el registro se ha completado con exito

def mostrar_cliente(): #Definicion para mostrar el cliente
    print("--Lista de clientes--")# Titulo de la lista de clientes
    if not clientes:# Si no hay clientes
        print("No hay ningún cliente en nuestra lista.") # Mostrarle al suuario que no hay ningun cliente en nuestra lista
        return
    for nombre, datos in clientes.items(): # Para los datos de nombre en clientes hacer
        print(f"Nombre: {datos['nombre']}, Apellido: {datos['apellido']}, Teléfono: {datos['telefono']}")# Imprimir el Nombre el apellido y el telefono


def realizar_compra():
    global contador_pedidos  # Usar la variable global contador_pedidos
    print("--Compra--") # Titulo de compra 
    nombre = input("Ingrese su nombre:") # Input para ingresar el nombre
    if nombre not in clientes:# Si nombre no esta en clientes
        print("El cliente no está registrado.") # Mostrarle al usuario que el cliente no esta registrado 
        return
    print("Bienvenido, estos son los productos disponibles.") # Mostrarle al usuario los productos disponibles
    for id_producto, datos in productos.items(): # Para los productos de la lista de prodcutos hacer
        print(f"ID: {id_producto}, Nombre: {datos['nombre']}, Precio: {datos['precio']}") # Imprimir el nombre y el precio

    seleccion = input("Ingrese los ID de los productos que desea comprar (sepárelos por comas):") # Le pediremos al usuario que ingrese el ID de los porductos que quiere comprar
    ID_producto = [int(id) for id in seleccion.split(",") if int(id) in productos]# ID de los productos seleccionados

    if not ID_producto: # Si no esta en la lista de productos seleccionados
        print("Selección inválida.") #Le diremos al usuario que la selccion no es valida
        return

    total = sum(productos[id_producto]['precio'] for id_producto in ID_producto)  # Le pondremos el precio total
    numero_pedido = str(contador_pedidos)  # Convertiremos a string el numero del pedido
    contador_pedidos += 1  # y le añadiremos 1 al contador de pedidos

    pedidos[numero_pedido] = {# Segun el numero del pedido, le diremos
        "cliente": nombre, #El nombre del cliente
        "productos": ID_producto, # Los productos comprados
        "total": total # Y el total de precio
    }

    print(f"Compra realizada con éxito. Número de pedido: {numero_pedido}") # Le diremos al usuario que su compra ha sido realizada con exito y le diremos su numero de pedido para que pueda visualizarlo luego


def seguimiento_compra(): # Definicion del seguimiento de la compra
    print("--Seguimiento de compra--") # Titulo del seguimiento de la compra
    numero_pedido = input("Ingrese el número de pedido:") # Le pediremos el numero del pedido al usuario
    
    if numero_pedido not in pedidos: # Si el numero del pedido no contiene ningun pedido
        print("Pedido no encontrado.") # Le diremos al usuario que el pedido no se ha encontrado
        return

    pedido = pedidos[numero_pedido] #Si el pedido esta en la lista de pedidos
    cliente = clientes[pedido["cliente"]] # Le diremos al usuario el cliente del pedido
    
    print(f"Número de pedido: {numero_pedido}") # Le diremos el numero del pedido
    print(f"Cliente: {cliente['nombre']} {cliente['apellido']}, Teléfono: {cliente['telefono']}") # el nombre, apellidos y telefono de la persona que ha realizado el pedido
    print("Productos:") # Los productos que ha pedido 
    for id_producto in pedido["productos"]: # para el id de los prodcutos en el pedido
        producto = productos[id_producto] # Le diremos los productos
        print(f"{producto['nombre']}: {producto['precio']}") # El nombre y el precio del producto
    print(f"Total: {pedido['total']}") # Y le diremos el total de coste de su pedido 

def menu(): # Definicion del menu
    while True:# Mientras que sea verdadero
        print("--Menu de gestion de pedidos--") # Titulo de Gestion de pedidos 
        print("1. Registrar cliente") # Para registrar un cliente 
        print("2. Mostrar clientes")# Para mostrar los clientes 
        print("3. Realizar compra") # para realizar una compra 
        print("4. Seguimiento de pedido") # para seguir un pedido 
        print("5. Salir") # Para salir del programa
        
        opcion = input("Seleccione una opcion:") # Le pediremos al usuario que selccione una opcion 
        
        if opcion == "1": # Si la opcion es 1 
            registrar_cliente() # Se activara la funcion de registrar el cliente 
        elif opcion == "2":# Si la opcion es 2
            mostrar_cliente() # Se activara la funcion de mostrar un cliente
        elif opcion == "3":# Si la opcion es 3
            realizar_compra() # Se activara la funcion para realizar una compra
        elif opcion == "4":# Si la opcion es 4
            seguimiento_compra() # Se activara al funcion para el seguimiento de una compra 
        elif opcion == "5":# Si la opcion es 5
            print("¡Adios!")# Saldremos del programa 
            break
        else:
            print("Opción no valida. Porfavor, intentelo de nuevo")  # Si no es ninguna de esas opciones, le diremos al usuario que su opcion no es valida y que ol intente de nuevo 

#Ejecutar aplicacion 
menu()
