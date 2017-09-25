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
