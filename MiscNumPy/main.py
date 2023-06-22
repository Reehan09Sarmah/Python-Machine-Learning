import numpy as np

# Load data from file
data = np.genfromtxt("data.txt", delimiter=',')
print(f'Data from file:\n {data}')

dataInt32 = data.astype('int32')
print(f'Data from file in int32 format:\n {dataInt32}')

# Boolean Masking and Advanced Indexing

# print array of boolean values telling if the numbers
# in dataInt32 array are greater than 30 or not, the comparisons may also vary like >x and <y , etc.
dataInt32Bool = dataInt32 > 30
print(f'Boolean Data from file (if > 30):\n {dataInt32Bool}')
# if any number in a column is > 30, it's true value
print(f'Column wise boolean values:\n {np.any(dataInt32 > 30, axis=0)}')

# You can index with a list in NumpY
# passing in indexes as an array for getting an array of elements we need
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a[[1, 2, 8]]
print(f'b as taken from a:\n {b}')


