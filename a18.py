from PIL import Image
from random import randrange

def fill(A):
    lst = []
    for i in range(0, len(A)):
        if A[i][0] == '.':
            lst.append((0,i))
        if A[i][len(A[0])-1] == '.':
            lst.append((len(A[0])-1, i))

    for i in range(0, len(A[0])):
        if A[0][i] == '.':
            lst.append((i,0))
        if A[len(A)-1][i] == '.':
            lst.append((i, len(A)-1))

    s0 = [(0,1),(0,-1), (1,0), (-1,0)]
    while len(lst) > 0:
        # print(len(lst))
        for l in lst.copy():
            A[l[1]][l[0]] = '-'
            lst.remove(l)
            for s in s0:
                x = l[0]+s[0]
                y = l[1]+s[1]
                if x < 0 or y < 0 or x >= len(A[0]) or y >= len(A):
                    continue
                if A[y][x] == '.':
                    if (x,y) not in lst:
                        lst.append((x,y))
    counter = 0
    for line in A:
        for l in line:
            if l == '#' or l == '.':
                counter += 1
    return counter

def p1():
    with open('data/a18.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n"))
        grid = {}
        x = y = 0
        dirmap = {'R':(1,0), 'L':(-1,0), 'U':(0,-1), 'D':(0,1)}
        for a in A:
            dir, steps, color = a.split(" ")
            dir = dirmap[dir]
            grid[(x,y)] = '#'

            for i in range((int)(steps)):
                x += dir[0]
                y += dir[1]
                grid[(x,y)] = '#'
        min_y = min(grid.keys(), key=lambda x:x[1])[1]
        min_x = min(grid.keys())[0]
        max_y = max(grid.keys(), key=lambda x:x[1])[1]
        max_x = max(grid.keys())[0]

        matrix = []
        for i in range(min_y, max_y+1):
            line = []
            for j in range(min_x, max_x+1):
                if grid.get((j,i)) is None:
                    line.append('.')
                else:
                    line.append('#')
            matrix.append(line)

        c = fill(matrix)
        print(c)

def gauss(A):
    sum = 0
    A = A[::-1]
    for i in range(len(A)):
        h = i-1
        j = (i+1)%len(A)
        sum += A[i][0]*(A[j][1]-A[h][1])
        # print(A[i][0], A[j][1], A[h][1])
    return (int)(abs(sum)*0.5)


def p2():
    with open('data/a18.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n"))
        grid = []
        grid.append((0,0))
        y = 0
        x = 1

        for i in range(len(A)-1):
            p1 = A[i].split(" ")
            p2 = A[i+1].split(" ")
            size = int(p1[2][2:7], 16)
            d1 = p1[2][-2]
            d2 = p2[2][-2]

            # size = int(p1[1])
            # d1 = p1[0]
            # d2 = p2[0]

            if d1 == 'R' or d1 == '0':
                if d2 == 'D' or d2 == '1':
                    x += size
                    grid.append((x,y))
                    y-=1
                else:
                    x += size-1
                    grid.append((x,y))

            elif d1 == 'D' or d1 == '1':
                if d2 == 'L' or d2 == '2':
                    y -= size
                    grid.append((x,y))
                    x -= 1
                else:
                    y -= size-1
                    grid.append((x,y))
            elif d1 == 'L' or d1 == '2':
                if d2 == 'D' or d2 == '1':
                    x -= size-1
                    grid.append((x,y))
                else:
                    x -= size
                    grid.append((x,y))
                    y += 1
            elif d1 == 'U' or d1 == '3':
                if d2 == 'L' or d2 == '2':
                    y += size-1
                    grid.append((x,y))
                else:
                    y += size
                    grid.append((x,y))
                    x += 1

        print(gauss(grid))

# p1()
p2()
