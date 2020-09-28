
def main(l, x, arr):
    q = []
    for i in range(0, l):
        e = arr[i]
        q.append([(e) // x, i + 1])

    q.sort()
    return q


if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        secondLine = input().split(' ')
        l = int(secondLine[0])
        x = int(secondLine[1])
        arr = [int(x) for x in input().split(' ')]
        arrInString = " ".join([str(x[1]) for x in main(l, x, arr)])
        str_ = "Case #" + str(i+1) + ": "+arrInString
        print(str_)
