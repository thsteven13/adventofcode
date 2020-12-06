import re
pattern = re.compile("[a-f0-9]+")
dict = {}
eyecolor = set()

def readline(filepath):
    input = []
    with open(filepath) as fp:
       line = fp.readline()
       cnt = 1
       while line:
           input.append(line)
           line = fp.readline()
           cnt += 1
       return input

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def reset():
    dict['byr'] = ""
    dict['iyr'] = ""
    dict['eyr'] = ""
    dict['hgt'] = ""
    dict['hcl'] = ""
    dict['ecl'] = ""
    dict['pid'] = ""
    dict['cid'] = ""

def validate(eyecolor, answer):
    count = 0
    if dict['byr'] != "":
        if len(dict['byr']) == 4:
            a = int(dict['byr'])
            if a >= 1920 and a <= 2002:
                count += 1
    if dict['iyr'] != "":
        if len(dict['iyr']) == 4:
            b = int(dict['iyr'])
            if b >= 2010 and b <= 2020:
                count += 1
    if dict['eyr'] != "":
        if len(dict['iyr']) == 4:
            c = int(dict['eyr'])
            if c >= 2020 and c <= 2030:
                count += 1
    if dict['hgt'] != "":
        meas = dict['hgt'][-2:]
        if meas == 'cm':
            num = int(dict['hgt'][:-2])
            if num >= 150 and num <= 193:
                count +=1
        elif meas == 'in':
            num = int(dict['hgt'][:-2])
            if num >= 59 and num <= 76:
                count += 1
    if dict['hcl'] != "":
        if dict['hcl'][0] == '#':
            if len(dict['hcl'][1:]) == 6:
                if pattern.fullmatch(dict['hcl'][1:]) is not None:
                    count += 1
    if dict['ecl'] != "":
        color = dict['ecl']
        if color in eyecolor:
            count += 1
    if dict['pid'] != "":
        if isint(dict['pid']):
            if len(dict['pid']) == 9:
                count += 1
    if count == 7:
        answer += 1
    reset()
    return answer

def populate_eyecolor():
    eyecolor.add("amb")
    eyecolor.add("blu")
    eyecolor.add("brn")
    eyecolor.add("gry")
    eyecolor.add("grn")
    eyecolor.add("hzl")
    eyecolor.add("oth")

def main():
    input = readline("input.txt")
    reset()
    populate_eyecolor()
    answer = 0

    for line in input:
        if line == "\n":
            answer = validate(eyecolor,answer)
        for field in line.split( ):
            if field.split(":")[0] == 'byr':
                dict['byr'] = field.split(":")[1]
            elif field.split(":")[0] == 'iyr':
                dict['iyr'] = field.split(":")[1]
            elif field.split(":")[0] == 'eyr':
                dict['eyr'] = field.split(":")[1]
            elif field.split(":")[0] == 'hcl':
                dict['hcl'] = field.split(":")[1]
            elif field.split(":")[0] == 'hgt':
                dict['hgt'] = field.split(":")[1]
            elif field.split(":")[0] == 'ecl':
                dict['ecl'] = field.split(":")[1]
            elif field.split(":")[0] == 'pid':
                dict['pid'] = field.split(":")[1]
            elif field.split(":")[0] == 'cid':
                dict['cid'] = field.split(":")[1]
            count = 0
    print(validate(eyecolor,answer))


if __name__ == '__main__':
    main()
