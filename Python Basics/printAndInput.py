print("What is up and welcome to the basics of python")
name = input("What is your name brother? ")

message = "what's up %s glad you like my github!" % name
print(message)

print("")
#another way of doing it:
secondMessage = "See you later {}".format(name)
print(secondMessage)