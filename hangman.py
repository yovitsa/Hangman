
import random
NUMBER_OF_TURNS = 10
# """This function has 2 arugments, it checks if the letter is in the word in question, 
# if it is not returns a '_' if it is there returns the list with letters"""
def reveal_letters(text, revealed):
    
    # empty list initilizaed
        letters = []
    
    #Looping though the text
        for letter in text:
                if letter in revealed:
                    letters.append(letter)
                else:
                    letters.append("_")
    
    #returns a string in a list     
        return " ".join(letters)


"""This function returns true if all the letters are revelaed otherwise it returns false"""
def all_letters_found(text, revealed):
    
    # using if statemnt to check for the letters
    if "_" in reveal_letters(text, revealed):
        return False
    else:
        return True
        
"""This function picks a random word from the file words.txt"""
def pick_random_word():
     
     #reading the file
     with open("words.txt", 'r') as fp:
          text = fp.read()

          #spliting the words in the file
          words = list(map(str, text.split()))

          #returns a random string from a file
          return random.choice(words)

def main(turns):
     
