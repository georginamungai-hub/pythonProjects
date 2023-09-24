import random

computer = ['Rock','Paper','Scissors']
# def determineWinner():
#     # while counter < 3:
#         player_turn = input('Enter a choice (Rock, Paper, Scissors): ')
#         computer_turn = random.choice(computer)
#         print("The Computer's Choice:",computer_turn)
#         print("The Player's Choice:", player_turn)

#         if (player_turn == computer_turn):
#             return ('TIE')
#         elif(player_turn == 'Rock'):
#             if (computer_turn == 'Paper'):
#                 return('THE COMPUTER WINS')
#             else:
#                 return('YOU WIN')
#         elif(player_turn == 'Scissors'):
#             if(computer_turn == 'Rock'):
#                 return('THE COMPUTER WINS')
#             else:
#                 return('YOU WIN')
#         elif(player_turn == 'Paper'):
#             if(computer_turn == 'Scissors'):
#                 return('THE COMPUTER WINS')
#             else:
#                 return('YOU WIN')        
#         # counter =+ 1
#         # break

# print(determineWinner()) 

def determineWinner():
    playerPoints = 0
    computerPoints = 0
    if (player_turn == computer_turn):
            return ('No Point Awarded')
    elif(player_turn == 'Rock'):
        if (computer_turn == 'Paper'):
            computerPoints = (computerPoints + 1)
            return (computerPoints, 'Point for the Computer')
        else:
            playerPoints = (playerPoints + 1)
            return (playerPoints,'Point for the Player')
    elif(player_turn == 'Scissors'):
        if(computer_turn == 'Rock'):
            computerPoints = (computerPoints + 1)
            return (computerPoints, 'Point for the Computer')
        else:
            playerPoints = (playerPoints + 1)
            return (playerPoints,'Point for the Player')
    elif(player_turn == 'Paper'):
        if(computer_turn == 'Scissors'):
            computerPoints = (computerPoints + 1)
            return (computerPoints, 'Point for the Computer')
        else:
            playerPoints = (playerPoints + 1)  
            return (playerPoints,'Point for the Player')



counter = 0
while counter < 5:
    counter += 1
    player_turn = input('Enter a choice (Rock, Paper, Scissors): ')
    computer_turn = random.choice(computer)
    print("The Computer's Choice:",computer_turn)
    print("The Player's Choice:", player_turn)      
    print(determineWinner())