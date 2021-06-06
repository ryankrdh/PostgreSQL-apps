from database import add_entry, get_entries

menu = """ Please select one of the following options:
1) Add new entry for today.
2) View Entries.
3) Exit.

Your selection: """

# USER MENU

welcome = "Welcome to the programming diary!"


def prompt_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")

    add_entry(entry_content, entry_data)


def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


print(welcome)
# User_input = input(menu)
# (Python3) parenthesis is required to get the user_input variable to hold the value of the input before checking to see if the answer equals "3".
while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        ("Invalid option, please try again!")


# PROGRAM LOGIC
