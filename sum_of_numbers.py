#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: April 13th, 2025
# This program asks the user to enter a positive number
# the input should only be a whole number, and then use the
# while loop to add and display the sum to the user.
def main():
    loop_counter = 0
    sum = 0
    # Ask user for a positive integer
    pos_int_as_string = input("Enter a positive integer: ")

    try:
        # Convert pos_number to an integer
        pos_number = int(pos_int_as_string)

        while loop_counter <= pos_number:
            print(f"The loop counter is {loop_counter}")
            sum = sum + loop_counter
            loop_counter = loop_counter + 1
            print(f"The sum is {sum}")

        if pos_number < 0:
            # If user number is a negative
            # we should let the user kno that.
            print(f"{pos_number} is not a positive number.")

    except:
        # When user inputs a float or string the below
        # code will be displayed.
        print("Please a valid integer.")
        print("Your input is an not an integer.")

    finally:
        # Once every code is executed the below code
        # will be displayed.
        print("Thank you and have a great day")


if __name__ == "__main__":
    main()
