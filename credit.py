
def america(cardno):
        if len(cardno)== 15:
                print('AMEX')
        else:
            print("Not available!")
        
def mastercard(cardno):
        if len(cardno) == 16: 
                print('MASTERCARD')
        else:
            print("Not available!")

def visa(cardno):
        if len(cardno) == 13 or len(cardno) == 16:
            print('VISA')
        else:
            print("Not available!")

def checksum(cardno):
    sum_odd = 0
    sum_even = 0
    total = 0
    cardno = cardno[::-1]
    for x in cardno[::2]:
        sum_odd += int(x)
    for x in cardno[1::2]:
        x = int(x)*2
        if x >= 10:
        else:
            sum_even += int(x)
    total = sum_odd + sum_even
    if total % 10 == 0:
        print('VALID')
    else:
        print('INVALID')
        exit()

cardno = input("Put your card number:")
cardno = cardno.replace('-','')
cardno = cardno.replace(' ','')
checksum(cardno)
loop = True
while loop:
    ques = str(input('Do you want to know the type of card? Yes or No?: ')).lower()
    if ques == 'yes':
                if cardno.startswith("37"):
                    america(cardno) 
                    break
                elif cardno.startswith("34"):
                    america(cardno)
                    break
                elif cardno.startswith("51"):
                    mastercard(cardno)
                    break
                elif cardno.startswith("52"):
                    mastercard(cardno)
                    break
                elif cardno.startswith("53"):
                    mastercard(cardno)
                    break
                elif cardno.startswith("54"):
                    mastercard(cardno)
                    break
                elif cardno.startswith("55"):
                    mastercard(cardno)
                    break
                elif cardno.startswith("4"):
                    visa(cardno)
                    break
                elif cardno.startswith("4"):
                    visa(cardno)
                    break
                else:
                    print('Not available!')
                    break
    elif ques == 'no':
        print('Thank you!')
        break
    else:
         print('Error! Try again.')




