def GCD(a: int, b: int) -> int:
    while b != 0:
        b, a = a % b, b

    return a


def solution() -> int:

    result_num = 1
    result_den = 1
    
    for num in range(10, 100):
        for den in range(num + 1, 100):
            common_digits = set(str(num)) & set(str(den))
            
            if "0" in common_digits:
                common_digits.remove("0")
            
            if len(common_digits) == 1:
                common_digit = list(common_digits)[0]
                new_num = str(num).replace(str(common_digit), "")
                new_den = str(den).replace(str(common_digit), "")
            
                if not new_num or not new_den:
                    continue
            
                if num * int(new_den) == den * int(new_num):
                    result_num *= num
                    result_den *= den
    
    gcd = GCD(result_num, result_den)
    return result_den // gcd

sol = solution()
print(sol)