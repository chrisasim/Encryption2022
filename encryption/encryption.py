alphabets ="ABCDEFGHIJKLMNPQRSTUVWXYZ"
string_input = input("Enter string as an input: ")
input_length = len(string_input)
print(string_input)
print(input_length)
string_output=""

for i in range(input_length):
 character = string_input[i]
 location_of_character = alphabets.find(character)
 new_location = location_of_character + 3;
 string_output += alphabets[new_location]


print("Encrypted text is the following one:", string_output)



