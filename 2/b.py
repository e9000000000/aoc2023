import sys
import re
from pprint import pp




with open(sys.argv[1], 'r') as f:
    # text = list(map(lambda l: list(map(int, l.split())), f.read().splitlines()))
    text = f.read().splitlines()
    games = []
    for line in text:
        game_num = re.match(r"Game (\d+)", line).group(1)
        shows_raw = re.findall(r"\d+ \w+", line)
        shows = list(map(lambda x: {"num": int(x.split()[0]), "color": x.split()[1]}, shows_raw))

        games.append({
            "id": int(game_num),
            "shows": shows
        })

    result = 0
    for game in games:
        maxnums = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }

        for show in game["shows"]:
            if maxnums[show["color"]] < show["num"]:
                maxnums[show["color"]] = show["num"]

        result += maxnums["red"] * maxnums["blue"] * maxnums["green"]


    print(result)
