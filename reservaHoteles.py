
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
    elif 200000 <= total <= 500000:
        return "Estandar"
    else:
        return "Premium"

def registrar_reserva():

    print("=== Registro Reserva ===")

    codigo = input("Ingrese Codigo: ").strip()
    
    if not validar_strings(codigo):
        print("Codigo no debe ir vacio, reintente.")
        return
    

    nombre = input("Ingrese Nombre: ")
    if not validar_strings(nombre):
        print("Nombre no debe ir Vacio, reintente.")
        return
    
    
    try:
        noches = int(input("Ingrese Noches de Estadia: "))
    except ValueError:
        print("Cantidad noches mayores a 0")
    
    try:
        valor_noche = int(input("Ingrese Valor Noches: "))
    except ValueError:
        print("Valor debe ser mayor a 0")
    
    if not mayor_zero(noches):
        print("Noches debe ser mayor a 0, reintente.")
        return
    
    if not mayor_zero(valor_noche):
        print("Valor debe ser mayor a 0, reintente.")

    total_reserva = total(noches, valor_noche)
    categoria = categoria_(total_reserva)

    nuevaReserva = {"codigo":codigo,
                    "nombre":nombre,
                    "noches":noches,
                    "valor":valor_noche,
                    "total":total_reserva,
                    "categoria":categoria
                    }
    
    lista_reservas.append(nuevaReserva)
    print(lista_reservas)

def buscar_reserva(lista):
    
    if len(lista) == 0 or lista == []:
        print("Primero registre una reserva.")
        return
    
    buscarCodigo = input("Ingrese codigo a buscar: ").strip()

    if not validar_strings(buscarCodigo):
        print("Ingrese codigo valido")

    for reserva in lista:
        if reserva["codigo"] == buscarCodigo:
            i = lista.index(reserva)
            x = f"""CODIGO:{reserva["codigo"]}
NOMBRE: {reserva["nombre"]}
CANTIDAD NOCHES: {reserva["noches"]}
VALOR POR NOCHE: {reserva["valor"]}
VALOR TOTAL: {reserva["total"]}
CATEGORIA: {reserva["categoria"]}
"""
            return print("\nPOSICION:",i), print(x)
        else:
            print("Reserva no encontrada.")
            return
        
def actualizar_reservas(lista):

    if len(lista) == 0 or lista == []:
        print("Primero registre una reserva.")
        return
    
    buscarCodigo = input("Ingrese codigo a buscar: ").strip()

    if not validar_strings(buscarCodigo):
        print("Ingrese codigo valido")

    for reserva in lista:
        if reserva["codigo"] == buscarCodigo:
            pass





registrar_reserva()
buscar_reserva(lista_reservas)

