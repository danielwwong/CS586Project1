import json

with open('game6.json') as read_add:
    appe = json.load(read_add)

with open('game1.json', 'r') as read:
    pre = json.load(read)

for i in range(0, len(appe)):
    pre.append(appe[i])

with open('game1.json', 'w') as out:
    json.dump(pre, out)

with open('game1.json') as check:
    leng = json.load(check)

print(len(leng))
