#pokemongen1basic
grass = ['bulbasaur', 'ivysaur','venasaur','oddish','gloom', 'vileplume','paras','parasect','bellsprout','weepinbell','victreebel','exeggcute','exeggutor','tangela']
fire = ['charmander','charmeleon','charizard','vulpix','ninetales','growlithe','arcanine','ponyta','rapidash','magmar','flareon','moltres']
water = ['squirtle','wartotle','blastoise','psyduck','golduck','poliwag','poliwhirl','poliwarth','tentacool','tentacruel','slowpoke','slowbro','seel','dewgong','shellder','colyster','krabby','kingler','horsea','seadra','goldeen','seaking','staryu','starmie','magikarp','gyarados','lapras','vaporeon','omanyte','omastar','kabuto','kabutops']
bug = ['caterpie','metapod','butterfree','weedle','kakuna','beedrill','venonat','venomoth','scyther','pinsir']
normal = ['pidgey','pidgeotto','pidgeot','rattata','raticate','spearow','fearow','jigglypuff','wigglytuff','meowth','persian','farfetchd','doduo',
          'dodrio','lickitung','chansey','kangaskhan','tauros','ditto','eevee','porygon','snorlax']
poison = ['ekans','arbok','nidorina','nidoqueen','nidorino','nidoking','zubat','golbat','grimer','muk','koffing','weezing']
fairy = ['clefairy','clefable','mr.mime']
ice = ['articuno']
ghost = ['gastly','haunter','gengar']
dragon = ['dragonair','dragonite','dratini']
electro = ['pikachu','raichu','magnemite','magneton','voltrob','electrode','electabuzz','jolteon','zapdos',]
fight = ['mankey','primeape','machop','machoke','machamp','hitmonlee','hitmonchan',]
psycho = ['abra','kadabra','alakazam','drowzee','hypno','jynx','mew','mewtwo',]
ground = ['sandshrew','sandslash','diglett','dugtrio','geodude','graveler','golem','onix','cubone','marowak','rhydon','rhyhorn']

z = ['bulbasaur', 'ivysaur','venasaur','oddish','gloom', 'vileplume','paras','parasect','bellsprout','weepinbell','victreebel','exeggcute','exeggutor','tangela', 'charmander','charmeleon','charizard','vulpix','ninetales','growlithe','arcanine','ponyta','rapidash','magmar','flareon','moltres','squirtle','wartotle','blastoise','psyduck','golduck','poliwag','poliwhirl','poliwarth','tentacool','tentacruel','slowpoke','slowbro','seel','dewgong','shellder','colyster','krabby','kingler','horsea','seadra','goldeen','seaking','staryu','starmie','magikarp','gyarados','lapras','vaporeon','omanyte','omastar','kabuto','kabutops','caterpie','metapod','butterfree','weedle','kakuna','beedrill','venonat','venomoth','scyther','pinsir','pidgey','pidgeotto','pidgeot','rattata','raticate','spearow','fearow','jigglypuff','wigglytuff','meowth','persian','farfetchd','doduo','dodrio','lickitung','chansey','kangaskhan','tauros','ditto','eevee','porygon','snorlax','ekans','arbok','nidorina','nidoqueen','nidorino','nidoking','zubat','golbat','grimer','muk','koffing','weezing','clefairy','clefable','mr.mime','articuno','gastly','haunter','gengar','dragonair','dragonite','dratini','pikachu','raichu','magnemite','magneton','voltrob','electrode','electabuzz','jolteon','zapdos', 'mankey','primeape','machop','machoke','machamp','hitmonlee','hitmonchan','abra','kadabra','alakazam','drowzee','hypno','jynx','mew','mewtwo','sandshrew','sandslash','diglett','dugtrio','geodude','graveler','golem','onix','cubone','marowak','rhydon','rhyhorn']

def pokelist(a):
          if a == 'yes':
            print (z)
          elif a == 'no':
            return exit
          else:
            print('Error. Try again!')

def quesone():
    loop = True
    while loop:
        a = str(input('Do you want to check the pokemon list? Yes or no?:')).lower()
        result = pokelist(a)
        if result == exit:
             print('Thanks! Enjoy playing!')
             break

def questwo():
     loop = True
     while loop:
          x = str(input('Player 1! Choose your pokemon!:')).lower()
          if x in z:
               print(x)
               break
          else:
               print('Error. Try again! Maybe check the spelling of your pokemon.')
               
     
     loop = True
     while loop:
          y = str(input('Player 2! Choose your pokemon!:')).lower()
          if y in z:
               print(y)
               break
          else:
               print('Error. Try again! Maybe check the spelling of your pokemon.')
               
     playone(x,y)

def playone(x,y):
     if x in fire:
          gamefire(y)
     elif x in water:
          gamewater(y)
     elif x in grass:
          gamegrass(y)
     elif x in bug:
          gamebug(y)
     elif x in normal:
          gamenormal(y)
     elif x in poison:
          gamepoison(y)
     elif x in fairy:
          gamefairy(y)
     elif x in ice:
          gameice(y)
     elif x in ghost:
          gameghost(y)
     elif x in dragon:
          gamedragon(y)
     elif x in electro:
          gameelectro(y)
     elif x in fight:
          gamefight(y)
     elif x in psycho:
          gamepsycho(y)
     elif x in ground:
          gameground(y)

def gamefire(y):
    if y in water:
          print('Player 2 wins!')
    elif y in fire:
          print('It is a tie!')
    elif y in grass:
         print('Player 1 wins!')
    elif y in bug:
         print('Player 1 wins!')
    elif y in normal:
         print('Player 2 wins!')
    elif y in poison:
         print('Player 2 wins!')
    elif y in fairy:
         print('Player 2 wins!')
    elif y in ice:
         print('Player 1 wins!')
    elif y in ghost:
         print('Player 1 wins!')
    elif y in dragon:
         print('Player 2 wins!')
    elif y in electro:
         print('Player 2 wins!')
    elif y in fight:
         print('Player 1 wins!')
    elif y in psycho:
         print('Player 2 wins!')
    elif y in ground:
         print('Player 2 wins!')
     
def gamewater(y):
    if y in fire:
         print('Player 1 wins!')
    elif y in water:
          print('It is a tie!')
    elif y in grass:
         print('Player 2 wins!')
    elif y in bug:
         print('Player 2 wins!')
    elif y in normal:
         print('Player 1 wins!')
    elif y in poison:
         print('Player 1 wins!')
    elif y in fairy:
         print('Player 2 wins!')
    elif y in ice:
         print('Player 2 wins!')
    elif y in ghost:
         print('Player 2 wins!')
    elif y in dragon:
         print('Player 1 wins!')
    elif y in electro:
         print('Player 2 wins!')
    elif y in fight:
         print('Player 1 wins!')
    elif y in psycho:
         print('Player 2 wins!')
    elif y in ground:
         print('Player 1 wins!')

def gamegrass(y):
    if y in fire:
         print('Player 2 wins!')
    elif y in water:
         print('Player 1 wins!')
    elif y in grass:
         print('It is a tie!')
    elif y in bug:
         print('Player 2 wins!')
    elif y in normal:
         print('Player 1 wins!')
    elif y in poison:
         print('Player 2 wins!')
    elif y in fairy:
         print('Player 2 wins!')
    elif y in ice:
         print('Player 2 wins!')
    elif y in ghost:
         print('Player 2 wins!')
    elif y in dragon:
         print('Player 1 wins!')
    elif y in electro:
         print('Player 2 wins!')
    elif y in fight:
         print('Player 2 wins!')
    elif y in psycho:
         print('Player 2 wins!')
    elif y in ground:
         print('Player 1 wins!')

def gamebug(y):
    if y in fire:
         print('Player 2 wins!')
    elif y in water:
         print('Player 1 wins!')
    elif y in grass:
         print('Player 1 wins!')
    elif y in bug:
         print('It is a tie!')
    elif y in normal:
         print('Player 1 wins!')
    elif y in poison:
         print('Player 1 wins!')
    elif y in fairy:
         print('Player 2 wins!')
    elif y in ice:
         print('Player 1 wins!')
    elif y in ghost:
         print('Player 2 wins!')
    elif y in dragon:
         print('Player 2 wins!')
    elif y in electro:
         print('Player 1 wins!')
    elif y in fight:
         print('Player 1 wins!')
    elif y in psycho:
         print('Player 1 wins!')
    elif y in ground:
         print('Player 2 wins!')

def gamenormal(y):
     if y in fire:
         print('Player 2 wins!')
     elif y in water:
         print('Player 2 wins!')
     elif y in grass:
         print('Player 2 wins!')
     elif y in bug:
         print('Player 2 wins!')
     elif y in normal:
         print('It is a tie!')
     elif y in poison:
         print('Player 2 wins!')
     elif y in fairy:
         print('Player 2 wins!')
     elif y in ice:
         print('Player 2 wins!')
     elif y in ghost:
         print('Player 2 wins!')
     elif y in dragon:
         print('Player 2 wins!')
     elif y in electro:
         print('Player 2 wins!')
     elif y in fight:
         print('Player 2 wins!')
     elif y in psycho:
         print('Player wins!')
     elif y in ground:
         print('Player 2 wins!')

def gamepoison(y):
     if y in fire:
         print('Player 1 wins!')
     elif y in water:
         print('Player 2 wins!')
     elif y in grass:
         print('Player 1 wins!')
     elif y in bug:
         print('Player 2 wins!')
     elif y in normal:
         print('Player 1 wins!')
     elif y in poison:
         print('It is a tie!')
     elif y in fairy:
         print('Player 1 wins!')
     elif y in ice:
         print('Player 2 wins!')
     elif y in ghost:
         print('Player 1 wins!')
     elif y in dragon:
         print('Player 1 wins!')
     elif y in electro:
         print('Player 1 wins!')
     elif y in fight:
         print('Player 1 wins!')
     elif y in psycho:
         print('Player 2 wins!')
     elif y in ground:
         print('Player 2 wins!')

def gamefairy(y):
     if y in fire:
         print('Player 1 wins!')
     elif y in water:
         print('Player 1 wins!')
     elif y in grass:
         print('Player 1 wins!')
     elif y in bug:
         print('Player 1 wins!')
     elif y in normal:
         print('Player 1 wins!')
     elif y in poison:
         print('Player 2 wins!')
     elif y in fairy:
         print('It is a tie!')
     elif y in ice:
         print('Player 1 wins!')
     elif y in ghost:
         print('Player 1 wins!')
     elif y in dragon:
         print('Player 1 wins!')
     elif y in electro:
         print('Player 1 wins!')
     elif y in fight:
         print('Player 1 wins!')
     elif y in psycho:
         print('Player 1 wins!')
     elif y in ground:
         print('Player 1 wins!')

def gameice(y):
     if y in fire:
         print('Player 1 wins!')
     elif y in water:
         print('Player 1 wins!')
     elif y in grass:
         print('Player 1 wins!')
     elif y in bug:
         print('Player 2 wins!')
     elif y in normal:
         print('Player 1 wins!')
     elif y in poison:
         print('Player 1 wins!')
     elif y in fairy:
         print('Player 2 wins!')
     elif y in ice:
         print('It is a tie!')
     elif y in ghost:
         print('Player 2 wins!')
     elif y in dragon:
         print('Player 1 wins!')
     elif y in electro:
         print('Player 2 wins!')
     elif y in fight:
         print('Player 1 wins!')
     elif y in psycho:
         print('Player 1 wins!')
     elif y in ground:
         print('Player 1 wins!')

def gameghost(y):
     if y in fire:
         print('Player 2 wins!')
     elif y in water:
         print('Player 1 wins!')
     elif y in grass:
         print('Player 1 wins!')
     elif y in bug:
         print('Player 1 wins!')
     elif y in normal:
         print('Player 1 wins!')
     elif y in poison:
         print('Player 2 wins!')
     elif y in fairy:
         print('Player 2 wins!')
     elif y in ice:
         print('Player 1 wins!')
     elif y in ghost:
         print('It is a tie!')
     elif y in dragon:
         print('Player 1 wins!')
     elif y in electro:
         print('Player 1 wins!')
     elif y in fight:
         print('Player 1 wins!')
     elif y in psycho:
         print('Player 1 wins!')
     elif y in ground:
         print('Player 1 wins!')

def gamedragon(y):
     if y in fire:
         print('Player 1 wins!')
     elif y in water:
         print('Player 2 wins!')
     elif y in grass:
         print('Player 2 wins!')
     elif y in bug:
         print('Player 1 wins!')
     elif y in normal:
         print('Player 1 wins!')
     elif y in poison:
         print('Player 2 wins!')
     elif y in fairy:
         print('Player 2 wins!')
     elif y in ice:
         print('Player 2 wins!')
     elif y in ghost:
         print('Player 2 wins!')
     elif y in dragon:
         print('It is a tie!')
     elif y in electro:
         print('Player 2 wins!')
     elif y in fight:
         print('Player 1 wins!')
     elif y in psycho:
         print('Player 1 wins!')
     elif y in ground:
         print('Player 1 wins!')

def gameelectro(y):
     if y in fire:
         print('Player 1 wins!')
     elif y in water:
         print('Player 1 wins!')
     elif y in grass:
         print('Player 1 wins!')
     elif y in bug:
         print('Player 2 wins!')
     elif y in normal:
         print('Player 1 wins!')
     elif y in poison:
         print('Player 2 wins!')
     elif y in fairy:
         print('Player 2 wins!')
     elif y in ice:
         print('Player 1 wins!')
     elif y in ghost:
         print('Player 2 wins!')
     elif y in dragon:
         print('Player 1 wins!')
     elif y in electro:
         print('It is a tie!')
     elif y in fight:
         print('Player 1 wins!')
     elif y in psycho:
         print('Player 2 wins!')
     elif y in ground:
         print('Player 2 wins!')

def gamefight(y):
     if y in fire:
         print('Player 2 wins!')
     elif y in water:
         print('Player 2 wins!')
     elif y in grass:
         print('Player 1 wins!')
     elif y in bug:
         print('Player 2 wins!')
     elif y in normal:
         print('Player 1 wins!')
     elif y in poison:
         print('Player 2 wins!')
     elif y in fairy:
         print('Player 2 wins!')
     elif y in ice:
         print('Player 2 wins!')
     elif y in ghost:
         print('Player 2 wins!')
     elif y in dragon:
         print('Player 2 wins!')
     elif y in electro:
         print('Player 2 wins!')
     elif y in fight:
         print('It is a tie!')
     elif y in psycho:
         print('Player 2 wins!')
     elif y in ground:
         print('Player 1 wins!')

def gamepsycho(y):
     if y in fire:
         print('Player 1 wins!')
     elif y in water:
         print('Player 1 wins!')
     elif y in grass:
         print('Player 1 wins!')
     elif y in bug:
         print('Player 2 wins!')
     elif y in normal:
         print('Player 1 wins!')
     elif y in poison:
         print('Player 1 wins!')
     elif y in fairy:
         print('Player 2 wins!')
     elif y in ice:
         print('Player 2 wins!')
     elif y in ghost:
         print('Player 2 wins!')
     elif y in dragon:
         print('Player 2 wins!')
     elif y in electro:
         print('Player 1 wins!')
     elif y in fight:
         print('Player 1 wins!')
     elif y in psycho:
         print('It is a tie!')
     elif y in ground:
         print('Player 1 wins!')

def gameground(y):
     if y in fire:
         print('Player 1 wins!')
     elif y in water:
         print('Player 2 wins!')
     elif y in grass:
         print('Player 2 wins!')
     elif y in bug:
         print('Player 1 wins!')
     elif y in normal:
         print('Player 1 wins!')
     elif y in poison:
         print('Player 1 wins!')
     elif y in fairy:
         print('Player 2 wins!')
     elif y in ice:
         print('Player 2 wins!')
     elif y in ghost:
         print('Player 2 wins!')
     elif y in dragon:
         print('Player 2 wins!')
     elif y in electro:
         print('Player 1 wins!')
     elif y in fight:
         print('Player 2 wins!')
     elif y in psycho:
         print('Player 2 wins!')
     elif y in ground:
         print('It is a tie!')




loop = True
while loop:
    ques = str(input('Hello! Do you want to play pokemon with your friend? Yes or no?:')).lower()
    if ques == 'yes':
          quesone()
          questwo()
    elif ques == 'no':
         print('Thanks! Have a great day!')
         break
    else:
         print('Error! Try again!')