def transpose(A):
    C = []
    for i in range(len(A[0])):
        row = ""
        for j in range(len(A)):
            row += A[j][i]
        C.append(row)
    return C

def expand_d(A):
    nr = 0
    for i, a in enumerate(A.copy()):
        if not '#' in a:
            A.insert(i+nr, a)
            nr += 1

def expand(A):
    expand_d(A)
    C = transpose(A)
    expand_d(C)
    A = transpose(C)
    return A

def distance(t1, t2):
    return abs(t1[0]-t2[0])+abs(t1[1]-t2[1])

def distance_leap(t1, t2, x_leaps, y_leaps):
    x_leap = y_leap = 0
    multiplier = 1000000
    X_range = range(min(t1[0],t2[0]), max(t1[0],t2[0]))
    for x in x_leaps:
        if x in X_range:
            x_leap += 1

    Y_range = range(min(t1[1],t2[1]), max(t1[1],t2[1]))
    for y in y_leaps:
        if y in Y_range:
            y_leap += 1

    return abs(t1[0]-t2[0])+abs(t1[1]-t2[1])-x_leap-y_leap+x_leap*multiplier+y_leap*multiplier

def p1():
    with open('data/a11.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n"))
        A = expand(A)
        galaxes = []
        for j in range(len(A)):
            for i in range(len(A[0])):
                if A[j][i] == '#':
                    galaxes.append((i,j))
        sum = 0
        for g1 in galaxes.copy():
            galaxes.remove(g1)
            for g2 in galaxes.copy():
                sum += distance(g1,g2)
        print(sum)

def p2():
    with open('data/a11.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n"))

        x_leaps = []
        y_leaps = []
        nr = 0
        for i, a in enumerate(A):
            if not '#' in a:
                y_leaps.append(i)
        B = transpose(A)
        for i, b in enumerate(B):
            if not '#' in b:
                x_leaps.append(i)

        # print(x_leaps, y_leaps)

        galaxes = []
        for j in range(len(A)):
            for i in range(len(A[0])):
                if A[j][i] == '#':
                    galaxes.append((i,j))
        sum = 0
        for g1 in galaxes.copy():
            galaxes.remove(g1)
            for g2 in galaxes.copy():
                sum += distance_leap(g1,g2,x_leaps,y_leaps)
        print(sum)


p1()
p2()
