import numpy as dlf
# # 1D array
# n=dlf.array([1,2,3,4,5])
# print(n)

# # 2D array
# n1=dlf.array([[2,3,4],[6,7,8]])
# print(n1)

# # methods and operations
# ndim()
# n1=dlf.array([[2,3,4],[6,7,8],[9,10,11]])
# print(n1.ndim)

# shape()
# print(n1.shape)

# size()
# print(n1.size)

# # dtype()
# print(n1.dtype)

# # creating array using numpy methods
# zeros()
# print(dlf.zeros(10))

# ones()
# print(dlf.ones(3))

# arange()
# print(dlf.arange(2,12,1))

# linspace()
# print(dlf.linspace(1,10,9))

# # mathematical operations
# aray=dlf.array([23,34,26374527384672873482748237445,56,78,89])  # # # # # # 
# print(aray+1)
# print(aray*0)
# print(aray**4567)
# print(aray/6)
# print(aray//3)
# print(aray%2)

# # aggregate operations
# sum()
# print(dlf.sum(aray))

# mean()
# print(dlf.mean(aray))

# max()
# print(dlf.max(aray))

# standerd division()
# print(dlf.std(aray))

# # multi dimensional arrays(matrix operation)
mat1=dlf.array([[1,2,3],[2,3,4],[6,7,8]])
mat2=dlf.array([[9,8,7],[6,5,4],[3,2,1]])
# print(mat1+mat2)
# print(mat1*mat2)
# print(mat1**mat2)

# dot()
print(dlf.dot(mat1,mat2))

# transpose
print(dlf.transpose(mat1))













































