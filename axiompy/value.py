import axiompy
from operator import *

class Value:
    
    def __init__(self, value, unit: axiompy.unit.Unit, db: axiompy.Units, dimension=1):
        self.value = value
        self.unit = unit
        self.dimension = dimension
        self.db = db

    def __str__(self):
        return f"<Value ({self.value} {self.unit}{f'^{self.dimension}' if self.dimension != 1 else ''})>"
    
    def __int__(self):
        return int(self.value)

    def incompatible_type(self, other):
        raise Exception(f"Incompatible types Value, {type(other)}")
    
    def incompatible_categories(self, other):
        raise Exception(f"Incompatible unit categories {self.unit.category}, {other.unit.category}")

    def __get_base_value(self, value):
        if isinstance(value, Value):
            return self.db.value_to_base(value).value # Convert it to the base unit

        elif isinstance(value, axiompy.unit.Unit):
            if self.unit.category != value.category:
                Value.incompatible_categories(value)
            return value.value

        elif isinstance(value, (int, float, complex)):
            return self.__get_base_value(Value(value, self.unit, self.db)) # Convert it to a Value so that the unit is correct, and then get base value. There is probably a nicer way to do this though.
        else:
            raise Exception(f"Unsupported value: {value}. Must be either a Value, Unit, float, int, or complex.")

    def __mul__(self, other):
        return self.__math_operator(mul, other)

    def __truediv__(self, other):
        return self.__math_operator(truediv, other)

    def __floordiv__(self, other):
        return self.__math_operator(floordiv, other)

    def __add__(self, other):
        return self.__math_operator(add, other)
    
    def __sub__(self, other):
        return self.__math_operator(sub, other)

    def __math_operator(self, operator, other_value):
        value1 = self.__get_base_value(self)
        value2 = self.__get_base_value(other_value)

        increasing_dimension = isinstance(other_value, Value)

        result_value = operator(value1, value2)

        if operator == mul and increasing_dimension:
            answer = Value(result_value / (self.unit.value ** (self.dimension + 1)), self.unit, self.db, dimension=(self.dimension + 1))
        else:
            answer = Value(result_value, self.db.base_unit_from_value(self), self.db)
        
        answer = self.db.unit_convert(answer, self.unit)

        return answer

    __rmul__ = __mul__
    __rtruediv__ = __truediv__
    __rfloordiv__ = __floordiv__
    __radd__ = __add__
    __rsub__ = __sub__