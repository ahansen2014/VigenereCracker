
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

vigenere = {
    'A' : ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
    'B' : ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A'],
    'C' : ['C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B'],
    'D' : ['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C'],
    'E' : ['E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D'],
    'F' : ['F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E'],
    'G' : ['G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F'],
    'H' : ['H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G'],
    'I' : ['I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H'],
    'J' : ['J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I'],
    'K' : ['K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J'],
    'L' : ['L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K'],
    'M' : ['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L'],
    'N' : ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M'],
    'O' : ['O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N'],
    'P' : ['P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'],
    'Q' : ['Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'],
    'R' : ['R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'],
    'S' : ['S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R'],
    'T' : ['T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S'],
    'U' : ['U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'],
    'V' : ['V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U'],
    'W' : ['W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V'],
    'X' : ['X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W'],
    'Y' : ['Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X'],
    'Z' : ['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
}

template = {'A':8.167, 'B':1.492, 'C':2.782, 'D':4.253, 'E':12.702, 'F':2.228, 'G':2.015, 'H':6.094, 'I':6.966,
            'J':0.153, 'K':0.772, 'L':4.025, 'M':2.406, 'N':6.749, 'O':7.507, 'P':1.929, 'Q':0.095, 'R':5.987,
            'S':6.327, 'T':9.056, 'U':2.758, 'V':0.978, 'W':2.361, 'X':0.150, 'Y':1.974, 'Z':0.074}

def findThreeLetterCombos(cipherString):
    '''
    This simple function starts with the first letter in the cipher string and simply grabs it and
    the next two letters to form a three letter combo.  It then checks to see if that combo has
    already been seen and if it has it increments the number of them by one.  If it is the first
    combo of it's type then it is recorded with an occurence of one.
    At the end of the function any combos that have occured only once are removed from the
    dictionary leaving only those combos that occured at least twice.
    :param cipherString: Find all the three letter combo in here
    :return: A dictionary with all the combos that occur more than once.
    '''
    threeLetterCombos = {} # All three letter combos will be recorded even if they only occur once

    for i in range(len(cipherString)-3): #From the beginning until 3 from the end
        # Make a three letter combo
        testCombo = ''
        testCombo += cipherString[i]
        testCombo += cipherString[i+1]
        testCombo += cipherString[i+2]
        '''
        Now look to see if we have seen this combo before
        If we have then increment the number of times
        we have seen it.  Otherwise, this is the first
        time.
        '''
        if testCombo in threeLetterCombos:
            threeLetterCombos[testCombo] += 1
        else:
            threeLetterCombos[testCombo] = 1
    '''
    Now go through all the three letter combos
    and delete the ones that only occur once
    '''
    for combo,occurence in threeLetterCombos.items():
        if occurence == 1:
            del threeLetterCombos[combo]

    return threeLetterCombos # Return the cleaned list.  Only recurring combinations are returned.


def findIntervals(listOfCombos, cipherString):
    repeats = {}
    '''
    The repeats dictionary will contain each three letter combination
    and the index of that combination in the cipherstring.
    The structure of each element in the dictionary is key:[value, value, etc]
    '''
    for combo,occurences in listOfCombos.items(): # For each 3 letter combo
        pointer = 0 # This points (initially) to the start of the cipher string
        while pointer < len(cipherString)-2: # While there are still 3 letter combos to check
            ''''
            The following code block looks for the three letter combination
            in the cipher string.  It simply counts how many matches there
            are between the combination and the current section of the
            cipher string.  Three matches means the code has found the
            combination in the cipher string and the index is appended
            the the list of indexes for that combination
            '''
            matches = 0
            for i in range(3):
                if combo[i] == cipherString[pointer + i]:
                    matches += 1
            if matches == 3:
                if combo in repeats:
                    repeats[combo].append(pointer)
                else:
                    repeats[combo] = [pointer]
            pointer += 1
    '''
    The sets of indexes is now converted to a list of absolute intervals by
    subtracting the smaller pointer from the next larger pointer for all of
    the combinations.
    If the resulting interval has not been seen before it is added to the
    intervals list.  If the interval has been seen before it is ignored.
    The final result is a list of unique intervals between combinations.
    '''
    intervals = []
    for substring,data in repeats.items():
        interval = data[1]-data[0]
        if interval not in intervals:
            intervals.append(interval)

    return intervals

def findKeyLength(intervals):
    '''
    To find the likely key length we need to take the intervals list and look
    for factors.  We will assume the key length is at least three letters long
    which is why we don't look for factors below three.
    Once we have all the factors and how often that factor has been identified
    we create and ordered list from most likely key length to least and return
    it.
    :param intervals: All the spaces between the repeated three letter combos.
    :return: An ordered list of likely key lengths and a confidence value.
    '''

    possibleKeyLengths = {}
    '''
    The possible key lengths dictionary will hold the factors themselves as we
    as the frequency of that factor.  Factors occuring more often are more
    likely to be the key length so we want to know what the factors are and
    how many times that factor occurs in the set.
    '''
    for interval in intervals:
        for i in range(3, interval-1): # Factors have to be 3 or greater
            if interval % i == 0:
                if i in possibleKeyLengths:
                    possibleKeyLengths[i] += 1
                else:
                    possibleKeyLengths[i] = 1

    for possibleKeyLength,occurence in possibleKeyLengths.items():
        if occurence < 4: # An arbitary value to remove unlikely key lengths
            del possibleKeyLengths[possibleKeyLength]

    orderedList = sorted(possibleKeyLengths.items(), key=lambda x: x[1])
    '''
    The previous line is clever.  It creates an ordered list of
    factor, occurence pairs based on the value of the occurence.
    The result is an ordered list of factors and the occurence of
    that factor in increasing occurences.
    '''

    keysAndFrequencies = []
    '''
    There may be any number of factors and thus key lengths
    It is probably safe to assume the correct one will be in
    the top ten.
    If there are more than ten possible key lengths just take
    the top ten.  Otherwise grab all that we have.
    '''
    if len(orderedList) > 10:
        for i in range(len(orderedList)-1, len(orderedList)-11, -1):
            keysAndFrequencies.append(orderedList[i])
    else:
        for i in range(len(orderedList)-1, -1, -1):
            keysAndFrequencies.append(orderedList[i])

    return keysAndFrequencies

def divideCiphertext(cipherText, keyLength):
    '''
    Dividing the cipher text into subtrings is easy.
    The function creates a list of substrings and
    populates that list with the appropriate number of
    empty subtrings.  The function then steps along
    the cipher string in steps of the key word length
    and grabs sequential letters and adds them to their
    appropriate substring.
    Finally the list of substrings is returned.
    :param CipherText: The complete body of the cipher text
    :param KeyLength: The proposed key length
    :return: A single ist containing the substrings
    '''
    substrings = []
    for i in range(keyLength):
        substring = ''
        substrings.append(substring)
    pointer = 0
    while pointer < len(cipherText) - keyLength:
        for i in range(keyLength):
            substrings[i] += cipherText[pointer + i]
        pointer += keyLength

    return substrings

def retrieveKeyword(substrings):
    '''
    The first half of this function creates the relative frequency
    distribution for the substring.  It does this by counting letters
    and storing the tally in the dist dictionary.  The tally for each
    letter is then divided by the length of the substring to create
    the relative distribution.
    The function then sets the fingerprint value to 1000 and progressively
    looks for a smaller value with each rotation.  When the smallest
    fingerprint is found the keyword letter is returned.
    :param substrings: The set of substrings.
    :return: The key word.
    '''
    keyword = ''

    for string in substrings:

        dist = {}

        for letter in string:
            if letter in dist:
                dist[letter] += 1
            else:
                dist[letter] = 1

        for letter in alphabet:
            if letter not in dist:
                dist[letter] = 0

        for letter,occurence in dist.items():
            dist[letter] = (float(occurence)/len(string)) * 100

        print dist
        testRotation = 0
        fingerprint = 1000
        keyLetter = 'A'
        while testRotation < 26:
            diff = 0
            for i in range(25):
                templateKey = alphabet[i]
                distKey = alphabet[(i+testRotation) % 25]

                diff += pow(template[templateKey] - dist[distKey],2)

            if diff < fingerprint:
                fingerprint = diff
                keyLetter = alphabet[testRotation]

            print 'Fingerprint = ', fingerprint

            testRotation += 1
        keyword += keyLetter
    return keyword

def doDecrypt(cipherText, keyword):
    '''
        This is the decryption routine.  Two strings are needed, the input string and the keyword.
        The input string is the encrypted uppercase string.  The keyword is sent as upper case as well.

        Any numbers are left in situ, which may weaken the encryption, and the remaining characters
        are encrypted acording to the vigenere dictionary.  First the shift alphabet is selected from
        the keyword letter.  Then the index of the cipher text letter in that alphabet is found.
        Finally, that index is used to find the plain text letter in the plain text alphabet.

        The final string is displayed in the lower text field.
        :param cipherText: The encrypted block of text
        :param keyword: The key word
        :return: The decrypted text.
    '''

    plainString = ''
    for i in range(len(cipherText)):
        if cipherText[i] in numbers:
            plainString = plainString + cipherText[i]

        elif cipherText[i] in alphabet:
            '''
            The following line cycles through the numbers 0 to
            one less than the length of the key word.  This
            allow the letters of the key word to be selected
            in turn without the need for its own loop.
            '''
            keywordIndex = i % len(keyword)

            keywordLetter = keyword[keywordIndex]
            vigenereAlphabet = vigenere[keywordLetter]
            plainIndex = vigenereAlphabet.index(cipherText[i])
            plainString = plainString + alphabet[plainIndex]

    return plainString