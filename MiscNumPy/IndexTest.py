# load data from assign.txt and perform some indexing
import numpy as np

field_data = np.genfromtxt('assign.txt', delimiter=',')
print(field_data, '\n')

# to get 11, 12, 16, 17 from field_data
get1 = field_data[2:4, 0:2]
print(f'First result:\n {get1}\n')

# to get 2, 8, 14, 20 using indexing --> [[row indexes], [column indexes]]
get2 = field_data[[0, 1, 2, 3], [1, 2, 3, 4]]  # match corresponding index to get each element
print(f'Second result:\n {get2}\n')

# to get 4,5, 24, 25, 29, 30 using indexing --> [[row indexes], column indexes]
get3 = field_data[[0, 4, 5], 3:]
print(f'Third result:\n {get3}\n')

