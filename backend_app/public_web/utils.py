from string import ascii_uppercase, digits
from random import randint


class CodeGenerator:

    """Random Code Generator using Uppercase and Numbers"""

    def __init__(self) -> None:
        self.code = ""

    def generate(self, code_len: int) -> str:

        """code generator method"""
        character_collection = [*ascii_uppercase, *digits]
        for _ in range(code_len):
            self.code += character_collection[
                int(randint(0, len(character_collection) - 1))
            ]

        return self.code
