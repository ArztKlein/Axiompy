import axiompy

class ACF: 
    """
    Axiom Configuration File, V0.1

    Sections:
        Sections are categories of variables. To create a section, start the line with a '@'.
        All ACF files require a section.
        Example:
            @length_units
            metre = 1
            centimetre = metre / 100
    Variables:
        Can be assigned values. You do not need to declare its type.
        Each variable is exclusive to it's section; it cannot be referenced from a section that it was not created in.
        You can perform math operations on the variables.
        Non-number variable values are interpreted as strings unless they are used in a math operation, where the interpreter will use it as a variable reference. 

    Math Operations:
        These operations are multiplying, dividing, adding, subtracting, and powers. (*,/,+,-,^)
        Order of operations is not yet supported (including brackets), so all operations are run executed in the order of which they were written as.
        Math operators must have a space on both sides to signify that it is an expression and not a string.
    """

    MATH_OPERATORS = {
        "ADD": "+",
        "SUBTRACT": "-",
        "MULTIPLY": "*",
        "DIVIDE": "/",
        "POWER": "^"
    }

    def __init__(self, lines):
        self.lines = lines
        self.parse()
    
    def parse(self):
        self.data = {
            "sections": {}
        }

        section = None

        for line in self.lines:
            if(line[0] == "@"): # section
                section = line[1:]
                self.data["sections"][section] = {}
            else: # section element
                if(section != None):
                    element = self.parse_element(line, section)
                    self.data["sections"][section][element["name"]] = element["value"]

    def parse_element(self, line: str, section:str):
        name = ""
        value = None

        for c in line:
            if(c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"):
                name += c
            elif (c == "="):
                break
        
        try:
            setter_index = line.index("=")
        except ValueError:
            ACF.throw_error(f"Setter not found in line: {line}")

        value = line[setter_index+1:].strip()

        return {"name": name, "value": self.parse_value(value, section)}

    def parse_value(self, value: str, section: str):
        tokens = self.format_tokens(value.split())

        length = len(tokens)

        i = 0
        while i < length:
            token = tokens[i]
            if(token in ACF.MATH_OPERATORS.values()):
                try:
                    answer = self.math_operation(token, tokens[i-1],tokens[i+1], section)
                    tokens.pop(i+1)
                    tokens.pop(i)
                    tokens.pop(i-1)
                    tokens.insert(i-1,answer)

                    length = len(tokens)
                    i = -1
                except KeyError:
                    ACF.throw_error(f"Math Operation without valid values - {value}")
            i += 1

        
        
        return tokens[0]

    def format_tokens(self, tokens):
        for i in range(len(tokens)):
            try:
                tokens[i] = float(tokens[i])
            except:
                pass
        return tokens

    def math_operation(self, symbol: str, value1, value2, section: str):
        ops = ACF.MATH_OPERATORS

        if(isinstance(value1, str)):
            value1 = self.get_value(value1, section)
        if(isinstance(value2, str)):
            value2 = self.get_value(value2, section)


        if(symbol == ops["MULTIPLY"]):
            return value1 * value2
        elif(symbol == ops["DIVIDE"]):
            return value1 / value2
        elif(symbol == ops["ADD"]):
            return value1 + value2
        elif(symbol == ops["SUBTRACT"]):
            return value1 - value2
        elif(symbol == ops["POWER"]):
            return value1 ** value2


    def get_value(self, name, section):
        try:
            return self.data["sections"][section][name]
        except:
            ACF.throw_error("Variable referenced before assignment. Cross-section variables are not supported.")



    @staticmethod
    def throw_error(error: str):
        raise Exception(f"Axiom Config Error: {error}")

        
    def __str__(self):
        return f"ACF<str(self.data)>"