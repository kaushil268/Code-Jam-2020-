import numpy as np

t = int(input())

for i in range(t):
    s = input()
    s = [int(x) for x in s]
    new = []
    count = 0
    for j in s:
        while count != j:
            if(count < j ):
                new.append("(")
                count = count + 1
            elif(count > j ):
                new.append(")")
                count = count - 1

        if (count == j):
            new.append(j)

    while(count != 0 ):
        new.append(")")
        count = count - 1

    new1 = ''.join(str(e) for e in new)
    print("Case #" + str(i+1) + ":", new1)









