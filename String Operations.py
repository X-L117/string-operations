# String Concatenation (joining strings together)
first_name = "X"
last_name = "L117"
full_name = first_name + "-" + last_name
print("Full name:", full_name)  # Output: X-L117

# String Repetition
echo = "Hello! " * 3
print("Echo:", echo)  # Output: Hello! Hello! Hello!

# Indexing (getting one character by position)
message = "Python"
print("First letter:", message[0])   # Output: P
print("Last letter:", message[-1])   # Output: n

# Slicing (getting part of the string)
print("First 3 letters:", message[0:3])  # Output: Pyt
print("From 3rd letter to end:", message[2:])  # Output: thon

# String Methods
greeting = "hello world"
print("Uppercase:", greeting.upper())        # Output: HELLO WORLD
print("Capitalized:", greeting.capitalize()) # Output: Hello world
print("Replace:", greeting.replace("world", "AK1731"))  # Output: hello AK1731

# Length of string
print("Length:", len(greeting))  # Output: 11

# Check if a substring is in a string
print("Contains 'world'?","world" in greeting)  # Output: True

# String Formatting
name = "AK1731"
language = "Python"
intro = f"My name is {name} and I am learning {language}."
print("Formatted String:", intro)
