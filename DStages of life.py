'''
Stages of Life:
 Write an if-elif-else chain that determines a person’s
stage of life.
Collect an input from a user and assign it to the variable age, and then:
• If the person is less than 2 years old, print a message that the person is
a baby.
• If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
• If the person is age 65 or older, print a message that the person is an
elder.
'''
#stages of life
age=int(input('state a person\'s age:\n '))#asks of an input as an integer (will be persons age0
if age <2:#if below 2 it will print 'that person is a baby'
    print('that person is a baby')
elif age <4 :#if below 4 it will print 'that person is a toddler'
    print('that person is a toddler')
elif age <13:#if below 13 it will print 'that person is a kid'
    print('that person is a kid')
elif age <20:#if below 13 it will print 'that person is a teenager'
    print('that person is a teenager')
elif age <65:#if below 65 it will print 'that person is an adult'
    print('that person is an adult')
else:#else will print 'that person is an elder'
    print('that person is an elder')