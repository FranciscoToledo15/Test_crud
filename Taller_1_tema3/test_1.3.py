class Cliente:
    def __init__(self, num_cliente, monto):
        self.num_cliente = num_cliente
        self.monto = monto

class Caja:
    def __init__(self, num_caja):
        self.num_caja = num_caja
        self.recaudacion = 0
        self.clientes_atendidos = 0
        self.clientes_por_atender = 0
        self.cola_clientes = []

class ListaCajas:
    def __init__(self, cajas):
        self.cajas = cajas
        self.cantidad_cajas = len(cajas)

def procesar_clientes(lista_cajas):
    for caja in lista_cajas.cajas:
        while len(caja.cola_clientes) > 0:
            cliente = caja.cola_clientes.pop(0)
            caja.recaudacion += cliente.monto
            caja.clientes_atendidos += 1

def agregar_cliente(lista_cajas, cliente):
    min_clientes_por_atender = float('inf')
    min_caja_index = -1

    for i in range(lista_cajas.cantidad_cajas):
        if lista_cajas.cajas[i].clientes_por_atender < min_clientes_por_atender:
            min_clientes_por_atender = lista_cajas.cajas[i].clientes_por_atender
            min_caja_index = i

    lista_cajas.cajas[min_caja_index].cola_clientes.append(cliente)
    lista_cajas.cajas[min_caja_index].clientes_por_atender += 1

def mostrar_clientes(lista_cajas):
    for i, caja in enumerate(lista_cajas.cajas):
        if len(caja.cola_clientes) > 0:
            print(f"Caja {i+1}:")
            for j, cliente in enumerate(caja.cola_clientes):
                print(f"    Cliente {j+1}:")
                print(f"        Número de cliente: {cliente.num_cliente}")
                print(f"        Monto: {cliente.monto}")

def main():
    cajas = [Caja(i) for i in range(5)]
    lista_cajas = ListaCajas(cajas)

    while True:
        print("1. Procesar clientes")
        print("2. Agregar cliente")
        print("3. Mostrar clientes")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            procesar_clientes(lista_cajas)
            print("Clientes procesados.")
        elif opcion == 2:
            num_cliente = int(input("Ingrese el número de cliente: "))
            monto = float(input("Ingrese el monto del cliente: "))
            cliente = Cliente(num_cliente, monto)
            agregar_cliente(lista_cajas, cliente)
            print("Cliente agregado.")
        elif opcion == 3:
            mostrar_clientes(lista_cajas)
        elif opcion == 4:
            break
        else:
            print("Esta opción es inválida, vuelva a ingresar.")

if __name__ == "__main__":
    main()
