#scrabblegame


points = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}


def scrabbleone(playerone):
    totalone = 0
    for x in playerone:
        totalone += points [(x)]
    return totalone


def scrabbletwo(playertwo):
    totaltwo = 0
    for y in playertwo:
        totaltwo += points [(y)]
    return totaltwo


def winner(totalone, totaltwo):
    if totalone > totaltwo:
        print('Player one wins!')
    elif totalone < totaltwo:
        print("Player two wins!")
    else:
        print("It is a tie!")
    

loop = True
while loop:
    ques = str(input('Do you want to play scrabble with your friend? Yes or no?:')).lower()
    if ques == 'yes':
        playerone = str(input('Player 1:')).lower()
        playertwo = str(input('Player 2:')).lower()
        totalone = scrabbleone(playerone)
        totaltwo = scrabbletwo(playertwo)
        winner(totalone,totaltwo)
    elif ques == 'no':
        print('Thank you!')
        break
    else: 
        print('Invalid answer. Try again!')

    









