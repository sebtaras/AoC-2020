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

# def num_of_arrangements(output_joltages):
#     valid_arrangements = [output_joltages]
#     new_arrangements = valid_arrangements[:]
#     while len(new_arrangements) > 0:
#         temp = []
#         for arrangement in new_arrangements:
#             for i in range(2, len(arrangement)):
#                 if arrangement[i] - arrangement[i-2] <= 3:
#                     new_arrangement = arrangement[:]
#                     new_arrangement.pop(i-1)    
#                     temp.append(new_arrangement)
#         for t in temp:
#             if t not in valid_arrangements:
#                 valid_arrangements.append(t)
#         new_arrangements = temp[:]
#     return len(valid_arrangements)

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
            t = 1 + len(p)-2
        elif len(p) == 4:
            t = 1 + len(p)-2 + len(p)-3
        elif len(p) == 5:
            t = 1 + len(p)-2 + len(p)-2
        res = res*t
        #print(p, t)
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