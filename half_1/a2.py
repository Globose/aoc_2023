# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

def p1():
    with open('data/a2.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        for i, s in enumerate(file):
            ok = True
            game = s.split(":")
            turns = game[1].split(";")
            for t in turns:
                parts = t.split(",")
                for p in parts:
                    ps = p[1:].split(" ")
                    color = ps[1].strip("\n")
                    value = (int)(ps[0])

                    if color == 'blue' and value > 14:
                        ok = False
                    if color == 'green' and value > 13:
                        ok = False
                    if color == 'red' and value > 12:
                        ok = False
            if ok:
                sum += i+1
        print(sum)

def p2():
    with open('data/a2.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        for s in file:
            game = s.split(":")
            turns = game[1].split(";")
            min_blue = 0
            min_red = 0
            min_green = 0

            for t in turns:
                parts = t.split(",")
                for p in parts:
                    ps = p[1:].split(" ")
                    color = ps[1].strip("\n")
                    value = (int)(ps[0])

                    if color == 'blue':
                        min_blue = max(min_blue, value)
                    if color == 'green':
                        min_green = max(min_green, value)
                    if color == 'red':
                        min_red = max(min_red, value)
            sum += min_blue*min_green*min_red
        print(sum)

p1()
p2()

