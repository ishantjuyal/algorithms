# Giving WA

t = int(input())
for _ in range(t):
    n, k, x, y = map(int, input().split())
    impact = 0

    x_direction = True
    y_direction = True

    while True:
        if x_direction == True:
            x_move = n - x
        else:
            x_move == x
        if y_direction == True:
            y_move = n - y
        else:
            y_move = y

        move = min(y_move, x_move)

        if x_direction == True:
            x = x + move
        else:
            x = x - move
        
        if y_direction == True:
            y = y + move
        else:
            y = y - move

        if x == n or y == n or x == 0 or y == 0:
            impact += 1
        
        if x == n:
            x_direction = False
        if x == 0:
            x_direction = True
        if y == n:
            y_direction = False
        if y == 0:
            y_direction = True

        if impact == k:
            print(x, y)
            break

        if (x == 0 and y == 0) or (x == 0 and y == n) or (y == 0 and x == n) or (x == n and y == n):
            print(x, y)
            break