import axiompy
import math

class Value:
    
    def __init__(self, value, unit: axiompy.unit.Unit, db: axiompy.Units,dimension=1):
        self.value = value
        self.unit = unit
        self.dimension=dimension
        self.db = db

    def __str__(self):
        return f"<Value ({self.value} {self.unit}{f'^{self.dimension}' if self.dimension != 1 else ''})>"
    
    def __int__(self):
        return int(self.value)

    def incompatible_type(self, other):
        raise Exception(f"Incompatible types Value, {type(other)}")
    
    def incompatible_categories(self, other):
        raise Exception(f"Incompatible unit categories {self.unit.category}, {other.unit.category}")

    def __mul__(self, other):
        if(isinstance(other, Value)):

            if(self.unit.category != other.unit.category):
                Value.incompatible_categories(other)
            
            value1 = self.db.value_to_base(self)
            value2 = self.db.value_to_base(other)
            dimension = self.dimension + other.dimension
            base_value = Value(value1.value * value2.value, self.db.base_unit_from_value(self), dimension)
            answer = self.db.unit_convert(base_value, self.unit)

            return answer

        elif(isinstance(other, axiompy.unit.Unit)):
            if(self.unit.category != other.category):
                Value.incompatible_categories(other)

            answer = self.db.value_to_base(self) * other.value
            answer.dimension = self.dimension + 1

            return answer

        elif(isinstance(other, (int, float, complex))):
            return Value(self.value * other, self.unit, self.db)

        Value.incompatible_type(other)

    def __truediv__(self, other):
        if(isinstance(other, Value)):

            if(self.unit.category != other.unit.category):
                Value.incompatible_categories(other)
            
            value1 = self.db.value_to_base(self)
            value2 = float(self.db.value_to_base(other))
            base_value = Value(value1.value / value2.value, self.db.base_unit_from_value(self), self.dimension)
            answer = self.db.unit_convert(base_value, self.unit)

            return answer

        elif(isinstance(other, axiompy.unit.Unit)):
            if(self.unit.category != other.category):
                Value.incompatible_categories(other)

            answer = self.db.value_to_base(self) / float(other.value)

            return answer

        elif(isinstance(other, (int, float, complex))):
            return Value(self.value / other, self.unit, self.db)

        Value.incompatible_type(other)

    def __floordiv__(self, other):
        if(isinstance(other, Value)):

            if(self.unit.category != other.unit.category):
                Value.incompatible_categories(other)
            
            value1 = self.db.value_to_base(self)
            value2 = float(self.db.value_to_base(other))
            base_value = Value(math.floor(value1.value / value2.value), self.db.base_unit_from_value(self), self.dimension)
            answer = self.db.unit_convert(base_value, self.unit)

            return answer

        elif(isinstance(other, axiompy.unit.Unit)):
            if(self.unit.category != other.category):
                Value.incompatible_categories(other)

            answer = math.floor(self.db.value_to_base(self) / float(other.value))

            return answer

        elif(isinstance(other, (int, float, complex))):
            return Value(math.floor(self.value / other), self.unit, self.db)

        Value.incompatible_type(other)


    def __add__(self, other):
        if(isinstance(other, Value)):

            if(self.unit.category != other.unit.category):
                Value.incompatible_categories(other)
            
            value1 = self.db.value_to_base(self)
            value2 = self.db.value_to_base(other)
            base_value = Value(value1.value + value2.value, self.db.base_unit_from_value(self), self.dimension)
            answer = self.db.unit_convert(base_value, self.unit)

            return answer

        elif(isinstance(other, axiompy.unit.Unit)):
            if(self.unit.category != other.category):
                Value.incompatible_categories(other)

            answer = self.db.value_to_base(self) + other.value

            return answer

        elif(isinstance(other, (int, float, complex))):
            return Value(self.value + other, self.unit, self.db)

        Value.incompatible_type(other)
    
    def __sub__(self, other):
        if(isinstance(other, Value)):

            if(self.unit.category != other.unit.category):
                Value.incompatible_categories(other)
            
            value1 = self.db.value_to_base(self)
            value2 = self.db.value_to_base(other)
            base_value = Value(value1.value - value2.value, self.db.base_unit_from_value(self), self.dimension)
            answer = self.db.unit_convert(base_value, self.unit)

            return answer

        elif(isinstance(other, axiompy.unit.Unit)):
            if(self.unit.category != other.category):
                Value.incompatible_categories(other)

            answer = self.db.value_to_base(self) - other.value

            return answer

        elif(isinstance(other, (int, float, complex))):
            return Value(self.value - other, self.unit, self.db)

        Value.incompatible_type(other)

    __rmul__ = __mul__
    __rtruediv__ = __truediv__
    __rfloordiv__ = __floordiv__
    __radd__ = __add__
    __rsub__ = __sub__