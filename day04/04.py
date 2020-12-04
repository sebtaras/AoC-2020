def is_valid_passport(passport):
    return check_byr(passport.get("byr")) and check_iyr(passport.get("iyr")) and check_eyr(passport.get("eyr")) and check_hgt(passport.get("hgt")) and check_hcl(passport.get("hcl")) and check_ecl(passport.get("ecl")) and check_pid(passport.get("pid"))

def check_byr(birth_year):
    if birth_year is None:
        return False
    elif len(birth_year)==4 and int(birth_year) <= 2002 and int(birth_year) >= 1920:
        return True
    else:
        return False

def check_iyr(issue_year):
    if issue_year is None:
        return False
    elif len(issue_year)==4 and int(issue_year) <= 2020 and int(issue_year) >= 2010:
        return True
    else:
        return False

def check_eyr(expiration_year):
    if expiration_year is None:
        return False
    elif len(expiration_year)==4 and int(expiration_year) <= 2030 and int(expiration_year) >= 2020:
        return True
    else:
        return False

def check_hgt(height):
    if height is None:
        return False
    elif "cm" in height:
        return True if int(height[:-2]) <= 193 and int(height[:-2]) >= 150 else False
    elif "in" in height:
        return True if int(height[:-2]) <= 76 and int(height[:-2]) >= 59 else False
    else:
        return False

def check_hcl(hair_color):
    if hair_color is None:
        return False
    elif hair_color[0] == "#" and len(hair_color) == 7:
        for c in hair_color[1:]:
            if ord(c) <= 102 and ord(c) >= 97 or ord(c) <=57 and ord(c) >= 48:
                return True
    else:
        return False

def check_ecl(eye_color):
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return eye_color in colors

def check_pid(passport_id):
    if passport_id is None:
        return False
    elif passport_id.isdecimal() and len(passport_id)==9:
        return True
    else:
        return False

f = open("04input.txt")

batch = []
entry = ""
for line in f:
    if line != "\n":
        entry = entry + " " + line.rstrip()
    else:
        batch.append(entry.strip())
        entry = ""
batch.append(entry.strip())

passports = []
for s in batch:
    pairs = s.split(" ")
    dictionary = {}
    for p in pairs:
        dictionary[p.split(":")[0]]=p.split(":")[1]
    passports.append(dictionary)

valid = 0
for p in passports:
    if is_valid_passport(p):
        valid += 1

print(valid)
