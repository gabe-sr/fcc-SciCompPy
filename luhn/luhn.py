# This is the second project from freeCodeCamp's Scientific Computing with Python (currently in Beta),
# available at https://www.freecodecamp.org/learn/scientific-computing-with-python.
#
# This is a card verification program, using Luhn's algorithm.
#
def verify_card_number(card_number):
    if(not card_number.isdigit()):
        return False
    sum_of_odd_digits = 0
    # when dealing with iterable objects, slicing is usually the most concise way of accessing and extracting data from it
    # three parameters can be used: starting pos (inclusive), end pos (exclusive), step
    # start and stop may be negative and would count down from -1 (last item)
    # step is the increment amount for each slice "iteration", may be negative for reverse traversal
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    return total % 10 == 0

def main():
    print('This is a card number verification software using Luhi\'s algorithm')
    card_number = str(input('Please enter card number in the format \'XXXX-XXXX-XXXX-XXXX\':\n'))
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

if __name__=='__main__':
    main()
