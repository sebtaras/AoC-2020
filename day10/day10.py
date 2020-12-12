import math

def num_of_diffs(output_joltages):
    prev = 0
    diff_1 = 0
    diff_3 = 0
    for i in range(0, len(output_joltages)):
        curr = output_joltages[i]
        if curr - prev == 1:
            diff_1 += 1
        elif curr - prev == 3:
            diff_3 += 1
        prev = curr
    return diff_1, diff_3

def num_of_arrangements(output_joltages):
    parts = []
    cutoff = 0
    for i in range(0, len(output_joltages)):
        if output_joltages[i] - output_joltages[i-1] == 3:
            parts.append(output_joltages[cutoff:i])
            cutoff = i
    res = 1
    for p in parts:
        t=1
        if len(p) == 3:
            t = 2
        elif len(p) == 4:
            t = 4
        elif len(p) == 5:
            t = 7
        res = res*t
        print(p, t)
    return res

f = open("day10input.txt")

output_joltages = [0]
for line in f:
    output_joltages.append(int(line.strip()))

output_joltages = sorted(output_joltages)
output_joltages.append(output_joltages[len(output_joltages)-1]+3)
diff_1, diff_3 = num_of_diffs(output_joltages)
num = num_of_arrangements(output_joltages)
print(diff_1 * diff_3, num)