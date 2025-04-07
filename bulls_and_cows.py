import random
import time
# https://flixbaba.com/tv/46922/ben-10-omniverse/season/2?e=5&p=1

# https://manytools.org/hacker-tools/ascii-banner/

BANNER = """
   ___  __  ____   __   ____  ___   _  _____    _________ _      ______
  / _ )/ / / / /  / /  / __/ / _ | / |/ / _ \  / ___/ __ \ | /| / / __/
 / _  / /_/ / /__/ /___\ \  / __ |/    / // / / /__/ /_/ / |/ |/ /\ \  
/____/\____/____/____/___/ /_/ |_/_/|_/____/  \___/\____/|__/|__/___/
                                                                       
"""
DIGIT_LENGTH = 4
NUM_GUESSES = 6


print(BANNER)
secret = random.sample(range(1, 10), DIGIT_LENGTH)

print(f"🤫🤫🤫🤫 pssstt, the answer is {secret}")

try:
    guess_number = 1
    while True:
        # ====> PARSE THE GUESS
        guess = input(f"❓ What is guess #{guess_number}?\n")
        guess_list = [int(c) for c in list(guess)]

        # ====> VALIDATE GUESS
        if len(guess_list) != DIGIT_LENGTH:
            print(f"⚠ Your guess needs to be {DIGIT_LENGTH} long!⚠")
            continue

        bull_count = 0
        cow_count = 0
        for i, guess_digit in enumerate(guess_list):
            # ====> BULL IF CORRECT DIGIT AND CORRECT POSITION
            if guess_digit == secret[i]:
                bull_count += 1
                continue
            # ====> ELSE, IF THE DIGIT IS CORRECT, BUT WRONG POSITION, THEN IT IS A COW
            if guess_digit in secret:
                cow_count += 1

        # ====> CHECK IF WE WON THE GAME, ELSE GIVE FEEDBACK!
        if bull_count == DIGIT_LENGTH:
            print("You won!!! Have a croissant 🥐")
            break
        else:
            print(f"{bull_count} Bulls 🐂 | {cow_count} Cows 🐄")

        # ====> END THE GAME IF WE GUESS TOO MUCH!
        if guess_number == NUM_GUESSES:
            print(f"Game over AFTER {NUM_GUESSES} guesses. 🥕 Correct answer is {secret}")
            break

        # ====> PREP FOR THE NEXT ROUND!
        guess_number += 1
        time.sleep(0.1)
except KeyboardInterrupt:
    # ====> WE DON'T WANT ERROR MESSAGES IN CONSOLE
    print("\nBye bye! 👋")
