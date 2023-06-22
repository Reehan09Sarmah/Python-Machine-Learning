import numpy as np


a = np.array([1, 2, 3])
print(a)
b = np.array([[2, 3, 5, 6], [9, 4, 5, 6]])
print(b)
# So if we know the size of data that would be stored here,
# we can/should specify the datatype
c = np.array([2, 5, 6], dtype='int16')
print(c)

# Get total number of elements
print('Get total number of elements')
print('a:', a.size)
print('b:', b.size)

# Get Dimensions
print("Get Dimensions")
print('a:', a.ndim)
print('b:', b.ndim)

# Get Shape --> Shape of Array (rows x columns)
print('Get Shape --> (rows, columns)')
print('b:', b.shape)

# Get Type --> data type of array
print('')
print(a.dtype)
print(b.dtype)
print(c.dtype)

# Get Size --> Sizer of each item --> int32 = 4, int16 = 2
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

# Total Size --> In terms of bytes = a.itemsize * a.size
print(c.nbytes)
