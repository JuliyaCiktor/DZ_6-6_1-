import string

input_str = input("Введіть дві літери через дефіс: ")
start_letter, end_letter = input_str.split('-')
start_index = string.ascii_letters.index(start_letter)
end_index = string.ascii_letters.index(end_letter)
result = string.ascii_letters[start_index:end_index + 1]
print(result)
