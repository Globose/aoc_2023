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
p1()