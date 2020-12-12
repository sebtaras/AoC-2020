from enum import Enum

class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    LEFT = "L"
    RIGHT = "R"
    FORWARD ="F"

class Position:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = Direction.EAST
        self.directions = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
        

    def update(self, dir, amt):
        if dir == Direction.NORTH or dir == 'N':
            self.y += amt
        elif dir == Direction.SOUTH or dir == 'S':
            self.y -= amt
        elif dir == Direction.EAST or dir == 'E':
            self.x += amt
        elif dir == Direction.WEST or dir == 'W':
            self.x -= amt
        elif dir == Direction.FORWARD or dir == 'F':
            self.update(self.dir, amt) 
        else: # R || L
            self.rotate(dir, amt)

    def rotate(self, dir, amt):
        curr_idx = self.directions.index(self.dir) + len(self.directions)
        turn_by = amt/90
        if dir == Direction.LEFT or dir == 'L':
            turn_by *=-1
        new_idx = int((curr_idx + turn_by) % len(self.directions))
        self.dir = self.directions[new_idx]
        
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    def __str__(self):
        return "X: " + str(self.x) + "\nY: " + str(self.y) + "\nFacing: " + str(self.dir) + "\n"


f = open("11input.txt")

pos = Position()

for line in f:
    print("NEW COMMAND: ", line.strip())
    dir = line[0]
    amt = int(line[1:])
    pos.update(dir, amt)
    print(str(pos))

print(pos.manhattan())