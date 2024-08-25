"""
Solution by Donaldson Tan (@geodome)

If you are unsure of this solution, reach out to me via Telegram. I will explain to you.
"""

def part1():
    """
    The idea here is you can perform branching by using hash map keys to replace the if-constructs.
    """
    points = {}
    points["rock"] = 1
    points["paper"] = 2
    points["scissors"] = 3
    points["win"] = 6
    points["draw"] = 3
    points["lose"] = 0
    rps = {}
    rps["A"] = "rock"
    rps["B"] = "paper"
    rps["C"] = "scissors"
    rps["X"] = "rock"
    rps["Y"] = "paper"
    rps["Z"] = "scissors"
    outcome = {}
    outcome["rock"] = {}
    outcome["rock"]["rock"] = "draw"
    outcome["rock"]["paper"] = "lose"
    outcome["rock"]["scissors"] = "win"
    outcome["paper"] = {}
    outcome["paper"]["rock"] = "win"
    outcome["paper"]["paper"] = "draw"
    outcome["paper"]["scissors"] = "lose"
    outcome["scissors"] = {}
    outcome["scissors"]["rock"] = "lose"
    outcome["scissors"]["paper"] = "win"
    outcome["scissors"]["scissors"] = "draw"
    score = 0
    with open("input.txt") as f:
        for line in f:
            # read A,B,C,X,Y,Z from input.txt
            other, me = line.strip().split(" ")
            # convert A,B,C,X,Y,Z to rock,paper,scissors,rock,paper,scissors respectively
            other, me = rps[other], rps[me]
            # compute the score
            score += points[outcome[me][other]] + points[me]
    print(score)

def part2():
    """
    The same solution technique is employed - using hash maps to perform branch without involving the if-construct.
    """
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
            # read A,B,C,X,Y,Z from input.txt
            other, me = line.strip().split(" ")
            # convert A,B,C,X,Y,Z to rock,paper,scissors,lose,draw,win respectively
            other, intent = rps[other], intentions[me]
            score += points[intentions[intent][other]] + points[intent]
    print(score)

part1()
part2()


