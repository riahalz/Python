# Print instructions for the game
def print_instructions():
    print("Welcome to Word Works! \n")
    print("You will be shown a word, and you need to enter as many words as you can think of that start with that word. \n")
    print("Type 'giveup' to skip to the next word.")
    print("Enter 'quit' to quit the game at any point once it starts. \n")
    print("Play in fullscreen mode for the best experience. \n")
    print("All the best! \n")
    print("Enter 'play' to start the game.")

# Word lists with spelling variations
words = ["Table", "Zip", "Wear", "Shut", "Keys", "Yolk", "Chain"]
word_lists = {
    "Table": ["Tables", "Tabled", "Tablet", "Tablets", "Tableau", "Tabletop", "Tableless", "Tableted", "Tableting", "Tableaus", "Tableware", "Tableful", "Tabletops", "Tablefuls", "Tablemate", "Tablemates", "Tablewares", "Tablelands", "Tableland", "Tablecloths", "Tablecloth", "Tablespoonful", "Tablespoon", "Tablespoons", "Tablespoonfuls"],
    "Zip": ["Zips", "Zipper", "Zippers", "Zippy", "Zipperless", "Zippered", "Zippiest", "Zippering", "Ziplock", "Ziplocks", "Ziplocking", "Ziplocked", "Zipless", "Zippier", "Zipping", "Zipped"],
    "Wear": ["Wearable", "Weary", "Wearing", "Wears", "Wearables", "Wearer", "Wearily", "Wearies", "Wearish", "Wearers", "Wearied", "Weariful", "Weariest", "Wearier", "Wearisome", "Wearingly", "Weariless", "Weariness", "Wearproof", "Wearifully", "Wearisomely", "Wearability", "Wearilessly", "Wearinesses", "Wearabilities", "Wearifulnesses", "Wearisomenesses"],
    "Shut": ["Shuts", "Shuttlecocking", "Shuttlecocked", "Shuttlecock", "Shuttlecocks", "Shutterless", "Shutterbugs", "Shuttleless", "Shutterbug", "Shuttering", "Shutdowns", "Shutdown", "Shuttered", "Shuttling", "Shuttlers", "Shuteyes", "Shuteye", "Shutoffs", "Shutouts", "Shutting", "Shutters", "Shuttled", "Shuttler", "Shuttles", "Shuttle", "Shutout", "Shutter", "Shutoff"],
    "Keys": ["Keystroke", "Keystroked", "Keystone", "Keystones", "Keysmith", "Keysmiths", "Keystrokes", "Keyset", "Keysets", "Keyster", "Keysters", "Keystroking"],
    "Yolk": ["Yolky", "Yolks", "Yolksy", "Yolkiest", "Yolked", "Yolkier", "Yolkless"],
    "Chain": ["Chains", "Chainsaw", "Chained", "Chainsaws", "Chainsawer", "Chainman", "Chainmen", "Chaining", "Chainfall", "Chainfalls", "Chainsawed", "Chainsawing", "Chainwheel"],
}

# Word spelling variations
variations = {
    "tableted": ["tabletted"],
    "tableting": ["tabletting"],
}

def normalize_word(word):
    for correct_spelling, var_list in variations.items():
        if word in var_list:
            return correct_spelling
    return word

# Game - Normal mode
def word_works():
    total_words = sum(len(set(normalize_word(w.lower()) for w in word_list)) for word_list in word_lists.values())
    score_counter = 0

    for word in words:
        print("\n Word:", word,)
        word_list = word_lists[word]
        correct_words = 0
        entered_words = {}
        missed_words = {normalize_word(w.lower()): w for w in word_list}

        print(f"Enter words starting with '{word}'")
        print("or type 'giveup' to skip to the next word:")

        while True:
            user_input = input().strip().capitalize()  # Capitalizing the first letter of each word
            normalized_input = normalize_word(user_input.lower())

            # If user inputs 'quit', end the game
            if user_input.lower() == 'quit':
                print("Quitting the game.")
                print(f"Your final score is: {score_counter}/{total_words} words.")
                return

            # If user inputs 'giveup', skip to next word
            if user_input.lower() == 'giveup':
                score_counter += correct_words
                print(f"\nYou found: {correct_words}/{len(word_list)} words.")
                break

            # Checks if user has entered the word more than once
            if normalized_input in entered_words:
                entered_words[normalized_input] += 1
                print(f"You've already entered '{user_input}' {entered_words[normalized_input]} times.")
                continue

            # Check if user's entered word is correct/incorrect
            matched_word = missed_words.get(normalized_input)
            if matched_word:
                print(f"Correct! '{user_input}' is a valid word.")
                correct_words += 1
                entered_words[normalized_input] = 1
                missed_words.pop(normalized_input)
            else:
                print("Incorrect!")

            # If user has guessed all the words correctly
            if correct_words == len(word_list):
                print(f"\nWell done! You found all {correct_words}/{len(word_list)} words starting with '{word}'! \n")
                score_counter += correct_words
                break

        # Print list of words missed by user
        if missed_words:
            print(f"Missed words for '{word}': {', '.join(sorted(missed_words.values()))} \n")

    # Print total score
    if score_counter == total_words:
        print(f"You're a word whiz! You guessed all {score_counter}/{total_words} words.")
    else:
        print(f"Game Over! Your final score is: {score_counter}/{total_words} words.")

def main():
    print_instructions()
    while True:
        mode = input().strip().lower()

#check mode - 'play' or 'quit'
        if mode == 'play':
            word_works()
            break
        elif mode == 'quit':
            print("Quitting the game.")
            break
        else:
            print("Invalid mode. Please enter 'play' or 'quit'.")

if __name__ == "__main__":
    main()
