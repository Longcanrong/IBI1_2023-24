import numpy as np 
import matplotlib.pyplot as plt

# susceptible = 0
# infected = 1
# recovered = 2
beta = 0.3 # infection rate
gamma = 0.05 # recovery rate

timestep = 100 #This is for "serires of plots", you can change the timestep to see the plot of which time.

population= np.zeros((100 , 100)) #create a population
outbreak= np.random.choice(a= range(100),size= 2) #randomly choose two numbers to act as x and y of the origin infected population
population [outbreak[0],outbreak[1]]=1
for j in range(timestep):
    infectedIndex = np.where(population==1)
    # by self-learning, I found it would return a tuple stored 2 array, each of it would store x or y, like([1,0,1],[0,1,0]).
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i] #get the ith data in the 1st array, which represents x value
        y = infectedIndex[1][i] #get the ith data in the 2nd array, which represents y value
        # recovery:
        population[x,y]= np.random.choice([1,2],1,p=[1-gamma,gamma])[0]
        # infect all 8 neighbours:
        offsets = [(i,j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0] # to find all 8 neighbours of 1 point
        neighbors = [(x+ dx, y+ dy) for dx, dy in offsets if 0<= x+ dx< 100 and 0<= y+ dy< 100] # Avoid situations where the point is a boundary point and the neighbour is out of range
        for neighbor in neighbors:
            if population[neighbor[0], neighbor[1]]== 0:
                population[neighbor[0],neighbor[1]]=np.random.choice(range(2),1,p=[1-beta,beta])[0] # infect
    
    plt.figure(figsize= (6,4), dpi=150)
    plt.imshow(population, cmap='viridis', interpolation='nearest') 
    plt.show()
