


import numpy as np # numpy is external library and need to be imported


# simple list 
list = [1,2,3]

# variable of numpy array type take list as argument
x = np.array(list)

print(type(x))
print(x)

# this is how numpy array turn multidementional array into matrix
myMatrix = [[1,2,3],[3,4,6],[3,6,9]]
print(np.array(myMatrix))

myMatrix2D = [[[1,2,3],[3,4,6],[3,6,9]],[[1,2,3],[3,4,6],[3,6,9]],[[1,2,3],[3,4,6],[3,6,9]],[[1,2,3],[3,4,6],[3,6,9]]]
print(np.array(myMatrix2D))

# this method create list of specified range
print(np.arange(0,5))

print(np.arange(0,15,4))


# this method specify list of zeros 
print(np.zeros(4))

# this method specify matrix of zeros 
print( np.zeros((4,3)))


# this method gives back list of ones 
print(np.ones(4))

# this method gives back matrix of ones
print( np.ones((4,3)))

# this is intresting method 
# gives back a specified range of numbers between two numbers  
print(np.linspace(3,4,7))

# this method gives identyty matrix of ones
print( np.eye(3))


# this method gives back random num between given range
#print( np.random.rand(1, 4))







 