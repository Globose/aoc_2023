def find_last(A):
    diff_list = []
    for i in range(1,len(A)):
        diff_list.append(A[i]-A[i-1])
    last_element = diff_list[-1]
    if sum(diff_list)!=0:
        last_element = find_last(diff_list)
    return last_element + A[-1]

def find_first(A):
    diff_list = []
    for i in range(1,len(A)):
        diff_list.append(A[i]-A[i-1])
    first_element = diff_list[0]
    if sum(diff_list)!=0:
        first_element = find_first(diff_list)
    return  A[0] - first_element

def p1():
    with open('data/a9.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []
        for s in file:
            A.append(s.strip("\n"))
        for i, a in enumerate(A):
            array = a.split(" ")
            int_A = []
            for s in array:
                int_A.append((int)(s))
            A[i] = int_A
            sum += find_last(A[i])
        print(sum)

def p2():
    with open('data/a9.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []
        for s in file:
            A.append(s.strip("\n"))
        for i, a in enumerate(A):
            array = a.split(" ")
            int_A = []
            for s in array:
                int_A.append((int)(s))
            A[i] = int_A
            sum += find_first(A[i])
        print(sum)

p1()
p2()