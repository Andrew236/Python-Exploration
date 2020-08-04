print("Here we are going to use some conditional statements")

user_choice = int(input("Enter a number between 1 and 10: "))
print(user_choice)
message1 = "You have entered one, now you must die"
if user_choice == 1:
    print("You have entered one so now you are going to die")
elif user_choice == 2:
    print("you have now entered 2 you just won a million Dollars")
else:
    print("Well you didn't guess write so nothing happens")
