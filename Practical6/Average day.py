import numpy as np
import matplotlib.pyplot as plt

# Create a dictionary to hold how a student spends their day
time = {
    'sleeping': 8,   # Hours sleeping
    'classes': 6,     # Hours in classes
    'studying': 3.5, # Hours studying
    'TV': 2,         # Hours watching TV
    'music': 1       # Hours listening to music
}

# Figure out the time left for other stuff and add it to the dictionary
time['other'] = 24 - sum(time.values())

# Show the whole dictionary - just to see everything that's going on
print(time)

# Print out the hours spent sleeping
print("Sleeping:", time['sleeping'])

# Make a pie chart
plt.figure() # Start a new figure
plt.pie(time.values(), labels=time.keys()) # Plot the pie chart with labels

# Show the pie chart on the screen
plt.show()

# Clear the figure so we can draw something new next time
plt.clf()