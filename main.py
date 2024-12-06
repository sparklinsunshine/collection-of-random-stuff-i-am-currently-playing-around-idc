
from functools import cache
from colorama import Fore, Back, Style
from wordlists import *
from mycrossword import *


word_list = {'Food': food_wordlist, 'Cable Nostalgia': cablenostalgia_wordlist,'Indian Mythology': indmyth_wordlist, 'To Infinity, aND BEYOND!': space_wordlist, 'The Korean X Factor': korean_wordlist, 'Marvel':marvel_wordlist, 'Sports':sports_wordlist}

print(Fore.CYAN, 'Welcome to Cross-search game!')


# print(word_list.keys())
# list_picker = input('Enter the theme name: ')
# the_final_list = word_list[list_picker]
# a = Crossword(14, 14, "-", 5000, the_final_list)
# a.compute_crossword(2)
# print(a.word_bank())
# print(a.solution())
# print(a.word_find())
# print(a.display())
# print(a.legend())
# print(len(a.current_word_list), "out of", len(food_wordlist))
# print(a.debug)
# crossword_mainwindow = 
def input_word():
    #the_final_list = word_list[input('Enter theme name: ')]
    #a = Crossword(14, 14, "_", 5000, word_list[the_final_list])
    print(*word_list.keys(), sep = ';')
    list_picker = input('Enter theme name: ')
    the_final_list = word_list[list_picker]
    a = Crossword(14, 14, "_", 5000, the_final_list)
    a.compute_crossword(2)
    print(Fore.LIGHTYELLOW_EX)
    input_keyword = input('Crossword or Wordsearch?:\n')
    if input_keyword == 'Crossword':
        print(Fore.GREEN, a.display(), end = '\n')
        print(a.legend(), end = '\n')
        print(len(a.current_word_list), "out of", len(food_wordlist), end = '\n')
        print(a.debug, end = '\n')
    elif input_keyword == 'Wordsearch':
        print(Fore.BLUE, a.word_find(), end = '\n')
        # print(a.legend())
        print(a.word_bank(), end = '\n')
        print(len(a.current_word_list), "out of", len(food_wordlist), '\n')
        print(a.debug, end = '\n')
    else:
        print(Fore.LIGHTRED_EX, 'Oops, this program ain\'t as intelligent as your pea brain to decipher what you just said. Please check your spelling and try again!', end = '\n')
        input_word()
    display_solution(a)
    return 1

input_word()

def display_solution():
     solution_prompt = input('Display the solution?? (Y/N): ')
     if solution_prompt == 'Y':
         print(Fore.LIGHTGREEN_EX, a.word_bank())
         print(a.solution())
     elif solution_prompt == 'N':
         try_again = input('Are you sure? (Y/N): ')
         if try_again == 'N':
             display_solution()
         elif try_again == 'Y':
             pass
         else:
             print(Fore.LIGHTRED_EX, 'Oops, this program ain\'t as intelligent as your pea brain to decipher what you just said. Please check your spelling and try again!')
     else:
         print(Fore.LIGHTRED_EX, 'Oops, this program ain\'t as intelligent as your pea brain to decipher what you just said. Please check your spelling and try again!')

