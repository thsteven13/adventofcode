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
    stopwords = ['bags.','no','other',',','bag.','1','2','3','4','5','6','7','8','9','0','bag','bags']
    input = readline("input.txt")
    bags = {}
    visited = set()
    ret = set()
    queue = []
    for line in input:
        valuebags = []
        input = line.split("contain")
        key = input[0].strip()[:-5]
        values = input[1].split(',')
        for value in values:
            splitval = value.split()
            resvalue = [word for word in splitval if word.lower() not in stopwords]
            result = ' '.join(resvalue)
            #print(result)
            valuebags.append(result)
        bags[key] = valuebags
    for i in bags:
        if 'shiny gold' in bags[i]:
            ret.add(i)
            queue.append(i)
    #print(ret)
    #print(queue)
    while len(queue) > 0 :
        key = queue.pop()
        if key not in visited:
            visited.add(key)
            for i in bags:
                #print(key)
                if key in bags[i]:
                    ret.add(i)
                    if i not in visited:
                        queue.append(i)
    print(ret)
    print(len(ret))


if __name__ == '__main__':
    main()
