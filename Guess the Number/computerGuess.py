import random 

def guess(x): 
    min = 1
    max = x
    feedback = ""
    while feedback != "C": 

        if min != max:
            guess = random.randint(min, max)
        else:
            guess = max
        
        feedback = input(f"Is {guess} too high, too low, or correct? (H/L/C)").upper()

        if feedback == "H":
            max = guess - 1
        elif feedback == "L":
            min = guess + 1
            
    print(f"The computer guessed the number {guess} correctly.")

guess(30)
