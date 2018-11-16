w_dict = {}

def letter_histogram(word):
    w_lst = list(word.split(" "))
    x = 0

    for i in w_lst:
        if (i not in w_dict):
            w_dict[i] = ["1"]
            x += 1
        elif (i in w_dict):
            w_dict[i] = ["2"]
            x += 0
    print (w_dict)

in_p = input("Type in a sentence > ")
letter_histogram(in_p)