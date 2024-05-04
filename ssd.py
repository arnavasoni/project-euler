import numpy as np

array = np.arange(1, 101)

# (1 + 2 + ... + 100)^2
arr_ele_sum_sq = np.square(np.sum(array))
print(arr_ele_sum_sq)

# 1^2 + 2^2 + 3^2 + ... + 100^2
arr_ele_sq_sum = np.sum(np.square(array))
print(arr_ele_sq_sum)

print(arr_ele_sum_sq - arr_ele_sq_sum)