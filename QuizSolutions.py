#1 They both do not give any of the answers in the options
A = [1,2,3,4,5,6]
B = [13,21,34]
A_B=A.extend(B)
A_B2
print(A_B)
print(A_B2)

#2 Create an identity matrix in python
np.identity(3)

#3) Lowest average fuel cost per unit burned
df_fuel.groupby("fuel_type_code_pudl")["fuel_cost_per_unit_burned"].mean().sort_values()

#4) Standard deviation and 75th percentile of (Fuel_mmbtu_per_unit)
print(df_fuel.describe())

#5) Skewness and kurtosis for the fuel quantity burned in two decimal places?
from scipy.stats import kurtosis, skew
print(kurtosis(df_fuel.fuel_qty_burned))
print(skew(df_fuel.fuel_qty_burned))

#6) 
# Find the total number of missing values in the columns
df_fuel.isnull().sum()

# Assign a variable to the total number of missing values in the fuel_unit column
replace_fuelunit = df_fuel.fuel_unit.isnull().sum()

# Calculate the number of rows in the fuel_unit column
Num_of_rows=len(df_fuel)

# Calculate the percentage of missing rows to the total number of rows in the dataset
missingdata=round((180/Num_of_rows)*100,3)
print(missingdata)

#10) Which year has the highest average fuel cost per unit delivered?
Fuel_CPU_del_year=round(df_fuel.groupby('report_year')['fuel_cost_per_unit_delivered'].mean(),2)
print(Fuel_CPU_del_year)
