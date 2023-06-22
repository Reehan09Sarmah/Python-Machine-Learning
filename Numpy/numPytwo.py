import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)

# Get a specific element --> same indexing rule as accessing elements from list
print(a[1, 5])
print(a[0, -5])

# Get a specific row -- let's say row 1 (index 1)
print(a[0, :])
# Get a specific column --let's say column 2 (index 2)
print(a[:, 2])

# getting more fancy --> row or column or both can be --> start: end: step
print(a[0, 0:6:2])  # from 1st row, fetch elements from 0 to 6-1 column in steps of 2

# if row / column part --> start : end --> goes from start to end-1
# fetch rows 0 to 2-1=1, then from those rows fetch from column 1 to 8-1 = 7 column
print(a[0:2, 1:8])


# To change
a[1, 5] = 20
print(a)

# For all rows, change the column 2 to 10s
a[:, 2] = 10  # or a[:, 2] = [10, 10] --> since we know 2 rows are there
print(a)


b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)
print(b[0, 1, 1])  # use indexes -- 0th greater array, smaller inside array 1, element 1 of it
# use indexes cleverly as you go deep inside


# getting 1st element of each smaller array
# all the bigger arrays, all the smaller arrays of each bigger array,
# element of index 0 of each smaller array of each bigger array
print(b[:, :, 0])  # similarly replace elements, array



