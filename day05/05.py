import math, sys

def calc_boarding_pass(row, column):
    return row * 8 + column

def parse_row(lower, upper, string):
    while(upper!=lower):
        char = string[0]    
        if char =="F":
            upper = upper - int(math.pow(2, len(string)-4))
        elif char == "B":
            lower = lower + int(math.pow(2, len(string)-4))
        string = string[1:]
    return lower, parse_column(0, 7, string)

def parse_column(lower, upper, string):
    while(lower != upper):
        char = string[0]
        if char == "L":
            upper = upper - int(math.pow(2, len(string)-1))
        elif char == "R":
            lower = lower + int(math.pow(2, len(string)-1))
        string = string[1:]
    return lower

f = open("05input.txt")

ids = []
highest_id = 0
lowest_id = sys.maxsize

for line in f:
    row, column = parse_row(0, 127, line.rstrip())
    id = calc_boarding_pass(row, column)
    ids.append(id)

    if id > highest_id:
        highest_id = id
    elif id < lowest_id:
        lowest_id = id

print("Highest id:", highest_id)
for i in range(lowest_id, highest_id):
    if i not in ids:
        print("My id:", i)
        break