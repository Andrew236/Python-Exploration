import json
from difflib import get_close_matches
import difflib

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        answer = input("Did you mean %s instead? " % get_close_matches(word, data.keys())[0]).lower()
        if answer == 'yes' :
            return data[get_close_matches(word,data.keys())[0]]
        elif answer == 'no' :
            return "The word doesn't exist please check spelling "
        else: "You are speaking in alien, please check your query "
        

    else:
        return "The word does not exist"
        
word = input("Enter Word: ").lower()

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
