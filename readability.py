#readability
    
text = str(input("Input a text:"))
#x for x essentially means "for each character x in text"
letters = len([x for x in text if x.isalpha()])


words = len(text.split())

pun = ["?", ".", '!']
sentence = sum(text.count(p) for p in pun)

L = (letters/words)*100
S = (sentence/words)*100
cole = (0.0588 * L) - (0.296 * S) - 15.8
rcole = round(cole)


if rcole < 1:
    print("Before Grade 1.")
elif rcole >= 16:
    print('Grade 16+')
elif rcole == 2:
    print("Grade 2")
elif rcole == 3:
    print("Grade 3")
elif rcole == 4:
    print("Grade 4")
elif rcole == 5:
    print("Grade 5")
elif rcole == 6:
    print("Grade 6")
elif rcole == 7:
    print("Grade 7")
elif rcole == 8:
    print("Grade 8")
elif rcole == 9:
    print("Grade 9")
elif rcole == 10:
    print("Grade 10")
elif rcole == 11:
    print("Grade 11")
elif rcole == 12:
    print("Grade 12")
elif rcole == 13:
    print("Grade 13")
elif rcole == 14:
    print("Grade 14")
elif rcole == 15:
    print("Grade 15")
elif rcole == 1:
    print("Grade 1")