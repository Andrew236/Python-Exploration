#loop fun
#looping through a list

#for loop style

loop_list1 = [1,2,3,4,5]

for count in loop_list1:
    print(count)

print("Now here is printing that list from 1 - 3")

#fix this 

#print first three elements of a list
#the start prints without the brackets of the list
print(*loop_list1[:3])

#here is how to do the same thing using a for loop :)
for x in loop_list1[:3]:
    print(x)

#print every other element in an array
print('\n')
print("Here we are printing every other item in the list")
for x in loop_list1[::2]:
    print(x)

#loop through the list and only print odd numbers
print('\n')
print("Here we will loop through a list and only print odd numbers")

for x in loop_list1:
    if(x % 2 != 0):
        print(x)
    

#same thing with even 

print('\n')
print("Here we will loop through a list and only print even numbers")

for x in loop_list1:
    if(x % 2 == 0):
        print(x)

#here is an example of a while loop in action
print('\n')
print("Here is an example of a basic while loop")
dog = 2

while dog < 5:
    print("Dog is still young")
    dog +=2

print("Dog is old now ")