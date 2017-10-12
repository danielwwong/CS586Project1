import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('result0-10.csv')
data.head()

dataa = pd.read_csv('result10-25.csv')
dataa.head()

dataaa = pd.read_csv('result25+.csv')
dataaa.head()

x = data['costPerHour']
y = data['percentage']

xx = dataa['costPerHour']
yy = dataa['percentage']

xxx = dataaa['costPerHour']
yyy = dataaa['percentage']

plt.style.use('ggplot')
fig = plt.figure()
plt.xlim(15, 1500)
plt.ylim(0, 0.45)
plt.bar(x, y, color='#7780FF', label = '$0-$10', width = 1)
plt.bar(xx, yy, color='#FF9A02', label = '$10-$25', width = 1)
plt.bar(xxx, yyy, color='#6DBE6E', label = '$25+', width = 1)
fig.suptitle('Result', fontsize = 20)
plt.xlabel('Cost Per Hour Per Person')
plt.ylabel('Percentage')
plt.grid(True)
plt.legend()
plt.show()
fig.savefig('result.png')
