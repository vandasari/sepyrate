from decimal import Decimal


def digit_separation(amount, tsep, dsep=None):
    # 1. Ensure it's a Decimal
    if not isinstance(amount, Decimal):
        amount = Decimal(str(amount))

    # 2. Standardize dsep if it's None
    if dsep is None:
        dsep = "," if tsep == "." else "."

    # 3. Format with comma as thousands separator and dot as decimal
    # This handles all the "math" of digit separation.
    formatted = f"{amount:,f}"

    # 4. Handle the split and swap
    if "." in formatted:
        int_part, frac_part = formatted.split(".")
        # Replace default comma with user's tsep
        return f"{int_part.replace(',', tsep)}{dsep}{frac_part}"
    else:
        # It's an integer
        return formatted.replace(",", tsep)
