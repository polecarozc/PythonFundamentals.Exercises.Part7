from typing import Dict

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {1: 'English', 2: 'Spanish'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {1: 'What is your name?', 2: 'Como te llamas?'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {1: 'Hello', 2: 'Hola'
}

def mode_setting():
    print("Set mode: \n1: Admin\n2: User")

def mode_input():
    choice = input("Please select a mode: ")
    return int(choice)

def admin_controls():
    print("Welcome to admin mode... Please select a prompt: \n1: Add language support\n2: Update greeting phrases")

def admin_mode_input():
    choice = input("please select a mode:")
    return int(choice)
def add_language():
    gate = 1
    while gate==1:
        language = input("Please enter a language that you would like to add: ")
        count =1
        size = len(lang_dict)
        lang_dict[size+count]  = language
        print("Language added, here is an updated list of languages")
        for i in lang_dict:
            print(f"{i}: {lang_dict[i]}")
        print("Would you like to add another language?: \n1: Yes\n2: No")
        gate = int(input("Please make a selection: "))
        if gate == 1:
            count+=1
        else:
            break

def main_admin_menu():
    print("Return to main admin menu? \n1: Yes\n2: No")
    choice = input("Please make a selection: ")
    return int(choice)

def add_phrase():
    print("Please enter the language for the phrase you would like to update")
    for i in lang_dict:
        print(f"{i}: {lang_dict[i]}")
    language_type = int(input("Please make your selection: "))
    print("Okay what would you like to do?: \n1:Change \n2:Remove")
    choice = int(input("Please make your selection: "))
    if choice == 1:
        new_phrase = input("Enter a new phrase: ")
        greetings_dict[language_type] = new_phrase
        new_question_greeting = input("Now Enter a new question phrase for the language you have selected: ")
        name_prompt_dict[language_type] = new_question_greeting
    elif choice == 2:
        print("Removing existing phrase")



def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print("Please choose a language: ")
    for i in lang_options:
        print(f"{i}: {lang_options[i]}")

def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    choice = input("pick a language: ")
    return int(choice)

def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    ret_val = lang_options.get(lang_choice)
    if ret_val is not None:
        return True
    else:
        return False



def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    answer = name_prompt_options.get(lang_choice)
    return answer

def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    answer = input(name_prompt)
    return answer

def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    phrase = greetings_options.get(lang_choice)
    print(phrase, name)

if __name__ == '__main__':
    gate = 1
    while gate==1:
        mode_setting()
        picked_mode = mode_input()
        if picked_mode == 1:
            admin_controls()
            picked_admin_input = admin_mode_input()
            if picked_admin_input==1:
                add_language()
                gate = main_admin_menu()
            elif picked_admin_input==2:
                add_phrase()
                gate = main_admin_menu()
        elif picked_mode == 2:
            print_language_options(lang_dict)
            chosen_lang = language_input()
            while language_choice_is_valid(lang_dict, chosen_lang) is False:
                print("Invalid selection. Try again.")
                chosen_lang = language_input()

            selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
            chosen_name = name_input(selected_prompt)
            greet(chosen_name, greetings_dict, chosen_lang)
            gate = main_admin_menu()


