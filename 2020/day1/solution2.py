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
    myset = set()

    for num in input:
        myset.add(int(num))

    for i in range(0, len(input), 1):
        for j in range(i+1, len(input), 1):
            inti = int(input[i])
            intj = int(input[j])
            twosum = inti + intj
            answer = 2020 - twosum
            if answer in myset:
                threesum = answer*inti*intj
                print(threesum)
                exit()



if __name__ == '__main__':
    main()

'''
Example:

total = 10

2
3
5
7

'''
