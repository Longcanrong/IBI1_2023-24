import numpy as np
import matplotlib.pyplot as plt

time = {'sleeping' : 8 , 'classes' : 6 , 'studying' : 3.5 , 'TV' : 2 , 'music' : 1 } 
time['other']= 24 - sum(time.values())
print(time)
print(time['sleeping'])

plt.figure()
plt.pie(time.values(), labels= time.keys())
plt.show()
plt.clf()