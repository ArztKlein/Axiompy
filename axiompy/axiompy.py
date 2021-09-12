from axiompy.unit import Unit
from axiompy.value import Value

class AxiomPy:

    #Length Units
    metre = Unit("metre", "m", 1, "length")

    yottametre = Unit("yottametre", "Ym", 10**24, "length")
    zettametre = Unit("zettametre", "Zm", 10**21, "length")
    exametre = Unit("exametre", "Em", 10**18, "length")
    petametre = Unit("petametre", "Pm", 10**15, "length")
    terametre = Unit("terametre", "Tm", 10**12, "length")
    gigametre = Unit("gigametre", "Gm", 10**9, "length")
    megametre = Unit("megametre", "Mm", 10**6, "length")
    kilometre = Unit("kilometre", "km", 10**3, "length")
    hectometre = Unit("hectometre", "hm", 10**2, "length")
    decametre = Unit("decametre", "dam", 10, "length")
    decimetre = Unit("decimetre", "dm", 10**-1, "length")
    centimetre = Unit("centimetre", "cm", 10**-2, "length")
    millimetre = Unit("millimetre", "mm", 10**-3, "length")
    micrometre = Unit("micrometre", "µm", 10**-6, "length")
    nanometre = Unit("nanometre", "nm", 10**-9, "length")
    picometre = Unit("picometre", "pm", 10**-12, "length")
    femtometre = Unit("femtometre", "fm", 10**-15, "length")
    attometre = Unit("attometre", "am", 10**-18, "length")
    zeptometre = Unit("zeptometre", "zm", 10**-21, "length")
    yoctometre = Unit("yoctometre", "ym", 10**-24, "length")

    #Imperial
    foot = Unit("foot", "ft", metre.value * 0.3048, "length")
    inch = Unit("inch", "in", foot.value / 12, "length")

    thou = Unit("thou", "th", inch.value / 1000, "length")
    barleycorn = Unit("barleycorn", "Bc", inch.value / 3, "length")
    hand = Unit("hand", "th", foot.value / 3, "length")
    yard = Unit("yard", "yd", foot.value * 3, "length")
    chain = Unit("chain", "ch", yard.value * 22, "length")
    furlong = Unit("furlong", "fur", 10 * chain.value, "length")
    mile = Unit("mile", "mi", furlong.value * 8, "length")
    league = Unit("league", "lea", mile.value * 3, "length")
    fathom = Unit("fathom", "ftm", yard.value * 2, "length")
    cable = Unit("thou", None, fathom.value * 100, "length")
    nautical_mile = Unit("nautical mile", "nmi", cable.value * 10, "length")
    link = Unit("link", None, 7.92 * inch.value, "length")
    rod = perch = pole = Unit("rod", None, link.value * 25, "length")

    #Time Units

    second = Unit("second", "sec", 1, "time")
    planck_time = Unit("planck time", "tp", 5.39 * 10**-44, "time")
    yoctosecond = Unit("yoctosecond", "ys", 10**-24, "time")
    zeptosecond = Unit("zeptosecond", "zm", 10**-21, "time")
    attosecond = Unit("attosecond", "as", 10**-18, "time")
    femtosecond = Unit("femtosecond", "fm", 10**-15, "time")
    svedberg = Unit("svedberg", "S", 10**-13, "time")
    picosecond = Unit("picosecond", "ps", 10**-12, "time")
    nansecond = Unit("nanosecond", "ns", 10**-9, "time")
    shake = Unit("shake", None, 10**-8, "time")
    microsecond = Unit("microsecond", "μs", 10**-6, "time")
    minute = Unit("minute", "min", 60, "time")
    hour = Unit("hour", "hr", minute.value * 60, "time")
    day = Unit("day", "d", hour.value * 24, "time")
    week = Unit("week", "w", day.value * 7, "time")
    month = Unit("month", "m", day.value * 30, "time")
    year = Unit("year", "y", day.value * 365, "time") #Common year
    leap_year = Unit("leap year", "ly", day.value * 366, "time")
    decade = Unit("decade", "dec", year.value * 10, "time")
    galactic_year = Unit("galactic year", "gy", 2.3*10**8 * year.value, "time")

    #Mass Units

    kilogram = Unit("kilogram", "kg", 1, "mass")
    pound = Unit("pound", "lb", 0.45359237 * kilogram.value, "mass")
    stone = Unit("pound", "st", 14 * pound.value, "mass")
    gram = Unit("gram", "g", kilogram.value / 1000, "mass")
    milligram = Unit("milligram", "mg", gram.value / 1000, "mass")
    carat = karat = Unit("carat", "ct", milligram.value * 200, "mass")
    microgram = Unit("microgram", "μg", milligram.value / 1000, "mass")
    long_ton = Unit("long ton", None, 2240 * pound.value, "mass")
    short_ton = Unit("short_ton", None, 2000 * pound.value, "mass")
    long_hundredweight = imperial_hundredweight = Unit("long hundredweight", "long cwt", 8 * stone.value, "mass")
    short_hundredweight = Unit("short hundredweight", "short cwt", 100 * pound.value, "mass")
    ounce = Unit("ounce", "oz", pound.value / 16, "mass")
    grain = Unit("grain", "gr", 64.79891 * milligram.value, "mass")
    drachm = Unit("drachm", "dr", grain.value * 60, "mass")
    tonne = metric_ton = Unit("tonne", "t", 1000 * kilogram.value, "mass")
    dalton = Unit("dalton", "Da", 1.66 * 10**-27 * kilogram.value, "mass")
    slug = Unit("slug", "sl", 14.6 * kilogram.value, "mass")
    pound = Unit("pound", "lb", 0.45 * kilogram.value, "mass")
    planck_mass = Unit("planck mass", "ℓP", 2.18 * 10**-8 * kilogram.value, "mass")
    solar_mass = Unit("solar mass", "M☉", 1.99 * 10**30 * kilogram.value, "mass")

    def base_unit_from_string(unit_cat: str):
        return AxiomPy.units[unit_cat]["base"]

    def base_unit_from_value(value):
        return AxiomPy.units[value.unit.category]["base"]

    def value_to_base(value):
        """
        Converts a value's unit to its base unit
        ie 15cm converts to 0.15m as metre is the base unit for length.

        >>> unit_to_base(Value(15, AxiomPy.centimetre))
        Value(0.15, AxiomPy.metre)
        """

        base_unit = AxiomPy.units[value.unit.category]["base"]

        return Value(value.unit.value * value.value, base_unit)

    def unit_convert(from_value, to_unit):
        """
        Params:
            from: axiompy.Value
            tounit: axiompy.Unit

        Converts an axiompy value to a desired unit.
        """

        from_unit = from_value.unit
        
        if(from_unit.category != to_unit.category):
            raise Exception(f"Incompatible unit categories {from_unit.category}, {to_unit.category}")

        to_unit_value = to_unit.value

        return Value((from_value.value * from_unit.value) / to_unit_value, to_unit, dimension=from_value.dimension)
        

    units = {
        "length": {
            "base": metre
        },
        "time": {
            "base": second
        },
        "mass": {
            "base": kilogram
        }
    }

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()