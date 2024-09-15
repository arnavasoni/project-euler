def is_paindrome(string):
    return True if string == string[::-1] else False

total = 0
for i in range(0, int(1e6)):
    i_bin = bin(i)
    i_bin = i_bin[2:]

    if is_paindrome(i_bin) and is_paindrome(str(i)):
        total += i

print(total)