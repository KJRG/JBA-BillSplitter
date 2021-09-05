# write your code here
from random import choice


def read_guests_names(guest_number):
    names = list()
    print('\nEnter the name of every friend (including you), each on a new line:')
    for _ in range(0, guest_number):
        name = input()
        names.append(name)
    return names


def get_bill_values(guests, total_value):
    value_per_guest = total_value / len(guests)
    rounded_value = round(value_per_guest, 2)
    return dict.fromkeys(guests, rounded_value)


def get_bill_values_with_lucky_guest(all_guests, total_value, lucky_guest):
    value_per_guest = total_value / (len(all_guests) - 1)
    rounded_value = round(value_per_guest, 2)
    guests_bill_values = dict.fromkeys(all_guests, rounded_value)
    guests_bill_values[lucky_guest] = 0
    return guests_bill_values


number_of_people = 0
try:
    number_of_people = int(input('Enter the number of friends joining (including you):\n'))
    assert number_of_people > 0
except (ValueError, AssertionError):
    print('No one is joining for the party')
else:
    guests_names = read_guests_names(number_of_people)
    total_bill_value = int(input('\nEnter the total bill value:\n'))
    bill_values = get_bill_values(guests_names, total_bill_value)
    lucky_guest_input = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky_guest_input == 'Yes' and number_of_people > 1:
        lucky_guest_name = choice(guests_names)
        print(f'\n{lucky_guest_name} is the lucky one!\n')
        bill_values = get_bill_values_with_lucky_guest(guests_names, total_bill_value, lucky_guest_name)
    else:
        print('\nNo one is going to be lucky\n')
    print(bill_values)
