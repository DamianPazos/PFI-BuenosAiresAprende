import functions as func

# Base de datos
base_datos = "inventario.db"
tabla = "productos"
conexion_bd = func.conectar_base(base_datos)
cursor_bd = func.crear_cursor(conexion_bd)
if not func.existe_tabla(tabla, conexion_bd):
    conexion_bd.execute('''
            CREATE TABLE IF NOT EXISTS ? (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
            )
            ''', (tabla))
    func.guardar_cambios(conexion_bd)

while True:
    # Menu principal
    func.mostrar_menu_principal()
    
    try:
        opcion_menu_principal = int(input('Ingrese el número de opción: '))
        if opcion_menu_principal == 1:
            func.registro(conexion_bd)
        elif opcion_menu_principal == 2:
            print(func.buscar(cursor_bd))
        elif opcion_menu_principal == 3:
            func.eliminar(cursor_bd, conexion_bd)
        elif opcion_menu_principal == 4:
            print(func.enlistar(cursor_bd))
        elif opcion_menu_principal == 5:
            func.modificar_cantidad(cursor_bd, conexion_bd)
        elif opcion_menu_principal == 6:
            print(func.reportar_bajo_stock(cursor_bd))    
        elif opcion_menu_principal == 7:
            conexion_bd.close()
            print('Usted ha elegido cerrar el programa')
            break
        else: 
            print('Selecciono un número invalido, reintente nuevamente')
    except ValueError:
        print('Ingreso invalido, reintente nuevamente')