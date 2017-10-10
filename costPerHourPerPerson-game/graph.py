import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('result.csv')
data.head()

x = data['costPerHourPerPerson']
y = data['number']

fig = plt.figure()
plt.xlim(100, 586900)
plt.ylim(0, 10500)
plt.plot(x, y)
fig.suptitle('Result', fontsize = 20)
plt.xlabel('Cost Per Hour Per Person')
plt.ylabel('Number')

plt.show()
fig.savefig('result.png')
