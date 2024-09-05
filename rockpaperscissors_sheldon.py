
#Mode 1 = 'Computer mode'
#Mode 2 = 'Player 1 vs Player 2'

loop = True
while loop:
 ques = int(input("Please enter 1 for computer mode and 2 for player vs. player mode:"))
 if ques == 1:
  import random
  y = ['Paper', 'Spock']
  z = ['Scissor','Lizard']
  l = ['Rock','Spock']
  m = ['Lizard','Paper']
  n = ['Rock','Scissor']
  while loop:
    s = input("Choose one among Rock, Paper, Scissor, Lizard, Spock:").lower()
    if s == 'rock':
        print (random.choice(y))
        print('You lose!')
        break
    elif s == 'paper':
        print(random.choice(z))
        print ('You lose!')
        break
    elif s == 'scissor':
        print(random.choice(l)) 
        print('You lose!')
        break
    elif s == 'spock':
        print(random.choice(m))
        print('You lose!')
        break
    elif s == 'lizard':
        print(random.choice(n))
        print('You lose!')
        break
    elif s!= ('rock', 'paper','scissor', 'lizard','spock'):
        print('Invalid. Try again!')

 elif ques == 2:
  a = 'rock'
  b = 'paper'
  c = 'scissor'
  d = 'spock'
  e = 'lizard'
  while loop:
   x = str(input("Player 1 - Choose one among Rock, Paper, Scissor, Spock, and Lizard:")).lower()
   if x not in ['rock', 'paper', 'scissor', 'spock','lizard']:
        print('Invalid. Try again!')
   else:
       break
       
  loop = True
  while loop:
   y = str(input("Player 2 - Choose one among Rock, Paper, Scissor, Spock, and Lizard:")).lower()
   if y not in ['rock', 'paper', 'scissor', 'spock','lizard']:
        print('Invalid. Try again!')
   else:
        break

  loop = True
  while loop:
   if x == a and y == a:
        print("It's a tie!")
        break
       
   elif x == b and y == b:
        print("It's a tie!")
        break
       
   elif x == c and y == c:
        print("It's a tie!")
        break
 
   elif x == d and y == d:
        print("It's a tie!")
        break
 
   elif x == e and y == e:
        print("It's a tie!")
        break
       
   elif x == a and  y == b:
        print("Player 2 wins!")
        break
       
   elif x == a and y == c:
        print("Player 1 wins!")
        break
 
   elif x == a and y == d:
        print("Player 2 wins!")
        break
 
   elif x == a and y == e:
        print("Player 1 wins!")
        break
      
   elif x == b and y == a:
        print("Player 1 wins!")
        break
      
   elif x == b and y == c:
        print("Playeer 2 wins!")
        break
 
   elif x == b and y == d:
        print("Playeer 1 wins!")
        break
 
   elif x == b and y == e:
        print("Playeer 2 wins!")
        break
       
   elif x == c and y == b:
        print("Player 1 wins!")
        break
       
   elif x == c and y == a:
        print("Player 2 wins!")
        break
 
   elif x == c and y == d:
        print("Player 2 wins!")
        break
 
   elif x == c and y == e:
        print("Player 1 wins!")
        break
 
   elif x == d and y == a:
        print("Player 1 wins!")
        break
 
   elif x == d and y == b:
        print("Player 2 wins!")
        break
 
   elif x == d and y == c:
        print("Player 1 wins!")
        break
 
   elif x == d and y == e:
        print("Player 2 wins!")
        break
 
   elif x == e and y == a:
        print("Player 2 wins!")
        break

   elif x == e and y == b:
        print("Player 1 wins!")
        break

   elif x == e and y == c:
        print("Player 2 wins!")
        break

   elif x == e and y == d:
        print("Player 1 wins!")
        break
 elif ques != ['1','2']:
  print('Invalid! Try again.')
 break

