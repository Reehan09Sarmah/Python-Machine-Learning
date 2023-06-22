import numpy as np

stats = np.array([[1, 2, 3], [4, 5, 6]])
print(f'stats: \n {stats}')

print(f'Min: {np.min(stats)}')
print(f'Max: {np.max(stats, axis=1)}')
# axis = 0 means give the array where max is and axis = 1 means give an array
# of the maximum number of the inside arrays

print(f'Sum: {np.sum(stats)}')
print(f'Sum Array:\n {np.sum(stats, axis=0)}')
# here, axis =0 means add corresponding elements (same index) of both arrays and return an array
# axis = 1 means add elements of each array within the array and return an array of their sums


# Vertically stack arrays
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
print(f'V1:\n {v1}')
print(f'V2:\n {v2}')

vx = np.vstack([v1, v2])
print(f'Vertically Staked V1 and V2 into Vx:\n {vx}')


# Horizontally stack arrays
h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))

hx = np.hstack([h1, h2])
print(f'Horizontally Staked h1 and h2 into hx:\n {hx}')
