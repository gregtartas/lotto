import random

def lotto():
    for i in range (1000):
        lotto_list = []
        for i in range(6):
            number = random.randint(1, 49)
            if number not in lotto_list:
                lotto_list.append(number)


        list_P = set([1, 7, 13, 18, 26, 44])

        set (lotto_list) | list_P
        set (lotto_list) - list_P
        bingo = set(lotto_list)& list_P
        len(bingo)
        print len(bingo)




                
lotto()


