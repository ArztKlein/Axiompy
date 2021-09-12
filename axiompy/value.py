import axiompy

class Value:
    
    def __init__(self, value, unit: axiompy.unit.Unit,dimension=1):
        self.value = value
        self.unit = unit
        self.dimension=dimension

    def __str__(self):
        return f"<Value ({self.value} {self.unit}{f'^{self.dimension}' if self.dimension != 1 else ''})>"
    
    def __int__(self):
        return int(self.value)

    def incompatible_type(other):
        raise Exception(f"Incompatible types Value, {type(other)}")
    
    def incompatible_categories(other):
        raise Exception(f"Incompatible unit categories {self.unit.category}, {other.unit.category}")


    def __mul__(self, other):
        if(isinstance(other, Value)):

            if(self.unit.category != other.unit.category):
                Value.incompatible_categories(other)
            
            value1 = axiompy.AxiomPy.value_to_base(self)
            value2 = axiompy.AxiomPy.value_to_base(other)
            dimension = self.dimension + other.dimension
            base_value = Value(value1.value * value2.value, axiompy.AxiomPy.base_unit_from_value(self), dimension)
            answer = axiompy.AxiomPy.unit_convert(base_value, self.unit)

            return answer

        elif(isinstance(other, axiompy.unit.Unit)):
            if(self.unit.category != other.category):
                Value.incompatible_categories(other)

            answer = axiompy.AxiomPy.value_to_base(self) * other.value
            answer.dimension = self.dimension + 1

            return answer

        elif(isinstance(other, (int, float, complex))):
            return Value(self.value * other, self.unit)

        Value.incompatible_type(other)

    def __div__(self, other):
        if(isinstance(other, Value)):

            if(self.unit.category != other.unit.category):
                Value.incompatible_categories(other)
            
            value1 = axiompy.AxiomPy.value_to_base(self)
            value2 = axiompy.AxiomPy.value_to_base(other)
            base_value = Value(value1.value / value2.value, axiompy.AxiomPy.base_unit_from_value(self), self.dimension)
            answer = axiompy.AxiomPy.unit_convert(base_value, self.unit)

            return answer

        elif(isinstance(other, axiompy.unit.Unit)):
            if(self.unit.category != other.category):
                Value.incompatible_categories(other)

            answer = axiompy.AxiomPy.value_to_base(self) / other.value

            return answer

        elif(isinstance(other, (int, float, complex))):
            return Value(self.value / other, self.unit)

        Value.incompatible_type(other)


    def __add__(self, other):
        if(isinstance(other, Value)):

            if(self.unit.category != other.unit.category):
                Value.incompatible_categories(other)
            
            value1 = axiompy.AxiomPy.value_to_base(self)
            value2 = axiompy.AxiomPy.value_to_base(other)
            base_value = Value(value1.value + value2.value, axiompy.AxiomPy.base_unit_from_value(self), self.dimension)
            answer = axiompy.AxiomPy.unit_convert(base_value, self.unit)

            return answer

        elif(isinstance(other, axiompy.unit.Unit)):
            if(self.unit.category != other.category):
                Value.incompatible_categories(other)

            answer = axiompy.AxiomPy.value_to_base(self) + other.value

            return answer

        elif(isinstance(other, (int, float, complex))):
            return Value(self.value + other, self.unit)

        Value.incompatible_type(other)
    
    def __sub__(self, other):
        if(isinstance(other, Value)):

            if(self.unit.category != other.unit.category):
                Value.incompatible_categories(other)
            
            value1 = axiompy.AxiomPy.value_to_base(self)
            value2 = axiompy.AxiomPy.value_to_base(other)
            base_value = Value(value1.value - value2.value, axiompy.AxiomPy.base_unit_from_value(self), self.dimension)
            answer = axiompy.AxiomPy.unit_convert(base_value, self.unit)

            return answer

        elif(isinstance(other, axiompy.unit.Unit)):
            if(self.unit.category != other.category):
                Value.incompatible_categories(other)

            answer = axiompy.AxiomPy.value_to_base(self) - other.value

            return answer

        elif(isinstance(other, (int, float, complex))):
            return Value(self.value - other, self.unit)

        Value.incompatible_type(other)