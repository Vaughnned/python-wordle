from termcolor import colored
import random

secret_List = ["apple", "swamp", "beget", "drain", "cause", "pitch", "trunk", "broad", "crane", "zoink"]
random_number = random.randint(1,10)
secret_word = secret_List[random_number]
attempts = 6
win = False
has_duplicate = False
correct_color = False
visited = set()
visited = list(visited)
guesses_so_far = []
guess = []
duplicate = []
color = ""
colortwo = "red"
final_word = ""

while attempts > 0 and not win:
  word = input("Guess a word: ")
  print()
  attempts = attempts - 1
  print("Remaining attempts: ", attempts)
  guesses_so_far.append(word)
  print("Guesses so far: ", guesses_so_far)
  for letter, secret_letter in zip(word[:5], secret_word):

    correct_color = False

    if secret_word.find(letter) == -1:
        guess.append(letter)
        color = "red"
    elif secret_word.find(letter) != -1:
        if letter == secret_letter and secret_word.count(secret_letter) == 1 and letter not in visited:
            visited.append(secret_letter)
            guess.append(letter)
            color = "green"
        elif letter == secret_letter and secret_word.count(secret_letter) == 1 and letter in visited:
            guess.append(letter)
            color = "green"
        elif letter == secret_letter and secret_word.count(secret_letter) > 1:
            duplicate.append(secret_letter)
            has_duplicate = True
            guess.append(letter)
            color = "green"
        elif letter != secret_letter and secret_word.count(secret_letter) > 1:
            duplicate.append(secret_letter)
            has_duplicate = True
            guess.append(letter)
            color = "yellow"
        if letter == secret_letter and word.count(letter) >= 1 and letter in visited and letter not in duplicate:
            correct_color = True
        if letter == secret_letter and word.count(letter) == 1 and letter not in visited and letter not in duplicate:
            correct_color = True
        if letter == secret_letter and letter in duplicate:
            correct_color = True

        if letter != secret_letter and word.count(letter) == 1 and letter not in visited and letter not in duplicate:
            correct_color = True
        if letter != secret_letter and word.count(letter) == 1 and letter in visited and letter not in duplicate:
            correct_color = True
        if letter != secret_letter and letter in duplicate:
            correct_color = True
        # if letter != secret_letter and word.count(letter) > 1 and letter not in visited and letter in duplicate:
        #     correct_color = True

        elif letter != secret_letter and has_duplicate and letter in duplicate and duplicate.count(secret_letter) <= 2 and word.count(letter) <= 2:
            guess.append(letter)
            color = "yellow"
        elif letter != secret_letter and has_duplicate and letter in duplicate and duplicate.count(secret_letter) <= 2 and word.count(letter) > 2:
            guess.append(letter)
            color = "red"
        elif letter != secret_letter and has_duplicate and letter not in duplicate and letter not in visited:
            guess.append(letter)
            color = "yellow"
        elif letter != secret_letter and has_duplicate and letter not in duplicate and letter in visited:
            guess.append(letter)
            color = "yellow"

        elif letter != secret_letter and secret_word.count(secret_letter) == 1 and letter not in visited:
            guess.append(letter)
            color = "yellow"
        elif letter != secret_letter and secret_word.count(secret_letter) == 1 and letter in visited:
            guess.append(letter)
            color = "red"
        elif letter != secret_letter and letter not in visited and letter not in duplicate:
            guess.append(letter)
            color = "yellow"
    
    if word == secret_word:
        win = True

    if correct_color:
        print(colored(letter, color))
    if not correct_color:
        print(colored(letter, colortwo))

if attempts == 0:
    print("Better luck next time...")

if win:
    print("Congrats! You guessed the wordle!")
    # for final_letter in final_word[:5]:
    #     print(colored(letter, color))
    # print(final_word)

# def check_duplicate(l):
#     visited = set()
#     has_duplicate = False
#     for element in l:
#         if element in visited:
#             pass
#         elif l.count(element) == 1:
#             visited.add(element)
#         elif l.count(element) > 1:
#             has_duplicate = True
#             print("The list contains duplicate elements.")
#             break
#     if not has_duplicate:
#         print("List has no duplicate elements.")
