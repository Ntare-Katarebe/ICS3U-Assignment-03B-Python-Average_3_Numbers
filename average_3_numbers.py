#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program calculates the average of 3 number
#    with number inputted from the user

import math
import constants


def main():
    # This function calculates the average of 3 number

    # input
    print("This program finds the average of three numbers")
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    third = int(input("Enter the third number: "))
    print("")

    # process
    sub_answer = first + second + third
    answer = sub_answer // constants.THREE
    # output
    if 0 <= answer <= 100:
        print("The average of the numbers is {}".format(answer))
    else:
        print("Not in between 0 - 100")
    print("\nDone.")


if __name__ == "__main__":
    main()
