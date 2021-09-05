NO_KEY_MESSAGE = "There is no such key"
key_to_delete = int(input())
deleted_value = squares.pop(key_to_delete, NO_KEY_MESSAGE)
print(deleted_value)
print(squares)
