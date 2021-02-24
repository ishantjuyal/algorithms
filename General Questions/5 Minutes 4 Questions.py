def add(s1, s2):
    n = len(s1)
    mid = n//2
    new = s1[:mid] + s2 + s1[mid:]
    return(new)

print(add("something", "great"))

def reorder(s):
    up = ''
    low = ''
    for i in s:
        if i.isupper() == True:
            up += i
        else:
            low += i
    new = up + low
    return(new)

print(reorder("HelloWorld"))

def count(a):
    a_dict = {}
    for i in a:
        if i in a_dict:
            a_dict[i] += 1
        else:
            a_dict[i] = 1
    return(a_dict)

print(count(["a", "b", "b"]))

def reverse(num):
    rev = 0
    t = num
    while t > 0:
        rev = rev*10 + (t%10)
        t = t//10
    return(rev)
print(reverse(123))