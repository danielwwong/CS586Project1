import pandas as pd

data = pd.read_csv('Players10000Table1.csv')
data.head()

count = 0
upper = 10
lower = 0
dataList = []
countList = []

for i in range(len(data['playerId'])):
    dataList.append(data['AvgCostPerHour'][i])

for i in range(0, 510):
    for j in range(len(dataList)):
        if (dataList[j] < upper and dataList[j] > lower):
            count += 1

    countList.append(count)
    count = 0
    upper += 10
    lower += 10

with open('result.csv', 'wb') as output:
    for i in range(0, 510):
        output.write(str(countList[i]))
        output.write('\n')
