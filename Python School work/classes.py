# Decalring variables with Specified types
name: str = "Samuel Bassey John"
age: int = 15
height: float = 5.9
print(name, age, height)

# string interpolation using f strings (Implicit format strings)
intro1: str = f"Name: {name} Age: {age}"

# string interpolation with %s
intro2: str = "My name is %s, and my age is %s" % (name, age)

# String interpolation with Explicit Format Method
name = "Samuel"
surname = "Bassey"

intro = " name: {}, surname: {}"
print(intro.format(name, surname))  # name: Samuel, surname: Bassey


# string escaping special characters with backslash \
quote1: str = "The teacher said, \"Don't go to class tomorrow\""

# convert to string
str(age)  # can be assigned to a variable

# convert to int
randomNumber: str = "2000"
int(randomNumber)

# convert to float
float(randomNumber)

# control flow statements
# if, else and else-if statements
if (age >= 18):
    print("Is an adult")
elif (age >= 15 | age <= 18):
    print("This one fit pass sha, but keep your eyes on him")
else:
    print("Is still a child")

# ternary operator # (Perform Action) if (condition if true) else (perform another action)
print("matured young man") if (age >= 18) else print(
    "carry this pikin commot for here")

# Strings in python are arrays of bytes represetning unicode characters
# python doesnt have a Character(char) type so a single character is a string of length 1.
# being an array, we can perform array methods on them.

# length of string
myName: str = "Samuel"
len(myName)  # 6.

myName[2]  # m

# check if a piece of string is in a string.
statement: str = "This is a boy"

"boy" in statement  # true # often wrapped in a print statement

# Slicing a string
# start index inclusive, end index exclusive
statement = "Anthropology"

statement[2:6]  # thro

# slice form beginning to index
statement[:6]  # Anthro

# slice from index to end
statement[6:]  # pology

# Negative indexing
# Negative indexing starts slice from the end
# They start from -1 to -(String length)
statement[-1]  # y
statement[2:-6]  # thro

# some other methods

# UpperCase
statement.upper()  # ANTHROPOLOGY
# Lowercase
statement.lower()  # anthrology

# Split
# this returns a list where the text between the specified separator becomes the list items.
statement = "My name is samuel bassey john"
statement.split(" ")  # ['My', 'name', 'is', 'samuel', 'bassey', 'john']

groceryList = "Today's groceries are: Turkey, meat, cabbage, ketchup, milk, milo, biscuit"
# ['Turkey', ' meat', ' cabbage', ' ketchup', ' milk', ' milo', ' biscuit']
print(groceryList[23:].split(","))

# PYTHON LISTS
names: list(str) = ["Samuel", "Bassey", "John"]
