from collections import defaultdict
import re

def get_lex_from_file(file_path):
    try:
        file = open(file_path)
    except FileNotFoundError:
        print("File Not Found: " + str(file_path))
    except IsADirectoryError:
        print("This is a directory: " + str(file_path))
    else:
        with file:
            file_lines = set()
            for line in file.readlines():
                file_lines.add(line.strip())
            return file_lines

#Function to check if negative word already exists in dictionary
def checkKey(dict, key):
    if key in dict.keys():
        return True
    else:
        return False

#Function to check if negative word appears immediately after the word "the" and immediately before the word "phone" in the textfile.
def checkLoc(phrase, word):
    if re.search(rf"(?<=the\s){word}(\sphone.)", phrase, re.IGNORECASE):
        return True
    else:
        return False

def run(input_file_path):

    negative_words = get_lex_from_file("negative-words.txt")
    phrases = get_lex_from_file(input_file_path)

    freq=defaultdict(int) # new dictionary. Maps each word to each frequency

    for phrase in phrases:
        #print (phrase)
        words=phrase.lower().strip().split(' ')
        for word in words:
            for negative_word in negative_words:
                if negative_word == word:
                    #print(negative_word)
                    if checkKey(freq, negative_word) == False and checkLoc(phrase, negative_word) == True:
                        freq[negative_word] += 1    #Increment freq counter by 1 if negative word is NOT in dictionary but is between key words
                    elif checkKey(freq, negative_word) == True and checkLoc(phrase, negative_word) == True:
                        freq[negative_word] += 1    #Increment freq counter by 1 if negative word is in dictionary and between key words
                    elif checkKey(freq, negative_word) == False and checkLoc(phrase, negative_word) == False:
                        freq[negative_word]=0   #Include negative word in dictionary (as a key) and mapped to value of if not in dictionary and not between key words
                    else:
                        pass
                else:
                    pass
    return freq

if __name__ == "__main__":
    print("senticounter.py")
    print(run("textfile_rev.txt"))
