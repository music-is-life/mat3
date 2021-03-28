#def revword and decapilize:
def revword (word:str):
    word = word.lower()
    return word[::-1]
    

#now will do countword function witch counting in every line
#how much of the first word is:
    
def countword ():
    count = 0
    fhand = open('C:/Users/Orang/Desktop/Intro_Data_Science/Assigments/second_assigment/text.txt')
    count_word = fhand.readline()
    count_word = count_word.strip()
    for line in fhand:
        splitted = line.split()
        for word in splitted:
            if revword(word) == count_word:
                count += 1                
    return print(count+1)

