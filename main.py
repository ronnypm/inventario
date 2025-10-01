from db import get_connection


cursor = get_connection

print("\nEscanea un código de barras (o escribe 's'): \n")

while True:
    codigo = input("> ")
    if codigo.lower().strip() == "s":
        break
    cursor.execute(
        "SELECT * FROM productos WHERE codigo_producto = %s", (codigo,))
    producto = cursor.fetchone()

    if producto:
        nuevo_stock = producto["stock"] + 1
        cursor.execute(
            "UPDATE productos SET stock = %s WHERE codigo_producto = %s", (nuevo_stock, codigo))
        print(
            f"Stock actualizado: {producto['nombre_producto']} ahora tiene {nuevo_stock}")

    else:
        print("❌ Producto no encontrado. Vamos a agregarlo:")
        nombre = input("Nombre: ").title()
        descripcion = input("Descripción: ").title()
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))

        cursor.execute("""
            INSERT INTO productos (codigo_producto, nombre_producto, descripcion, stock, precio )
            VALUES (%s, %s, %s, %s, %s)""", (codigo, nombre, descripcion, stock, precio))
        print("Producto agregado")
    conexion.commit()


if "conexion" in locals() and conexion.is_connected():
    cursor.close()
    conexion.close()
    print("Conexion cerrada")
