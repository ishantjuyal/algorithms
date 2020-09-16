def mex(A):
    if A == []:
        return(0)
    for i in range(max(A)+2):
        if i not in A:
            return(i)



t = int(input())
for _ in range(t):
    n = int(input())
    S = list(map(int, input().split()))

    if 0 not in S:
        print(0)
        continue

    if S.count(0) == 1:
        print(mex(S))
        continue
    
    adict = {}
    for i in S:
        if i in adict:
            adict[i] += 1
        else:
            adict[i] = 1

    A = []
    B = []

    values = sorted(list(adict.keys()))

    for i in values:
        if adict[i] > 1:
            A = A + [i]*(adict[i]//2)
            B = B + [i]*(adict[i] - (adict[i]//2))

        else:
            #print(A)
            #print(i)
            if mex(A + [i]) > mex(A):
                A.append(i)
            else:
                B.append(i)

    print(mex(A) + mex(B))
