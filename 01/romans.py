++def int_to_roman(num):
    # Implemente sua função aqui
    if not isinstance(num, int) or num <= 0 or num > 3999:
        raise ValueError("O número deve ser maior que 1 e menor que 4000")
    
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

++def roman_to_int(s):
    # Implemente sua função aqui
    if not isinstance(s, str) or not s:
        raise ValueError("Não pode estar vazio")
    
    roman_dict = {
        'M': 1000, 'CM': 900,
        'D': 500, 'CD': 400,
        'C': 100, 'XC': 90,
        'L': 50, 'XL': 40,
        'X': 10, 'IX': 9,
        'V': 5, 'IV': 4,
        'I': 1
    }
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in roman_dict:
            num += roman_dict[s[i:i+2]]
            i += 2
        else:
            num += roman_dict[s[i]]
            i += 1
    return num

    print(int_to_roman(x))
    print(roman_to_int(x))
