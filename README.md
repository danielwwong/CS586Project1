CS586Project1
===

The aim of this project is to gather all games' price on Steam.

---

- *game.py* is the main code
- *game.json* is the output of the games' price, currently, it has ***13,671*** records. There're ***48,213*** games on Steam.
- *gameID.json* is from http://api.steampowered.com/ISteamApps/GetAppList/v0001/
It contains all games' IDs

---

Currently, the project is built by obtaining 200 games per time, then pause for 305 seconds. And then obtaining the second 200 games and so on.

Due to the problem that Steam API will not response after several hundreds of HTTP get command, the retrieve should be paused for several minutes every time.

---

Check this for Steam API's limitation:
https://steamdb.info/blog/store-prices-api/

---
Charts
===

*Please click on the chart to download the original picture. All blue words are links. Please click on the blue words to go to the corresponding file/folder.*

**[costPerHourPerPerson-game Folder](https://github.com/danielwwong/CS586Project1/tree/master/costPerHourPerPerson-game)**

In this folder, the games information was divided into 2 parts, based on the average play time/person. It was divided by < 1 and >= 1.

**[<1(regret games)](https://github.com/danielwwong/CS586Project1/tree/master/costPerHourPerPerson-game/%3C1)**

This folder has the regret games price distributions.

![img](https://github.com/danielwwong/CS586Project1/raw/master/costPerHourPerPerson-game/%3C1/result(interval%3D1%20all).png)

In this chart, all regret games were included. The interval of the price is $1. For example, for the price range of $0-$1, there're 566 regret games within this range. And it is 12.76% of all regret games.

![img](https://github.com/danielwwong/CS586Project1/blob/master/costPerHourPerPerson-game/%3C1/result(interval%3D0.2%20top20).png)

In this chart, only the games price are between $0-$20 were included. The interval of the price is $0.2. **The games price that's in $0-$20 is 97.57% of all regret games.**

*If you want to calculate the mean value or the standard deviation value, etc., you could click [this csv file](https://github.com/danielwwong/CS586Project1/blob/master/costPerHourPerPerson-game/%3C1/result(interval%3D1%20all).csv) for all regret games prices.*

---

**[>=1](https://github.com/danielwwong/CS586Project1/tree/master/costPerHourPerPerson-game/%3E%3D1)**

This folder contains the games that have the average play time/person >= 1.

The cost/hr/person for those games were drew here.

![img](https://github.com/danielwwong/CS586Project1/blob/master/costPerHourPerPerson-game/%3E%3D1/result(interval%3D1%20all).png)

In this chart, all games that have the average play time/person >= 1 were included. The interval of cost/hr/person is 1. For example, for the cost/hr/person range of 0-1, there're 2,180 games within this range. And it is 27.44% of all games.

![img](https://github.com/danielwwong/CS586Project1/blob/master/costPerHourPerPerson-game/%3E%3D1/result(interval%3D0.15%20top15).png)

In this chart, only the games that has the cost/hr/person between 0-15 were included. The interval of the cost/hr/person is 0.15. **The games that has the cost/hr/person within 0-15 is 98.67% of all games.**

![img](https://github.com/danielwwong/CS586Project1/blob/master/costPerHourPerPerson-game/%3E%3D1/result(interval%3D0.015%20top1.5).png)

In this chart, only the games that has the cost/hr/person between 0-1.5 were included. The interval of the cost/hr/person is 0.015.

---

**[costPerHourPerPerson-user Folder](https://github.com/danielwwong/CS586Project1/tree/master/costPerHourPerPerson-user)**

In this folder, cost/hr/user was drew.

The data is based on ***11,366*** sample users' data.

![img](https://github.com/danielwwong/CS586Project1/blob/master/costPerHourPerPerson-user/result(interval%3D10%20all).png)

This chart included all sample users' data. The interval of cost/hr is 10. For example, for the cost/hr range of 0, there're 4,454 users within this range. And it is 39.57% of all sample users. For the range of 0-10, which 0 is not included, there're 5,954 users within this range. It is 52.92% of all users.

![img](https://github.com/danielwwong/CS586Project1/blob/master/costPerHourPerPerson-user/result(interval%3D1%20top100).png)

This chart included the sample users that have cost/hr within 0-100. The interval of cost/hr is 1. **The users that has cost/hr within 0-100 is 98.19% of all sample users.**

![img](https://github.com/danielwwong/CS586Project1/blob/master/costPerHourPerPerson-user/result(interval%3D0.05%20top5).png)

This chart included the sample users that have cost/hr within 0-5. The interval of cost/hr is 0.05. **The users that has cost/hr within 0-5 is 89.18% of all sample users.**

---

**[descriptiveFigures Folder](https://github.com/danielwwong/CS586Project1/tree/master/descriptiveFigures)**

In this folder, game price distribution was drew.

![img](https://github.com/danielwwong/CS586Project1/blob/master/descriptiveFigures/result(interval%3D1%20all).png)

All current game prices in Steam is included in this chart, free games are included. The price interval is $1. For example, there're 9,400 free games, it is 23.14% of all games. And there're 3,547 games that are within $0-$1. It is 8.73% of all games.

![img](https://github.com/danielwwong/CS586Project1/blob/master/descriptiveFigures/result(interval%3D0.5%20top20).png)

The games that have the price of $0-$20 is included. The price interval is $0.5. **The games that have the price within $0-$20 is 95.62% of all games.**

---
Notes
===

- May add histograms later.
- May make it look better later.
- The chart of number of games purchased per user is not generated be.
- The chart of account value (total money spent on purchasing games per user) is not generated.
- The subgroups of regret games cannot be generated because I cannot divide the games based on its' types as I don't have the data of the game types.
