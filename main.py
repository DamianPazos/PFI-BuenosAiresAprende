import functions as func

productos = []

while True:
    func.mostrar_menu_principal()
    try:
        opcion_menu_principal = int(input('Ingrese el número de opción: '))
        if opcion_menu_principal == 1:
            func.registro(productos)
        elif opcion_menu_principal == 2:
            func.enlistar(productos)
        elif opcion_menu_principal == 3:
            busqueda = func.buscar(productos)
            if busqueda != None:
                func.eliminar(busqueda, productos)
                print('Se elimino correctamente')
            else:
                print('No se encontro producto')
        elif opcion_menu_principal == 4:
            print('Usted ha elegido cerrar el programa')
            break
        else: 
            print('Selecciono un número invalido, reintente nuevamente')
    except ValueError:
        print('Ingreso invalido, reintente nuevamente')