def convert_cups_to_grams(uk_ingredient, cups):
    return int(uk_ingredient) * float(cups)


def convert_temperature(temperature, conversion):
    if conversion == "fahrenheit":
        result = (int(temperature) - 32) * 5 / 9
    elif conversion == "celsius":
        result = (int(temperature) * 9 / 5) + 32
    elif conversion == "gas_mark_f":
        result = 275 + (25 * (int(temperature) - 1))
    elif conversion == "gas_mark_c":
        result = 140 + (10 * (int(temperature) - 1))

    return round(result, 2)
