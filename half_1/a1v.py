from a1 import p3
def txt_to_list(file_name:str):
    numbers = []

    with open(file_name, 'r') as file:
        numbers = list(map(str, file.readlines()))
    # print(numbers)
    return numbers

def first_and_last(lst:list):
    total = 0
    row = 0
    A = []
    for item in lst:
        row += 1
        i = 0
        first = 0
        last = 0
        word = ""
        for letter in item:
            if letter.isnumeric() and i == 1:
                last = letter
            if letter.isnumeric() and i == 0:
                first = letter
                last = letter
                i += 1

            word += letter
            if num_check(word) and i == 1:
                last = num_check(word)
                word = ""
            if num_check(word) and i == 0:
                first = num_check(word)
                last = num_check(word)
                i += 1
                word = ""
        # print("row", row)
        # print(first, last)
        # print(int(str(first) + str(last)))
        total += int(str(first) + str(last))
        A.append((item,int(str(first) + str(last))))
    # print(total)
    return A

def num_check(string:str):
    if "one" in string:
        return 1
    if "two" in string:
        return 2
    if "three" in string:
        return 3
    if "four" in string:
        return 4
    if "five" in string:
        return 5
    if "six" in string:
        return 6
    if "seven" in string:
        return 7
    if "eight" in string:
        return 8
    if "nine" in string:
        return 9
    else:
        return False


if __name__ == "__main__":
    A = first_and_last(txt_to_list("data/a1.txt"))
    A2 = p3()
    for i in range(len(A)):
        if not A[i][1] == A2[i][1]:
            print(i, A[i], A2[i])