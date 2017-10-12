CS586Project1
===

The aim of this project is to gather all games' price on Steam.

---

- *game.py* is the main code
- *game.json* is the output of the games' price, currently, it has ***48,213*** records.
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

![img](https://github.com/danielwwong/CS586Project1/blob/master/costPerHourPerPerson-game/%3C1/result(interval%3D1%20top50).png)

In this chart, only the games price are between $0-$50 were included. The interval of the price is $1. **The games price that's in $0-$50 is 99.64% of all regret games.**

![img](https://github.com/danielwwong/CS586Project1/blob/master/costPerHourPerPerson-game/%3C1/resultTriple(interval%3D15%200-1500).png)

In this chart, the games are divided into three groups, which are $0-$10, $10-$25 and $25+. The chart shows their cost/hr/person distributions. The interval of the cost/hr/person is 15. The range of the cost/hr/person is 0-1500.

![img](https://github.com/danielwwong/CS586Project1/blob/master/costPerHourPerPerson-game/%3C1/resultTriple(interval%3D4%200-400).png)

In this chart, the interval of the cost/hr/person is 4. The range of the cost/hr/person is 0-400.

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

In this folder, game price distribution, account value distribution and number of games that users have distribution are drawn.

![img](https://github.com/danielwwong/CS586Project1/blob/master/descriptiveFigures/result(interval%3D1%20all).png)

All current game prices in Steam is included in this chart, free games are included. The price interval is $1. For example, there're 9,400 free games, it is 23.14% of all games. And there're 3,547 games that are within $0-$1. It is 8.73% of all games.

![img](https://github.com/danielwwong/CS586Project1/blob/master/descriptiveFigures/result(interval%3D2%20top80).png)

The games that have the price of $0-$80 is included. The price interval is $2. **The games that have the price within $0-$80 is 99.73% of all games.**

![img](https://github.com/danielwwong/CS586Project1/blob/master/descriptiveFigures/resultValue(interval%3D100%20all).png)

We used 25,260 sample users' information to generate the user value distribution and the number of games that users purchased distribution.

All sample users' account values are included in this chart. The account value interval is $100. For example, there're 11,577 users' account value is 0, it is 45.83% of all sample users.

![img](https://github.com/danielwwong/CS586Project1/blob/master/descriptiveFigures/resultValue(interval%3D15%20top3000).png)

The users account value that is within $0-$3,000 are included. The account value interval is $15. **The users account value that is in $0-$3,000 is 99.45% of all sample users.**

![img](https://github.com/danielwwong/CS586Project1/blob/master/descriptiveFigures/resultNumberOfGames(interval%3D25%20all).png)

All sample users' number of games are included in this chart. The number of games interval is 25. For example, there're 11,577 users do not have any games. It is 45.61% of all sample users.

![img](https://github.com/danielwwong/CS586Project1/blob/master/descriptiveFigures/resultNumberOfGames(interval%3D1%20top125).png)

The users' number of games that is within 0-125 are included. The number of games interval is 1. **The users' number of games that is in the range of 0-125 is 98.81% of all sample users.**
