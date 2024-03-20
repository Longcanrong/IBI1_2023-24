import numpy as np
import matplotlib.pyplot as plt

time = {'sleeping' : 8 , 'classes' : 6 , 'studying' : 3.5 , 'TV' : 2 , 'music' : 1 } #input the data
time['other']= 24 - sum(time.values()) #get the time of 'others'
print(time) #output
print(time['sleeping'])

plt.figure()
plt.pie(time.values(), labels= time.keys()) #make a pie chart
plt.show()
plt.clf()