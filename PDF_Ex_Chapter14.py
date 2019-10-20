import collections

if __name__== "__main__":
    filename = str(input("Please enter the file name: "))
    if not filename.__contains__(".txt"):
        raise ValueError ("You entered wrong file name!")
    k = int(input("Please enter the number of most common words: "))

    try:
        file = open(filename, "r")
        count = collections.Counter()
        for word in file.read().split():
            count[word.lower()] +=1
        print("The most " + str(k) + " common words are: " + str(list(dict(count.most_common(k)).keys())))
    except FileNotFoundError:
        print("File not found!")
    except IOError:
         print("Something went wrong while reading from file..")
