import sqlite3

# Registro de producto
def registro(almacenamiento):
    try:        
        nombre = input('Ingrese el nombre del producto: ')
        descripcion = input('Ingrese la descripción del producto: ')
        precio = float(input('Ingrese el precio del producto: $'))
        stock = int(input('Ingrese la cantidad de stock del producto: '))
        categoria = input('Ingrese la categoria del producto: ')
        almacenamiento.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
            ''', (nombre, descripcion, stock, precio, categoria))
        almacenamiento.commit()
    except ValueError:
        print('Ingresaste un valor no valido, reintentalo nuevamente')
        registro(almacenamiento)
    except sqlite3.Error as e:
        print("Hubo un error en el registro del producto: {e}")  

# Modificacion de un producto
# TODO: Opcion salir
# TODO: Expeciones

def modificar_cantidad(cursor, almacenamiento):
    try:
        producto_modificado = int(input('¿Que producto desea modificar?\n'))
        valor = int(input('¿Cual es la nueva cantidad?\n'))
        cursor.execute('''
                        UPDATE productos SET cantidad = ?
                        WHERE id = ?
                        ''',(valor, producto_modificado,))
        almacenamiento.commit()
    except ValueError:
        print('Ingreso un valor invalido, reintentelo nuevamente')
        modificar_cantidad(cursor, almacenamiento)
    except sqlite3.Error as e:
        print(f"Hubo un error en la modificacion del producto: {e}")

# Busqueda de producto (ID)
def buscar(cursor):
    try:
        valor = input('¿Que producto desea buscar?\n')
        cursor.execute('''
                        SELECT * FROM productos
                        WHERE id = ?
                        ''', (valor,))
        return cursor.fetchall()
    except ValueError:
        print('Ingreso un valor invalido, reintentelo nuevamente')
        buscar(cursor)
    except sqlite3.Error as e:
        print(f"Hubo un error en la busqueda del producto: {e}")

# Eliminar producto
def eliminar(cursor, almacenamiento):
    try:
        valor = int(input('¿Que producto desea eliminar?\n'))
        cursor.execute('''
                        DELETE FROM productos
                        WHERE id = ?
                        ''', (valor,))
        almacenamiento.commit()
    except ValueError:
        print('Ingreso un valor invalido, reintentelo nuevamente')
        eliminar(cursor, almacenamiento)
    except sqlite3.Error as e:
        print(f"Hubo un error en la eliminacion del producto: {e}")

# Enlista los productos
def enlistar(cursor):
    try:
        cursor.execute('''
                        SELECT * FROM productos
                        ''')
        return cursor.fetchall()
    except ValueError:
        print('Ingreso un valor invalido, reintentelo nuevamente')
        enlistar(cursor)
    except sqlite3.Error as e:
        print(f"Hubo un error en la muestra de los productos: {e}")


# Muestra menu principal
def mostrar_menu_principal ():
    print('\n\nMENU DE OPCIONES\n\n')
    print('1. Registrar producto\n2. Buscar producto\n3. Eliminar producto\n4. Enlistar productos\n5. Modificar producto\n6. Reporte de bajo stock\n7. Salir del programa\n\n')

# Conexion y/o creacion de base de datos
def conectar_base(nombre):       
    try:
        conexion = sqlite3.connect(nombre)
        return conexion
    except sqlite3.Error as e:
        print(f"Error con la conexion en la base de datos: {e}")
        return None
    
# Creacion de cursor para base de datos
def crear_cursor(conexion):
    if conexion:
        try:
            return conexion.cursor()
        except sqlite3.Error as e:
            print(f'Error al crear cursor para base de datos: {e}')
            return None
        
# Guardar cambios en base de datos
def guardar_cambios(conexion):
    if conexion:
        try:
            conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al querer guardar los cambios en la base de datos: {e}")

# Existencia de tabla
def existe_tabla(nombre, cursor):
    try:
        cursor.execute(f"SELECT * FROM {nombre} LIMIT 1")
        return True
    except sqlite3.OperationalError:
        return False
    
# Reporte de bajo stock
def reportar_bajo_stock(cursor):
    try:
        cursor.execute('''
                       SELECT * FROM productos WHERE cantidad < 20
                       ''',)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Hubo un error en la generacion del reporte: {e}")