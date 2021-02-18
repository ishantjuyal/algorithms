alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
code_dict = {}

def encode(character):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    code = ''
    l = 16
    for _ in range(4):
        if character in a[:l//2]:
            code += '0'
            a = a[:l//2]
        else:
            a = a[l//2:]
            code += '1'
        l = l//2
    code_dict[code] = character

for charac in alphabets:
    encode(charac)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = ''
    for i in range(n//4):
        code = s[i*4: i*4 + 4]
        ans = ans +  code_dict[code]
    print(ans)