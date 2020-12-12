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
        self.wp_x = 10
        self.wp_y = 1
        

    def update(self, dir, amt):
        if dir == Direction.NORTH or dir == 'N':
            self.wp_y += amt
        elif dir == Direction.SOUTH or dir == 'S':
            self.wp_y -= amt
        elif dir == Direction.EAST or dir == 'E':
            self.wp_x += amt
        elif dir == Direction.WEST or dir == 'W':
            self.wp_x -= amt
        elif dir == Direction.FORWARD or dir == 'F':
            self.update_position(amt)
        elif dir == "L":
            turn_by = amt/90
            while turn_by > 0:
                self.rotate()
                turn_by -=1
        else:
            amt = 360 - amt
            turn_by = amt/90
            while turn_by > 0:
                self.rotate()
                turn_by -=1

    def update_position(self, amt):
        self.x = self.x + amt*self.wp_x
        self.y = self.y + amt*self.wp_y

    def rotate(self):
        (old_x, old_y) = (self.wp_x, self.wp_y)
        (self.wp_x, self.wp_y) = (-1*old_y, old_x)
        
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    def __str__(self):
        return "X: " + str(self.x) + "\tX_wp: " + str(self.wp_x) + "\nY: " + str(self.y) +"\tY_wp: " + str(self.wp_y) + "\nFacing: " + str(self.dir) + "\n"


f = open("12input.txt")

pos = Position()

for line in f:
    dir = line[0]
    amt = int(line[1:])
    pos.update(dir, amt)

print(pos.manhattan())