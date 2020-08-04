dicton = {"John": 10, "Andrew":2}

#print the whole entire dictionary items
#note to print the whole dictionary without the tuple print out
#you have to set two vars that loop and then after your dict name
#add items() to the end , then printing X Y
for x,y in dicton.items():
    print(x,y)

#print only the values
#note with values you have to print the position of the actual loop IE "x"
dicton2 = {"AndyW":13, "Johnny boy": 15}

for x in dicton2:
    print(dicton2[x])

#print only the keys:
#note with keys you just straight up print..easy stuff

dicton3 = {"Wally":22, "Decker": 100}

for i in dicton3:
    print(i)