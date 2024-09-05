def add(numb1, numb2):
    return numb1+numb2
def sub(numb1, numb2):
    return numb1-numb2
def multiply(numb1, numb2):
    return numb1*numb2
def divide(numb1, numb2):
    return numb1/numb2

numb1 = float(input ("Put a number:"))
numb2 = float(input ("Put another number:"))

loop = True
while loop:
    operator = (input ("Choose an operator from +, -, *, / now:"))
    if operator == '+':
    
     answer = add(numb1,numb2)
     print(answer)
     break

    elif operator == '-':
    
     answer = sub(numb1,numb2)
     print(answer)
     break
     
    elif operator == '*':
    
     answer = multiply(numb1,numb2)
     print(answer)
     break
     
    elif operator == '/':
    
     answer = divide(numb1,numb2)
     print(answer)
     break
    elif operator != ('+', '-','*','/'):
     print("Invalid! Try again!")

while loop:
 ques = str(input("Do you want to put another number? Yes or no?")).lower()

 if ques == 'yes':
  numb3 = float(input ("Put another number:"))
  while loop:
   operator = (input ("Choose an operator from +, -, *, / now:"))
   if operator == '+':
        
     ans = add(answer, numb3)
     print(ans)
     break

   elif operator == '-':
 
     ans = sub(answer, numb3)
     print(ans)
     break
     
   elif operator == '*':
    
     ans = multiply(answer, numb3)
     print(ans)
     break
     
   elif operator == '/':
     
     ans = divide(answer, numb3)
     print(ans)
     break
    
   elif operator != ('+', '-','*','/'):
     print("Invalid! Try again!")

  continue
 
 elif ques == 'no':
    print ("Okay, thank you!")
    break

 elif ques != ('no','yes'):
   print('Invalid answer. Try again!')
   

 
