def the_cabin_class_of_a_cruise_ship():
    the_cabin_class = input("enter your standard:")
    if the_cabin_class =='LUX':
        print(" upper-deck cabin with a balcony.")
    elif the_cabin_class =='A':
        print("above the car deck, equipped with a window.")
    elif the_cabin_class =='B':
        print("windowless cabin above the car deck.")
    elif the_cabin_class =='C':
        print("windowless cabin below the car deck.")
    else:
        print("invalid cabin class")
the_cabin_class_of_a_cruise_ship()