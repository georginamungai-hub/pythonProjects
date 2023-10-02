import random

wordBank = ['jam','kettle']

choice = random.choice(wordBank)
guesses = 0

def Jam(guesses):
    while guesses < 2:
        blank = ['-','-','-']
        print(blank)
        guess1 = input('Please enter the first Letter: ')
        if (guess1 == 'j'):
            blank[0]= 'j'
            print(blank)
        elif(guess1 == 'a'):
            blank[1]= 'a'
            print(blank)
        elif(guess1 == 'm'):
            blank[2]= 'm'
            print(blank)
        else:
            print(blank)
        guesses = guesses +1
        guess2 = input('Please enter the second Letter: ')
        if (guess2 == 'j'):
            blank[0]= 'j'
            print(blank)
        elif(guess2 == 'a'):
            blank[1]= 'a'
            print(blank)
        elif(guess2 == 'm'):
            blank[2]= 'm'
            print(blank)
        else:
            print(blank)
        guesses = guesses +1    
        guess3 = input('Please enter the third Letter: ')
        if (guess3 == 'j'):
            blank[0]= 'j'
            print(blank)
        elif(guess3 == 'a'):
            blank[1]= 'a'
            print(blank)
        elif(guess3 == 'm'):
            blank[2]= 'm'
            print(blank)
        else:
            print(blank)
    print('You Lose!')

def Kettle(guesses):
    while guesses <5:
        blank = ['-','-','-','-','-','-']
        print(blank)
        guess1 = input('Please enter the first Letter: ')
        if (guess1 == 'k'):
            blank[0]= 'k'
            print(blank)
        elif(guess1 == 'e'):
            blank[1]= 'e'
            print(blank)
        elif(guess1 == 't'):
            blank[2]= 't'
            print(blank)
        elif(guess1 == 't'):
            blank[3]= 't'
            print(blank)
        elif(guess1 == 'l'):
            blank[4]= 'l'
            print(blank)
        elif(guess1 == 'e'):
            blank[5]= 'e'
            print(blank)
        else:
            print(blank)
        guesses = guesses +1
        guess2 = input('Please enter the second Letter: ')
        if (guess2 == 'k'):
            blank[0]= 'k'
            print(blank)
        elif(guess2 == 'e'):
            blank[1]= 'e'
            print(blank)
        elif(guess2 == 't'):
            blank[2]= 't'
            print(blank)
        elif(guess2 == 't'):
            blank[3]= 't'
            print(blank)
        elif(guess2 == 'l'):
            blank[4]= 'l'
            print(blank)
        elif(guess2 == 'e'):
            blank[5]= 'e'
            print(blank)
        else:
            print(blank)
        guesses = guesses +1    
        guess3 = input('Please enter the third Letter: ')
        if (guess3 == 'k'):
            blank[0]= 'k'
            print(blank)
        elif(guess3 == 'e'):
            blank[1]= 'e'
            print(blank)
        elif(guess3 == 't'):
            blank[2]= 't'
            print(blank)
        elif(guess3 == 't'):
            blank[3]= 't'
            print(blank)
        elif(guess3 == 'l'):
            blank[4]= 'l'
            print(blank)
        elif(guess3 == 'e'):
            blank[5]= 'e'
            print(blank)
        else:
            print(blank)
        guesses = guesses +1
        guess4 = input('Please enter the fourth Letter: ')
        if (guess4 == 'k'):
            blank[0]= 'k'
            print(blank)
        elif(guess4 == 'e'):
            blank[1]= 'e'
            print(blank)
        elif(guess4 == 't'):
            blank[2]= 't'
            print(blank)
        elif(guess4 == 't'):
            blank[3]= 't'
            print(blank)
        elif(guess4 == 'l'):
            blank[4]= 'l'
            print(blank)
        elif(guess4 == 'e'):
            blank[5]= 'e'
            print(blank)
        else:
            print(blank)
        guesses = guesses +1    
        guess5 = input('Please enter the fifth Letter: ')
        if (guess5 == 'k'):
            blank[0]= 'k'
            print(blank)
        elif(guess5 == 'e'):
            blank[1]= 'e'
            print(blank)
        elif(guess5 == 't'):
            blank[2]= 't'
            print(blank)
        elif(guess5 == 't'):
            blank[3]= 't'
            print(blank)
        elif(guess5 == 'l'):
            blank[4]= 'l'
            print(blank)
        elif(guess5 == 'e'):
            blank[5]= 'e'
            print(blank)
        else:
            print(blank)
    print('You Lose!')

if (choice == 'jam'):
    Jam(guesses)
else:
    Kettle(guesses)




# def Jam1(guess1):
#     blank = ['-','-','-']
#     print(blank)
    # if (guess1 == 'j'):
    #     blank[0]= 'j'
    #     print(blank)
    # elif(guess1 == 'a'):
    #     blank[1]= 'a'
    #     print(blank)
    # elif(guess1 == 'm'):
    #     blank[2]= 'm'
    #     print(blank)
    # else:
    #     print(blank)
# def Jam2(guess2):
#     blank = ['-','-','-']
#     print(blank)
#     if (guess2 == 'j'):
#         blank[0]= 'j'
#         print(blank)
#     elif(guess2 == 'a'):
#         blank[1]= 'a'
#         print(blank)
#     elif(guess2 == 'm'):
#         blank[2]= 'm'
#         print(blank)
#     else:
#         print(blank)
# def Jam3(guess3):
#     blank = ['-','-','-']
#     print(blank)
#     if (guess3 == 'j'):
#         blank[0]= 'j'
#         print(blank)
#     elif(guess3 == 'a'):
#         blank[1]= 'a'
#         print(blank)
#     elif(guess3 == 'm'):
#         blank[2]= 'm'
#         print(blank)
#     else:
#         print(blank)

# guesses = 0
# guess1 = input('Please enter the first Letter: ')
# guess2 = input('Please enter the first Letter: ')
# guess3 = input('Please enter the first Letter: ')
# while guesses <3:
#     if(choice == 'jam'):
#         Jam1(guess1)
#         guesses = guesses +1
#         Jam2(guess2)
#         guesses = guesses +1
#         Jam3(guess3)
#     else:
#         break


        
    
    