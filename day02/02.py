def is_password_valid(char, index, password):
    return True if password[index-1] == char else False

f = open("02input.txt")

passwords = list(map(lambda x: x.strip().split(": "), f.readlines()))
num_valid_policy1 = 0
num_valid_policy2 = 0
for p in passwords:     #p[0] = rules, p[1] = password
    lower = int(p[0].split("-")[0])
    upper = int(p[0].split("-")[1].split(" ")[0])
    char = p[0].split(" ")[1]
    
    if p[1].count(char) >= lower and p[1].count(char) <= upper:
        num_valid_policy1 += 1
    
    if is_password_valid(char, lower, p[1]) == True and is_password_valid(char, upper, p[1]) == False:
        num_valid_policy2 += 1
    elif is_password_valid(char, lower, p[1]) == False and is_password_valid(char, upper, p[1]) == True:
        num_valid_policy2 += 1

print(num_valid_policy1, num_valid_policy2)S