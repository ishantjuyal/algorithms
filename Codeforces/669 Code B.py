def find_gcd(x, y): 
    while(y):
        x, y = y, x % y 
    return x

def gcd(l):
    num1 = l[0] 
    num2 = l[1] 
    gcd = find_gcd(num1, num2) 
    for i in range(2, len(l)): 
        gcd = find_gcd(gcd, l[i])
    return(gcd)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(a)[::-1]
    gcd = b[0]
    for i in range(1, n):
        value = 0
        swap = 1
        for j in range(i, n):
            #temp_arr = b[:i] + [b[j]]
            temp = find_gcd(gcd, b[j])
            if temp > value:
                value = temp
                swap = j
        gcd = value
        b[i], b[swap] = b[swap], b[i]

    print(*b)
