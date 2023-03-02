'''
FizzBuzz is a challenge that involves writing code that labels;

numbers divisible by three as “Fizz,”
numbers divisible by five as “Buzz”
and numbers divisible by both 3 and 5 as “FizzBuzz.”
'''
for num in range (1,101):
    if num % 3==0 and num % 5==0:
        print('Buzz')
    elif num % 3 == 0:
        print('Fizz')

    elif num % 5 == 0:
     print('FizzBuzz')

    else:
        print(num)
