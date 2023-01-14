def hang_man(word):
    new_word = ""
    count_num = len(word)
    for x in range(count_num):
        new_word = new_word +"_"

    print(new_word)
    counter_check = 0
    letter = input("write letter ")
    list1 = []
    while counter_check != count_num :
        for y in range(count_num-1):
            if word[y] == letter:

                new_word = new_word.replace(new_word[y], letter)

                print(new_word)
                counter_check = counter_check +1
            else:
                continue
        letter = input("write letter ")


hang_man("sas")
#multipile correct letter + number of loops running