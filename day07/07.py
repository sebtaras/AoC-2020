def how_many_contain(rules, color, visited):
    cnt = 0
    for r in rules:
        for l in rules[r]:
            if color in l and r not in visited:
                visited.append(r)
                cnt = cnt + 1 + how_many_contain(rules, r, visited)
    return cnt

def how_many_inside(rules, color):
    cnt = 0
    for l in rules[color]:
        num = l.split(" ")[0]
        if num != "no":
            new_color = l.split(" ")[1] + " " + l.split(" ")[2]
            cnt = cnt + int(num) + int(num) * how_many_inside(rules, new_color)
    return cnt

f = open("07input.txt")
COLOR = "shiny gold"

rules = {}
for line in f:
    temp = line.strip()[:-1].split("contain ")
    parent = temp[0].strip()[:-5]
    children = temp[1].split(", ")
    rules[parent] = children

first = how_many_contain(rules, COLOR, [])
second = how_many_inside(rules, COLOR)
print(first, second)

