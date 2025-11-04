from typing import Dict


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
        GET_WORD: "Get word",
        ADD_WORD: "Add word",
        DELETE_WORD: "Delete word",
        EXIT: "Exit"
    }
    words_dict: Dict[str, str] = {}
    while True:
        display_menu(main_menu)
        choice = input("Enter choice: ")

        if choice == GET_WORD:
            handle_get_word(words_dict)

        elif choice == ADD_WORD:
            handle_add_word(words_dict)

        elif choice == DELETE_WORD:
            handle_delete_word(words_dict)

        elif choice == EXIT:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
