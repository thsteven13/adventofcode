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
    dict = {}
    notvisited = set()
    total = 0
    key = 0
    loop = True
    for i in range(0,len(input),1):
        dict[i] = input[i]
        notvisited.add(i)
    while key in notvisited:
        print(key)
        notvisited.remove(key)
        val = dict[key].split( )
        arg = val[0]
        num = int(val[1])
        if arg == "acc":
            key = key + 1
            total = total + num
        elif arg == "jmp":
            key = key + num
        elif arg == "nop":
            key = key + 1
    print(total)



if __name__ == '__main__':
    main()
