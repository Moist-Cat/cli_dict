import sys
import json
from pathlib import Path
from difflib import get_close_matches

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "data.json") as file:
    data = json.load(file)

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
    meaning = input("The word is not in the database. Write the meaning to add it or press Enter: ")
    if meaning:
        data[word] = meaning
        with open(BASE_DIR / "data.json", "w") as file:
            json.dump(data, file, indent=4)
        return data[word]

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except KeyboardInterrupt:
        print("\naborted")
