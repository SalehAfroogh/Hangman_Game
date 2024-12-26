import random
# a list of words
# select random word
# get a user chr 
# check => show feedback
# guess >0 => win/loss

word_list = ["Habib", "Mahyar", "Reza", "Rezvaneh", "Shirin"]
Selected_word = random.choice (word_list).lower()

guess_count = len(Selected_word)
guess_list = ["_"] * len(Selected_word) 


while guess_count > 0:
    guess_chr = input("Enter a chr: \n")
    
    if guess_chr.isalpha():
        if guess_chr in Selected_word:
            if guess_chr in guess_list:
                print("You already entered it. Try a new one")
            else:
                for idx, chr in enumerate(Selected_word):
                    if chr == guess_chr:
                        guess_list[idx] = guess_chr
                current_guess = " ".join(guess_list)
                print(f"Perfect => {current_guess}") 
                
                if not "_" in guess_list:
                    print("You win!")
                    break
        else:
            guess_count -= 1
            if guess_count > 0:
                print (f"wrong! => remained guess: {guess_count}")
            else:
                print (f"wrong! You lost! => remained guess: {guess_count}")
                
        
    else:
        print("Enter a valid chr")    
    

