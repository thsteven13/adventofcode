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
    answer = 177777905
    order = []
    count = 0
    for line in input:
        order.append(int(line))

    for i in range(0, len(order), 1):
        preamble = answer
        min = 2147483647
        max = -2147483647
        for j in range(i, len(order), 1):
            if order[j] < min:
                min = order[j]
            if order[j] > max:
                max = order[j]
            preamble = preamble - order[j]
            if preamble == 0:
                print(min+max)
                return
            if preamble < 0:
                break

if __name__ == '__main__':
    main()
