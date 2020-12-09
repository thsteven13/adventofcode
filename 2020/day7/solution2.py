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
    stopwords = ['bags.','no','other',',','bag.','bag','bags']
    input = readline("input.txt")
    bags = {}
    visited = set()
    ret = []
    queue = []
    for line in input:
        valuebags = []
        input = line.split("contain")
        key = input[0].strip()[:-5]
        values = input[1].split(',')
        bettervaluebags = []
        for value in values:
            splitval = value.split()
            resvalue = [word for word in splitval if word.lower() not in stopwords]
            result = ' '.join(resvalue)
            #print(result)
            valuebags.append(result)
        for v in valuebags:
            if len(v) > 0:
                num = int(v[0])
                print(v[2:])
                for i in range(0,int(num),1):
                    bettervaluebags.append(v[2:])
        bags[key] = bettervaluebags
        #bags[key] = valuebags
    #print(bags)
    for i in bags:
        if 'shiny gold' in i:
            for val in bags['shiny gold']:
                ret.append(val)
                queue.append(val)
    #print(ret)
    #print(queue)
    while len(queue) > 0 :
        key = queue.pop()
        for i in bags:
            if key == i:
                for val in bags[key]:
                    ret.append(val)
                    queue.append(val)
    #print(ret)
    print(len(ret))


if __name__ == '__main__':
    main()


'''
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
'''
