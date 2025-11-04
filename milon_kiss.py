from typing import Dict
from enum import Enum


class Options(Enum):
    GET_WORD = "1"
    ADD_WORD = "2"
    DELETE_WORD = "3"
    EXIT = "4"


def display_menu(menu: Dict[str, str]) -> None:
    """Displays a given menu."""
    for key, val in menu.items():
        print(f"{key}. {val}")


def handle_get_word(words_dict: Dict[str, str]) -> None:
    """Gets a translation from the dictionary"""
    word_to_get = input("Word to get: ")
    word_meaning = words_dict.get(word_to_get)
    if word_meaning is None:
        print(f"The word {word_to_get} doesnt exist!")
        return
    print(f"{word_to_get} means {word_meaning}.")


def handle_add_word(words_dict: Dict[str, str]) -> None:
    """Adds a word to the dictionary"""
    word_to_add = input("Word to add: ")
    word_meaning = input(f"Meaning of {word_to_add}: ")
    words_dict[word_to_add] = word_meaning
    print(f"{word_to_add}={word_meaning} was added.")


def handle_delete_word(words_dict: Dict[str, str]) -> None:
    """Deletes a word from the dictionary"""
    word_to_delete = input("Word to delete: ")
    deleted_word = words_dict.pop(word_to_delete, None)
    if deleted_word is None:
        print("Word does not exist!")
        return
    print(f"{word_to_delete} has been erased.")


def main() -> None:
    main_menu = {
        Options.GET_WORD.value: "Get word",
        Options.ADD_WORD.value: "Add word",
        Options.DELETE_WORD.value: "Delete word",
        Options.EXIT.value: "Exit"
    }
    functions = {
        Options.GET_WORD.value: handle_get_word,
        Options.ADD_WORD.value: handle_add_word,
        Options.DELETE_WORD.value: handle_delete_word
    }
    words_dict: Dict[str, str] = {}
    while True:
        display_menu(main_menu)
        choice = input("Enter choice: ")

        if choice in (Options.GET_WORD.value, Options.ADD_WORD.value, Options.DELETE_WORD.value):
            functions[choice](words_dict)
        elif choice == Options.EXIT.value:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
