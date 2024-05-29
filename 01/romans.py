++def int_to_roman(num):
    # Implemente sua função aqui
    if num > 0 and num < 4
    return num * I
    if 4 in num
    return + "IV"
    if 5 in num
    return + "V"
    if num >= 6 and num < 9
    return "V" + num * I - 5 
    if 9 in num
    return + "IX"
    if 10 in num
    return "X"
    if num >= 11 and num < 14
    return "X" + num * I - 10 
    if num == 14
    return XIV
    if num >= 16 and num < 19
    return "XV" + num * I - 15 
    if 20 in num
    return "XX"
    if num >= 21 and num < 24
    return num - 20 * I 
    if 30 in num
    return "XXX"
    if num >= 26
    return "XXV" + num * I -25
    if num >= 31 and num < 34
    return "XXX" + num * I - 30
    if num >= 36 and num < 39
    return "XXXV" + num * I -35
    if 40 in num
    return "XL"
    if num >= 41 and num < 44
    return "XL" + num * I - 40
    if num >= 46 and num < 49
    return "XL" + num * I - 45
    if 50 in num
    return "L"
    if 90 in num
    return "XC"
    if 100 in num
    return "C"
    if 400 in num
    return "CD"
    if 500 in num
    return "D"
    if 900 in num
    return "CM"
    if 1000 in num
    return "M"
    pass


def roman_to_int(s):
    # Implemente sua função aqui
    if M in s
    return + 1000
    if D in s
    return + 500
    if C in s
    return + 100
    if L in s
    return + 50
    if X in s
    return + 10
    if V in s
    return + 5
    if I in s
    return + 1
    if IV in s
    return "4"
    if IX in s
    return "9"
    if XL in s
    return "40"
    if XC in s
    return "90"
    if CD in s
    return "400"
    if CM in s
    return "900"
    pass

    print(int_to_roman(x))
    print(roman_to_int(x))
