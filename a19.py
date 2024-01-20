IND = {'x':0, 'm':1, 'a':2, 's':3}
def work(htable, part, name):
    if name == "A":
        return True
    if name == "R":
        return False
    hlst = htable.get(name)
    for rule in hlst:
        if rule.find(">") == -1 and rule.find("<") == -1:
            return work(htable, part, rule)

        col_index = rule.find(":")
        num = (int)(rule[2:col_index])
        index = IND[rule[0]]
        if (rule[1] == '>' and part[index] > num) or (rule[1] == '<' and part[index] < num):
            return work(htable, part, rule[col_index+1:])

def p1():
    with open('data/a19.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n"))

        workflow = {}
        parts = []
        upper = True

        for a in A:
            if a == "":
                upper = False
                continue
            if upper:
                x = a.find("{")
                name = a[:x]
                rules = a[x+1:-1].split(",")
                workflow[name] = rules
            else:
                a1 = a[1:-1].split(",")
                lst = []
                for c in a1:
                    lst.append((int)(c[2:]))
                parts.append(lst)

        totalsum = 0
        for p in parts:
            accept = work(workflow, p, "in")
            if accept:
                totalsum += sum(p)
        print(totalsum)

def p2_work(htable, id, part):
    # print("N", id, part)
    for p in part:
        if p[1] < p[0]:
            return 0
    if id == "A":
        psum = 1
        for p in part:
            psum *= p[1]-p[0]
        # print("  ", psum)
        return psum
    if id == "R":
        return 0
    hlst = htable.get(id)
    totalsum = 0
    for rule in hlst:
        if rule.find(">") == -1 and rule.find("<") == -1:
            totalsum += p2_work(htable, rule, part)
            continue

        col_index = rule.find(":")
        num = (int)(rule[2:col_index])
        index = IND[rule[0]]
        if rule[1] == '>':
            p1 = part.copy()
            p2 = part.copy()
            p1[index] = (max(num+1, p1[index][0]),p1[index][1])
            p2[index] = (p2[index][0], min(num+1, p2[index][1]))
            # print("R", rule, p1)
            totalsum += p2_work(htable, rule[col_index+1:], p1)
            part = p2
        else:
            p1 = part.copy()
            p2 = part.copy()
            p1[index] = (p1[index][0],min(num, p1[index][1]))
            p2[index] = (min(num, p2[index][1]), p2[index][1])
            totalsum += p2_work(htable, rule[col_index+1:], p1)
            part = p2
    return totalsum

def p2():
    with open('data/a19.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n"))

        htable = {}

        for a in A:
            if a == "":
                break
            x = a.find("{")
            name = a[:x]
            rules = a[x+1:-1].split(",")
            htable[name] = rules
        start = [(1,4001), (1,4001), (1,4001), (1,4001)]
        q = p2_work(htable, "in", start)
        print(q)

p2()