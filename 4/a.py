import re
from pprint import pp


with open("inp", "r") as f:
    text = f.read().splitlines()

    wins = {}
    last_card_num = 0

    for raw_line in text:
        line = re.match(r"Card\s+(\d+):\s+([\s\d]+)+\s+\|([\s\d+]+)", raw_line)
        card_number = int(line.group(1))
        win_nums = list(map(int, re.findall(r"\d+", line.group(2))))
        card_nums = list(map(int, re.findall(r"\d+", line.group(3))))

        last_card_num = card_number

        enterance = 0
        for win_num in win_nums:
            if win_num in card_nums:
                enterance += 1

        if card_number not in wins:
            wins[card_number] = 1
        else:
            wins[card_number] += 1
        if enterance:
            for i in range(enterance):
                if card_number+i+1 not in wins:
                    wins[card_number+i+1] = 0
                wins[card_number+i+1] += wins[card_number]

        pp(wins)

    summ = 0
    for card_num, win_amount in wins.items():
        if card_num > last_card_num:
            continue

        summ += win_amount

    pp(wins)
    print(summ)
