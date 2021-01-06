# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is a level mark program


def level_grade(mark):
    # this function converts the level mark to a percentage    
    
    percentage = 0
    # process

    if mark == "4+":
        percentage = 97
    elif mark == "4":
        percentage = 90
    elif mark == "4-":
        percentage = 83
    elif mark == "3+":
        percentage = 78
    elif mark == "3":
        percentage = 75
    elif mark == "3-":
        percentage = 71
    elif mark == "2+":
        percentage = 68
    elif mark == "2":
        percentage = 65
    elif mark == "2-":
        percentage = 61
    elif mark == "1+":
        percentage = 58
    elif mark == "1":
        percentage = 53
    elif mark == "R":
        percentage = 51
    else:
        percentage = -1

    return percentage


def main():
    # input
    while True:
        user_input_str = input("Enter the level of mark: ")

        try:
            # calling functions
            grade_percentage = level_grade(user_input_str)
            # output
            if grade_percentage == -1:
                print("Sorry, that was an invalid level.")
            else:
                print("The percentage is {0}%".format(grade_percentage))
                break

        except Exception:
            print("Something wrong")
            print("Please re-enter the values.")


if __name__ == "__main__":
    main()
