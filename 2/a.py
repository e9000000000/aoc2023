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
        possible = True
        for show in game["shows"]:
            if show["color"] == "blue" and show["num"] > 14:
                possible = False
            if show["color"] == "red" and show["num"] > 12:
                possible = False
            if show["color"] == "green" and show["num"] > 13:
                possible = False
        if possible:
            result += game["id"]


    print(result)
