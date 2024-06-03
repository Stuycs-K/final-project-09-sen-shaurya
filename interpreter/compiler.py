
class Compiler:
    """
    compiles tokens into code
    """

    def __init__(self, tokens):
        self.tokens = tokens

    def _compile_print(self, expression):
        return f"print('hi')\n"

    def compile(self):
        code = ""
        # go through the commands
        for token in self.tokens:
            command = token.type
            expression = token.value

            if (command == "PRINT"):
                code += self._compile_print(expression)
        return code

    