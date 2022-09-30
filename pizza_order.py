#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Sept 2022
# This program calculates the cost of pizza

import constants


def main():
    # This function calculates the cost of pizza

    # input
    diameter = int(input("Enter the diameter of the pizza (in): "))

    # process
    sub_total = (
        (diameter * constants.MATERIALS_COST_PER_INCH)
        + constants.LABOR_COST
        + constants.RENT
    )
    total = sub_total + (sub_total * constants.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is: ${1:,.2f}.".format(diameter, total))

    print("\nDone.")


if __name__ == "__main__":
    main()
