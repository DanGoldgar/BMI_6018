import numpy as np
import pandas as pd
import urllib.request
from numpy.f2py.rules import numpy_version

print("Problem 1:")
# Print current numpy version
print(f"Current version of numpy: {numpy_version}")

print("Problem 2:")
# Create simple 1D array
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr)

print("Problems 3 & 4:")
# Retrieve data file from url
irisdata = urllib.request.urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# Create array from data. Type is set to None to preserve native float and str types
irisarr = np.genfromtxt(irisdata, delimiter =',', dtype = None)

# Check value at petal width column for each row until condition is met
for i in range(len(irisarr)):
    if irisarr[i][3] > 1.0:
        print(irisarr[i])   
        print(f"First element with petal width greater than 1.0 is at position {i}")
        break

print("Problem 5:")
np.random.seed(100)
a = np.random.uniform(1,50, 20)
# Replace values less than 10 and greater than 30 with 10 and 30 respectively
a[a < 10] = 10
a[a > 30] = 30
print(a)
# Note: Output for replaced values is unexpectedly formatted as
# (10.     ) or (30.     ) and it is unclear why or how to correct