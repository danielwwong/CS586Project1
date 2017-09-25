import requests
import json

with open('gameID.json') as src:
    app_id = json.load(src)

with open('game.json', 'w') as init:
    json.dump([], init)
init.close()

count = len(app_id["applist"]["apps"]["app"])
for i in range(0, count):
    url_id = str(app_id["applist"]["apps"]["app"][i]["appid"])
    r = requests.get('http://store.steampowered.com/api/appdetails?appids=' + url_id + '&cc=us&filters=price_overview')
    output_data = r.json()
    with open('game.json', 'r') as read:
        appe = json.load(read)
    appe.append(output_data)
    with open('game.json', 'w') as out:
        json.dump(appe, out)

src.close()
read.close()
out.close()
