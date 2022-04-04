import sys
parent = [0] * 100
size = [0] * 100


def find_set(v):
    if (v == parent[v]):
        return v
    parent[v] = find_set(parent[v])

    return parent[v]


def union_sets(a, b):
    a = find_set(a)
    b = find_set(b)

    if (a != b):

        if (size[a] < size[b]):
            a, b = b, a

        parent[b] = a
        size[a] += size[b]
        return 1

    return 0


def MST(houses, n):
    v = []
    for i in range(n):
        for j in range(i + 1, n):
            p = ((((houses[i][0] - houses[j][0]) ** 2) + ((houses[i][1] - houses[j][1]) ** 2)) ** 0.5)

            v.append([p, i, j])

    v = sorted(v)

    for i in range(n):
        parent[i] = i
        size[i] = 1

    ans = 0
    for x in v:

        if (union_sets(x[1], x[2])):
            ans += x[0]

    answer = str(round(ans, 2))

    print(ans)


if __name__ == '__main__':
    houses = input('prompt users here if you want: ')
    N = len(houses)
    print(houses)

    MST(houses, N)