
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
#Add all digits in the odd places from right to left. so we need to reverse the string at first
    cardno = cardno[::-1]
#this will reverse the string and assign it from the opposite
    for x in cardno[::2]:
#this is repeat over every second digit within our cardno
        sum_odd += int(x)
#The plus-equals operator += provides a convenient way to add a value to an existing variable and assign the new value back to the same variable.
#Double every second digit from right to left.
#(If result is a two-digit number, add the two-digit number together to get a single digit.)
    for x in cardno[1::2]:
        x = int(x)*2
        if x >= 10:
            sum_even += (1+ (x % 10))
 #the largest number here can be 18 as 9 is the largest number. so 18%10 is 8 and 8+1 is 9. 
        else:
            sum_even += int(x)
#Sum the totals of steps 2 & 3
    total = sum_odd + sum_even
# If sum is divisible by 10, the credit card number is valid
    if total % 10 == 0:
        print('VALID')
    else:
        print('INVALID')
        exit()

cardno = input("Put your card number:")
#Remove any '-' or ' '
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




