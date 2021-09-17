# Axiompy
Python library to convert, and perform math operations on values of particular units.
Includes SI Base units, and non-standard units such as the ones adopted in the imperial system.

## Installation

```
pip install axiompy
```

## Usage
Convert between units by using the unit_convert method.
```python
from axiompy import axiompy.units as _units
units = _units.Units()

print(units.unit_convert(3 * units.metre), units.foot)
```