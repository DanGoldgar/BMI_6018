import pandas as pd

# Import data and rename columns with field names from file
bc_data = pd.read_csv("breast+cancer/breast-cancer.data", header = None)
bc_data.columns = ['Class','Age','Menopause','Tumor-Size','Inv-Nodes','Node-Caps','Deg-Malig','Breast','Breast-Quad','Irradiat']
# Test print
print(bc_data)

# 1. Demonstrate melt function: Melt table using class as ID column, shown against age variable
print('Melt:')
melt_1 = pd.melt(bc_data, id_vars = ['Class'], value_vars= ['Age'])
# Here we see the dataframe has been resized to 286 x 3
print(melt_1)
# If we do not specify value_vars, dataframe includes all variables and is resized to 2574 x 3
melt_2 = pd.melt(bc_data, id_vars = ['Class'])
print(melt_2)

# 2. Demonstrate pivot function
# Add column of unique event indices to facilitate pivot function and avoid duplicates
print('Pivot:')
bc_data_1 = bc_data.reset_index()
bc_data_1.rename(columns = {'index':'Event No.'}, inplace = True)
print(bc_data_1)
# Pivot on Event No. & Class
pivot_1 = bc_data_1.pivot(index = 'Event No.', columns = 'Class')
print(pivot_1)

# 3. Demonstrate aggregate functionality: Print sum, min, max, and mean of 'Deg-Malig' field
print('Aggregate:')
print(bc_data.aggregate({'Deg-Malig':['sum','min', 'max', 'mean']}))

# 4. Demonstrate iterrows function: Iterate over the rows of the dataset, print values for age and menopause fields
print('Iterrows:')
for index, row in bc_data.iterrows():
    print(f"{index} - Age: {row['Age']} - Menopause: {row['Menopause']}")

# 5. Demonstrate groupby function. Because most values are non-numerical, we can only calculate statistics
# on the 'Deg-Malig' int values (as with .aggregate). In the 2nd example we return the first value for string fields
print('Groupby:')
bc_data_age = bc_data.groupby(['Age']).mean(numeric_only=True)
print(bc_data_age)
# Here the groupby function alerts us to missing data values in the 'Breast-Quad' field, as the value '?' appears
# in the breast quadrant groups
bc_data_quad = bc_data.groupby(['Breast-Quad']).first()
print(bc_data_quad)

