print("********** Programmed by: **********")
print("********** Lyza Jorella R. Del Rosario **********")
print("********** BSCOE 2-2 **********")

#letters with corresponding asterisks for my nickname "Lyza"

alphabetletters = {
    
    'L': ['*    ', '*    ', '*    ', '*    ', '*****'],
    'Y': ['*   *', ' * * ', '  *  ', '  *  ', '  *  '],
    'Z': ['*****', '   * ', '  *  ', ' *   ', '*****'],
    'A': [' *** ', '*   *', '*****', '*   *', '*   *'],
}

string = "Lyza"

#print(len(string))
for i in range(5):

    for word in range(len(string)):
        current_word = string[word].upper()
        #print(current_word)
        if word == len(string)-1 :
            print(alphabetletters[current_word][i])
        else :
            print(alphabetletters[current_word][i],end='  ')
