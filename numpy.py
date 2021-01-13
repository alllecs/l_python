import numpy as np
import numpy.linalg as alg

#a = np.array([[3, 4, -2], [-2, -1, 4], [1, 2, 1]])
#a = np.array([['3', '4', '-2'], ['-2', '-1', '4'], ['1', '2', '1']], dtype = int)

# Сложение
a = np.array([[3, 4, -1], [-2, 1, 3]])
b = np.array([[1, 0, -5], [2, 2, -1]])
c = a + b

#Умножение

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8], [9, 1], [2, 3]])
c = np.dot(a, b)

c = 5 * a

# Определитель
a = np.array([[1, 2, 3], [0, 1, -3], [2, 1, 4]])
det_a = alg.det(a)

# Обратная матрица
inv_a = alg.inv(a)

