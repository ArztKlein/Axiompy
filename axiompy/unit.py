import axiompy

class Unit:
    def __init__(self, name, value, category, db):
        self.name = name
        self.value = value
        self.category = category
        self.db = db

    def __str__(self):
        return f"<Unit ({self.name})>"

    def __mul__(self, other):
        if(isinstance(other, (int, float, complex))):
            return axiompy.Value(other, self, self.db)
        elif(isinstance(other, axiompy.value.Value)):
            return axiompy.Value(self.value * other.value, self, self.db)

    __rmul__ = __mul__
