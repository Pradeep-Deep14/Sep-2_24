# Original dictionary
d = {"name": "hello"}

# Get the value from the dictionary
word = d["name"]

# Create a new dictionary with each character as the key and "hello" as the value
new_dict = {x: word for x in word}

print(new_dict)


#{'h': 'hello', 'e': 'hello', 'l': 'hello', 'o': 'hello'}
