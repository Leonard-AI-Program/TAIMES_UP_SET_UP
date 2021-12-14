# %%
import random
import pandas as pd

# %%
WORDS_URL = "https://raw.githubusercontent.com/Leonard-AI-Program/TAIMES_UP/main/TAIMES_UP.csv?token=ANUHFYGN676HMKLLGVVECBDBYH6SO"
RNG_SOURCE = list(pd.read_csv(WORDS_URL)["Word"])

# %%
keep_playing = True
while keep_playing:
    word_to_guess = random.choice(RNG_SOURCE)
    print(word_to_guess)
    RNG_SOURCE.remove(word_to_guess)
    answer = input("Draw another word? - Yes or No")
    if answer.lower() == "yes" or answer.lower() == "y":
        pass
    else:
        keep_playing = False
# %%
