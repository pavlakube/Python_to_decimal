def to_decimal(binary_str):
    try:
        decimal_value = int(binary_str, 2)
        return decimal_value
    except ValueError:
        return "Chyba: Zadaný řetězec není platný binární řetězec."

binary_input = input("enter binary string: ")
result = to_decimal(binary_input)
print(result)


