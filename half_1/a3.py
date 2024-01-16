def p1():
    with open('data/a3.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []
        for s in file:
            A.append(s.strip("\n"))

        allNums = [[] for i in range(len(A))]
        for i, line in enumerate(A):
            j = 0
            while j < len(line):
                if line[j].isdigit():
                    num = ""
                    index_start = j
                    index_end = j
                    while j < len(line) and line[j].isdigit():
                        num += line[j]
                        j += 1
                        index_end = j
                    allNums[i].append((index_start, index_end-1, (int)(num)))
                j+=1
            allNums[i].sort()

        for i, line in enumerate(A):
            for j, c in enumerate(line):
                if not (c.isdigit() or c == '.'):
                    for k in range(i-1,i+2):
                        if i < 0 or i >= len(line):
                            continue
                        for tup in allNums[k].copy():
                            for d in range(tup[0],tup[1]+1):
                                if d in range(j-1, j+2):
                                    sum += tup[2]
                                    allNums[k].remove(tup)
                                    break
        print(sum)

def p2():
    with open('data/a3.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []
        for s in file:
            A.append(s.strip("\n"))

        allNums = [[] for i in range(len(A))]
        for i, line in enumerate(A):
            j = 0
            while j < len(line):
                if line[j].isdigit():
                    num = ""
                    index_start = j
                    index_end = j
                    while j < len(line) and line[j].isdigit():
                        num += line[j]
                        j += 1
                        index_end = j
                    allNums[i].append((index_start, index_end-1, (int)(num)))
                j+=1
            allNums[i].sort()
        allSymbs = []
        for i, line in enumerate(A):
            for j, c in enumerate(line):
                if not (c.isdigit() or c == '.'):
                    if not c == '*':
                        continue
                    adj_num = []
                    for k in range(i-1,i+2):
                        if i < 0 or i >= len(line):
                            continue
                        for tup in allNums[k].copy():
                            for d in range(tup[0],tup[1]+1):
                                if d in range(j-1, j+2):
                                    adj_num.append(tup[2])
                                    #allNums[k].remove(tup)
                                    break
                    if (len(adj_num) == 2):
                        sum += adj_num[0]*adj_num[1]
        print(sum)

p1()
p2()