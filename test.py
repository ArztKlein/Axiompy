from axiompy import Units, Value

units = Units()

# print(units.metre * 3 + units.centimetre * 7)
# print(units.unit_convert(units.metre * 3, units.foot))
# print((units.centimetre * 3) * (units.metre * 1))

print(units.unit("kilometre") * 2.5)

print((units.centimetre * 3) - 19)

# print(units.unit_convert(3 * units.metre, units.foot))