import sys
import os


def circularArrayRotation(a, k, queries):
    count = 0
    list2 = []
    for i in range(len(a) - 1, -1, -1):
        count += 1
        if count > k:
            break
        else:
            list2.append(a[i])
    for j in range(k):
        a.pop()
    output = list2[::-1] + a
    for l in queries:
        print(output[l])


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for index in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    circularArrayRotation(a, k, queries)