# Registro de producto
def registro(almacenamiento):
    nombre = input('Ingrese el nombre del producto: ')
    precio = float(input('Ingrese el precio del producto: $'))
    stock = int(input('Ingrese la cantidad de stock del producto: '))
    
    producto = {
        'nombre': nombre,
        'precio' : precio,
        'stock': stock,
    }
    almacenamiento.append(producto)

def modificar(clave, valor, almacenamiento):
    for producto in almacenamiento:
        if producto[clave] == valor:
            new_valor = input('Ingrese el nuevo valor')
            producto[clave] = new_valor

def buscar(almacenamiento):
    valor = input('¿Que producto desea buscar?\n')
    for producto in almacenamiento:
        if producto['nombre'] == valor:
            return producto

