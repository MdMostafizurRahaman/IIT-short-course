sentence = input("Enter a sentence: ")

# Step by step applying methods
clean_sentence = sentence.strip()               # Removing leading/trailing spaces
lower_sentence = clean_sentence.lower()         # Converting all letters to lowercase
underscore_sentence = lower_sentence.replace(" ", "_") # Replacing spaces with underscores
hashtag = "#" + underscore_sentence             # Adding a # at the beginning

print("Output:", hashtag)