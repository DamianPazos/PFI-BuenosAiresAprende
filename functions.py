# Registro de producto
# TODO: Excepciones
def registro(almacenamiento):
    nombre = input('Ingrese el nombre del producto: ')
    precio = float(input('Ingrese el precio del producto: $'))
    stock = int(input('Ingrese la cantidad de stock del producto: '))
    
    producto_final = {
        'nombre': nombre,
        'precio' : precio,
        'stock': stock,
    }
    almacenamiento.append(producto_final)

# Modificacion de un producto
# TODO: Opcion salir
# TODO: Expeciones
def modificar(producto, almacenamiento):
    for producto_modificar in almacenamiento:
        if producto_modificar == producto:
            opcion_clave = int(input('Que desea modificar:\n1. Nombre\n2. Precio\n3. Stock\n'))
            if opcion_clave == 1:
                clave = 'nombre'
            elif opcion_clave == 2:
                clave = 'precio'
            elif opcion_clave == 3:
                clave = 'stock'
            new_valor = input('Ingrese el nuevo valor')
            producto_modificar[clave] = new_valor


# Busqueda de producto
def buscar(almacenamiento):
    valor = input('¿Que producto desea buscar?\n')
    for producto in almacenamiento:
        if producto['nombre'] == valor:
            return producto
    return None

# Eliminar producto
def eliminar(producto, almacenamiento):
    almacenamiento.remove(producto)

def enlistar(almacenamiento):
    contador = 1
    for producto in almacenamiento:
        print(f'Producto N°{contador}\n{producto}')
        contador = contador + 1


# Muestra menu principal
def mostrar_menu_principal ():
    print('MENU DE OPCIONES\n\n')
    print('1. Registrar producto\n2. Mostrar productos\n3. Eliminar producto\n4. Salir del programa\n\n')

'''
def menu_modificar():
    print('Que valor desea modificar\n1. Nombre\n2. Precio\n3. Stock\n4. Atras')
    opcion = int(input())
    if opcion == 1:
        return 'Nombre'
    elif opcion == 2:
        return 'Precio'
    elif opcion == 3:
        return 'Stock'
    else:
        pass'''