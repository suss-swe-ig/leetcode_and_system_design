"""
Solution by Donaldson Tan (@geodome)

If you are unsure of this solution, reach out to me via Telegram. I will explain to you.
"""

from typing import List, Tuple, Set, Dict

class BadRope(Exception):
    def __init__(self):
        Exception.__init__(self, "bad rope")

class Coords:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._history: Set[Tuple[int,int]] = set()
        self._history.add((self._x, self._y))
    
    @property
    def coords(self) -> Tuple[int, int]:
        return self._x, self._y

    def move(self, unit: "Coords") -> None:
        dx, dy = unit.coords
        self._x += dx 
        self._y += dy 
        self._history.add((self._x, self._y))
        
    
    @property
    def history(self) ->Set[Tuple[int, int]]:
        return self._history
    
    def adjacent(self, other: "Coords") -> bool:
        if self.coords == other.coords:
            return True
        x, y = other.coords
        if x == self._x:
            return abs(y - self._y) == 1
        if y == self._y:
            return abs(x - self._x) == 1
        if abs(x - self._x) == 1 and abs(y - self._y) == 1:
            return True
        return False

def readFile(filename: str) -> List[Tuple[str, int]]:
    moves: List[Tuple[str, int]] = []
    with open(filename) as f:
        for line in f:
            dir, steps = line.strip().split()
            moves.append((dir, int(steps)))
    return moves


def simulate(moves: List[Tuple[str, int]], rope: List["Coords"]) -> Set[Tuple[int, int]]:
    steps: Dict[str, "Coords"] = {
        "U":  Coords( 0,  1), 
        "D":  Coords( 0, -1), 
        "L":  Coords(-1,  0), 
        "R":  Coords( 1,  0),
        "UL": Coords(-1,  1),
        "UR": Coords( 1,  1),
        "DL": Coords(-1, -1),
        "DR": Coords( 1, -1),
    }
    if len(rope) > 1:
        # a rope consists of at least 2 parts - a head and a tail.
        head = rope[0]
        for dir, count in moves:
            while count > 0:
                head.move(steps[dir])
                prev = head
                for tail in rope[1:]:
                    # every time the head moves, update the position of each tail
                    if not prev.adjacent(tail):
                        # if the tail is adjacent, tail position remains unchanged.
                        x0, y0 = prev.coords
                        x1, y1 = tail.coords
                        if x0 == x1:
                            # same col
                            if y0 > y1:
                                # head is above tail
                                tail.move(steps["U"])
                            else:
                                # head is below tail
                                tail.move(steps["D"])   
                        elif y0 == y1:
                            # same row
                            if x0 > x1:
                                # head is on the right side of the tail
                                tail.move(steps["R"])
                            else:
                                # head is on the left side of thej tail
                                tail.move(steps["L"])
                        else:
                            if x0 > x1:
                                # head is on the right side of the tail
                                if y0 > y1:
                                    # head is above the tail
                                    tail.move(steps["UR"])
                                else:
                                    # head is below the tail
                                    tail.move(steps["DR"])
                            else:
                                # head is on the left side of the tail
                                if y0 > y1:
                                    # head is above the tail
                                    tail.move(steps["UL"])
                                else:
                                    # head is below the tail
                                    tail.move(steps["DL"])
                    prev = tail
                count -= 1
        return rope[-1].history
    raise BadRope()

def ropeWithNParts(n: int) -> List["Coords"]:
    if n < 1:
        raise BadRope()
    return [Coords(0,0) for _ in range(n+1)]


def main():
    moves = readFile("input.txt")
    history1 = simulate(moves, ropeWithNParts(1))
    print("no. of historical coordinates of tail for 1-part rope:", len(history1))
    history2 = simulate(moves, ropeWithNParts(9))
    print("no. of historical coordinates of tail for 9-part rope:", len(history2))


if __name__ == "__main__":
    main()