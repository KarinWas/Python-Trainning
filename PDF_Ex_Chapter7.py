import collections
#Ex 7.1
def open_file(filename):
    file = open(filename, "r")
    for line in file:
        print(line)
    file.close()

if __name__== "__main__":
    open_file("Test.txt")

    #7.2
    file = open("Shakespeare.txt", "r")
    count = collections.Counter()
    for word in file.read().split():
        count[word.lower()] +=1
    print("The most 20 common words are: " + str(list(dict(count.most_common(20)).keys())))
    print("The unique words are: " + str(list(dict(count).keys())))
    words_above_5_times = [w for w in count.keys() if count[w] >=5]
    print("Words that used at least 5 times: " + str(list(words_above_5_times)))

    fileToWrite = open("most_200_Common_words", "w")
    fileToWrite.write(str(count.most_common(200)))
    fileToWrite.close()
