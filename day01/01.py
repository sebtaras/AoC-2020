f = open("01input.txt")

SUM_GOAL = 2020
entries = [int(l) for l in f.readlines()]

for i in range (0, len(entries)):
    for j in range (i, len(entries)):
        if entries[i] + entries[j] == SUM_GOAL:
            print(entries[i] * entries[j])

for i in range (0, len(entries)-2):
    for j in range (i+1, len(entries)-2):
        for k in range(j+1, len(entries)-2):
            if entries[i] + entries[j] + entries[k] == SUM_GOAL:
                print(entries[i] * entries[j] * entries[k])