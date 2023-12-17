import random, os

word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]

def start_game():
    global lives, guessed_letters, gaps, chosen_word, wanna_play

    chosen_word = random.choice(word_list)
    gaps = list(len(chosen_word) * '_')
    lives = 10
    guessed_letters = []
    wanna_play = True

def guess_letter():
    return input("Guess a letter:\n")[0].lower()

def modify_gaps(letter):
    for i in range(len(chosen_word)):
        if chosen_word[i] == letter:
            gaps[i] = letter
    
def check_guess(aorb):
    global lives, guessed_letters, gaps, chosen_word, wanna_play

    if aorb in guessed_letters:
        decrease_lives()
        print('You already guessed this letter. You lost one life.')
    elif aorb in chosen_word:
        modify_gaps(aorb)
        guessed_letters.append(aorb)
    else:
        decrease_lives()
        guessed_letters.append(aorb)
        # print(f'You have {lives} lives now.\n')

def reset_game():
    global wanna_play
    wanna_play = False

    start_game()

def close_game():
    global wanna_play
    wanna_play = False

    print('Thank you for playing.\n')
    
def decrease_lives():
    global lives
    lives -= 1

def clear_screen():
    os.system('cls')

# game starts
start_game()

while wanna_play:
    print(f"lives: {lives} // gaps: {gaps} // guessed letters: {guessed_letters}\n")
    # print(f"lives: {lives} // wanna play: {wanna_play} // guessed letters: {guessed_letters} // gaps: {gaps} // chosen word: {chosen_word}\n\n")

    check_guess(guess_letter())

    if not ('_' in gaps):
        play_again = input('Wanna play again?\n')[0].lower()

        if  play_again == 'y':
            reset_game()
        else:
            close_game()
             
    if lives == 0:
        play_again = input('You lost all of your lives. Wanna play again?\n')[0].lower()

        if play_again == 'y':
            reset_game()
        else:
            close_game()

    clear_screen()


# implement guess the rest of the world upfront