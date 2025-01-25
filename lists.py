#a list is a collection of items in a particular order
#names of lists must always be plural.
#[] represent lists.
#(i) individual elements in the list are separated by commas(,)
cars = ['BMW','Benz','Posch','Ford']#string#variable#example
print(cars)

#(ii) YOU CAN ACCESS ANY ELEMENT IN A LIST
cars = ['BMW','Benz','Posch','Ford']#string#variable#example
print(cars[0])#the 1st element is denoted the number zero as interpreted by python

#(iii)
cars = ['BMW','Benz','Posch','Ford']#string#variable#example
print(cars[1].upper())#using what i learned about methods to make the output more neat and with same format.
#if we replaced the'1' with '-1' then python would return 'Ford' as an output

#(iv)
cars = ['BMW','Benz','Posch','Ford']#string#variable#example
message = 'The '+ cars[0]+' is really fast'#string#variable#string concatenation#using one of the elements to construct a sentence.
print(message)

#CHANGING, ADDING AND REMOVING ELEMENTS
#Most lists coded will be dynamic, meaning youll add, and remove elements from the list as the program runs.
#an example is a game whereby you shoot aliens, u could add a set of aliens in a list and remove any when it is shot, when a new alien appears on the screen u add it to the list.

#(v) MODIFYING A LIST.
#the syntax for modifying a list is similar to one for replacing an element, when replacing an element use the name of the list followed by the index of the element to replace then provide a new value for the item to replace
#EXAMPLE
motorcycles = ['honda', 'yamaha', 'suzuki']#variable#list
print(motorcycles)#the list is unchanged

#(vi)
motorcycles = ['honda', 'yamaha', 'suzuki']#variable#list
motorcycles[0] = 'BMW'#name of list and index of the element to change = name to replace with
print(motorcycles)#changed list

#(vii) ADDING ELEMENTS TO A LIST
#elements are addeded for lots of reasons, example would be the aliens in the game.
#APPENDING ELEMENTS TO THE END OF LISTS
#the simplest way is to append an element to the end of a list, this is done by using the .append() method.

cars = ['BMW', 'Benz', 'Porch', 'Ford']#list
cars.append('Toyota')#the append method makes it easier to build lists dynamically.
print(cars)#output is a list with the element 'Toyota' at the end of the list.

#(viii)
cars = []#you can add elements to an empty list
cars.append('BMW')#the append method can add only one item per method
cars.append('toyota')
print(cars)#output list with two elements.

#(ix) INSERTING ELEMENTS TO A LIST
#this is different form adding an element, because when u add an element you just use the .append() method to add it at the end of the list
#when inserting u can choose on which index u wanna insert it, it is inserted using the .insert() method.
cars = ['bmw', 'benz', 'ford', 'porch']#list
cars.insert(0,'toyota')#.insert() method
print(cars)#output list with the toyota brand inserted at the start.

#(x) REMOVING ELEMENTS FROM A LIST
#often u will want to remove an item from a list, an example is when an alien is shot down, then u will have to remove it from the list.
#remove an item using the del statement.
cars = ['BMW', 'Benz', 'Porch', 'Ford']#when u know the position or index of the item u can remove it using the del statement.
del cars[0]#deletes BMW#del statement
print(cars)#output of a list without the 1st item on the list.

#(xi) removing an item using the pop() method.
#used when u wanna use the value of an item after u removed it from the list.
#an example is when u wanna get the x and y position of an alien that was shot down to draw an explosion at that position.
#the .pop() method lets u remove the last item from a list but still be able to work with it afterwards
cars = ['BMW', 'Benz', 'Porch', 'Ford']
print(cars)
#(xii)
popped_cars = cars.pop()
print(cars)#prints cars without the last item.
#(xiii)
print(popped_cars)#prints the popped item.

#one of the useful uses of the pop() method is when we have a colletion of cars in chronological order, then we can use this .pop() method to determine which car we owned last
#(xiv)
cars = ['BMW', 'Benz', 'Porch', 'Ford']
owned_cars = cars.pop()#variable and its value of the last item on the list.
print('The last car i owened was ' + owned_cars + ' and it was beautiful')#string concatination.

#(xv) #POPPING ITEMS FROM ANY POSITION
#u can do this by including the idex of the item in the method.
cars = ['BMW', 'Benz', 'Porch', 'Ford']
nice_cars = cars.pop(0)#index include in the method
print (cars)#executes a list without BMW

#(xvi)
cars = ['BMW', 'Benz', 'Porch', 'Ford']
nice_cars = cars.pop(0)
print('i can argue that the ' + nice_cars + ' is the fastest car among its rivals')

#(xvii)#REMOVING AN ITEM BY VALUE.
#when u don't know the position/index of the item u want to remove u can use its value.
cars = ['BMW', 'benz', 'Porch', 'Ford']
cars.remove('BMW')
print(cars)

#(xviii)
cars = ['BMW', 'Benz', 'Porch', 'Ford']
print(cars)#executes original list
#(xix)
ugly = 'BMW'
cars.remove('BMW')
print(cars)#executes list without BMW because it is ugly
#(xx)
print('\nA ' + ugly + ' is not the car for me')#executes reason for excluding BMW in list.

#EXERCISES
#making a list of names for attendace to dinner
#(xxi)
Dinner = ['lefa', 'lesedi', 'lethabo']
print(Dinner)
#(xxii)
print('\nDear ' + str(Dinner) + ' I, Khutso would like to invite u all to Dinner')
#NOW U HEAR THAT ONE OF UR GUESTS WONT BE ABLE TO MAKE IT, NOW SEND A NEW SET OF INVITATIONS AND SOMEONE ELSE TO INVITE
popped_Dinner = Dinner.pop(0)

Dinner.insert(0, 'kabelo')
#(xxiii)
print('\nUnfortunately ' + popped_Dinner + ' will not make it thus we will now fill the gab with ' + Dinner[0] + ' the new list will be ' + str(Dinner) + '.')
#(xxiv) NOW U FOUND A LARGER TABLE SO U DECIDE TO INVITE MORE PEOPLE, THUS UPDATE THE LIST AND INVITATIONS
print(' \nDear Friends I have found a new larger table therefore I will try and invite others')
Dinner.insert(0,'Solly')
Dinner.insert(0,'Mohale')
Dinner.append('Refilwe')
#(xxv)
print(Dinner)
#(xxvi)
print('\nDear Family, the new set of names in the list is ' + str(Dinner) +', I am Looking forward to seeing u there.')
#(xxvii) NOW U FIND OUT THAT UR NEW TABLE WONT ARRIVE IN TIME FOR THE DINNER THEREFORE U WILL HAVE SPACE FOR ONLY 2 PEOPLE
print('\n\tNew devolopment, it will not be possible to host all of u, due to some inconvenience with the dinner table thus \tonly two people will be able to attend')
#(xxviii)
popped_name = Dinner.pop(2)
print('\n\t' + popped_name + ' I apologise for the inconvenience, but it will no longer be possible to host u, due to unforseen issues.')
#(xxix)
popped_name = Dinner.pop(4)
print('\n\t' + popped_name + ' I apologise for the inconvenience, but it will no longer be possible to host u, due to unforseen issues.')
#(xxx)
popped_name = Dinner.pop()
print('\n\t' + popped_name + ' I apologise for the inconvenience, but it will no longer be possible to host u, due to unforseen issues.')
#(xxxi)
popped_name = Dinner.pop(0)
print('\n\t' + popped_name + ' I apologise for the inconvenience, but it will no longer be possible to host u, due to unforseen issues.')
#(xxxii)
print('\n\tDear Family, Due to certain issues and circumstances all the other fellow FAM members will not join us thus only \tu which is ' + str(Dinner) + ' will join us ' + ' . I look forward to meeting u there.')
print(len(Dinner))


