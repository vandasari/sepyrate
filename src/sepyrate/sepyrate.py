from decimal import Decimal


def digit_separation(amount, tsep, dsep=None):
    # 1. Standardize dsep if it's None
    if dsep is None:
        dsep = "," if tsep == "." else "."

    # 2. Format with comma as thousands separator and dot as decimal
    # This handles all the "math" of digit separation.
    formatted = f"{amount:,f}"

    # 3. Split into integer and fractional parts
    # Using 'f' in f-string prevents scientific notation (e.g., 1E+2)
    int_part, frac_part = formatted.split(".")

    # 4. Swap separators
    # Replace the default comma with a placeholder,
    # then swap to the user's preferred separators.
    res_int = int_part.replace(",", tsep)

    return f"{res_int}{dsep}{frac_part}"
