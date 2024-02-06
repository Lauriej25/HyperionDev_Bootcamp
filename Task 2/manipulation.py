# Practical Task 1
# Ask the user to enter a sentence
str_manip = input("Enter a sentence: ")

# Calculate and display the length of the sentence (str_manip)
length_of_str = len(str_manip)
print(f"Length of the sentence: {length_of_str}")

# Find the last letter in the sentence (str_manip) and replace all of the reoccuring letters with '@'
last_letter = str_manip[-1]
str_manip_last = str_manip.replace(last_letter, '@')
print(f"Modified sentence: {str_manip_last}")

# Print the last 3 characters of the sentence (str_manip) backwards 
last_3_chars_backwards = str_manip[-3:][::-1]
print(f"Last 3 characters backwards: {last_3_chars_backwards}")

# Create a five-letter word from the first three and last two characters of the sentence
five_letter_word = str_manip[:3] + str_manip[-2:]
print(f"Five-letter word: {five_letter_word}")

