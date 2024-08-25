# index of fibonacci number that has 1000 digits

# fibonacci basic structure
def fib():
    arr = [0, 1]

    i = 2
    l = 1
    temp_arr = {0: 1}
    while i:
        temp = arr[i-1] + arr[i-2]
        arr.append(temp)

        if len(str(arr[i])) == 1000:
            print(i)
            break

        i += 1
        
fib()