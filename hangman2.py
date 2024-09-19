import random
text_file = 'words.txt'

# class SecretWord:

#     def __init__(self,secret_word = None):

#         if secret_word is not None:
#             self.secret_word = secret_word
#         else:
#             with open('words.txt', 'r') as fp:
#                 self.secret_word = random.choice(fp.readlines()).strip()


    
#     def show_letters(self, letters):
#         letters = [letter.upper() for letter in letters]

#         revelead_letters = [letter if letter in letters else "_" for letter in self.secret_word]

#         return " ".join(revelead_letters)

#     def check_letters(self, letters):
#        letters = [letter.upper() for letter in letters]
#        return all(letter in letters for letter in self.secret_word.upper() )
    
#     def check(self, secret_word):
#         return True if secret_word else False

    
    
# word = SecretWord()

# print(word.show_letters(['a','p' 'p','l','e']))



# class SecretWord:

#     def __init__(self,secret_word =True):
#     #     def pick_random_word():
#     # """Opens the words.txt file, picks and returns a random word from the file"""
#     # with open("words.txt") as fp:
#     #     lines = fp.readlines()
#     #     word = random.choice(lines)
#     #     return word.strip()

#         if secret_word is not None:
#             self.secret_word = secret_word
#         else:
#             with open('words.txt', 'r')as fp:
#                 self.secret_word = random.choice(fp.readlines()).strip()

#     def show_letters(self, letters):
#     #     uppercase = [let.upper() for let in letters]
#     # word = word.upper()
#     # filtered = [letter if letter in uppercase else "_" for letter in word]
#     # return " ".join(filtered)
#         letters = [letter.upper() for letter in letters]

#         revelead_letters = {letter if letter in letters else "_" for letter in self.secret_word }
#         return "_".join(revelead_letters)

#     def check_letters(self, letters):
#         letters = [letter.upper() for letter in letters]
#         return all(letter in letters for letter in self.secret_word )
    

#     def check(self,secret_word):
#         return True if secret_word else False


 


