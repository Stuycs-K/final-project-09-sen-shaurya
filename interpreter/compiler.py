
class Compiler:
    """
    compiles tokens into code
    """

    # COMPILED INPUT CODE #
    # var0 = input()
    # print(var0)

    def __init__(self, tokens):
        self.tokens = tokens

    def _compile_print(self, expression):
        if (expression.type == "LITERAL"):
            if (expression.value[0] == "STRING"):
                return f"print('{expression.value[1]}')\n"
        elif (expression.type == "VARIABLE"):
            return f"print({expression.value})\n"
    
    def _compile_input(self, expression):
        return f"{expression} = input()\n"

    def compile(self):
        code = ""
        for token in self.tokens:
            command = token.type
            expression = token.value
            if (command == "INPUT"):
                code += self._compile_input(expression)
            if (command == "PRINT"):
                code += self._compile_print(expression)
            
        return code

