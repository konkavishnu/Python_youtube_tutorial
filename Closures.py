# Closure is a function having access to the scope of its parent function after the parent function has returned


def parent_func(person):
    coins = 3  # --> this will be manipulated by the child method below and will have the updated value in the memory each time when it is accessed

    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left")
        elif coins == 1 :
            print("\n" + person + " has " + str(coins) + " coin left")
        else:
            print("\n" + person + " is out of coins ")

    return play_game


tommy = parent_func("Tommy")
jenny = parent_func("Jenny")

tommy()
jenny()
tommy()
