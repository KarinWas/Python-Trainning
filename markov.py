import random
import sys

def process_line(line, k):
    '''
    Process a line of text to extract (state, new_word) pairs.
    Note that we remove uppercase letters in this example, though
    you don't have to.

    Example:
    process_line("In winter I get up at night") =
    [('BEGIN', 'in'),
     ('in', 'winter'),
     ('winter', 'i'),
     ('i', 'get'),
     ('get', 'up'),
     ('up', 'at'),
     ('at', 'night'),
     ('night', 'END')]

    We add the BEGIN and END keywords so that we can initialize the
    sentence and know when the line ends.
    '''
    if (line == ''):
        return (tuple(zip('BEGIN', 'END')))

    words = line.split()
    beginWords = []
    firstWord = 'BEGIN'
    for i in range (k-1):
        firstWord += ' ' + words[i]
    beginWords.append(firstWord)
    endWords = []
    endWords.append(words[0 + k - 1])
    for index in range(len(words)):
        if (index + k <= len(words)):
            groupWords = ''
            for i in range(k):
                groupWords += words[index + i] + ' '
            beginWords.append(groupWords)
        if (index + k) < len(words):
            endWords.append(words[index + k])
    
    endWords.append('END')

    return (tuple(zip(beginWords, endWords)))

def process_textfile(filename, k):
    '''
    Creates a dictionary with transition pairs
    based on a file provided

    For the first part of the assignment, we use a
    placeholder text that you will have to replace
    at some point.

    Based on the placeholder text, the dictionary
    should contain the following key-value pairs:

    'blue,': ['END']
    'by': ['yellow', 'day.', 'day?']
    'still': ['hopping', 'going']
    '''
    d = {}

    f = open(filename,"r").read().split('\n')
    # text from http://www.bygosh.com/Features/082000/rhymes.htm

    for line in f:
        for word in process_line(line, k):
           key, value = zip(word)
           if str(key[0]).lower() in d.keys():
                d[str(key[0]).lower()].append(value[0])
           else:
                d[str(key[0]).lower()] = list(value)

    return d

def generate_line(d, k):
    '''
    Generates a random sentence based on the dictionary
    with transition pairs

    Note that the first state is BEGIN but that we
    obviously do not want to return BEGIN

    Some sample output based on the placeholder text:
    'i have to go to go to go to go to play,'

    Hint: use random.choice to select a random element from a list
    '''
    sentence = []
    keyWords = []
    for key in d.keys():
        if key.split()[0] == 'begin':
            keyWords.append(key)
    chosenWord = random.choice(keyWords)
    word = random.choice(d[chosenWord])
    wordToAppend = chosenWord.replace('begin ', '')
    sentence.append(wordToAppend)
    while ('END' not in word):
        keyWords = []
        for key in d.keys():
            if key.split()[0] == word.lower():
                keyWords.append(key)
        if (len(keyWords) == 0):
            for key in d.keys():
                if key.split()[-1] == word.lower():
                    keyWords.append(key)
            wordToAppend = word
        else:
            wordToAppend = random.choice(keyWords)
        sentence.append(wordToAppend)
        chosenWord = random.choice(keyWords)
        word = random.choice(d[chosenWord])
        
    return(' '.join(sentence))

if __name__ == '__main__':
    a = process_textfile("newText.txt", 4)
    print (generate_line(a, 4))

     #if len(sys.argv) != 2:
      #  print 'ERROR: Run as python markov.py <filename>'
       # exit()

   # d = process_textfile("Shakespeare.txt")
    #print generate_line(d)