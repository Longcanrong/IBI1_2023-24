import numpy as np 
import matplotlib.pyplot as plt

# susceptible = 0
# infected = 1
# recovered = 2
beta = 0.3 # infection rate
gamma = 0.05 # recovery rate

population= np.zeros((100 , 100))
outbreak= np.random.choice(a= range(100),size= 2)
population [outbreak[0],outbreak[1]]=1
for j in range(100):
    infectedIndex = np.where(population==1)
    # by self-learning, I found it would return a tuple stored 2 array, each of it would store x or y, like([1,0,1],[0,1,0]).
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i] #get the ith data in the 1st array, which represents x value
        y = infectedIndex[1][i] #get the ith data in the 2nd array, which represents y value
        # recovery:
        population[x,y]= np.random.choice([1,2],1,p=[1-gamma,gamma])[0]
        # infect all 8 neighbours:
        offsets = [(i,j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]
        neighbors = [(x+ dx, y+ dy) for dx, dy in offsets if 0<= x+ dx< 100 and 0<= y+ dy< 100]
        for neighbor in neighbors:
            if population[neighbor[0], neighbor[1]]== 0:
                population[neighbor[0],neighbor[1]]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    
plt.figure(figsize= (6,4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest') 
plt.show()
