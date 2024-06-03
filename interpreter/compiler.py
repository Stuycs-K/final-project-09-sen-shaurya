
class Compiler:
    """
    compiles tokens into code
    """

    def __init__(self, tokens):
        self.tokens = tokens
        self.code = ""

    def compile(self):
        # go through the commands
        for token in self.tokens:
            command = token.type
            expression = token.value

            print("command: ")
            print(command)
            print("expression: " )
            print(expression)
