import sys

def check_number(number, list):
    for i in range(0, len(list)-1):
        for j in range(i, len(list)):
            if number == list[i] + list[j]:
                return True
    return False

def find_contiguous(number, list, span):
    for start in range(0, len(list)-span):
        if(sum(list[start:span+start]) == number):
            add_smallest_largest(list[start:span+start])
            return True
    return False

def add_smallest_largest(list):
    min = sys.maxsize
    max = 0
    for n in list:
        if n < min:
            min = n
        if n > max:
            max = n
    print(min+max)

f = open("09input.txt")

OFFSET = 25
numbers = []
for line in f:
    if len(numbers) < OFFSET:
        numbers.append(int(line))
    elif check_number(int(line), numbers[-1*OFFSET:]):
        numbers.append(int(line))
    else:
        first = int(line)
        break

print(first)

for i in range(2, len(numbers)):
    if find_contiguous(first, numbers, i):
        break

        

