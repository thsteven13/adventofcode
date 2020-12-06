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
    for i in input:
        find = 2020-int(i)
        if find in myset:
            answer = int(i)*int(find)
            print(answer)
        myset.add(int(i))

if __name__ == '__main__':
    main()
