out_number = 100

def transform_string(number: int) -> str:
    ending = number % 10
    print(out_number)
    if 10 <= number < 21 or ending >= 5 or ending == 0:
        format_string = f'{number} процентов'
    elif ending == 1:
        format_string = f'{number} процент'
    else:
        format_string = f'{number} процента'
    return format_string

transform_string(1)
print(ending)
'''
def digit_sum(number):
    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number % 10   #421
        number //= 10
    return sum_of_digits


def print_digit_sum(number):
    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number % 10   #421
        number //= 10
    print(sum_of_digits)


total_sum = 0
for number in range(21, 42, 2):
    init_number = number
    # sum_of_digits = digit_sum(number)
    sum_of_digits = print_digit_sum(number)
    print(number, sum_of_digits)
    if sum_of_digits % 7 == 0:
        total_sum += init_number
'''