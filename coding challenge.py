"""You have a number pad of 10 numbers, numbered 0-9. Write a function
 to find the 4-digit PIN that unlocks the number pad in a brute-force fashion.

 The user will create the pin that the program has to guess"""


def check_length():
    """
    This function will test to see if the PIN has a length of 4 digits
    :return: pin with length of 4 digits
    """
    p_bool = True
    while p_bool:
        pin = str(input("Test a 4-digit PIN: \n"))
        if len(pin) == 4:
            p_bool = False
        else:
            print("Error: The PIN is not 4 digits!\nTry again. \n")
    return pin


def print_pin(pin):
    """
    This function will properly format the PIN if it is less than 1000
    :param pin: int PIN guess
    :return: string PIN
    """
    if pin in range(0, 10):
        return "000" + str(pin)

    if pin in range(10, 100):
        return "00" + str(pin)

    if pin in range(100, 1000):
        return "0" + str(pin)

    if pin in range(1000, 10000):
        return str(pin)


def check_pin(guess):
    """
    This function will guess the user's pin in a brute-force fashion
    :param guess: 4 digit int PIN
    :return: True if correct PIN
    """
    guess = int(guess)
    for i in range(0000, 10000):
        if i == guess:
            p_guess = print_pin(i)
            print("The correct PIN is: " + p_guess + "!\n")
            return True
        else:
            p_guess = print_pin(i)
            print("The system guessed: " + p_guess + ", but that is incorrect.\n")
            i += 1


# Ask user for the PIN number
print("This program will test a 4 digit PIN in a brute-force fashion. \n")
user_pin = check_length()
if check_pin(user_pin):
    print("END PROGRAM")
