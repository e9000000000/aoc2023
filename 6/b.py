def count_wins(game: tuple[int]) -> int:
    given_time = game[0]
    given_distance = game[1]

    wins = 0
    for time in range(given_time+1):
        distance = (given_time - time) * time
        if distance > given_distance:
            wins += 1
    return wins


with open('inp', 'r') as f:
    lines = f.read().splitlines()

times = [int("".join(lines[0].split()[1:]))]
distances = [int("".join(lines[1].split()[1:]))]
games = zip(times, distances)

result = 1
for game in games:
    wins = count_wins(game)
    result *= wins

print(result)
