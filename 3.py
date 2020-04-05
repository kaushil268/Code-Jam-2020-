def fun1(abc, xyz):
    if abc[0] > xyz[0] and abc[0] < xyz[1]:
        return True
    if abc[1] > xyz[0] and abc[1] < xyz[1]:
        return True
    return False


def funR(abc, xyz):
    return fun1(abc, xyz) or fun1(xyz, abc) or abc[0] == xyz[0] or abc[1] == xyz[1]


t = int(input())

for var1 in range(t):
    n = int(input())

    array = []
    for i in range(n):
        sa = input().split(" ")
        inp = (int(sa[0]), int(sa[1]), i)
        array.append(inp)

    org = array
    array.sort(key=lambda x: x[0])
    print("Case #" + str(var1 + 1) + ": ", end='')

    arrayj = []
    arrayc = []
    pqr = srt = 0
    pos = True
    for i in range(len(array)):
        if array[i][0] >= pqr:
            arrayj.append(array[i][2])
            pqr = array[i][1]
        else:
            if array[i][0] >= srt:
                arrayc.append(array[i][2])
                srt = array[i][1]
            else:
                pos = False
                break

    if not pos:
        print("IMPOSSIBLE")
    else:
        que = [0] * len(array)
        for i in arrayj:
            que[i] = "J"
        for i in arrayc:
            que[i] = "C"
        print(''.join(que))