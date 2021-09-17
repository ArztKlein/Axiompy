from axiompy.fileutils import FileUtils as fu
import axiompy.units as _units

units = _units.Units()

print(units.metre * 3 + units.centimetre * 7)
print(units.unit_convert(units.metre * 3, units.foot))

# print(units.units)
print(units.value_to_base(units.galactic_year * 1))