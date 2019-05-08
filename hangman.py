import string
from words import choose_word
from images import IMAGES

# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    # '''

    if get_guessed_word(secret_word, letters_guessed) == secret_word :
        return True
    return False

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    print "guessed word" + " ==>  " + str(letters_guessed) + "\n"
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''

    import string
    all_letters = string.ascii_lowercase
    index = 0
    letters_left = ""
    while index < len(all_letters) :
      if all_letters[index] in letters_guessed:
          index += 1
      else :
          letters_left = letters_left + all_letters[index]
          index += 1
    return letters_left

def hint(secret_word, letters_guessed):
    import random
    letters_not_guessed = []
    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)
        index += 1
    return random.choice(letters_not_guessed)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    Total_live = remaining_lives = 8
    image_selection = [0,1,2,3,4,5,6,7]
    Level = raw_input("for eazy level, type ====>>  e \n""for midium level, type ===>>  m \n""for hard level, type ====>>  h \ntype here your choice =====>> ")
    if Level not in ["e","m","h"]:
        print "invelid choice \nthe game going on in eazy mode\n"
    else :
        if Level == "m" :
            Total_live = remaining_lives = 6
            image_selection = [0,2,3,5,6,7]
        elif Level == "h" :
            Total_live = remaining_lives = 4
            image_selection = [1,3,5,7]        
        elif Level == "e" :
            Total_live = remaining_lives = 8
            image_selection = [0,1,2,3,4,5,6,7]

    letters_guessed = []
    while remaining_lives > 0 :
        available_letters = get_available_letters(letters_guessed)
        print ""
        print ("Available letters: " + available_letters + "\n")
        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()
        if letter == "hint" :
            print "The hint is ===>>" + (hint(secret_word,letters_guessed))
        else :
            if ((len(letter)) == 1) and (letter.isalpha() == True):
                if letter in secret_word:
                    letters_guessed.append(letter)
                    print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                    print ("")
                    if is_word_guessed(secret_word, letters_guessed) == True:
                        print (" * * Congratulations, you won! * * ")
                        print ("")
                        break
                    remaining_lives += 1 
                else:
                    letters_guessed.append(letter)
                    print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                    print ("")
                    print (IMAGES[image_selection[Total_live - remaining_lives]])
            else :
                print ("invelid input")
                print ("")
                remaining_lives += 1
        remaining_lives -= 1
        print "Remaining lives  ===>>  ", remaining_lives
    else :
        print ("Game Over")
        print ("the expected word is" + "   " + (secret_word))
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
