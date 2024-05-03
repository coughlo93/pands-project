# Import Libraries
# Importing libraries or modules in Python is essential for accessing their functionalities, such as predefined functions, classes, or variables. 
# By importing libraries, I will be able to utilise the work already done by others, which helps save time and effort when coding common tasks.

# Data Frames
import pandas as pd
# Plotting
import matplotlib.pyplot as plt
# Numerical arrays.
import numpy as np

# Load Data
# By loading the data, this allows me to work with datasets directly within the python environment. 
# This is essential in data analysis as it ensures I will be able to manipulate, analyse, visualise and process the data using the extensive libraries available in python such as Pandas, NumPy etc.
# It turns writing code and working with data into a seamless transition.

# Fetch Data From URL
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Inspect the data.
# Inspecting data in Python allows you to gain insights into its structure, content, and quality. 
# This process is crucial for data preprocessing, as it helps identify potential issues or anomalies that may need to be addressed before further analysis or modeling

# Inspect the data.
df 

# Inspect the Types
# Inspecting types in Python is a valuable tool for understanding, debugging, and ensuring the correctness of your code.
# It helps you write more robust and maintainable programs, especially in large and complex codebases
# Inspect the Types
df.dtypes 

# Summary of the Data
df.describe()

# Variable Plots
# Get just petal length
plen = df['petal_length']
# Show
print(plen)
# Type
print(type(plen))

# Just the NUMPY array
plan = plen.to_numpy()

# Show
plen

# Get just petal width
pwidth = df['petal_width'].to_numpy()
# Show
pwidth

# Create a Simple Plot
plt.plot(plen, pwidth, 'x')
# Axis labels
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
#Title
plt.title('Iris Data Set')
# X Limits
plt.xlim(0, 8)
# Y Limits
plt.ylim(0, 4)

# Create a new figure and set of axes
fig, ax = plt.subplots(1, 1)
# Simple Plot
ax.plot(plen, pwidth, 'x')
# Axis labels
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal Width (cm)')
#Title
ax.set_title('Iris Data Set')
# X Limits
ax.set_xlim(0, 8)
# Y Limits
ax.set_ylim(0, 4)

# Add a Best Fit Line

# Define variables
m = 2
c = 3
x = 5
# Compute y
y = m * x + c
# Print the result
print("y =", y)

# Best fit line equation
# y = mx + c =p_1 x^1 + p_0 = p_1 x+p_0

# Fit a straight line between x and y
m, c = np.polyfit(plen,pwidth, 1)
# Show m and c
m, c

# Create a new figure and set of axes
fig, ax = plt.subplots(1, 1)
# Simple Plot
ax.plot(plen, pwidth, 'x')
# Simple Plot
ax.plot(plen, m * plen + c , 'r-')
# Axis labels
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal Width (cm)')
#Title
ax.set_title('Iris Data Set')
# X Limits
ax.set_xlim(0, 8)
# Y Limits
ax.set_ylim(0, 4)

# X Values for best fit line
bf_x = np.linspace(0.0, 8.0, 100)
# Y Values for best fit line
bf_y = m * bf_x + c

# Create a new figure and set of axes
fig, ax = plt.subplots(1, 1)
# Simple Plot
ax.plot(plen, pwidth, 'x')
# Simple Plot
ax.plot(bf_x, bf_y, 'r-')
# Axis labels
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal Width (cm)')
#Title
ax.set_title('Iris Data Set')
# X Limits
ax.set_xlim(0, 8)
# Y Limits
ax.set_ylim(-1, 4)

# Measure the correlation
np.corrcoef(plen, pwidth) 

