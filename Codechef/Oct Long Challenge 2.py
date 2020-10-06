# Easy Queries

t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    q = list(map(int, input().split()))
    
    if sum(q) <= 3000000:
        i = 0
        queries = 0
        resolved = 0
        while True:
            if i < n:
                queries += q[i]
            if queries < k:
                print(i+1)
                break
            else:
                resolved += k
                queries -= k
            i += 1
    else:
        print(sum(q)//k + 1)