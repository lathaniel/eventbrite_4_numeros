import random

def output(text):
    print(text)

def match(x, y):
    # Compares two numbers, given as strings
    # Returns array with number of correct and regular digits
    bien = 0
    reg = 0

    for i in range(4):
        if str(x)[i] == str(y)[i]:
            bien += 1
        elif str(y)[i] in str(x):
            reg += 1
    
    return [bien, reg]

def verify_numero(num):
    # Make sure number is in range:
    if int(num) < 1234:
        return False
    
    # Make sure number has no repeated digits
    if len(str(num)) != len(set(str(num))):
        return False

    return True    

def generar_guess(dig1, dig2, dig3, dig4):
    num = ''
    num += dig1[random.randint(0, len(dig1) - 1)]
    num += dig2[random.randint(0, len(dig2) - 1)]
    num += dig3[random.randint(0, len(dig3) - 1)]
    num += dig4[random.randint(0, len(dig4) - 1)]
    return int(num)

def generar_numero(dig_list):
    # Generate number for user to guess
    num = ''

    for i in range(4):
        if i==0:
            # First digit cannot be zero
            while True:
                dig = dig_list[random.randint(0, len(dig_list) - 2)]
                if dig != 0:
                    break
        else:
            dig = dig_list[random.randint(0, len(dig_list) - 1)]
        num += dig 
        dig_list.remove(dig)
    
    return int(num)

def give_user_feedback(num, guess):
    m = match(num, guess)
    s = "Bien: %s\nRegular: %s" %(m[0], m[1])
    output(s)
    return m

def get_user_feedback(guess):
    s = 'Mi adivinanza es %s' %guess
    output(s)
    bien = int(input("Cuántos están bien?"))
    reg = int(input("Cuántos son regulares?"))
    return [bien, reg]

def player_guess():
    # PC Generates number
    dig_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # Make sure the guess is good:
    while True:
        num = generar_numero(dig_list)
        if verify_numero(num):
            break

    # Loop until user guesses number
    while True:
        # Ask user to make a guess
        s = "Enter a four-digit guess:"
        
        while True:
            output(s)
            guess = input()
            if verify_numero(guess):
                break

        give_user_feedback(num, guess)

        if match(num, guess) == [4,0]:
            # User Guessed number
            output("You Win!")
            break
def computer_guess():
    # User thinks of number
    s = "Think of a four-digit number"
    dig_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    # Loop until computer guesses number
    while True:
        # Computer makes a guess
        guess = generar_numero(dig_list)

        # Get user feedback
        fb = get_user_feedback(guess)

        # Update arrays based on user feedback
        if fb == [0,0]:
            for i in str(guess):
                dig_list.remove(i)
        elif fb == [4,0]:
            # Computer guessed number
            output("Thanks for playing")
            break



def main():
    #player_guess()

    computer_guess()

if __name__=="__main__":
    main()