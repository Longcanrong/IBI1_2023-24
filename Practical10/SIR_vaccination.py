import numpy as np 
import matplotlib.pyplot as plt

def caculate_infected(vac):
    N = 10000  # Total population
    S = int(9999 * (1-vac))  # Susceptible
    I = 1               # Infected
    R = 0               # Recovered

    beta = 0.3 # infection rate
    gamma = 0.05 # recovery rate

    infected = [I]

    for t in range(1000):
        contact_rate = beta * I / N

        infection_choices = np.random.choice([1, 0], size=S, p=[contact_rate, 1-contact_rate])
        new_infections = infection_choices.sum()

        recovery_choices = np.random.choice([1, 0], size=I, p=[gamma, 1-gamma])
        new_recoveries = recovery_choices.sum()

        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries
        
        infected.append(I)
    return infected

vaccination_rates = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.figure(figsize=(6, 4), dpi=150)
for vac in vaccination_rates:
    infected_list= caculate_infected(vac)
    plt.plot(infected_list, label=f'{vac*100} %')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR Model with different vaccination rates')
plt.legend()
plt.show()

plt.savefig("SIR Model", type="png")