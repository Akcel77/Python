from random import randint
 
# Pick a Number
just_price = randint(1, 1000)  
 
#For while loop
running = True
 
# while loop
while running :
    user_price = int(input("Entrer un prix : "))
    if user_price == just_price :
        print('Felicitations vous avez trouve le juste prix')
        running = False
    elif user_price > just_price:
        print("C'est moins")
    elif user_price < just_price:
        print("C'est plus")
print('Press')
