file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

passports = []

p = dict()

colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

for line in myin:
    if line:
        for e in line.split(" "):
            k, v = e.split(":")
            p[k] = v
    else:
        passports.append(p.copy())
        p.clear()


def part_one():
    valid = 0
    for passport in passports:
        if "cid" in passport and len(passport.keys()) == 8:
            valid += 1
        elif "cid" not in passport and len(passport.keys()) == 7:
            valid += 1
    print(valid)


def part_two():
    valid = 0
    for passport in passports:
        try:
            byr = 1920 <= int(passport['byr']) <= 2002
            iyr = 2010 <= int(passport['iyr']) <= 2020
            eyr = 2020 <= int(passport['eyr']) <= 2030
            height, measure = int(passport['hgt'][:-2]), passport['hgt'][-2:]
            hgt = (measure == "cm" and 150 <= height <= 193) or (measure == "in" and 59 <= height <= 76)
            hcl = passport['hcl'][0] == "#"
            try:
                if type(int(passport['hcl'][1:], 16)) == int:
                    hcl = hcl and True
            except:
                pass
            ecl = passport['ecl'] in colors
            pid = passport['pid'].isdigit() and len(passport['pid']) == 9

            if all([byr, iyr, eyr, hgt, hcl, ecl, pid]):
                valid += 1
        except:
            pass
    print(valid)


part_one()
part_two()
