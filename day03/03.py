import math

class Rule:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def traverse_map(trees, rule):
    position = 0
    num_trees = 0
    for i in range(0, len(trees), rule.y):
        num_trees = num_trees + 1 if trees[i][position] == '#' else num_trees
        position = (position + rule.x)%len(trees[0])
    return num_trees

f = open("03input.txt")
lines = list(map(lambda x: x.strip(), f.readlines()))

print(traverse_map(lines, Rule(3, 1)))      #1

rules = list()                              #2
rules.append(Rule(3, 1))        
rules.append(Rule(1, 1))
rules.append(Rule(5, 1))
rules.append(Rule(7, 1))
rules.append(Rule(1, 2))

results = list()
for rule in rules:
    results.append(traverse_map(lines, rule))

print(math.prod(results))