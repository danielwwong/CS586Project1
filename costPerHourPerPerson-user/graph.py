import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('result.csv')
data.head()

x = data['costPerHour']
y = data['percentage']

fig = plt.figure()
plt.xlim(0, 5100)
plt.ylim(0, 0.55)
plt.plot(x, y)
fig.suptitle('Result', fontsize = 20)
plt.xlabel('Cost Per Hour')
plt.ylabel('Percentage')

plt.show()
fig.savefig('result.png')
