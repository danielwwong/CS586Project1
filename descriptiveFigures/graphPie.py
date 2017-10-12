import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('resultForPie.csv')
data.head()

sizes = data['number']
labels = data['avgPlayTime']
colors = ['#7780FF', '#FF9A02', '#6DBE6E', '#FEB3AF', '#DFCBE2']
explode = (0.3, 0.05, 0.05, 0.05, 0.05)

plt.style.use('ggplot')
fig = plt.figure()
plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%3.2f%%', shadow = True, startangle = 90, pctdistance = 0.6)
plt.axis('equal')
fig.suptitle('Average Play Time', fontsize = 20)
plt.legend()
plt.show()
fig.savefig('result.png')
