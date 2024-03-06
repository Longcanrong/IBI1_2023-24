a=0.05 #density
max=0.9 #density max value
i=1 #days
while a<max: #judge if the density reaches 90%
    i+=1 #record days
    a*=2 #change density
print(i) #cout days
