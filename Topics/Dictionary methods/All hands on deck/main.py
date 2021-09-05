card_values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}

NUMBER_OF_INPUT_VALUES = 6

user_card_values = list()
for _ in range(0, NUMBER_OF_INPUT_VALUES):
    user_card_values.append(card_values.get(input()))
mean_of_card_values = sum(user_card_values) / NUMBER_OF_INPUT_VALUES
print(mean_of_card_values)
