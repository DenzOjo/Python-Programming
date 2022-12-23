'''1. Counting to Twenty: Use a for loop to
print the numbers from 1 to 20,inclusive.

2. One Hundred: Make a list of the numbers from one to one hundred, and then
use a for loop to print the numbers.

3.Summing a hundred: Make a list of the numbers from one to one hundred, and
then use min() and max() to make sure your list actually starts at
one and ends at one hundred.Also, use the sum() function to see how
quickly Python can add a hundred numbers.

4. Odd Numbers: Use the third argument of the range() function to make a
list of the odd numbers from 1 to 20. Use a for loop to print each number.

5. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.

6. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.

7. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.

'''
#1
twenty=[]
for values in range(1,21):
    print(values)
print()
#2
for values in range (1,101):
     print(values)
print()
#3
hundred_two=list(range(1,101))
print(f'the minimum value in the list hundred_two is {min(hundred_two)}')
print(f'the maximum value in the list hundred_two is {max(hundred_two)}')
print(f'the sum of all the items in the list hundred_two is {sum(hundred_two)}')
print()
#4
for values in range (1,21,2):
    print(values)
print()
#5
threes=[values *3 for values in range (1,31)]
print(threes)
print()
#6
for values in range(1, 11):
    print(values**3)
print()
#7
list=[values**3 for values in range(1, 11)]
print(list)
