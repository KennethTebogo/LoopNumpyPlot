

### PRAC 3 ###

########################################

# Put your full name here :Kenneth 
# Put your student number here :3968676
# Don't forget to rename this file with your student number!
# For instance, my file would be named 1234567_prac4.py 
# Also don't forget to comment your code or you get no marks! 

########################################

### Question 1 ### Programming practice - loops

########################################

### Q1.1 

# Put your code here

# Define a function to count the number of characters in a given string
def count_characters(s):
    # Initialize a counter to zero
    count = 0
    
    # Iterate over each character in the string
    for _ in s:
        # Increment the counter by 1 for each character
        count += 1
    
    # Return the total count of characters
    return count

# Call the function with the string "Kenneth" and store the result in 'result'
result = count_characters("“antidisestablishmentarianism")

# Print the result, which is the number of characters in the string "Kenneth"
print(result)  # Output will be 29

### Q1.2 

# Put your code here 
# Define the word to search
word = "antidisestablishmentarianism"

# Initialize a counter for the letter 'i'
count_i = 0

# Iterate over each character in the word using a different variable name
for letter in word:
    # Check if the current character is 'i'
    if letter == 'i':
        # Increment the counter if it is 'i'
        count_i += 1

# Print the total count of 'i' in the word
print("The letter 'i' appears", count_i, "times in the word.")

### Q1.3 

# Put your code here 
def sum_of_positive_numbers(numbers):
    # Initialize a variable to hold the sum of positive numbers
    total_sum = 0
    
    # Iterate over each number in the list
    for number in numbers:
        # Check if the number is positive
        if number > 0:
            # Add the positive number to the total sum
            total_sum += number
    
    # Return the total sum of positive numbers
    return total_sum

# Example usage

numbers_list = [2, -1, 9, 0]
result = sum_of_positive_numbers(numbers_list)
print("The sum of positive numbers is:[2, -1, 9, 0]:", result)
#Result:11
numbers_list = [-5, -9, 3, -1, 11, 0]
result = sum_of_positive_numbers(numbers_list)
print("The sum of positive numbers is:[-5, -9, 3, -1, 11, 0]:", result)
#Result:14
### Q1.4 

# Put your code here 
def sum_of_powers(x, n):
    # Initialize the sum to 0
    total_sum = 0
    
    # Initialize the current power to x^0, which is 1
    current_power = 1
    
    # Loop from 0 to n (inclusive)
    for i in range(n + 1):
        # Add the current power to the total sum
        total_sum += current_power
        # Update the current power to the next power of x
        current_power *= x
    
    # Return the total sum
    return total_sum

# Example usage
x = 2.7
n = 8
result = sum_of_powers(x, n)
print("The sum of the series is:", result)
#Result:4485.057344110002

########################################

### Question 2 ### Numpy functions

########################################

### Q2.1 

# Put your code here 
import numpy as np

# Define the function
def calculate_f(x):
    return np.sin(2 * x) * np.exp(-x / 5)

# Test for a single value
single_value = 3.5
result_single = calculate_f(single_value)
print(f"f({single_value}) = {result_single}")

# Test for an array of values
array_values = np.array([1.9, 8.9, 3.5])
result_array = calculate_f(array_values)
print(f"f({array_values}) = {result_array}")
#result:f([1.9 , 8.9 , 3.5]) = [-0.418426 , -0.14624337 , 0.32624989]

### Q2.2 

# Put your code here 
import numpy as np

# Define the function
def calculate_f(x):
    return np.log(x) - (x / 8) ** 2

# Test for a single value
single_value = 3.5
result_single = calculate_f(single_value)
print(f"f({single_value}) = {result_single}")

# Test for an array of values
array_values = np.array([1.9, 8.9, 3.5])
result_array = calculate_f(array_values)
print(f"f({array_values}) = {result_array}")
#result:f([1.9 8.9 3.5]) = [0.58544764 0.94839503 1.06135672]


########################################

### Question 3 ### Scientific plotting

########################################

### Q3.1 

# Put your code here 
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.sin(2 * x) * np.exp(-x / 5)

# Define the range of x values
x = np.linspace(1, 10, 500)

# Compute the function values
y = f(x)

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$f(x) = \sin(2x) \cdot e^{-x/5}$')
plt.title('Plot of $f(x) = \sin(2x) \cdot e^{-x/5}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

### Q3.2 

# Put your code here 
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.log(x) - (x / 8)**2

# Define the range of x values
x = np.linspace(1, 10, 500)

# Compute the function values
y = f(x)

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = ln(x) - (x/8)^2')
plt.title('Plot of f(x) = ln(x) - (x/8)^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()


########################################

### Question 4 ###

########################################

### Q4.1 

# Put your code here 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Given data
x_cm = np.array([5, 10, 15, 20])  # extension in cm
force_N = np.array([1.27, 2.14, 2.69, 4.00])  # force in N

# Convert extension from cm to meters
x_m = x_cm / 100

# Perform linear regression to find the best-fit line
slope, intercept, r_value, p_value, std_err = linregress(x_m, force_N)
spring_constant = slope

# Calculate predicted forces using the given spring constant
given_spring_constant = 25  # N/m
predicted_forces = given_spring_constant * x_m

# Plot the experimental data with circle markers
plt.figure(figsize=(10, 6))
plt.plot(x_m, force_N, 'o', color='red', label='Measured Data')

# Plot the best-fit line for the experimental data
plt.plot(x_m, slope * x_m + intercept, color='blue', label=f'Best-fit Line\nExperimental Spring Constant = {spring_constant:.2f} N/m')

# Plot the predicted force values with the given spring constant
plt.plot(x_m, predicted_forces, '--', color='green', label=f'Predicted Line\nGiven Spring Constant = {given_spring_constant} N/m')

# Add titles and labels
plt.title('Hooke\'s Law Experiment')
plt.xlabel('Extension (m)')
plt.ylabel('Force (N)')
plt.legend()
plt.grid(True)
plt.show()

# Output the calculated spring constant
print(f"Calculated spring constant: {spring_constant:.2f} N/m")


### Q4.2 

### This question is written only, no code required.
# No calculated spring constant is 17.48N/m and you bought a spring with constant of 25N/m which mean the spring is weaker.

########################################

### Question 5 ###

########################################

# Put your code here 

# Put your code here 
import numpy as np
import matplotlib.pyplot as plt

# Define the function for gravitational potential energy
def gravitational_potential_energy(mass, height, g=9.81):
    """
    Calculate the gravitational potential energy.
    
    Parameters:
    mass (float): Mass of the object in kilograms.
    height (numpy array): Heights at which to calculate potential energy in meters.
    g (float): Acceleration due to gravity in m/s^2 (default is 9.81 m/s^2).
    
    Returns:
    numpy array: Gravitational potential energy at each height.
    """
    return mass * g * height

# Define parameters
mass = 10  # mass in kilograms
height_range = np.linspace(0, 100, 500)  # heights from 0 to 100 meters

# Compute gravitational potential energy
energy = gravitational_potential_energy(mass, height_range)

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(height_range, energy, label=f'Gravitational Potential Energy (mass = {mass} kg)', color='blue')
plt.title('Gravitational Potential Energy vs. Height')
plt.xlabel('Height (m)')
plt.ylabel('Gravitational Potential Energy (J)')
plt.grid(True)
plt.legend()
plt.show()


########################################

### Question 6 ###

########################################

### Q6.1 

# Put your code here 
import numpy as np
import matplotlib.pyplot as plt

# Constants
v0 = 61  # Initial velocity in m/s
theta_deg = 50  # Angle in degrees
g = 1.62  # Moon's gravity in m/s^2

# Convert angle to radians
theta_rad = np.radians(theta_deg)

# Calculate initial velocity components
v0x = v0 * np.cos(theta_rad)  # x component of initial velocity
v0y = v0 * np.sin(theta_rad)  # y component of initial velocity

# Calculate the time of flight
t_max = 2 * v0y / g

# Create an array of time steps
t = np.linspace(0, t_max, num=500)

# Calculate x and y coordinates
x = v0x * t
y = v0y * t - 0.5 * g * t**2

# Plot the trajectory
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Projectile Trajectory')
plt.title('Projectile Motion of a Soccer Ball on the Moon')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.grid(True)
plt.legend()
plt.show()


### Q6.2 

### This question is written only, no code required.
#The ball travels approximately 2262.02 meters before hitting the ground.

########################################

########################################
