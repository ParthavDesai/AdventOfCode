def main():
    part1()
    part2()


def part1():
    height = 0
    depth = 0
    f = open("input2.txt", "r")
    for line in f.readlines():
        val = line.split()
        if val[0] == "forward":
            depth += int(val[1])
        elif val[0] == "up":
            height += int(val[1])
        elif val[0] == "down":
            height -= int(val[1])
    f.close()
    ans = abs(height * depth)
    print("answer for part 1 is: " + str(ans))


def part2():
    height = 0
    depth = 0
    aim = 0
    f = open("input2.txt", "r")
    for line in f.readlines():
        val = line.split()
        if val[0] == "forward":
            height += int(val[1])
            depth += int(aim) * int(val[1])
        elif val[0] == "up":
            aim += int(val[1])
        elif val[0] == "down":
            aim -= int(val[1])
    f.close()
    ans = abs(height * depth)
    print("answer for part 2 is:" + str(ans))


if __name__ == "__main__":
    main()
