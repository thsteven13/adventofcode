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
    truth = set()
    group = set()
    first = True
    for line in input:
        #print(line)
        if line == "\n":
            answer = answer + (len(truth))
            #print(answer)
            first = True
            group = set()
            truth = set()
        elif first is False:
            #print(line)
            for i in line:
                if i in truth:
                    if i != "\n":
                        group.add(i)
            truth = set()
            truth = group
            group = set()
        elif first is True:
            for i in line:
                if i != "\n":
                    truth.add(i)
            #print(truth)
            first = False

    answer = answer + (len(truth))
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
