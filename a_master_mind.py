import random

def generate_rand_code():
    return [random.randint(1,6) for i in range( 4 )]

def find_correct_matches(code, guess):
    corretct_known_values = []

    # check if it is correct leter by leter
    for char_code, char_guess in zip(code, guess):
        is_correct = char_code == char_guess;

        if is_correct :
            corretct_known_values.append(char_guess)

    return corretct_known_values
        


def count_matching_members(code, guess):
    str_code = str(code)
    str_guess = str(guess)

    matching_count = 0
    for element in str_code:
        if element in str_guess:
            matching_count += 1

    return matching_count

def generate_guess(digits = 4):
    guess = []
    for a in range(1, 7):
        for b in range(1, 7):
            for c in range(1,7):
                for d in range(1,7):
                    guess.append([a,b,c,d])

    return guess

def generate_hints(code, guess):
    first_hint = find_correct_matches(code, guess)
    second_hint = count_matching_members(code, guess) - len(first_hint)

    return first_hint, second_hint




def a_master_mind_code_maker():

    try_right = 12
    remained_try_right = try_right

    # generate rand code:
    code = generate_rand_code(4)
    int_code = int("".join(map(str, code)))

    # main loop
    for trying in range(1, try_right + 1):

        is_win = None
        guess = input("Enter your guess as int: ")
        guess = [int(digit) for digit in str(guess)] # prepare it for zip()

        # prepare first hint
        corretct_known_values = find_correct_matches(code, guess)

        # prepare second hint
        second_hint = count_matching_members(int_code, guess) - len(corretct_known_values)

        # check if it is a win
        if len(corretct_known_values) == 4:
            print("You won!! 🎉")
            is_win = True
            break
        else :
            print(f"first hint: {len(corretct_known_values)}, second hint: {second_hint}")
            remained_try_right -= 1
        
        if remained_try_right <= 0:
            is_win = False
        
        if not is_win and not is_win == None:
            print(f"you lost! code was: {int_code}")


def a_master_mind_code_breaker(code):
    try_right = 12

    guesses = generate_guess()

    for trying in range(1, try_right + 1):

        guess = random.choice(guesses)

        if guess == code:
            print(f"found right value: {int_guess}")
            break

        first_hint, second_hint = generate_hints(code, guess)

        guesses = [
            guess for guess in guesses
            if generate_hints(code, guess) == (first_hint, second_hint)
        ]

        print(f"trying guess: {guess}")

    print(f"failed, code: {code}")

        

        
code = generate_rand_code()
print(code)

a_master_mind_code_breaker(code)