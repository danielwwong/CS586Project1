import json

with open('gameID.json') as src:
    id = json.load(src)

with open('game.json') as read:
    data = json.load(read)

count = 0
upper = 10
lower = 0
idList = []
dataList = []
priceList = []
countList = []

for i in range(len(id['applist']['apps']['app'])):
    idList.append(id['applist']['apps']['app'][i]['appid'])

for i in range(len(idList)):
    dataList.append(data[i][str(idList[i])])

for i in range(len(dataList)):
    if dataList[i]['success'] is True:
        if len(dataList[i]['data']) is 0:
            priceList.append(0)
        else:
            priceList.append(dataList[i]['data']['price_overview']['final'])
