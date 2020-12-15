import random 

def game():
    user = input("Choose one \n 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer: 
        return("It is a tie")

    if is_winner(user, computer):
        return("You are the winner")
    
    return("Computer won!") 

def is_winner(player, comp):
    # returns true only if player wins the game
    # r > s, s > p, p > r
    if (player == 'r' and comp == 's') or (player == 's' and comp == 'p') \
        or (player == 'p' and comp == 'r'):
        return True
          
print(game())
