import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# |x| + |y| <= 1
# |y| + |z| <= 1
# |z| + |x| <= 1

# Create a grid of points in the range -1 to 1
x = np.linspace(-1, 1, 25)
y = np.linspace(-1, 1, 25)
z = np.linspace(-1, 1, 25)

# Create a meshgrid from x, y, and z
X, Y, Z = np.meshgrid(x, y, z)

# Calculate the condition for each point in the meshgrid
condition1 = np.abs(X) + np.abs(Y) <= 1
condition2 = np.abs(Y) + np.abs(Z) <= 1
condition3 = np.abs(Z) + np.abs(X) <= 1

# Combine the conditions using logical AND
combined_condition = condition1 & condition2 & condition3

# Create a figure and a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points that satisfy the combined condition
ax.scatter(X[combined_condition], Y[combined_condition], Z[combined_condition], c='b', marker='o', label='Satisfies conditions')

# Set labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.legend()
plt.show()