# LoopNumpyPlot
The LoopNumpyPlot function is a common pattern used for iterating over a range of parameters, computing results with NumPy, and visualizing the results using Matplotlib. This pattern can be particularly useful when you want to explore how different parameters affect the behavior of a function or model. 

# Programming practice - loops.
Loops are what makes programming powerful. A loop is simply a programming structure that performs a particular
task again and again. Loops are what allows us to process many millions of pieces of data! Here we will practice
writing loops. Most of these will be the for loop. A for loop operates a known number of times. For instance, if you
know you have to perform an operation for each element in an array, you know how many times the loop will execute (it will be the same as the length of the array), so you can use a for loop. Most loops you write will be for loops.
The other type of loop you may come across is the while loop. You usually use these when you don’t know how
many times something will execute. A while loop includes a condition. When that condition turns False, the loop
ends.

1. a) Write some python code that counts how many letters are in a string. Use a loop, don’t use a built-in
function like len.
b) Test your code for the word “antidisestablishmentarianism”.
2. a) Write some python code that uses a for loop to count how many times the letter “i” appears in the word
“antidisestablishmentarianism”.
b) Be sure to include the answer in your report.
3. a) Write a function that takes a list of numbers as input and returns the sum of all the positive numbers in
the list. Make sure you use a loop and not any built-in methods.
b) Test your function for [-5, -9, 3, -1, 11, 0] and [2, -1, 9, 0] and include the answers in your report.
4. a) Write a function that takes two input arguments: a number, x, and an integer, n. Use a loop to find
x^0 + x^1 + x^2 + .... + x^n and return this result.
b) Test your function for x = 2.7 and n = 8 and include the answers in your report.

# Numpy functions.

Numpy (https://numpy.org/) is a powerful python library capable of performing mathematical operations and
manipulating arrays. It is the cornerstone of any scientific analysis. To start off with, we will demonstrate how
numpy can perform the kind of tasks you may use your calculator for. But numpy can be used to solve problems
that you would struggle to solve with a calculator or spreadsheet alone.
I recommend going through this tutorial up to and including the section on “how do array mathematics work”:
https://www.datacamp.com/community/tutorials/python-numpy-tutorial.
Another tutorial that could be a useful resource is on the numpy website itself: https://numpy.org/devdocs/
user/quickstart.html
You will need to install the numpy library (follow instructions in the how to install python video on iKamva) and
whenever you want to use it you need to add this line at the top of your script:
import numpy as np
You can then access any numpy function like this: np.sin() (you use np to tell python which library to use, followed
by a dot and the function you want).
One thing to note is that all numpy functions can operate on arrays. A numpy array is essentially a list of numbers
such as:
x = np.array([0.5, 0., 1])
and
np.sin(x)
will produce:
array([0.47942554, 0. , 0.84147098])

1. a) Write a python function to calculate the following mathematical function:
    f(x) = sin(2x)e^(−x/5)
b) Test your function for x = 3.5 and for the array x = np.array([1.9, 8.9, 3.5]).

3. a) Write a python function to calculate the following mathematical function:
    f(x) = ln(x) − (x/8)^2
b) Test your function for x = 3.5 and for the array x = np.array([1.9, 8.9, 3.5]).

# Scientific plotting.

Scientists use plots to visualise data, understand their models and look for relationships. The plots are the most
important part of any paper, and you’ll find tons of them in industry too.
Matplotlib is the main scientific plotting library in python. It is incredibly flexible and can make everything from
simple line plots to advanced scatter plots, histograms and pie charts. This is a great tutorial for matplotlib:
https://www.w3schools.com/python/matplotlib_intro.asp
I will just introduce the basics of matplotlib plotting here by getting you to visualise the functions you coded up
in the previous question.
You will need to install the matplotlib library (follow instructions in the how to install python video on iKamva)
and whenever you want to use it you need to add this line at the top of your script (this is the standard way of
using matplotlib):
import matplotlib.pyplot as plt
You can then make a simple line plot like this:
x = np.linspace(1, 10, 100)
y = np.linspace(1, 10, 100)
plt.plot(x, y)
plt.show()
Notice how I use a function from numpy called linspace to create an array that has 100 values between 1 and 10.
How convenient!

#Questions:
1. a) Make a plot, for x-values from 1 to 10, of the following mathematical function:
    f(x) = sin(2x)e^(−x/5)
b) Be sure to include the plot in your report, as well as your well-commented code.
2. a) Make a plot, for x-values from 1 to 10, of the following mathematical function:
    f(x) = ln(x) − (x/8)^2
b) Be sure to include the plot in your report, as well as your well-commented code

# A dodgy spring.

Imagine you are a physics lecturer setting up a Hooke’s Law experiment for the students. You have bought a pack
of springs with a labelled spring constant of 25N/m. However, you are suspicious and think the springs might be
weaker than that. So you perform some measurements yourself, measuring the force for different extensions in cm.
You obtain the following measurements:
x (cm) force (N)
 5       1.27
 10      2.14
 15      2.69
 20      4.00
1. On the same plot, show the measured extensions and forces (using circle markers) and a line showing the
predicted force values for the same extension, if the given spring constant were correct (Hint: to plot two
things on the same plot, simply call plt.plot twice with the different sets of arguments).
2. Do you think the given value for k is accurate?

#  function.

A classic physics function: the gravitational potential energy function. In undergraduate physics, this function is used to describe the potential energy of an object in a gravitational field.

Gravitational Potential Energy Function
The gravitational potential energy 𝑈
of an object of mass 𝑚
at a height ℎ
above a reference level is given by:

𝑈(ℎ)=𝑚𝑔ℎ

where:

𝑚 is the mass of the object,
𝑔 is the acceleration due to gravity (approximately 9.81m/s near the Earth's surface),
h is the height above the reference level.

# How a physicist watches soccer.

Imagine you are playing soccer on the moon (so you can ignore air resistance). The moon’s gravity is 1.62m2/s.
You kick the ball at a 50 degree angle with an initial velocity of 61 m/s. You’re going to need to write some python
code to visualise the projectile motion of this ball.
A couple of hints:
• You’ll need the x and y component of the initial velocity. Something to remember is that for numpy’s
trignomometric functions, it expects the angle in radians not in degrees.
• You can calculate the maximum flight time of the ball using one of the equations of motion and the ycomponent of the initial velocity.
• Once you know the total flight time of the ball, you can make a numpy array of time steps and evaluate the
x and y coordinates at each point in time (remember numpy functions work on the entire array).

Answer the following:

1. Make a plot of the ball’s trajectory. Include a very clear description of how you generated this plot, including
writing down what equations you had to use. Also include your well-commented code.
2. How far does the ball travel before it hits the ground?
