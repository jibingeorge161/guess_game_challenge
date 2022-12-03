#!/usr/bin/env python
# coding: utf-8

# ## Guessing Game Challenge

# --> The program picks a random integer from 1 to 100 and the user has to guess the number in a limited number of steps. <br>
# --> On the player's first turn, if the player's guess is within 10 of the original number, then it will return "WARM"; otherwise, it will return "COLD". <br>
# --> On subsequent guesses, if a guess is closer to the original number than the previous guess, it will return "WARMER"; otherwise, it will return "COLDER".

# Step 1 : Game introduction and rules

# --> Hi, I am a number between 1 and 100. Can you figure me out? <br>
# --> If your guess is more than 10 away from me, then I will return "COLD". <br>
# --> If your guess is within 10 of me, I will return "WARM". <br>
# --> If your guess is farther from me than your most recent guess, I will return "COLDER". <br>
# --> If your guess is closer to me than your most recent guess, I will return "WARMER." <br>

# Step 2 : Generating random integer

# In[1]:


from random import randint
number = randint(1,100)


# Step 3 : Create an empty list to store guesses.

# In[2]:


guess_list = [0] # 0 is used as a place holder


# Step 4 : Create the game.

# In[3]:


while True:

    guess = int(input('I am a number between 1 and 100. What is your guess : '))

    # valid guess check
    if (guess < 1) | (guess > 100):
        print(f'OUT OF BOUNDS!, {guess}')
        continue
    
    # correct guess
    if guess == number :
        print(f'Hooray! You guessed the number : {number} in {len(guess_list)} guesses.')
        break

    guess_list.append(guess)

    # COLDER, WARMER check
    if guess_list[-2]: # checking with the previous guess
        if abs(number - guess) <= abs(number - guess_list[-2]):  # abs or absolute difference will be lesser if the new guess is closer than the previous guess.
            print(f'WARMER!, {guess}')
        else:
            print(f'COLDER!, {guess}')
    
    # COLD, WARM check
    else: # checking with the current guess
        if abs(number - guess) <= 10:
            print(f'WARM!, {guess}')
        else:
            print(f'COLD!, {guess}')

