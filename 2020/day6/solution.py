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

def main():
    input = readline("input.txt")
    answer = 0
    group = set()
    for line in input:
        if line == "\n":
            answer = answer + (len(group)-1)
            group.clear()
        for i in line:
            if i not in group:
                group.add(i)
    answer = answer + (len(group)-1)
    print(answer)


if __name__ == '__main__':
    main()

'''
abc

a
b
c

ab
ac

a
a
a
a

b
'''
