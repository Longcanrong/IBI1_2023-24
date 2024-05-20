import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("F:\Desktop\IBI\Practical7")
os.getcwd()
os.listdir()
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# show the fourth column (the DALYs) from every 10th row:
print(dalys_data.iloc[0:101:10, 3])

print('\n')

# used a Boolean to show DALYs for all rows corresponding to Afghanistan:
my_row = []
for entity in dalys_data.loc[:,'Entity']:
    if entity == 'Afghanistan':
        my_row.append(True)
    else:
        my_row.append(False)
print(dalys_data.loc[my_row, 'DALYs'])

# China:
tem_dic = {'Entity':[],'Year':[],'DALYs':[]}
for entity,year,daly in zip(dalys_data['Entity'], dalys_data['Year'], dalys_data['DALYs']):
    if entity == 'China':
        tem_dic['Entity'].append('China')
        tem_dic['Year'].append(year)
        tem_dic['DALYs'].append(daly)
china_data = pd.DataFrame(tem_dic)
mean_dalys = np.mean(china_data['DALYs'])
print(f"Mean dalys of China is {mean_dalys}")

dalys_2019 = china_data[china_data['Year'] == 2019]['DALYs'].values[0]
if dalys_2019 > mean_dalys:
    print("2019 was above the mean.")
else:
    print("2019 was below the mean.")

plt.plot(china_data['Year'], china_data['DALYs'], 'r')
plt.xlabel('Years')
plt.ylabel('DALYs of China')
plt.title('DALYs in China Over Time')
plt.xticks(china_data.Year,rotation=-45)
plt.show()

# Question: How has the relationship between the DALYs in China and the UK changed over time? Are they becoming more similar, less similar
tem_dic = {'Entity':[],'Year':[],'DALYs':[]}
for entity,year,daly in zip(dalys_data['Entity'], dalys_data['Year'], dalys_data['DALYs']):
    if entity == 'United Kingdom':
        tem_dic['Entity'].append('United Kingdom')
        tem_dic['Year'].append(year)
        tem_dic['DALYs'].append(daly)
UK_data = pd.DataFrame(tem_dic)

difference_data = {'Year':[], 'difference_of_DALYs':[]}
for year,china_DALY, UK_DALY in zip(UK_data['Year'],china_data['DALYs'], UK_data['DALYs']):
    difference_data['Year'].append(year)
    difference_data['difference_of_DALYs'].append(china_DALY - UK_DALY)

plt.plot(difference_data['Year'], difference_data['difference_of_DALYs'], 'r')
plt.xlabel('Years')
plt.ylabel('The difference in DALYs of China and UK')
plt.title('The difference in DALYs of China and UK Over Time')
plt.xticks(china_data.Year,rotation=-45)
plt.show()
# Because the slope is negative, it means that the DALYs in the china and UK are becoming similar
print("Because the slope is negative, it means that the DALYs in the china and UK are becoming similar")
