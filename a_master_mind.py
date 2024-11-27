import random

def a_master_mind():
    try_right = 12

    remained_try_right = try_right

    # generate rand code:
    code = [random.randint(1,6) for i in range(4)]

    int_code = int("".join(map(str, code)))

    # print(code)

    # main loop
    for try_right in range(1, try_right + 1):

        is_win = None

        # logic
        guess = input("Enter your guess as int: ") #temprorary, we will change it to user input later
        guess = [int(digit) for digit in str(guess)]

        correct_guess_counter = 0

        # check if it is correct letter by letter
        for char_code, char_guess in zip(code, guess):
            is_correct = char_code == char_guess;

            if is_correct :
                correct_guess_counter += 1

        # check if it is a win
        if correct_guess_counter == 4:
            correct_guess_counter = 0
            print("You won!! 🎉")
            is_win = True
            break
        else :
            print(correct_guess_counter)
            correct_guess_counter = 0

            remained_try_right -= 1
        
        if remained_try_right <= 0:
            is_win = False
        
        if not is_win and not is_win == None:
            print(f"you lost! code was: {int_code}")


a_master_mind()