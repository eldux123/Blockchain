import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from blockchain import Blockchain


def mostrar_menu():
    print("\n==============================")
    print("       BLOCKCHAIN PYTHON")
    print("==============================")
    print("1. Agregar bloque")
    print("2. Leer bloque")
    print("3. Modificar bloque")
    print("4. Borrar bloque")
    print("5. Verificar cadena")
    print("6. Mostrar todos los bloques")
    print("0. Salir")
    print("==============================")


def mostrar_todos(blockchain):
    for block in blockchain.chain:
        print("\n------------------------------")
        print(f"Índice: {block.index}")
        print(f"Información: {block.data}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Hash anterior: {block.previous_hash}")
        print(f"Dificultad: {block.difficulty}")
        print(f"Nonce: {block.nonce}")
        print(f"Hash: {block.hash}")


def main():

    blockchain = Blockchain()

    print("\nBlockchain creada correctamente.")
    print(
        "Estado inicial:",
        "VÁLIDA" if blockchain.is_chain_valid() else "INVÁLIDA"
    )

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            data = input("Ingrese la información del bloque: ")

            blockchain.add_block(data)

        elif opcion == "2":

            try:
                index = int(input("Ingrese el índice del bloque: "))
                blockchain.read_block(index)

            except ValueError:
                print("Debe ingresar un número válido.")

        elif opcion == "3":

            try:
                index = int(input("Ingrese el índice del bloque: "))

                print("\nDeje vacío cualquier campo que no quiera modificar.")

                data = input("Nueva información: ")
                previous_hash = input("Nuevo hash anterior: ")
                timestamp = input("Nuevo timestamp: ")

                difficulty_input = input("Nueva dificultad: ")
                nonce_input = input("Nuevo nonce: ")

                data = data if data else None
                previous_hash = previous_hash if previous_hash else None
                timestamp = timestamp if timestamp else None

                difficulty = (
                    int(difficulty_input)
                    if difficulty_input
                    else None
                )

                nonce = (
                    int(nonce_input)
                    if nonce_input
                    else None
                )

                blockchain.modify_block(
                    index,
                    data,
                    previous_hash,
                    timestamp,
                    difficulty,
                    nonce
                )

            except ValueError:
                print("Ingrese valores válidos.")

        elif opcion == "4":

            try:
                index = int(input("Ingrese el índice del bloque: "))
                blockchain.delete_block(index)

            except ValueError:
                print("Debe ingresar un número válido.")

        elif opcion == "5":

            if blockchain.is_chain_valid():
                print("\nLa cadena es VÁLIDA.")
            else:
                print("\nLa cadena es INVÁLIDA.")

        elif opcion == "6":

            mostrar_todos(blockchain)

        elif opcion == "0":

            print("Programa finalizado.")
            break

        else:

            print("Opción no válida.")


if __name__ == "__main__":
    main()