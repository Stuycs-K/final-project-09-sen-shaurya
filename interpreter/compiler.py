
class Compiler:
    """
    compiles tokens into code
    """

    def __init__(self, tokens):
        self.tokens = tokens

    def _compile_expression(self, expression):
        binary_ops = [ "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "EQ", "GT", "LT"]
        binary_ops_symbols = ['+','-','*','/','==','>','<']
        binary_index = -1
        try:
            binary_index = binary_ops.index(expression.type)
        except Exception as e:
            pass

        if (expression.type == "LITERAL"):
            if (expression.value[0] == "STRING"):
                return f"'{expression.value[1]}'"
            if (expression.value[0] == "FLOAT"):
                return f"{expression.value[1]}"
        elif (expression.type == "VARIABLE"):
            return f"{expression.value}"
        elif (binary_index != -1):
            left = self._compile_expression(expression.value[0])
            right = self._compile_expression(expression.value[1])
            return f"{left} {binary_ops_symbols[binary_index]} {right}"

    def _compile_print(self, expression):
        return f"print({self._compile_expression(expression)})\n"
    
    def _compile_input(self, variable):
        return f"{variable} = input()\n{variable} = int({variable}) if {variable}.isnumeric() else {variable}\n"

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

