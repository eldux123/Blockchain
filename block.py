import hashlib
from datetime import datetime


class Block:

    def __init__(
        self,
        index,
        data,
        previous_hash,
        timestamp=None,
        difficulty=4,
        nonce=0,
        hash=None
    ):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = timestamp or datetime.now().isoformat()
        self.difficulty = difficulty
        self.nonce = nonce
        self.hash = hash or self.calculate_hash()

    def calculate_hash(self):
        block_content = (
            f"{self.index}"
            f"{self.data}"
            f"{self.previous_hash}"
            f"{self.timestamp}"
            f"{self.difficulty}"
            f"{self.nonce}"
        )

        return hashlib.sha256(block_content.encode("utf-8")).hexdigest()

    def mine_block(self):
        target = "0" * self.difficulty

        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(f"Bloque minado: {self.hash}")
