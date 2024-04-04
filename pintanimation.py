import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_GLASSES = 5  # Number of glasses
AXIS_LIMITS = (0.5, 5.5)  # Axis limits from 1 to 5

# Initialize the glasses with initial water levels
glasses = np.zeros(NUM_GLASSES)

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(*AXIS_LIMITS)
ax.set_ylim(0, 1)
bars = ax.bar(range(1, NUM_GLASSES + 1), glasses, color='blue')  # Adjusted range for x-axis

# Function to update the plot for each frame
def update(frame):
    global glasses
    if frame % 2 == 0:  # Ali's turn
        distribute_water(glasses, 0.1)
    else:  # Beth's turn
        remove_water(glasses, (frame - 1) % NUM_GLASSES, ((frame - 1) % NUM_GLASSES + 1) % NUM_GLASSES)
    ax.clear()
    for i in range(len(glasses)):
        ax.bar(i + 1, glasses[i], color='blue')  # Adjusted x-position
    ax.set_xlim(*AXIS_LIMITS)
    ax.set_ylim(0, 1)

# Function to distribute water evenly among glasses
def distribute_water(glasses, water):
    glasses += water

# Function to remove water from two adjacent glasses
def remove_water(glasses, index1, index2):
    glasses[index1] = max(0, glasses[index1] - 0.5)
    glasses[index2] = max(0, glasses[index2] - 0.5)

# Animation function
ani = FuncAnimation(fig, update, frames=range(1, 21),  # Adjusted number of frames for both Ali's and Beth's turns
                    blit=False, interval=500, repeat=False)

# Save the animation as a GIF
ani.save('pintanimation.gif', writer='pillow', fps=2)

plt.show()
