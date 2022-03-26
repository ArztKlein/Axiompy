from axiompy import Units, Value

units = Units()

print(units.metre * 3 + units.centimetre * 7)
print(units.unit_convert(units.metre * 3, units.foot))
print((units.centimetre * 3) * (units.metre * 1))

value = units.kilometre * 2.5

print((units.centimetre * 3) - 19)