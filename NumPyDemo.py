import numpy as np

a = np.array([1,2,3,4,5])
print(a)
print(type(a))

print(a.shape)

a[3] = 40

print(a)

l1 = [1,2,3,4,5]
print(l1)
print(type(l1))

a = np.zeros((3,))
a = np.ones((4,4))
a = np.full((3,4), 5.4)
a = np.eye(4)
a = np.random.randint(1, 10, (3,4), int)

print(a)

arr = np.array([[-1, 2, 0, 4], 
                [4, -0.5, 6, 0], 
                [2.6, 0, 7, 8], 
                [3, -7, 4, 2.0]]) 

temp = arr[1::, ::2] # [:2,::2]

print(temp)

temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]] 
print ("\nElements at indices (0, 3), (1, 2), (2, 1),"
                                    "(3, 0):\n", temp) 
cond = arr <= 1 # cond is a boolean array 
temp = arr[cond] 
print ("\nElements greater than 0:\n", temp) 


# Basic operations
a = np.array([1, 2, 5, 3]) 
print('Shape:', a.shape)

# add 1 to every element 
print ("Adding 1 to every element:", a+1) 

# subtract 3 from each element 
print ("Subtracting 3 from each element:", a-3) 
  
# multiply each element by 10 
print ("Multiplying each element by 10:", a*10) 
  
# square each element 
print ("Squaring each element:", a**2) 

print(a)

# modify existing array 
a *= 2
print ("Doubled each element of original array:", a) 

# transpose of array 
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]]) 

print ("\nOriginal array:\n", a) 
print ("Transpose of array:\n", a.T) 

arr = np.array([[1, 5, 6], 
                [4, 7, 2], 
                [3, 1, 9]]) 
  
# maximum element of array 
print ("Largest element is:", arr.max()) 
print ("Row-wise maximum elements:", arr.max(axis = 1)) 

# minimum element of array 
print ("Column-wise minimum elements:", arr.min(axis = 0))

  
# sum of array elements 
print ("Sum of all array elements:", arr.sum()) 

print('Original Array:\n', arr)
# cumulative sum along each row 
print ("Cumulative sum along each row:\n", arr.cumsum(axis = 1))

