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
            # prints
            
        except:
            print("Something wrong")
            print("Please re-enter the values.")


if __name__ == "__main__":
    main()
