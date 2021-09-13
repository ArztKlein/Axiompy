#Axiompy
Python library to convert, and perform math operations on values of particular units.
Includes SI Base units, and non-standard units such as the ones adopted in the imperial system.

##Installation

```
pip install axiompy
```

##Usage
Convert between units by using the unit_convert method.
```python
import AxiomPy

print(AxiomPy.unit_convert(3 * AxiomPy.metre), AxiomPy.foot)
```