def p1():
    with open('data/a4.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []
        for s in file:
            A.append(s.strip("\n")[10:])

        for a in A:
            spl = a.split("|")
            winning = spl[0].split(" ")
            nums = spl[1].split(" ")
            counter = 0
            for w in winning.copy():
                if w == '':
                    continue
                if w in nums:
                    counter += 1

            if counter > 0:
                sum += 2**(counter-1)

        print(sum)

def p2():
    with open('data/a4.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n")[10:])
        A_amount = [1 for _ in range(len(A))]

        for i, a in enumerate(A):
            spl = a.split("|")
            winning = spl[0].split(" ")
            nums = spl[1].split(" ")
            counter = 0
            for w in winning.copy():
                if w == '':
                    continue
                if w in nums:
                    counter += 1

            for j in range(i+1, i+counter+1):
                A_amount[j] += A_amount[i]

        # print(A_amount)
        res = sum(A_amount)
        print(res)

p1()
p2()