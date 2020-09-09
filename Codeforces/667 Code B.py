t = int(input())
for _ in range(t):
    a,b,x,y,n = map(int, input().split())

    min_val = min(a, b)
    max_val = max(a, b)
    diff_1 = a-x
    diff_2 = b-y
    values = []
    if n >= diff_1 + diff_2:
        values.append(x*y)
    else:
        if diff_1 <= n:
            min_val = x
            n_copy = n - diff_1
            max_val = max_val - n_copy
            values.append(min_val*max_val)
            if diff_2 <=n:
                min_val = min(x, b-diff_2)
                if min_val != x:
                    n_copy = n - diff_2
                    max_val = max(x,a-n_copy)
                    values.append(min_val*max_val)
            else:
                min_val = b - n
                max_val = a
                values.append(min_val*max_val)
        else:
            #min_val = min_val - n
            #values.append(min_val*max_val)
            if diff_2 <=n:
                min_val = min(x, b-diff_2)
                if min_val != x:
                    n_copy = n - diff_2
                    max_val = a-n_copy
                    values.append(min_val*max_val)
            else:
                min_val = b - n
                max_val = a
                values.append(min_val*max_val)
                min_val = a-n
                max_val = b
                values.append(min_val*max_val)
    print(min(values))
