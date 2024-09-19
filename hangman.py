
import random
NUMBER_OF_TURNS = 10
text_file = 'words.txt'
"""This function has 2 arugments, it checks if the letter is in the word in question, 
        if it is not returns a '_' if it is there returns the list with letters"""
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
    
    # using if statement to check for the letters
    if '"_"' in reveal_letters(text, revealed):
        return False
    else:
        return True
        
"""This function picks a random word from the file words.txt"""
def pick_random_word(text_file):
     
     #reading the file
     with open("words.txt", 'r') as fp:
          text_file = fp.read()

          #spliting the words in the file
          words = list(map(str, text_file.split()))

          #returns a random string from a file
          return random.choice(words)


    # '''Runs the game. Allows for "turns" loops (attempts).
    #     At each turn:
    #     1. Ask the user for a letter
    #     2. Add the letter to the list of letters already tried by the player
    #     3. If the letter was already tried, ask again
    #     4. Use the show_letters_in_word function to display hints about the word
    #     5. Remove 1 to the number of tries left
    #     6. Check if the player
    #         - won (= word has been found)
    #         - lost (= word has not been found, no tries left)

    #     Do not forget to pick a random word first :-)
    # '''  
"""
    -Main function 
    takes turns for an argument
    asks a user for input
    -checks if the user input is correct
    -co
"""
def main(turns, word=None):
   
   #picking a random word
   #random_word = (pick_random_word(text_file))
   #list of the letters that user tried
   tried_letters = [] 
   #winner
#    winner_player = (all_letters_found(random_word, tried_letters))
   #count of the tries
   count = 0
    # looping though the function, asks user for the input while tunrs are smaller than count, when count reaches 0 it exit the loop
    #checks if user input is all letters and if there is an user input in the first place
    #if the letter is a prt of the word asked it adds them to list
    #print the numbers of counts left and printas the word at the end
   if word is None:
        word = pick_random_word() 

       # print(reveal_letters(text, revealed))


   while turns > count :
        
        new_letter_input = input('Please enter a letter: ')

        if new_letter_input.isalpha() == False or (len(new_letter_input) < 1) :
             print('Please remeber you enter only letters, please entere a letter!')
        elif new_letter_input in tried_letters:
             print("You have already tried this letter")
        else:
             tried_letters.append(new_letter_input)
             print(tried_letters)
        print(reveal_letters(random_word, tried_letters))
        print(f'This was your no.{count + 1} try')
        count += 1

        winner_player = (all_letters_found(random_word, tried_letters))
        
        if count == 10:
             print(f'You used {turns} tries, better luck next time!')
             print(f'The hidden word was {random_word}')
             break
        elif winner_player == True :
             print('Congratulations, you won!')
       
        
        
        
             

        print()    

             
main(NUMBER_OF_TURNS)       


       

        
     
   


