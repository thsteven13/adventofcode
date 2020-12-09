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
    for i in range(0,len(input),1):
        dict[i] = input[i]
        notvisited.add(i)

    for i in range(0,len(input),1):
        key = 0
        total = 0
        notvisited.clear()
        for j in range(0,len(input),1):
            dict[j] = input[j]
            notvisited.add(j)

        cval = dict[i].split( )
        carg = cval[0]
        cnum = cval[1]

        if carg == "jmp":
            carg = "nop"
        elif carg == "nop":
            carg = "jmp"

        dict[i] = " ".join([carg, cnum])
        print(dict[i])

        while key in notvisited:
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
            if key == len(dict):
                print(total)
                return

if __name__ == '__main__':
    main()
