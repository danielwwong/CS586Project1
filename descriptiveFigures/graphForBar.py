import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('result.csv')
data.head()

x = data['price']
y = data['percentage']

fig = plt.figure()
plt.xlim(0, 80)
plt.ylim(0, 0.24)
plt.bar(x, y, width = 0.8)
fig.suptitle('Result', fontsize = 20)
plt.xlabel('Price')
plt.ylabel('Percentage')

plt.show()
fig.savefig('result.png')
