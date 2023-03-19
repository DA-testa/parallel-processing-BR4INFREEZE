def process(n, m, data):
    output = []
    work = []
    i = 0
    b = 0
    for init in range(n):
        work.append(0)
    for k in range(m):
        cr(k,work,data,i,n)


def cr(k,work,data,i,n):
    for a in range(n):
        if work[a] == i:
            print(a, work[a])
            work[a] = work[a] + data[k]
            break
        elif a == n - 1:
            i = min(work)
            cr(k,work,data,i,n)


def main():
    first = list(map(int, input().split()))
    data = list(map(int, input().split()))
    assert len(data) == first[1]
    process(first[0], first[1], data)

main()
