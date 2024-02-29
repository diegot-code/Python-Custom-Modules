
from greeting import greet
from math_use import add
from string_methods import dataCheck
from inp_val_ck import check
from average_amount import calculate_average


# Imports above

def main():

    greet("Good Morning", "James")
    
    print(add(4, 5))

    print(dataCheck("GiLberT"))

    # print(check("Yes"))

    print(calculate_average([24, 56, 23, 78, 123, 12, 53, 36, 90]))

if __name__ == "__main__":
    main()