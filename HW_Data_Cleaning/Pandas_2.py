import pandas as pd
import numpy as np

# Assignment: Pandas_2
# Dan Goldgar u0414652

# Question 1: Compute Euclidean distance between p and q
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
diff = p - q
e_dist = np.sqrt(np.dot(diff.T, diff))
print(e_dist)

# Question 2: Swap columns A and C in a dataframe
col_swap = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
df2 = col_swap[['c', 'b', 'a', 'd', 'e']]
print(df2)

# Question 3: Swap columns A and C with a function
col_swap2 = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
# Function for swapping two columns at provided indices
def df_column_swap(df, index1, index2):
    col_list = list(df.columns)
    a, b = index1, index2
    col_list[b], col_list[a] = col_list[a], col_list[b]
    df = df[col_list]
    return df

df3 = df_column_swap(col_swap2,0,2)
print(df3)

# Question 4: Format or suppress scientific notations in a pandas dataframe.
df4 = pd.DataFrame(np.random.random(4)**10, columns=['random'])
pd.options.display.float_format = '{:.4f}'.format
print(df4)

# Question 5: Create a new column that contains the row number of nearest column by euclidean distance.
# Create a new column such that, each row contains the row number of nearest row-record by euclidean distance.
df5 = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1),
                  columns=list('pqrs'), index=list('abcdefghij'))

def euclidean_distance(list1, list2):
    list_diff = list1 - list2
    distance = np.sqrt(np.dot(list_diff.T, list_diff))
    return distance
# Initialize variables
current_dist = 0
distance_col = []
row_index_col = []
row_name_col = []
# Loop compares distance between each row and all others, retains minimum distance row and index
for i in range(df5.shape[0]):
    min_dist = 10000.0
    min_dist_index = 0
    min_dist_row = ''
    for j in range(df5.shape[0]):
        if i != j: current_dist = euclidean_distance(df5.iloc[i],df5.iloc[j])
        if current_dist < min_dist:
            min_dist = current_dist
            min_dist_index = j
            min_dist_row = df5.index[j]
    row_index_col.append(min_dist_index)
    distance_col.append(min_dist)
    row_name_col.append(min_dist_row)

df5['nearest_row'] = row_name_col
df5['distance'] = distance_col
print(df5)

# Question 6: Correlation - use the .corr() method to generate a correlation matrix
data6 = {'A': [45, 37, 0, 42, 50],
'B': [38, 31, 1, 26, 90],
'C': [10, 15, -10, 17, 100],
'D': [60, 99, 15, 23, 56],
'E': [76, 98, -0.03, 78, 90]}
df6_input = pd.DataFrame(data6)
df6 = df6_input.corr()
print(df6)