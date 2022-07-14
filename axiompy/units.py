import axiompy
import pkg_resources

class Units:
    def __init__(self):

        rsman = pkg_resources.ResourceManager()

        unit_file = rsman.resource_string('axiompy', 'db/en_units.acf').decode('utf-8')
        lines = unit_file.splitlines()

        lines = list(filter(None, lines)) #Remove empty lines

        self.units_dict = axiompy.ACF(lines).data

        self.units = self.acf_dict_to_units(self.units_dict)

    def acf_dict_to_units(self, d):
        """
        Converts the dictionary generated by the ACF to units
        so that the unit doesn't need to be found every time it is called for - to improve performance.
        """

        units = {"base_units": {}}

        for category in d["sections"].keys():
            for unit in d["sections"][category].keys():
                if(unit == "base_unit"):
                    units["base_units"][category] = d["sections"][category]["base_unit"]
                else:
                    value = d["sections"][category][unit]
                    units[unit] = axiompy.Unit(unit, value, category, self)

        return units

    def unit_convert(self, from_value, to_unit: "Unit"):
        """
        Params:
            from: axiompy.Value
            to_unit: axiompy.Unit

        Converts an axiompy value to a desired unit.
        """

        from_unit = from_value.unit
        to_unit_value = to_unit.value
        
        # Make sure that units from different categories aren't being converted (eg hours to metres)
        if(from_unit.category != to_unit.category):
            raise Exception(f"Incompatible unit categories {from_unit.category}, {to_unit.category}")

        return axiompy.Value((from_value.value * from_unit.value) / to_unit_value, to_unit, self, dimension=from_value.dimension)

    def base_unit_from_string(self, unit_cat: str):
        return self.units[self.units["base_units"][unit_cat]]

    def base_unit_from_value(self, value):
        return self.base_unit_from_string(value.unit.category)

    def value_to_base(self, value):
        """
        Converts a value's unit to its base unit
        ie 15cm converts to 0.15m as metre is the base unit for length.

        >>> value_to_base(Value(15, units.centimetre))
        Value(0.15, units.metre)
        """

        base_unit = self.base_unit_from_value(value)

        return axiompy.Value(value.unit.value * value.value, base_unit, self)        

    def __getattr__(self, name):
        return self.unit(name)

    def unit(self, name: str):
        """
        Get a unit from a string name.
        """

        try:
            value = self.units[name]
        except ValueError:
            raise Exception(f"Could not find Unit with name {name}. This unit does not exist. Check for typos.")
        
        return value
