import random#imports a set of functions (random)
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1', '2','3','4','5','6','7','8','9']
symbols=['!','"','£','$','%','^','&','*','(',')','@']
#list of leters numbers and symbols that will be mixed to create a passwords
print('welcome to the password generator!')#welcome statement

nr_letters=int(input('how many letters would you like in your password?\n'))#ask how many letters and numbers and symobls in the pass that u would like
nr_numbers=int(input('how many numbers would you like in your password?\n'))
nr_symbols=int(input('how many symbols would you like in your password?\n'))

password_letter=[]
for number in range (0,nr_letters):
    random_letter=letters[random.randint(0,len(letters)-1)]#does a loop to make all the letters or numbers or symbols to randomize
    password_letter+=(random_letter)

password_number=[]
for number in range (0,nr_numbers):
    random_number=numbers[random.randint(0,len(numbers)-1)]
    password_number+=(random_number)

password_symbol=[]
for number in range (0,nr_symbols):
    random_symbol=symbols[random.randint(0,len(symbols)-1)]
    password_symbol+=(random_symbol)

password=password_number+password_symbol+password_letter#adds all the pieces for the pass together

random.shuffle(password) #shuffles the elements in the list password


password_ = ""
for i in password:#removes all the commas and quotation markss
    password_+=i
print(f'here is your password {password_}')#gives you the password