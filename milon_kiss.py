from typing import Dict


dic: Dict[str, str] = {}


def display_menu() -> None:
    """Displays the choice menu."""
    print(
        "1. Get word\n"
        "2. Add word\n"
        "3. Delete word\n"
        "4. Exit"
    )


def handle_get_word() -> None:
    """Gets a translation from the dictionary"""
    word_to_get = input("Word to get: ")
    if word_to_get not in dic:
        print(f"The word {word_to_get} doesnt exist!")
        return
    print(f"{word_to_get} means {dic[word_to_get]}.")


def handle_add_word() -> None:
    """Adds a word to the dictionary"""
    word_to_add = input("Word to add: ")
    word_meaning = input(f"Meaning of {word_to_add}: ")
    dic[word_to_add] = word_meaning
    print(f"{word_to_add}={word_meaning} was added.")


def handle_delete_word() -> None:
    """Delets a word from the dictionary"""
    word_to_delete = input("Word to delete: ")
    if word_to_delete not in dic:
        print("Word does not exist!")
        return
    del dic[word_to_delete]
    print(f"{word_to_delete} has been erased.")


def main() -> None:
    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            handle_get_word()

        elif choice == "2":
            handle_add_word()

        elif choice == "3":
            handle_delete_word()

        elif choice == "4":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
