import os
import sys

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
if MODULE_DIR not in sys.path:
    sys.path.insert(0, MODULE_DIR)

try:
    from .block import Block
except ImportError:
    from block import Block

__all__ = ["Blockchain"]


class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    # Crear bloque génesis
    def create_genesis_block(self):
        genesis = Block(
            index=0,
            data="Bloque Génesis",
            previous_hash="0"
        )

        genesis.mine_block()
        self.chain.append(genesis)

    # Agregar bloque
    def add_block(self, data):
        previous_block = self.chain[-1]

        new_block = Block(
            index=len(self.chain),
            data=data,
            previous_hash=previous_block.hash
        )

        new_block.mine_block()
        self.chain.append(new_block)

    # Leer bloque
    def read_block(self, index):
        if index < 0 or index >= len(self.chain):
            print("El bloque no existe.")
            return

        block = self.chain[index]

        print("\n--- BLOQUE ---")
        print(f"Índice: {block.index}")
        print(f"Información: {block.data}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Hash anterior: {block.previous_hash}")
        print(f"Dificultad: {block.difficulty}")
        print(f"Nonce: {block.nonce}")
        print(f"Hash: {block.hash}")

    # Modificar bloque
    def modify_block(
        self,
        index,
        data=None,
        previous_hash=None,
        timestamp=None,
        difficulty=None,
        nonce=None
    ):
        if index < 0 or index >= len(self.chain):
            print("El bloque no existe.")
            return

        block = self.chain[index]

        if data is not None:
            block.data = data

        if previous_hash is not None:
            block.previous_hash = previous_hash

        if timestamp is not None:
            block.timestamp = timestamp

        if difficulty is not None:
            block.difficulty = difficulty

        if nonce is not None:
            block.nonce = nonce

        block.hash = block.calculate_hash()

        print("Bloque modificado.")

    # Borrar bloque
    def delete_block(self, index):
        if index == 0:
            print("No se puede borrar el bloque génesis.")
            return

        if index < 0 or index >= len(self.chain):
            print("El bloque no existe.")
            return

        self.chain.pop(index)

        for i in range(index, len(self.chain)):
            self.chain[i].index = i

        print("Bloque eliminado.")

    # Verificar cadena
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):

            current = self.chain[i]
            previous = self.chain[i - 1]

            # Verificar que el hash no haya sido alterado
            if current.hash != current.calculate_hash():
                return False

            # Verificar conexión con el bloque anterior
            if current.previous_hash != previous.hash:
                return False

        return True