import numpy

t = int(input())
for i in range(t):
    N = int(input())

    matrix = [[] *3]*3
    matrix = numpy.zeros((N,N))
    rowc=0
    colc=0
    for j in range(N):
        abc = input().split(" ")
        diagonal = []

        for k in abc:
            if k in diagonal:
                rowc = rowc + 1
                break
            diagonal.append(k)

        length_abc=len(abc)

        for k in range(length_abc):
            matrix[k][j] = abc[k]


    for j in matrix:
        diagonal = []
        for k in j:
            if k in diagonal :
                colc = colc + 1
                break
            diagonal.append(k)

    print("Case #" + str(i+1) + ":", int(matrix.trace()) , rowc , colc)

















