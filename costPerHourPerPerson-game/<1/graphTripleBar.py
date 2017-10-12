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

total_width, n = 5, 3
width = total_width / n

plt.style.use('ggplot')
fig = plt.figure()
plt.xlim(4, 400)
plt.ylim(0, 0.16)
plt.bar(x-width, y, color='#7780FF', label = '$0-$10', width = width)
plt.bar(xx, yy, color='#FF9A02', label = '$10-$25', width = width)
plt.bar(xxx+width, yyy, color='#6DBE6E', label = '$25+', width = width)
fig.suptitle('Result', fontsize = 20)
plt.xlabel('Cost Per Hour Per Person')
plt.ylabel('Percentage')
plt.grid(True)
plt.legend()
plt.show()
fig.savefig('result.png')
