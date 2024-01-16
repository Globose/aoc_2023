from math import lcm

def p1():
    with open('data/a8.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []
        for s in file:
            A.append(s.strip("\n"))

        rule = A[0]
        A = A[2:]

        dct = {}
        for i, a in enumerate(A):
            p = a.split(" = ")
            dct[p[0]] = (p[1][1:4], p[1][6:9])

        i = 0
        code = 'AAA'
        while True:
            instr = dct[code]
            if code == 'ZZZ':
                break
            if rule[i%len(rule)] == 'R':
                code = instr[1]
            else:
                code = instr[0]
            i += 1
        print(i)

def p2():
    with open('data/a8.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []
        for s in file:
            A.append(s.strip("\n"))

        rule = A[0]
        A = A[2:]

        dct = {}
        for i, a in enumerate(A):
            p = a.split(" = ")
            dct[p[0]] = (p[1][1:4], p[1][6:9])

        codes = []
        for c in dct.keys():
            if c[-1] == 'A':
                codes.append(c)

        allNums = []
        for c in codes:
            code = c
            i = 0
            cd = {code:[i]}
            zs = []

            while True:
                instr = dct[code]
                if rule[i%len(rule)] == 'R':
                    code = instr[1]
                else:
                    code = instr[0]
                value = (i+1)%len(rule)
                if code[-1] == 'Z':
                    zs.append(i)
                if cd.get(code) is None:
                    cd[code] = [value]
                else:
                    if value in cd[code]:
                        i = i-value+1
                        break
                    else:
                        cd[code].append(value)
                i += 1

            allNums.append((zs[-1],i))
        a0 = allNums[0]
        value = 0
        y = 1
        while y < len(allNums):
            a1 = allNums[y]

            x = 0
            value = 0
            while True:
                value = a0[0]+x*a0[1]
                if value%a1[1] == a1[0]:
                    break
                x+=1

            a0 = (value, lcm(a0[1],a1[1]))
            y+=1
        print(a0[0]+1)

p1()
p2()