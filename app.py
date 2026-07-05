def menu_principal():print("""
========== MENÚ PRINCIPAL ==========
1. Stock por categoría
2. Buscar productos por rango de precio
3. Actualizar precio 
4. Agregar producto
5. Eliminar producto
6. Mostrar productos
7. Salir
===================================
""")
# Validaciones

def validar_codigo(codigo, productos):
    return codigo.strip().lower() not in [llave.lower() for llave in productos] and codigo.strip() != ""

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_precio(precio):
    try:
        return int(precio) > 0
    except ValueError:
        return False

def validar_disponible(opcion):
    return opcion.strip().lower() in ['s', 'n']

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

def leer_opcion():
    try:
        opcion = int(input("Ingrese opcion: "))
        if 1 <= opcion <= 7:
            return opcion
        else:
            return -1
    except ValueError:
        return -1
        
def stock_categoria(categoria, productos, inventario):
    total_stock = 0
    categoria_buscada = categoria.lower()
    for codigo, datos in productos.items():
        if datos[1].lower() == categoria_buscada:
            total_stock += inventario[codigo][0]
    print(f"\nStock total para la categoria '{categoria}' es: {total_stock}")

def buscar_precio(precio_min, precio_max, productos, inventario):
    resultados = []
    for codigo, datos in productos.items():
        precio = datos[2]

        if precio_min <= precio <= precio_max and inventario[codigo][0] > 0:
            resultados.append((datos[0], codigo))
            
    if not resultados:
        print("\nNo se encontraron productos en ese rango de precio con stock disponible.")
        return
    
    resultados.sort(key=lambda x: x[0].lower())
    print("\nProductos encontrados: ")
    for nombre, codigo in resultados:
        print(f"{nombre} -- {codigo}")

def buscar_codigo(codigo, productos):
    for llave in productos:
        if llave.lower() == codigo.strip().lower():
            return True
    return False

def actualizar_precio(codigo, nuevo_precio, productos):
    if buscar_codigo(codigo, productos):
        llave = llave_real(codigo, productos)
        productos[llave][2] = int(nuevo_precio)
        return True
    return False
        

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    if buscar_codigo(codigo, productos):
        return False
    
    if disponible.strip().lower() == "s":
        disponible = True
    else:
        disponible = False
    
    productos[codigo] = [nombre, categoria, int(precio), disponible]
    inventario[codigo] = [int(stock), int(vendidos)]
    return True

def llave_real(codigo, productos):
    for llave in productos:
        if llave.lower() == codigo.strip().lower():
            return llave
    return codigo

def eliminar_producto(codigo, productos, inventario):
    if buscar_codigo(codigo, productos):
        llave = llave_real(codigo, productos)
        del productos[llave]  
        del inventario[llave] 
        return True
    return False

def mostrar_productos(productos, inventario):
    if not productos:
        print("\nNo hay productos registrados.")

    for codigo in productos:
        print(f"\nCODIGO: {codigo}")
        print(f"Nombre: {productos[codigo][0]}")
        print(f"Categoria: {productos[codigo][1]}")
        print(f"Precio: {productos[codigo][2]}")
        print(f"Disponible: {productos[codigo][3]}")
        print(f"Stock: {inventario[codigo][0]}")
        print(f"Vendidos: {inventario[codigo][1]}")

def main():
    productos = {
        "P101":["Cuaderno","Papeleria",2490,True],
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

            try:
                precio_min = int(input("Ingrese precio minimo: "))
                precio_max = int(input("Ingrese precio maximo: "))
                if precio_min < 0 or precio_max < 0 or precio_min > precio_max:
                    print("Valores de precio no validos.")
                else:
                    buscar_precio(precio_min, precio_max, productos, inventario)
            except ValueError:
                print("Error: Los precios deben ser numeros enteros.")

        elif opcion == 3:
            while True:
                codigo = input("Ingrese codigo de producto a actualizar: ")
                if not buscar_codigo(codigo, productos):
                    print("Codigo inexistente")
                else:
                    try:
                        nuevo_precio = int(input("Ingrese el nuevo precio: "))
                        if validar_precio(nuevo_precio):
                            actualizar_precio(codigo, nuevo_precio, productos)
                            print("Precio actualizado exitosamente.")
                        else:
                            print("El precio debe ser un entero mayor a cero")
                    except ValueError:
                        print("ERROR: Precio debe ser un numero entero.")
                
                opcion_ciclo = input("¿Desea actualizar otro precio? (s/n):")
                if opcion_ciclo.lower() != 's':
                    break

        elif opcion == 4:
            print("--- Registro de nuevo producto ---")
            codigo = input("Codigo: ")
            if not validar_codigo(codigo, productos):
                print("Codigo no valido.")
                continue
            
            nombre = input("Nombre: ")
            if not validar_nombre(nombre):
                print("Nombre no valido.")
                continue

            categoria = input("Categoria: ") 
            if not validar_categoria(categoria):
                print("Categoria no valida.")
                continue

            precio = input("Precio: ")
            if not validar_precio(precio):
                print("Precio no valido.")
                continue

            disponible = input("Disponible (s/n): ")
            if not validar_disponible(disponible):
                print("Opcion no valida.")
                continue

            stock = input("Stock Inicial: ")
            if not validar_stock(stock):
                print("Stock no valido.")
                continue

            vendidos = input("Cantidad vendida: ")
            if not validar_vendidos(vendidos):
                print("Cantidad vendida no valida.")
                continue
            
            exito = agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario)
            if exito:
                print("Producto agregado exitosamente.")
            else:
                print("Error al agregar el producto.")


        elif opcion == 5:
            codigo = input("Ingrese codigo de producto a eliminar: ")
            if eliminar_producto(codigo, productos, inventario):
                print("Producto eliminado exitosamente.")
            else:
                print("Codigo no fue encontrado.")

        elif opcion == 6:
            mostrar_productos(productos, inventario)

        elif opcion == 7:
            break


main()