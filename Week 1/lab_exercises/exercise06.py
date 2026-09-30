## Uppercase
my_text = "Hello, World"
my_text = my_text.upper() # will turn into "HELLO, WORLD"
print(my_text)

## Replacing strings - 01
second_text = "I have an apple, you have an apple."
replaced_text = second_text.replace("apple", "orange")
print(replaced_text)

## Replacing strings - 02
third_text = "           I have an apple, you have an apple.      "
no_trailings = third_text.strip(" ")
print(no_trailings) # Output without the extra spaces at start + end

## Split a string
languages = "Python Java C++"
split_languages = languages.split(" ") # it then turns it into an array. each word in this, split with the " " will turn into an object inside of the array 
print(split_languages)

## Count characters
bananas = "Bananas are a great source of Potassium"
print(bananas.count("a"))

## Find length
bananas = "Bananas are a great source of Potassium"
print(len(bananas)) # prints out the number of characters in the string

## Concatenation of strings
a = "It is"
b = "3"
c = "hrs long"

print(a + b + c) # This will print as "It is3hrs long" - because there are no trailing spaces in the variables a, b, c

