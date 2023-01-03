import sys
import json
from difflib import get_close_matches

with open("data.json") as file:
    data = json.load(open("data.json"))

def main(word):
    result = get_meaning(word)
    if type(result) == list:
        for i in result:
            print(i)
    else:
        print(result)

def get_meaning(word):
    word = word.lower()
    # case: direct match
    if word in data:
        return data[word]

    # case: close match
    close_words = get_close_matches(word, data.keys())
    if any(close_words):
        indx = input("Did you mean any of %s instead? Enter the index if it is: " % close_words)
        try:
            indx = int(indx)
            if indx in range(len(close_words)):
                return data[get_close_matches(word, data.keys())[indx]]
        except ValueError:
            pass

    # case: add new word
    word = input("The word is not in the database. Write the meaning to add it or press Enter: ")
    if word:
        data[word] = input("Enter the meaning of the word: ")
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        return data["word"]

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except KeyboardInterrupt:
        print("\naborted")
