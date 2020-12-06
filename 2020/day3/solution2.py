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

def checkslope(right, down, input):
    answer = 0
    start = 0
    for i in range(0,len(input),down):
        if input[i][start] == '#':
            answer += 1
        if start+right > len(input[i])-1:
            diff = start+right-(len(input[i])-1)
            start = diff
        elif start+right == len(input[i])-1:
            start = 0
        else:
            start = start + right
    return answer

def main():
    input = readline("input.txt")
    a = checkslope(1,1,input)
    b = checkslope(3,1,input)
    c = checkslope(5,1,input)
    d = checkslope(7,1,input)
    e = checkslope(1,2,input)
    answer = a*b*c*d*e
    print(answer)

if __name__ == '__main__':
    main()

'''

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

'''
