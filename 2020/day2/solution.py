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
    for line in input:
        count  = 0
        parsed = line.split( )
        num = parsed[0].split('-')
        min = int(num[0])
        max = int(num[1])
        char = parsed[1][0]
        password = parsed[2]
        for i in range(0, len(password), 1):
            if password[i] == char:
                count += 1
        if count >= min and count <= max:
            answer += 1
    print(answer)

if __name__ == '__main__':
    main()
