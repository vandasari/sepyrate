# Sepyrate

Sepyrate is a lightweight Python library for formatting numbers with custom thousands and decimal separators. It supports common delimiters such as commas (`","`), dots (`"."`), spaces (`" "`), and apostrophes (`"'"`).

This library is particularly useful for localized currency formatting in web frameworks like Django or Flask, where you may need to display numbers according to regional standards (e.g., changing `12879.45` to `12.879,45` or `12 879.45`).

## (1) Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install sepyrate:

```
pip install sepyrate
```

## (2) Prerequisites

None.

## (3) Usage

The primary function is `digit_separation()`. It accepts the following arguments:

- `amount`: The value to format. Supports `int`, `float`, `numpy.float32`, `numpy.float64`, and `decimal.Decimal`.
- `tsep`: The character to use as the thousands separator [`str`].
- `dsep` (Optional): The character to use as the decimal separator [`str`]. Defaults to `None` (automatically inferred based on `tsep`).

The function returns string of digits.

## (4) Supported Separator Combinations

Following [Wikipedia](https://en.wikipedia.org/wiki/Decimal_separator#Examples_of_use) standards:

| `tsep` (Thousands) | Supported `dsep` (Decimal) |
| ------------------ | -------------------------- |
| Comma (`,`)        | `.`                        |
| Dot (`.`)          | `,` or `'`                 |
| Space (` `)        | `,` or `.`                 |
| Apostrophe (`'`)   | `,` or `.`                 |

Note: he Indian numbering system (e.g., `1,00,000`) is not currently supported but is planned for a future release.

## (5) Examples

### To use, import the function:

```
from sepyrate import digit_separation
```

### Formatting Floating-Point Numbers, numpy.float32, or numpy.float64:

```
amount = 1200.56 # or amount = np.float64(1200.56)

# Using a dot for thousands and a comma for decimals
print(digit_separation(amount, tsep='.', dsep=',')) # Output: '1.200,56'

# dsep is inferred as ',' if tsep is '.'
print(digit_separation(amount, tsep='.'))           # Output: '1.200,56'
```

### Formatting Integers

```
value = 10000000

# Grouping by space without decimals
print(digit_separation(value, tsep=' '))            # Output: '10 000 000'
print(digit_separation(value, tsep='.'))            # Output: '10.000.000'
```

### Django Usage

In `models.py`:

```
from django.db import models
from sepyrate import digit_separation


class Project(models.Model):
    name = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    ... # other fields

    def budget_display(self):
        """Returns the budget formatted with dot thousands and comma decimals."""
        return digit_separation(self.budget, tsep='.', dsep=',')

    # Optional: This allows the method to be used in the Django Admin 'list_display'
    budget_display.short_description = 'Formatted Budget'
```

In your Django template (e.g., `project_detail.html`)

```html
<p>Total Budget: {{ project.budget_display }}</p>
```
