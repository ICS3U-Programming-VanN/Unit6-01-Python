#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: December 13, 2022
# This program generates ten random numbers and stores then in a list
# The program will then calculate the average of all the numbers
# and display it to the console


import constants
import random


def main():
    # Initialized Variables
    list_of_integers = []
    sum = 0
    average = 0

    # Loops through 10 times to generate ten random numbers
    for counter in range(constants.MAX_LIST_SIZE):
        # Generates a random number and added it to a list
        list_of_integers.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))

        # Displays to console what number was added to the list and what position it is at
        print(f"{list_of_integers[counter]} added to the list at position {counter}")

    # Loops through 10 times to add all the numbers to a sum
    for counter in range(0, constants.MAX_LIST_SIZE):
        # Adds number to sum variable
        sum += list_of_integers[counter]

    # Calculates the average of the numbers in the list
    average = sum / constants.MAX_LIST_SIZE

    # Displays the average of the numbers to the user
    print(f"\nThe average of these numbers: {average}")


if __name__ == "__main__":
    main()
