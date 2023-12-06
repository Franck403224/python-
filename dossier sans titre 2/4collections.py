#4collections.py

# 4.1 PYTHON Lists

fruits = ["kiwi", "pineapple", "apple"]

# 4.1.1 Print the second item in the fruits list.
# TODO: Write your code below
fruits = ["kiwi", "pineapple", "apple"]
print(fruits[1])  # Lists are zero-indexed, so the second item is at index 1

# 4.1.2 Change the value from "kiwi" to "orange", in the fruits list.
# TODO: Write your code below
fruits[0] = "orange"  # Replace the first item (index 0) with "orange"



# 4.1.3 Use the insert method to add "lemon" as the second item in the fruits list.
# TODO: Write your code below

fruits.insert(1, "lemon")  # Insert "lemon" at index 1


# 4.1.4 Use the remove method to remove "pineapple" from the fruits list.
# TODO: Write your code below
fruits.remove('pineapple')
print('pineapple removed from list :', fruits)


# 4.1.5 Use negative indexing to print the last item in the list.
# TODO: Write your code below
print(fruits[-1])

# 4.1.6 Use a range of indexes to print the third, fourth, and fifth item in the list fruits2.

fruits2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# TODO: Write your code below
print(fruits[2:5])

# 4.1.7 Use the correct syntax to print the number of items in the list fruits
# TODO: Write your code below

print(len(fruits))

# 4.1.8  Write a program that add the average of numbers in a list scores.
# you are not allowed to use the sum() or len() functions.

scores = [50, 55, 56, 70, 80, 60, 66]

# TODO: Write your code below
print("originals scores:", scores[:1])
print("average scores:" , scores[:1])

# 4.1.9 Write a program that calculates the highest number in a list scores
# you are not allowed to use the max or min functions.
scores = [50, 55, 56, 70, 80, 60, 66]

# TODO: Write your code below
max = -100
for x in scores:
    if x>max:
        max=x
print('largest number in scores list is: ', max)

# 4.1.10






# 4.2. PYTHON Dictionaries

car =	{
  "brand": "Renault",
  "model": "Clio",
  "year": 2018
}

# 4.2.1 Use the get method to print the value of the "model" key of the car dictionary.
# TODO: Write your code below

print('value for model in car dictionary', car.get('model'))

# 4.2.2 Change the "year" value from 2018 to 2020 in the car dictionary.
# TODO: Write your code below
car["year"]=2020
print("update year:", car["year"] )

# 4.2.3 TODO: Add the key/value pair "color" : "blue" to the car dictionary.
# TODO: Write your code below
car["color"] = "blue"
print('updated dictionary car ', car)


# 4.2.4 Use the pop method to remove "model" from the car dictionary.
# TODO: Write your code below

car.pop('model')
print('model removed from car dict : ',car)

# 4.2.5 Use the clear method to empty the car dictionary.
# TODO: Write your code below
car.clear()
print('cleared car dict :', car)