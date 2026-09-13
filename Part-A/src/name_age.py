"""A simple program that asks the user for their name and age, then prints them back.

Input:
    name (str): The user's name.
    age (int): The user's age.

Process:
    The program collects the user's name and age, converts the age to an integer,
    and prepares a formatted message.

Output:
     A message displaying the user's name and age.

Typical usage example:
    Enter your name: Korinne
    Enter your age: 32
    Hello, Korinne! You are 32 years old.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
 
    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"Hello, {name}! You are {age} years old.")
    print(f"You were probably born around {birth_year}.")
    


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# TODO: Replace with an APA-style reference for a source you used, or delete.
# TODO: Replace with another APA-style reference, or delete this TODO line.
