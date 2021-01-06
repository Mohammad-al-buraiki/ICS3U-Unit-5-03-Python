# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is a tringle area program


def level_grade(mark):
    # this function is calculation the tringle area
    
    # process
    
if mark == 4+:
        return mark
    elif mark == 4:
        return mark
    elif mark == 4-:
        return mark
    elif mark == 3+ :
        return mark
    elif mark == 3 :
        return mark
    elif mark == 3- :
        return mark
    elif mark == 2+ :
        return mark
    elif mark == 2 :
        return mark
    elif mark == 2- :
        return mark
    elif mark == 1+ :
        return mark
    elif mark == 1 :
        return mark
    elif mark == R:
        return mark
    else:
        return mark


def main():
    # input
    while True:
        user_input_str = input("Enter the level you want converted to a percentage: ")

        try:
            input_from_user = int(user_input_str)

            # calling functions
            level_grade(user_input_str)
            # output
            print("Level {0} has a middle percentage of {0}.".format(level_grade)
            break
            print("Level 4 has a middle percentage of 90%")
            break
            print("Level 4- has a middle percentage of 83%")
            break
            print("Level 3+ has a middle percentage of 78%")
            break
            print("Level 3 has a middle percentage of 74%")
            break
            print("Level 3- has a middle percentage of 71%")
            break
            print("Level 2+ has a middle percentage of 68%")
            break
            print("Level 2 has a middle percentage of 64%")
            break
            print("Level 2- has a middle percentage of 61%")
            break
            print("Level 1+ has a middle percentage of 58%")
            break
            print("Level 1 has a middle percentage of 54%")
            break
            print("Level 1- has a middle percentage of 51%")
            break
            print("Level R has a middle percentage of 25%")
            break
        except:
            print("Something wrong")
            print("Please re-enter the values.")


if __name__ == "__main__":
    main()
