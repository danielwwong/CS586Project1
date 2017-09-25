import requests
import json
import time

with open('gameID.json') as src:
    app_id = json.load(src)

with open('game.json', 'w') as init:
    json.dump([], init)
init.close()

count = len(app_id["applist"]["apps"]["app"])#48213

for i in range(1, 81):#242
    for j in range((200 * i) - 200, 200 * i):
        url_id = str(app_id["applist"]["apps"]["app"][j]["appid"])
        r = requests.get('http://store.steampowered.com/api/appdetails?appids=' + url_id + '&cc=us&filters=price_overview')
        output_data = r.json()
        with open('game.json', 'r') as read:
            appe = json.load(read)
        appe.append(output_data)
        with open('game.json', 'w') as out:
            json.dump(appe, out)
    time.sleep(305)

src.close()
read.close()
out.close()
