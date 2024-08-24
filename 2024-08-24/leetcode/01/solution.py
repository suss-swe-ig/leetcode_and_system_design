def part1():
    points = {}
    points["rock"] = 1
    points["paper"] = 2
    points["scissors"] = 3
    points["win"] = 6
    points["draw"] = 3
    points["lose"] = 0
    beat = {}
    beat["rock"] = "paper"
    beat["paper"] = "scissors"
    beat["scissors"] = "rock"
    rps = {}
    rps["A"] = "rock"
    rps["B"] = "paper"
    rps["C"] = "scissors"
    rps["X"] = "rock"
    rps["Y"] = "paper"
    rps["Z"] = "scissors"
    score = 0
    with open("input.txt") as f:
        for line in f:
            other, me = line.strip().split(" ")
            other, me = rps[other], rps[me]
            if other == beat[me]:
                score += points["lose"] + points[me]
            elif me == beat[other]:
                score += points["win"] + points[me]
            else:
                score += points["draw"] + points[me]
    print(score)

def part2():
    rps = {}
    rps["A"] = "rock"
    rps["B"] = "paper"
    rps["C"] = "scissors"
    beat = {}
    beat["scissors"] = "rock"
    beat["paper"] = "scissors"
    beat["rock"] = "paper"
    lose = {}
    lose["rock"] = "scissors"
    lose["scissors"] = "paper"
    lose["paper"] = "rock"
    draw = {}
    draw["rock"] = "rock"
    draw["paper"] = "paper"
    draw["scissors"] = "scissors"
    intentions = {}
    intentions["X"] = "lose"
    intentions["Y"] = "draw"
    intentions["Z"] = "win"
    intentions["win"] = beat
    intentions["lose"] = lose
    intentions["draw"] = draw
    points = {}
    points["rock"] = 1
    points["paper"] = 2
    points["scissors"] = 3
    points["win"] = 6
    points["draw"] = 3
    points["lose"] = 0
    score = 0
    with open("input.txt") as f:
        for line in f:
            other, me = line.strip().split(" ")
            other, intent = rps[other], intentions[me]
            score += points[intentions[intent][other]] + points[intent]
    print(score)

part1()
part2()

