import random

def hangman(word_list):
    """
    Play Hangman
    """
    word = word_list[random.randint(0,len(word_list)-1)]
    wrong = 0
    stages = ["",
              "_________          ",
              "|        |         ",
              "|        o         ",
              "|       /|\        ",
              "|       / \        ",
              "|                  "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to the Hangman")
    print(" ".join(board))
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Please guess one figure."
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose! Answer is {}.".format(word))


#main
word_list = ["cat","dog","snake","hello"]
hangman(word_list)
