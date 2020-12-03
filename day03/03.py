class Rule:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def is_tree(c):
    return c == '#'

def extend(line, length):
    res = line
    while(len(res) < length):
        res += res
    return res

def traverse_map(grid, rule):
    position = 0
    num_trees = 0
    for i in range(0, len(grid)):
        if position < len(grid[i]) and i%rule.y == 0:
            num_trees = num_trees + 1 if is_tree(map_trees[i][position]) else num_trees
            position += rule.x
    return num_trees

def product(list):
    res = 1
    for l in list:
        res *= l
    return res

f = open("03input.txt")
lines = list(map(lambda x: x.strip(), f.readlines()))

map_trees = list()
for line in lines:
    map_trees.append(line*100)

# 1.
print(traverse_map(map_trees, Rule(3, 1)))

# 2.
rules = list()
rules.append(Rule(3, 1))
rules.append(Rule(1, 1))
rules.append(Rule(5, 1))
rules.append(Rule(7, 1))
rules.append(Rule(1, 2))

results = list()
for rule in rules:
    results.append(traverse_map(map_trees, rule))

#153 66 79 92 33
print(product(results))