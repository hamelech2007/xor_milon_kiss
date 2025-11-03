from typing import Dict


GET_WORD = "1"
ADD_WORD = "2"
DELETE_WORD = "3"
EXIT = "4"


def display_menu() -> None:
    """Displays the choice menu."""
    menu = {
        GET_WORD: "Get word",
        ADD_WORD: "Add word",
        DELETE_WORD: "Delete word",
        EXIT: "Exit"
    }

    for key, val in menu.items():
        print(f"{key}. {val}")


def handle_get_word(dic: Dict[str, str]) -> None:
    """Gets a translation from the dictionary"""
    word_to_get = input("Word to get: ")
    if word_to_get not in dic:
        print(f"The word {word_to_get} doesnt exist!")
        return
    print(f"{word_to_get} means {dic[word_to_get]}.")


def handle_add_word(dic: Dict[str, str]) -> None:
    """Adds a word to the dictionary"""
    word_to_add = input("Word to add: ")
    word_meaning = input(f"Meaning of {word_to_add}: ")
    dic[word_to_add] = word_meaning
    print(f"{word_to_add}={word_meaning} was added.")


def handle_delete_word(dic: Dict[str, str]) -> None:
    """Deletes a word from the dictionary"""
    word_to_delete = input("Word to delete: ")
    if word_to_delete not in dic:
        print("Word does not exist!")
        return
    del dic[word_to_delete]
    print(f"{word_to_delete} has been erased.")


def main() -> None:
    dic: Dict[str, str] = {}
    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == GET_WORD:
            handle_get_word(dic)

        elif choice == ADD_WORD:
            handle_add_word(dic)

        elif choice == DELETE_WORD:
            handle_delete_word(dic)

        elif choice == EXIT:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
