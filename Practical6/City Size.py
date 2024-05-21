import matplotlib.pyplot as plt
import numpy as np

UK_tem_cities = [0.56, 0.62, 0.04, 9.7]  # input populations of UK cities
UK_cities = sorted(UK_tem_cities)  # sort the populations of UK cities
UK_labels = ['Edinburgh', 'Glasgow', 'Stirling', 'London']  # input name of UK cities

China_tem_cities = [0.58, 8.4, 29.9, 22.2]  # input populations of China cities
China_cities = sorted(China_tem_cities)  # sort the populations of China cities
China_labels = ['Haining', 'Hangzhou', 'Shanghai', 'Beijing']  # input name of China cities

index = np.arange(4)  # set the index for 4 cities

# Plot for UK cities
plt.figure()  # create a figure
plt.bar(index, UK_cities, 0.8)  # create a bar chart showing UK cities
plt.xticks(index, UK_labels)  # set xticks' labels to UK cities' names
plt.title("City Size of Population")  # mark the title
plt.show()

# Plot for China cities
plt.clf()  # clear the previous figure
plt.figure()  # create a new figure
plt.bar(index, China_cities, 0.8)  # create a bar chart showing China cities
plt.xticks(index, China_labels)  # set xticks' labels to China cities' names
plt.title("City Size of Population")  # mark the title
plt.show()