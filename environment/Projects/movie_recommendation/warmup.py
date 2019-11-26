from numpy import *

data = array([[1,2,3],[1,2,3]])
print data

print data.shape

zeroes_matrix = zeros((1,2))

print zeroes_matrix

ones_matrix = ones((1,2))

print ones_matrix

rand_matrix = random.randint(10, size = (10,5))

print rand_matrix

col_vector = random.randint(10, size = (10,1))
print col_vector

col_vector[0] = 100
print col_vector

print rand_matrix[0, 0]

print rand_matrix[:, 0:1]

print rand_matrix[0:1, :]

cols = array([[1,2,4]])
print rand_matrix[0, cols]

flattened = rand_matrix.T.flatten()

print flattened

rand_matrix2 = random.randint(10, size=(5,2))

dot_product = rand_matrix.dot(rand_matrix2)

print dot_product