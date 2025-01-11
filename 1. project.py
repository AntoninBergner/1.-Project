"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Antonín Bergner
email: tonda.bergner@gmail.com
discord: tondoj
"""

# List of users and their passwords
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Texts to analyze
texts = [
    '''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# User log in
username = input("Username: ")
password = input("Password: ")

# Verification
if username in users and users[username] == password:
    print("_" *40)
    print(f"Welcome to the text analyser {username}.")
    print(f"You have {len(texts)} texts to be analyzed.")
    print("_" *40)

else:
    print("$ python projekt1.py")
    print("Incorrect username or password. The program will be terminated!")
    exit()

# Text choice
try:
    text_choice = int(input("Enter number between 1 and 3 to choose text: "))
    if text_choice < 1 or text_choice > len(texts):
        print("Invalid choice. Program will be terminated!")
        exit()
except ValueError:
    print("Invalid input. Program will be terminated!")
    exit()

# Text analyze 
selected_text = texts[text_choice - 1]
words = selected_text.split()

word_count = len(words)
titlecase_count = sum(1 for word in words if word.istitle())
uppercase_count = sum(1 for word in words if word.isupper())
lowercase_count = sum(1 for word in words if word.islower())
number_count = sum(1 for word in words if word.isdigit())
number_sum = sum(int(word)for word in words if word.isdigit())

# Word lenght
word_length = {}
for word in words:
    clean_word = word.strip(".,!?")
    length = len(clean_word)
    if length > 0:
        word_length[length] = word_length.get(length, 0) + 1

# Result of analysis
print("-" * 40)
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {number_count} numeric strings.")
print(f"The sum of all the numbers is {number_sum}")
print("-" * 40)

print(f"{'LEN':<3}| {'OCCURENCES':<12}| NR.")
print("-" * 40)
for length, count in sorted(word_length.items()):
    print(f"{length:<3}| {'*' * count:<12}| {count}")