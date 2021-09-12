import axiompy

class Unit:
    def __init__(self, name, name_short, value, category):
        self.name = name
        self.name_short = name_short
        self.value = value
        self.category = category

    def __repr__(self):
        return "Unit(self.name, self.name_short, self.value,self.category)"

    def __str__(self):
        return self.name

    def __mul__(self, other):
        if(isinstance(other, (int, float, complex))):
            return axiompy.value.Value(other, self)
        elif(isinstance(other, axiompy.value.Value)):
            return axiompy.value.Value(self.value * other.value, self)

    __rmul__ = __mul__
