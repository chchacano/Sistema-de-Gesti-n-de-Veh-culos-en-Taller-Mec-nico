lista_reservas = []


def validar_strings(cadena):
    return cadena.strip() != ""


def validar_noches(noches):
    return noches > 0


def mayor_zero(numero):
    return numero > 0


def total(noches, valor_noche):
    return noches * valor_noche


def categoria_(total):

    if total < 200000:
        return "Economica"
    elif total <= 500000:
        return "Estandar"
    else:
        return "Premium"


def registrar_reserva():

    print("\n=== Registro Reserva ===")

    codigo = input("Ingrese Codigo: ").strip()

    if not validar_strings(codigo):
        print("Codigo no debe ir vacio.")
        return

    # Validar código único
    for reserva in lista_reservas:
        if reserva["codigo"] == codigo:
            print("El codigo ya existe.")
            return

    nombre = input("Ingrese Nombre: ")

    if not validar_strings(nombre):
        print("Nombre no debe ir vacio.")
        return

    try:
        noches = int(input("Ingrese Noches de Estadia: "))
    except ValueError:
        print("Cantidad de noches debe ser numerica.")
        return

    if not validar_noches(noches):
        print("Cantidad de noches debe ser mayor a 0.")
        return

    try:
        valor_noche = int(input("Ingrese Valor por Noche: "))
    except ValueError:
        print("Valor debe ser numerico.")
        return

    if not mayor_zero(valor_noche):
        print("Valor debe ser mayor a 0.")
        return

    total_reserva = total(noches, valor_noche)
    categoria = categoria_(total_reserva)

    nuevaReserva = {
        "codigo": codigo,
        "nombre": nombre,
        "noches": noches,
        "valor": valor_noche,
        "total": total_reserva,
        "categoria": categoria
    }

    lista_reservas.append(nuevaReserva)

    print("Reserva registrada correctamente.")
    print(lista_reservas)


def buscar_reserva(lista):

    print("\n=== Buscar Reserva ===")

    if not lista:
        print("Primero registre una reserva.")
        return

    buscarCodigo = input("Ingrese codigo a buscar: ").strip()

    if not validar_strings(buscarCodigo):
        print("Ingrese un codigo valido.")
        return

    for i, reserva in enumerate(lista):

        if reserva["codigo"] == buscarCodigo:

            print(f"\nPOSICION: {i}")

            print(f"""
CODIGO: {reserva["codigo"]}
NOMBRE: {reserva["nombre"]}
CANTIDAD NOCHES: {reserva["noches"]}
VALOR POR NOCHE: {reserva["valor"]}
VALOR TOTAL: {reserva["total"]}
CATEGORIA: {reserva["categoria"]}
""")
            return

    print("Reserva no encontrada.")


def actualizar_reservas(lista):

    print("\n=== Actualizar Reserva ===")

    if not lista:
        print("Primero registre una reserva.")
        return

    buscarCodigo = input("Ingrese codigo a buscar: ").strip()

    if not validar_strings(buscarCodigo):
        print("Ingrese un codigo valido.")
        return

    for reserva in lista:

        if reserva["codigo"] == buscarCodigo:

            print(f"Reserva '{reserva['codigo']}' encontrada.")

            nuevoNombre = input("Ingrese nuevo nombre: ")

            if not validar_strings(nuevoNombre):
                print("Nuevo nombre no debe estar vacio.")
                return

            try:
                nuevaCantidadNoche = int(
                    input("Ingrese nueva cantidad de noches: "))
            except ValueError:
                print("Ingrese solo numeros.")
                return

            if not validar_noches(nuevaCantidadNoche):
                print("Nueva cantidad debe ser mayor a 0.")
                return

            try:
                nuevaValorNoche = int(
                    input("Ingrese nuevo valor por noche: "))
            except ValueError:
                print("Ingrese solo numeros.")
                return

            if not mayor_zero(nuevaValorNoche):
                print("Nuevo valor debe ser mayor a 0.")
                return

            nueva_total_reserva = total(
                nuevaCantidadNoche,
                nuevaValorNoche
            )

            nueva_categoria = categoria_(nueva_total_reserva)

            reserva["nombre"] = nuevoNombre
            reserva["noches"] = nuevaCantidadNoche
            reserva["valor"] = nuevaValorNoche
            reserva["total"] = nueva_total_reserva
            reserva["categoria"] = nueva_categoria

            print("Reserva actualizada correctamente.")
            print(lista)

            return

    print("Reserva no encontrada.")


# PRUEBAS

registrar_reserva()
registrar_reserva()

actualizar_reservas(lista_reservas)

buscar_reserva(lista_reservas)