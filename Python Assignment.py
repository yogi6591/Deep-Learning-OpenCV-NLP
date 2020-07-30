# Write a program which will find all such numbers which are divisible by 7 but
# are not a multiple of 5 btwn 2000 and 3200

for num in range(2000,3200+1):
    if num%7==0 and num%5!=0:
        print(num,end=',')

# Write a Python program to accept the user's first and last name and then getting them
# printed in the the reverse order with a space between first name and last name.

FirstName = input('Enter your first name')
LastName = input('Enter your last name')
name = ''
name += FirstName + ' '
name +=LastName
print(name[::-1])

# Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r 3

dia = 12
volume =  (4/3) * (3.14) * (dia**3)
print(volume)

