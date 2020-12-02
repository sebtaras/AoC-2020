def num_occurences(char, password):
    occ = 0
    for c in password:
        if c == char:
            occ += 1
    return occ

def check_index(char, index, password):
    return True if password[index-1] == char else False

f = open("02input.txt")

passwords = list(map(lambda x: x.strip().split(": "), f.readlines()))
num_valid_policy1 = 0
num_valid_policy2 = 0
for p in passwords:
    lower = int(p[0].split("-")[0])
    upper = int(p[0].split("-")[1].split(" ")[0])
    char = p[0].split(" ")[1]
    
    if num_occurences(char, p[1]) >= lower and num_occurences(char, p[1]) <= upper:
        num_valid_policy1 += 1
    
    if check_index(char, lower, p[1]) == True and check_index(char, upper, p[1]) == False:
        num_valid_policy2 += 1
    elif check_index(char, lower, p[1]) == False and check_index(char, upper, p[1]) == True:
        num_valid_policy2 += 1

print(num_valid_policy1, num_valid_policy2)