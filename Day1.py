def main():
    f = open("input.txt", "r")
    li = []
    for x in f.readlines():
        for i in x.split():
            if i.isdigit():
                li.append(int(i))
    f.close()
    part1(li)
    part2(li)


def part1(li):
    ans = 0
    for i in range(1, len(li)):
        if li[i - 1] < li[i]:
            ans += 1
    print("answer for part1:" + str(ans))


def part2(li):
    # basically a+b+c < b+c+d == a<d therfore just have to check a and d values
    ans = 0
    for i in range(0, len(li) - 3):
        if li[i] < li[i + 3]:
            ans += 1
    print("answer for part 2 of day 1 is:" + str(ans))


if __name__ == "__main__":
    main()
