f = open("06input.txt")

i = 0
answers = {}
temp = []
for line in f:
    if line == "\n":
        answers[i] = temp
        i += 1
        temp = list()
    else:
        temp.append(line.strip())
answers[i] = temp

sum_first = 0
sum_second = 0
for i in range(0, len(answers)):
    temp_first = set(answers[i][0])
    temp_second = set(answers[i][0])
    for a in answers[i]:
        if len(temp_first) != 0:
            temp_first = temp_first.union(set(a))    
            temp_second = temp_second.intersection(set(a))
    sum_first += len(temp_first)
    sum_second += len(temp_second)

print(sum_first, sum_second)