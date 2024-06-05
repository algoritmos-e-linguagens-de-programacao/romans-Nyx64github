def int_to_roman(num):
    # Implemente sua função aqui
    if not isinstance(num, int) or num <= 0 or num > 3999:
        raise ValueError("O número deve ser maior que 0 e menor que 4000")
    
    rom2 = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    num2 = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]

    roman_num = ''
    for i in range(len(num2)):
        count = num // num2[i]
        roman_num += rom2[i] * count
        num -= num2[i] * count
    return roman_num

def roman_to_int(s):
    # Implemente sua função aqui
    if not isinstance(s, str) or not s:
        raise ValueError("A string de input não deve estar vazia")
    
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }
    
    num = 0
    prev_value = 0
    for char in reversed(s):
        if char not in roman_dict:
            raise ValueError("Há letras ou números inválidos na string")
        value = roman_dict[char]
        if value < prev_value:
            num -= value
        else:
            num += value
        prev_value = value
    return num
    
    print(int_to_roman(x))
    print(roman_to_int(x))
