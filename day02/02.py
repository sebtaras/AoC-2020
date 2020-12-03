def is_password_valid(char, index, password):
    return password[index-1] == char

f = open("02input.txt")

passwords = list(map(lambda x: x.strip().split(": "), f.readlines()))
num_valid_policy1 = 0
num_valid_policy2 = 0
for p in passwords:     #p[0] = rules, p[1] = password
    lower = int(p[0].split("-")[0])
    upper = int(p[0].split("-")[1].split(" ")[0])
    char = p[0].split(" ")[1]

    if lower <= p[1].count(char) <= upper:
        num_valid_policy1 += 1
    
    if is_password_valid(char, lower, p[1]) ^ is_password_valid(char, upper, p[1]):
        num_valid_policy2 += 1

print(num_valid_policy1, num_valid_policy2)