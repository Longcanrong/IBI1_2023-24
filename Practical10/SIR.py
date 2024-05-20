import numpy as np 
import matplotlib.pyplot as plt 

N = 10000  # Total population
S = 9999   # Susceptible
I = 1      # Infected
R = 0      # Recovered

beta = 0.3 # infection rate
gamma = 0.05 # recovery rate

susceptible = [S]
infected = [I]
recovered = [R]

for t in range(1000):
    contact_rate = beta * I / N

    infection_choices = np.random.choice([1, 0], size=S, p=[contact_rate, 1-contact_rate])
    new_infections = infection_choices.sum()

    recovery_choices = np.random.choice([1, 0], size=I, p=[gamma, 1-gamma])
    new_recoveries = recovery_choices.sum()

    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries
    
    susceptible.append(S)
    infected.append(I)
    recovered.append(R)
    print(S,I,R)

# Plot
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(susceptible, label='Susceptible')
plt.plot(infected, label='Infected')
plt.plot(recovered, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR Model')
plt.legend()
plt.show()

# Save the plot
plt.savefig("SIR Model", type="png")