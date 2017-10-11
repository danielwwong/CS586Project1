import pandas as pd

data = pd.read_csv('gamesTable.csv')
data.head()

count = 0
upper = 1
lower = 0
dataList = []
countList = []

for i in range(len(data['index'])):
    dataList.append(data['price'][i])

for i in range(0, 400):
    for j in range(len(dataList)):
        if (dataList[j] <= upper and dataList[j] > lower):
            count += 1

    countList.append(count)
    count = 0
    upper += 1
    lower += 1

with open('result.csv', 'wb') as output:
    for i in range(0, 400):
        output.write(str(countList[i]))
        output.write('\n')
