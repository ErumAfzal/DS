
Numpy-2D_Erum.ipynb
Numpy-2D_Erum.ipynb_
italicized text# 2D Numpy in Python



[1]
0s
# Import the libraries

import numpy as np
Consider the list a, which contains three nested lists each of equal size.


[7]
0s
a = np.array([[101,39,59,61],[102,58,89,67 ], [103,59,78,72]]) # one data point
a
array([[101,  39,  59,  61],
       [102,  58,  89,  67],
       [103,  59,  78,  72]])

[8]
0s
# Create a list

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a
[[11, 12, 13], [21, 22, 23], [31, 32, 35]]
We can cast the list to a Numpy Array as follows:


[9]
0s
# Convert list to Numpy Array
# Every element is the same type

A = np.array(a)
A
array([[11, 12, 13],
       [21, 22, 23],
       [31, 32, 33]])
We can use the attribute ndim to obtain the number of axes or dimensions, referred to as the rank.


[10]
0s
# Show the numpy array dimensions

A.ndim
2
Attribute shape returns a tuple corresponding to the size or number of each dimension.


[ ]
# Show the numpy array shape

A.shape # number of rows and number of columns
(3, 3)
The total number of elements in the array is given by the attribute size.


[ ]
# Show the numpy array size

A.size
9

[12]
a1 = np.array([11, 12, 13])
a1[2]
np.int64(13)
Accessing different elements of a Numpy Array
We can use rectangular brackets to access the different elements of the array. The correspondence between the rectangular brackets and the list and the rectangular representation is shown in the following figure for a 3x3 array:


We can access the 2nd-row, 3rd column as shown in the following figure:


We simply use the square brackets and the indices corresponding to the element we would like:


[ ]
# Access the element on the second row and third column

A[1, 2]
23
We can also use the following notation to obtain the elements:


[ ]
A[1]
array([21, 22, 23])

[ ]
# Access the elements on the second row first, then get the third element

A[1][2]
23
Consider the elements shown in the following figure


We can access the element as follows:


[ ]
# Access the element on the first row and first column

A[0][0]
11
We can also use slicing in numpy arrays. Consider the following figure. We would like to obtain the first two columns in the first row


This can be done with the following syntax:


[15]
0s
# Access the element on the first row and first and second columns

A[0][0:2] # important

array([11, 12])
Similarly, we can obtain the first two rows of the 3rd column as follows:


[17]
# Access the element on the first and second rows and third column


A[0:2, 2]

array([13, 23])
Corresponding to the following figure:



Basic Operations
We can also add arrays. The process is identical to matrix addition. Matrix addition of X and Y is shown in the following figure:


The numpy array is given by X and Y


[ ]
# Create a numpy array X

X = np.array([[1, 0], [0, 1]])
X
array([[1, 0],
       [0, 1]])

[ ]
# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]])
Y
array([[2, 1],
       [1, 2]])
We can add the numpy arrays as follows.


[ ]
# Add X and Y

Z = X + Y
Z
array([[3, 1],
       [1, 3]])
Multiplying a numpy array by a scaler is identical to multiplying a matrix by a scaler. If we multiply the matrix Y by the scaler 2, we simply multiply every element in the matrix by 2, as shown in the figure.


We can perform the same operation in numpy as follows


[ ]
# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]])
Y
array([[2, 1],
       [1, 2]])

[ ]
# Multiply Y with 2

Z = 2 * Y
Z
array([[4, 2],
       [2, 4]])
Multiplication of two arrays corresponds to an element-wise product or Hadamard product. Consider matrix X and Y. The Hadamard product corresponds to multiplying each of the elements in the same position, i.e. multiplying elements contained in the same color boxes together. The result is a new matrix that is the same size as matrix Y or X, as shown in the following figure.


We can perform element-wise product of the array X and Y as follows:


[ ]
# Create a numpy array X

X = np.array([[1, 0], [0, 1]])
X
array([[1, 0],
       [0, 1]])

[ ]
# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]])
Y
array([[2, 1],
       [1, 2]])

[ ]
# Multiply X with Y

Z = X * Y
Z
array([[2, 0],
       [0, 2]])
We can also perform matrix multiplication with the numpy arrays A and B as follows:

First, we define matrix A and B:


[ ]
# Create a matrix A

A = np.array([[0, 1, 1], [1, 0, 1]])
A
array([[0, 1, 1],
       [1, 0, 1]])

[ ]
# Create a matrix B

B = np.array([[1, 1], [1, 1], [-1, 1]])
B
array([[ 1,  1],
       [ 1,  1],
       [-1,  1]])
We use the numpy function dot to multiply the arrays together.


[ ]
# Calculate the dot product

Z = np.dot(A,B)
Z
array([[0, 2],
       [0, 2]])

[ ]
# Calculate the sine of Z

np.sin(Z)
array([[0.        , 0.90929743],
       [0.        , 0.90929743]])
We use the numpy attribute T to calculate the transposed matrix


[18]
0s
# Create a matrix C

C = np.array([[1,1],[2,2],[3,3]])
C
array([[1, 1],
       [2, 2],
       [3, 3]])

[19]
0s
# Get the transposed of C

C.T
array([[1, 2, 3],
       [1, 2, 3]])
Quiz on 2D Numpy Array
Consider the following list a, convert it to Numpy Array.


[ ]
# Write your code below and press Shift+Enter to execute

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
Click here for the solution
Calculate the numpy array size.


[ ]
# Write your code below and press Shift+Enter to execute

Click here for the solution
Access the element on the first row and first and second columns.


[ ]
# Write your code below and press Shift+Enter to execute

Click here for the solution
Perform matrix multiplication with the numpy arrays A and B.


[ ]
# Write your code below and press Shift+Enter to execute

B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
Click here for the solution
The last exercise!
Congratulations, you have completed your first lesson and hands-on lab in Python.


[ ]

Start coding or generate with AI.
Colab paid products - Cancel contracts here
[0][0:3]
