def menu_principal():"""
========== MENÚ PRINCIPAL ==========
1. Stock por categoría
2. Buscar productos por rango de precio
3. Actualizar precio 
4. Agregar producto
5. Eliminar producto
6. Mostrar productos
7. Salir
===================================
"""
# Validaciones

def validar_codigo(codigo, productos):
    return codigo.lower() not in productos and codigo.strip() != ""

def validar_nombre(nombre, productos):
    return nombre.strip() != ""

def validar_categoria(categoria, productos):
    return categoria.strip() != ""

def validar_precio(precio):
    try:
        return int(precio) > 0
    except ValueError:
        return False

def validar_disponible(opcion):
    if opcion.lower() == "s":
        return True
    elif opcion.lower() == "n":
        return False

def validar_stock(stock):
    try:
        return int(stock) >= 0
    except ValueError:
        return False

def validar_vendidos(vendidos):
    try:
        return int(vendidos) >= 0
    except ValueError:
        return False

# Funciones

def leer_opcion():
    pass

def stock_categoria(categoria, productos, inventario):
    pass

def buscar_precio(precio_min, precio_max, productos, inventario):
    pass

def buscar_codigo(codigo, productos):
    pass

def actualizar_precio(codigo, nuevo_precio, productos):
    pass

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    pass

def eliminar_producto(codigo, productos, inventario):
    pass

def mostrar_productos(codigo, productos, inventario):
    pass

def main():
    productos = {
        "P101":["Cuaderno","Papeleria",590,True],
        "P102":["Lápiz","Papelería",590,True],
        "P103":["Botella","Accesorios",6990,False],
        "P104":["Mochila","Accesorios",24990,True]
    }
    inventario = {
        "P101":[30,15],
        "P102":[120,50],
        "P103":[0,10],
        "P104":[8,25]
    }

    while True:
        menu_principal()
        opcion = leer_opcion()

        if opcion == 1:
            categoria = input("Ingrese categoria a calcular: ")
            stock_categoria(categoria, productos, inventario)
        elif opcion == 2:
            buscar_precio
        elif opcion == 3:
            actualizar_precio()
        elif opcion == 4:
            agregar_producto()
        elif opcion == 5:
            eliminar_producto()
        elif opcion == 6:
            mostrar_productos()
        elif opcion == 7:
            break


main()