
class Compiler:
    """
    compiles tokens into code
    """

    def __init__(self, tokens):
        self.tokens = tokens

    def _compile_print(self, expression):
        return f"print('{expression.value[1]}')\n"

    def compile(self):
        code = ""
        for token in self.tokens:
            command = token.type
            expression = token.value
            if (command == "PRINT"):
                code += self._compile_print(expression)
        return code

