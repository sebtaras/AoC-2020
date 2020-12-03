import math
class Rule:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def is_tree(c):
    return c == '#'

def traverse_map(trees, rule):
    position = 0
    num_trees = 0
    grid = extend(trees, rule)
    for i in range(0, len(grid)):
        if position < len(grid[i]) and i%rule.y == 0:
            num_trees = num_trees + 1 if is_tree(grid[i][position]) else num_trees
            position += rule.x
    return num_trees

def extend(trees, rule):
    res = list()
    for t in trees:
        res.append(t*math.ceil(((len(trees)*rule.x)/(len(trees[0]))*rule.y)))
    return res

def product(list):
    res = 1
    for l in list:
        res *= l
    return res

f = open("03input.txt")
lines = list(map(lambda x: x.strip(), f.readlines()))

# 1.
print(traverse_map(lines, Rule(3, 1)))

# 2.
rules = list()
rules.append(Rule(3, 1))
rules.append(Rule(1, 1))
rules.append(Rule(5, 1))
rules.append(Rule(7, 1))
rules.append(Rule(1, 2))

results = list()
for rule in rules:
    results.append(traverse_map(lines, rule))

#153 66 79 92 33
print(product(results))