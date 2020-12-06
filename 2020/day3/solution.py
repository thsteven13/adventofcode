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
    start = 0
    for line in input:
        print(start)
        if line[start] == '#':
            answer += 1
        if start+3 > len(line)-1:
            print('overflow')
            diff = start+3-(len(line)-1)
            start = diff
        elif start+3 == len(line)-1:
            print('exact')
            start = 0
        else:
            start = start + 3
    print('answer')
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
