# Sepyrate

Sepyrate is a Python library to display digits separated into groups of thousands and decimal using delimiters such as comma (`","`), dot (`"."`), space (`" "`), or apostrophe (`"'"`).

## (1) Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install sepyrate:

```
pip install sepyrate
```

## (2) Prerequisites

None.

## (3) Usage

The function to group digits in this library is `digit_separation()`, where its required input arguments are:

- `amount` [int or float]: the digits to be separated
- `tsep` [str]: delimiter for thousands separator

and the optional argument:

- `dsep` [str]: delimiter for decimal separator, defaults to `dsep='None'`

The function returns string of digits.

Following [Wikipedia](https://en.wikipedia.org/wiki/Decimal_separator#Examples_of_use):

- For comma thousands separator `tsep=","`: available delimiters for decimal separator are `dsep="None"` and `dsep="."`.
- For dot thousands separator `tsep="."`: available delimiters for decimal separator are `dsep="None"`, `dsep=","` and `dsep="'"`.
- For space thousands separator `tsep=" "`: available delimiters for decimal separator are `dsep="None"`, `dsep=","` and `dsep="."`.
- For apostrophe thousands separator `tsep="'"`: available delimiters for decimal separator are `dsep="None"`, `dsep=","` and `dsep="."`.
- Due to the complexity of Indian numbering system, it's not yet included here. But future release may have this system.

To use, import the function:

```
from sepyrate import digit_separation
```

For floating-point value digits, such as

```
amount = 1200.56
```

to display the digits into thousands with dot delimiter `tsep='.'`, we can either include `dsep=','` or without, such as

```
print(digit_separation(amount, '.', dsep=','))
```

or

```
print(digit_separation(amount, '.'))
```

Both will display

```
'1.200,56'
```

For integer digits, such as

```
value = 10000000
```

to display the digits delimited by space without decimal

```
print(digit_separation(value, ' '))

```

will display

```
'10 000 000'
```

or with decimal with comma delimiter

```
print(digit_separation(value, tsep=' ', dsep=','))

```

will display

```
'10 000 000,00'
```

or with decimal with dot delimiter

```
print(digit_separation(value, tsep=' ', dsep='.'))

```

will display

```
'10 000 000.00'
```

## (5) Contributing

Interested in contributing? Please contact me directly.
