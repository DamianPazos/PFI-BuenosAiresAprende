import functions as func

# Menu de PFI
def mostrar_menu (almacenamiento,estado_programa):
    print('MENU DE OPCIONES\n\nSeleccione el numero de la opcion solicitada')
    print('1. Registrar producto\n2. Modificar producto\n3. Eliminar producto\n4. Listado de productos\n5. Productos con poco stock\n6. Busqueda de producto\n7. Salir del programa\n\n')
    numero_opcion = int(input())
    seleccion_opcion(numero_opcion, almacenamiento, estado_programa)

# Seleccion de opcion
def seleccion_opcion(numero, almacenamiento, estado) :
    if numero == 1 :
        func.registro(almacenamiento)
    elif numero == 2 :
        busqueda = func.buscar(almacenamiento)
        if busqueda != None:
            func.modificar(any,any,any,almacenamiento)
    elif numero == 3 :
        busqueda = func.buscar(almacenamiento)
        if busqueda != None:
            func.eliminar(busqueda,almacenamiento)
    elif numero == 4:
        func.enlistar(almacenamiento)
    elif numero == 5:
        #TODO: funcion poco stock
        pass
    elif numero == 6:
        busqueda = func.buscar(almacenamiento)
        if busqueda != None:
            print(busqueda)
        else:
            print('No se encontro un producto con ese nombre')
    elif numero == 7:
        func.funcionamiento(estado)


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
        pass