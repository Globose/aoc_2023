def p1():
    with open('data/a1.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        for s in file:
            dig1 = ""
            for i in range(len(s)):
                if (s[i].isdigit()):
                    dig1 += s[i]
                    break
            for i in range(len(s)-1, -1, -1):
                if (s[i].isdigit()):
                    dig1 += s[i]
                    break
            sum += (int)(dig1)
        print(sum)


def p2():
    with open('data/a2.txt', 'r', encoding='UTF-8') as file:
        # file = ["ftwonevbhlhlqhsix5dzfqgsone", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
        sum = 0
        valid = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        A = []
        for s in file:
            allDigits = []
            for i, d in enumerate(s):
                if d.isdigit():
                    allDigits.append((i,(int)(d)))

            for value, v in enumerate(valid):
                ind = s.find(v)
                if ind == -1:
                    continue
                allDigits.append((ind, value+1))

            for value, v in enumerate(valid):
                ind = s.rfind(v)
                if ind == -1:
                    continue
                allDigits.append((ind, value+1))


            allDigits.sort()
            dig1 = allDigits[0][1]
            dig2 = allDigits[-1][1]
            string = str(dig1)+str(dig2)
            sum += (int)(string)
            # print(allDigits)
            # print(s, dig1, dig2)
            A.append((s, int(str(dig1) + str(dig2))))
        print(sum)
        return A

p1()
p2()
