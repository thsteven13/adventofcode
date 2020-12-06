import math

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

#lower half
def front(min,max):
    pair = []
    pair.append(min)
    pair.append(math.floor((min+max)/2))
    return pair

def back(min,max):
    pair = []
    pair.append(math.ceil((min+max)/2))
    pair.append(max)
    return pair

def main():
    input = readline("input.txt")
    max_answer = 0
    for line in input:
        min = 0
        max = 127
        rowmin = 0
        rowmax = 7
        for c in line:
            if c == 'F':
                res = front(min,max)
                min = res[0]
                max = res[1]
            elif c == 'B':
                res = back(min,max)
                min = res[0]
                max = res[1]
            elif c == 'L':
                res = front(rowmin,rowmax)
                rowmin = res[0]
                rowmax = res[1]
            elif c == 'R':
                res = back(rowmin,rowmax)
                rowmin = res[0]
                rowmax = res[1]
        if ((min*8)+rowmin) > max_answer:
            max_answer = ((min*8)+rowmin)
    print(max_answer)
if __name__ == '__main__':
    main()

#BFFFBBFRRR
