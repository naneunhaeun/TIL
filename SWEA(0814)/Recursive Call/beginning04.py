arr = ['A', 'B', 'C', 'D', 'E']
path = []

n = 3


def fx(lev, start):
    if lev == n:
        print(*path)
        return

    for i in range(start, 5):
        path.append(arr[i])
        fx(lev + 1, i + 1)
        path.pop()


fx(0, 0)