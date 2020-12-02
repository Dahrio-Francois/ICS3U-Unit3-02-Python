#!/usr/bin/env python 3
#
# Created by: Dahrio Francois
# Created on: December 2020
# this program makes you guess a number between 0 - 9


import constants


def main():
    # this function makes the number you need to guess

    # input
    guessing_number = int(input("Guess your number between 0 & 9: "))
    print("")

    # process
    if guessing_number > constants.MAX_GUESS_NUMBER:
        # output
        print("Too high")
    if guessing_number < constants.MAX_GUESS_NUMBER:
        print("Too low")
    if guessing_number == constants.MAX_GUESS_NUMBER:
        print("Correct")


if __name__ == "__main__":
    main()
