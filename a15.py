def hash_1(s):
    c_val = 0
    for c in s:
        c_val += ord(c)
        c_val *= 17
        c_val %= 256
    return c_val

def p1():
    with open('data/a15.txt', 'r', encoding='UTF-8') as file:
        A = []
        sum = 0
        for s in file:
            A.append(s)
        A = A[0].split(",")
        for a in A:
            sum += hash_1(a)
        print(sum)

def remove(D:list, label):
    for d in D:
        if label == d[0]:
            D.remove(d)
            return

def replace(D:list, label, num):
    for i,d in enumerate(D):
        if label == d[0]:
            D[i] = (label, num)
            return
    D.append((label,num))

def p2():
    with open('data/a15.txt', 'r', encoding='UTF-8') as file:
        A = []
        sum = 0
        for s in file:
            A.append(s)
        A = A[0].split(",")
        B = [[] for _ in range(256)]
        for a in A:
            hstring = ""
            sign = None
            num = 0
            for i, c in enumerate(a):
                if c == '-':
                    sign = c
                    break
                if c == '=':
                    sign = c
                    num = (int)(a[i+1:])
                    break
                hstring+= c

            box_index = hash_1(hstring)
            if sign == '-':
                remove(B[box_index], hstring)
            else:
                replace(B[box_index], hstring, num)
        for box_nr, b in enumerate(B):
            for slot_nr, lens in enumerate(b):
                sum += (1+box_nr)*(slot_nr+1)*lens[1]
        print(sum)

p1()
p2()
