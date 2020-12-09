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
    preamble = 25
    order = []
    count = 0
    for line in input:
        order.append(int(line))

    for i in range(preamble, len(order), 1):
        hashset = set()
        count = 0
        for j in range(i-preamble,i,1):
            hashset.add(order[j])
        #print(hashset)
        for k in range(i-preamble,i,1):
            find = order[i] - order[k]
            hashset.remove(order[k])
            #print(find)
            if find not in hashset:
                count += 1
        #print(count)
        if count == preamble:
            print(order[i])



if __name__ == '__main__':
    main()
