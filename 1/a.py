with open("input.txt", "r") as f:
    # text = f.read()
    text = f.read().splitlines()
    # text = list(map(lambda l: list(map(int, l.split())), f.read().splitlines()))
    sm = 0
    for line in text:
        first = None
        last = None
        for l in line:
            if l in "1234567890":
                first = l
                break
        for l in line[::-1]:
            if l in "1234567890":
                last = l
                break
        sm += int(first + last)
    print(sm)

