w_dict = {}
punctuation = "'"'"'".,!?"

def letter_histogram(msg):
    word_list = list(msg.split(" "))

    for word in word_list:
        if (word not in w_dict):
            for char in word:
                if char in punctuation:
                    word = word.replace(char,"")
            w_dict[word] = 1
        elif (word in w_dict):
            w_dict[word] += 1
    print (w_dict)

in_p = input("Type in a sentence > ")
letter_histogram(in_p)