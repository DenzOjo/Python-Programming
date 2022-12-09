'''
#Creating a list
Create a list of 10 different elements (must contain all basic datatypes i.e integers, floats, strings, booleans)

#Accessing elements in a list
print out the 2nd,
                         4th,
       and last element on your list

#Applying methods to elements in a list
- apply upper method to 2 different strings in the list
- apply lower method to 2 different strings in the list

#List slicing
- slice from the first element to the 6th element on the list and print out
- slice from the 7th element to the last element on the list and print out
- slice from  the 4th element to the 8th element on the list

#Adding elements to a list
- add the string 'Luminous' to the list
- add the string 'Formal' to the 7th position in the list
- add both 'Joy', and 'Love' to the list at the same time
- add integer 200 to the 3rd position on the list

#Removing elements from/items from a list
- remove 'Joy' from the list
- remove the 4th to the 7th element from the list
'''
print()
#list
hw_list=[1, 1.5, 'string', 'string2', True, False, 'element', 'element2', 2, 2.5]
print()
#Acessing elemnts in a list
print(hw_list[1])
print(hw_list[3])
print(hw_list[-1])
print()
#Applying methods to elements in a list
print(hw_list[2].upper())
print(hw_list[3].upper())
print(hw_list[6].lower())
print(hw_list[7].lower())
print()
#list slicing
print(hw_list[0:7])
print(hw_list[7:])
print(hw_list[4:9])
print()
#adding elements to a list
hw_list.append('luminous')
print(hw_list)
hw_list.insert(6,'formal')
print(hw_list)
hw_list.extend(['Joy','love'])
print(hw_list)
hw_list.insert(2,200)
print (hw_list)
print()
#removing elements from/items frpm a list
del hw_list[-2]
print(hw_list)
del hw_list[3:7]
print(hw_list)







print()
'''4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
4-2. Animals: Think of at least three different animals that have a common characteristic.
Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.
• Modify your program to print a statement about each animal, such as
A dog would make a great pet.
• Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet!
'''
print()
pizzas=['pepperoni','mozerella','chicken fiesta']
for names in pizzas:
    print(names)
    print(f' my favourite pizza is {names}')
print('i like all the three choices')
print ()
animals=['leopard','cheetah','lion']
for names in animals:
    print(names)
    print(f'a {names} would probably make terrible pets and destroy your home')
print(f'Any of this animals would shred you to pieces and eat you alive')
print('These animals all'
      ' have a similarity which is that they\'re all part of the large cat group')