import numpy as np
import matplotlib.pyplot as plt
# You will need to install "opencv-python" on Thonny. Go to "Tools -> Manage
# Packages" and then type in "opencv-python" and click install.
import cv2


##################### Coding Problem 1 ##########################
## Part a - Define the 3x3 rotation matrix.

## Part b - Define the vector y, setup the algebraic problem, and then solve for x



######################### Coding problem 2 ###################
## Part (a) - Think about how the matrix equation is setup!

## Part (b) - Write the matrix-vector equation
# Define W8, W9, W10, and W11
W8 = 12000
# etc.

# Predefine the square-root term and the matrix, A, and the vector b
s = 1 / np.sqrt(17) 
AA = np.zeros([19,19]) 
b = np.zeros([19, 1]) 
# It starts off with a lot of zeros. Now update part by part.

# Equation 1
j = 1-1 # because python indexing begins at 0, F1 is actually F[0]
AA[j, 1-1] = -s # Coefficient of F1
AA[j, 2-1] = 1  # Coefficient of F2
AA[j, 12-1] = s # Coefficient of F12

# Equation 2
j = 2-1  # because python indexing begins at 0, F[1] is actually F[0]
AA[j, 1-1] = -4 * s # Coefficient of F1
AA[j, 12-1] = -4 * s # Coefficient of F12


# Equation 3
j = 3-1 
# You fill this one in

# Equation 4
j = 4-1 
# You fill this one in

# Equation 5
j = 5-1 
# You fill this one in

# Equation 6
j = 6-1 
# You fill this one in

# Equation 7
j = 7-1 
# You fill this one in

# Equation 8
j = 8-1 
# You fill this one in


# Equation 9
j = 9-1 
# You fill this one in

# Equation 10
j = 10-1 
# You fill this one in

# Equation 11
j = 11-1 
# You fill this one in

# Equation 12
j = 12-1 
# You fill this one in

# Equation 13
# This is the first equation that has a W_n term in it. That does not multiply
# any of the unknows, W_k, so we move it to the right-hand side: it is part of b
j = 13-1 
AA[j, 18-1] = 4 * s
AA[j, 19-1] = 4 * s
b[j] = W8 

# Equation 14
j = 14-1 
# You fill this one in

# Equation 15
j = 15-1 
# You fill this one in

# Equation 16
j = 16-1 
# You fill this one in

# Equation 17
j = 17-1 
# You fill this one in

# Equation 18
j = 18-1 
# You fill this one in

# Equation 19
j = 19-1 
# You fill this one in

## Part c - save A

## Part d - Find the forces

## Part e - Find the largest force
# Make sure you have the order correct: we want the largest OF the absolute
# values!


## Part f - We now need to loop somehow. Once one of the forces exceeds 44000
# Newtons, the bridge collapses. It *can* be exactly 44000 Newtons without
# collapsing.
# You will need a break statement if the bridge collapses!


##################### Coding Problem 3 ##########################
## Load in the image of beautiful Olive
A = cv2.imread('olive.jpg', 0) # Make sure that 'olive.jpg' is in the same
                               # folder as this file

## Part (a) - Perform SVD
U, S, Vt = np.linalg.svd(A, full_matrices=False) # Vt = V transpose

## Part (b) - Find the 15 largest singular values.
# Remember that the singular values are ranked by default!

## Part (c) - Calculate the rank-1 energy proportion
total_energy = np.sum(S)
# Now use that to get A12

## Part (d) - Calculate the proportion of energy in the rank-15 approximation

## Part (e) - Find the rank-r approximation that holds 75% of the total energy.
# Use np.where! Don't hard code this!



