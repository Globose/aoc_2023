def transpose(A):
    C = []
    for i in range(len(A[0])):
        row = ""
        for j in range(len(A)):
            row += A[j][i]
        C.append(row)
    return C

def sym(A):
    for i in range(0, len(A)-1):
        sym = True
        for j in range(0, len(A)-i):
            if i-j < 0 or i+j+1 >= len(A):
                break
            if A[i-j] != A[i+j+1]:
                sym = False
                break
        if sym:
            return i
    return None

def get_diff(a1, a2):
    d = 0
    for i in range(len(a1)):
        if a1[i] != a2[i]:
            d += 1
    return d

def sym_smudge(A):
    for i in range(0, len(A)-1):
        sym = True
        diff = 0
        for j in range(0, len(A)-i):
            if i-j < 0 or i+j+1 >= len(A):
                break
            diff += get_diff(A[i-j], A[i+j+1])
        if diff == 1:
            return i
    return None

def p1():
    with open('data/a13.txt', 'r', encoding='UTF-8') as file:
        A = []
        sum = 0
        for s in file:
            A.append(s.strip("\n"))
        B = []
        C = []
        for a in A:
            if a == '':
                C.append(B)
                B = []
            else:
                B.append(a)
        C.append(B)

        for c in C:
            line = sym(c)
            if line is None:
                line = sym(transpose(c))
                sum += line+1
            else:
                sum += (line+1)*100
        print(sum)

def p2():
    with open('data/a13.txt', 'r', encoding='UTF-8') as file:
        A = []
        sum = 0
        for s in file:
            A.append(s.strip("\n"))
        B = []
        C = []
        for a in A:
            if a == '':
                C.append(B)
                B = []
            else:
                B.append(a)
        C.append(B)

        for c in C:
            line = sym_smudge(c)
            if line is None:
                line = sym_smudge(transpose(c))
                sum += line+1
            else:
                sum += (line+1)*100
        print(sum)

p1()
p2()