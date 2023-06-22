import math

import numpy as np

# All 0s matrix
a = np.zeros((2, 3), dtype='int16')  # (rows, columns) -> 2 major arrays, inside each -> 3 nums
print(f'a: {a}\n')
# All 1s matrix
# 4 major arrays,
# inside each major array -> 2 smaller arrays,
# inside each smaller array ->  2 elements
b = np.ones((4, 2, 2), dtype='int16')
print(f'b: {b}\n')

# All any number matrix --> np.full(shape, value)
c = np.full((2, 2), 100, dtype='int16')
print(f'c: {c}\n')

# can use existing arrays shape and fill it
d = np.full_like(a, 44, dtype='int16')
print(f'd: {d}\n')

# with random numbers from 1 to 10  --> by default 0 to 1
ax = np.random.rand(4, 2) * 10
print(f'ax: {ax}\n')

# use other's shape
bx = np.random.random_sample(b.shape)
print(f'bx: {bx}\n')

# random integer
cx = np.random.randint(0, 10, size=(2, 4), dtype='int16')
print(f'cx: {cx}\n')

# identity matrix
dx = np.identity(5, dtype='int16')
print(f'dx: {dx}\n')

# Matrix with 1s in the boundaries and 9 in the middle surrounded by 0s
# n = int(input('Enter a number: \n'))
# tx = np.ones((n, n), dtype='int16')
# print(f'Step 1:\n {tx}\n')
#
# for i in range(1, n-1):
#     for j in range(1, n-1):
#         tx[i, j] = 0
#
#
# print(f'Step 2:\n {tx}\n')
#
# mid = n // 2
#
# tx[mid, mid] = 9
# print(f'Result :\n {tx}\n')

# Another faster way to do above thing
n = int(input('Enter any odd number:  '))
output = np.ones((n, n), dtype='int16')  # main array
z = np.zeros((n-2, n-2), dtype='int16')  # would replace middle part of output
mid = (n-2) // 2  # to get to the middle element
z[mid, mid] = 9  # replace the mid element

output[1:n-1, 1:n-1] = z  # replace the middle part of output by z
print(output)


# Be Careful while copying arrays  --> if a is an array,
# b = a means a and b are pointing to same array, changes in one change another

