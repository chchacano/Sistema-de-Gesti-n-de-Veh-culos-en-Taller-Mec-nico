reservas = []


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

    codigo = input("Ingrese Codigo: ")
    nombre = input("Ingrese Nombre: ")
    noches = int(input("Ingrese Noches de Estadia: "))
    valor_noche = int(input("Ingrese Valor Noches: "))

    if not validar_strings(codigo):
        print("Codigo no debe ir vacio, reintente.")
        return

    if not validar_strings(nombre):
        print("Nombre no debe ir Vacio, reintente.")
        return
    
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
    
    reservas.append(nuevaReserva)
    print(reservas)

registrar_reserva()

