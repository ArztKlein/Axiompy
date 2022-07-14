![PyPI - Downloads](https://img.shields.io/pypi/dm/axiompy)
![PyPI](https://img.shields.io/pypi/v/axiompy)

# Axiompy
Python library to convert, and perform math operations on values of particular units.
Includes SI Base units, and non-standard units such as the ones adopted in the imperial system.

## Interchangable spellings
One goal of Axiompy was to have interchangable spellings, so that both british/american spellers can choose how they want to spell.
For example, `metre`, and `meter` are interchangable spellings.

## Installation

```
pip install axiompy
```

# Usage
## Convert between units
```python
from axiompy import Units
units = Units()
print(units.unit_convert(3 * units.metre, units.foot))
```

## Get Unit from String

If you wanted to get the unit from a string instead of using the `__attr__`, you can use Unit.unit()

```python
from axiompy import Units
units = Units()
print(units.unit_convert(3 * units.unit("metre"), units.foot))
```

## Convert value to its base value
```py
from axiompy import Units
units = Units()

value = Value(15, units.centimetre, units) # Create 15 centimetres

print(units.value_to_base(value)) # Convert the value to have the base unit of centimetres (metres)
>>> <Value (0.15 <Unit (metre)>)>
```
