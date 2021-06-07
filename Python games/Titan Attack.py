#Code By Axel Diagne
#01/10/2019

#Attack on Titan




#The fight is in 4 attacks ( 2 times player 1, 2 times player 2)
#The attack have one luck to miss and one to hit
#At the end the player with more health win

#We must explain each attack by a print ( the player have to understand what's happend)


import random

def welcome_message():
    """
    display instructions of the game
    """
    print("Hi, welcome to Attack on Titan")
    
    print("\
    \n This game is a 1 vs 1 game\
    \n Each player have 250 health point (HP)\
    \n It's a turn by turn game, in 4 attacks\
    \n 2 attacks per player\
    \n You can miss the hit and you can attack to (0 damage) and hit a critical attack max (100)\
    \n The player with the higher health at the end win.\
    \n Good luck !")
    print("")
    print("")

def player_name():
    """
    Ask the user to enter a player name
    """
       
    player = input("Hello Player, please enter your name: ")
    print("Welcome {}, be ready for the fight !".format(player))
    return player

def start_fight():
    """
    display message to informe the user the start fight
    """
    print(" \
    \n \t Fight Start\
    \n ")
    
def attack():
    """
    define a number between 1 and 0 to know if the player hit or no if random attack is True define a number between 0 and 100
    """
    random_attack = random.randint(0,1)
    random_attack = bool(random_attack)
    
    
    if random_attack == True:
        random_damage = random.randint(0, 100)
        return random_damage
    else:
        print("You miss the hit, Unlucky this turn")
        return False
    
    
def damage(attack):
    """
    Conditional statement to return a message. The message is in function of the attack
    """
    if attack >= 1 or random_damage < 100:
        return ("Good job , you inflict {} damage.".format(attack))
            
    elif attack == 100:
        return ("Amazing, critical hit minus {} hp .".format(attack))
        
    else:
        return ("You inflict {} damage, next time try to hit stonger.".format(attack))

def damage_to_hp(hp, damage):
    """
    return an integer equal to health point - damage
    """
    return int( hp - damage )


#Game Start
welcome_message()

#player 1 name and hp start
player_one = player_name()
player_one_hp = 250

print("")

#player 2 name and hp start
player_two = player_name()
player_two_hp = 250


start_fight()

input()
#Attack 1

print("Attack one from {} to {} :".format(player_one, player_two))
print("")

attack_one = attack()

if attack_one == False:
    pass
else:
    attack_one = int(attack_one)
    damage_done = damage(attack_one)
    print(damage_done)
    
    hp_left_two = damage_to_hp(player_two_hp, attack_one)    
    player_two_hp = hp_left_two
    
print("{} have {} hp left".format(player_two, player_two_hp))

input()
#Attack 2

print("")
print("Attack two from {} to {} :".format(player_two, player_one))
print("")

attack_two = attack()

if attack_two == False:
    pass
else:
    attack_two = int(attack_two)
    damage_done = damage(attack_two)

    print(damage_done)
    hp_left = damage_to_hp(player_one_hp, attack_two)
    player_one_hp = hp_left
    
print("{} have {} hp left".format(player_one, player_one_hp))

input()
#Attack 3

print("")
print("Attack three from {} to {} :".format(player_one, player_two))
print("")

attack_three = attack()

if attack_three == False:
    pass
else:
    attack_two = int(attack_three)
    damage_done = damage(attack_three)

    print(damage_done)
    hp_left_two = damage_to_hp(player_two_hp, attack_three)
    player_two_hp = hp_left_two
    
print("{} have {} hp left".format(player_two, player_two_hp))

input()
#Attack 4

print("")
print("Attack two from {} to {} :".format(player_two, player_one))
print("")

attack_four = attack()

if attack_four == False:
    pass
else:
    attack_two = int(attack_four)
    damage_done = damage(attack_four)

    print(damage_done)
    hp_left = damage_to_hp(player_one_hp, attack_four)
    player_one_hp = hp_left
    
print("{} have {} hp left".format(player_one, player_one_hp))

input()
print("\n FIGHT END !\n")
print("{} : {} HP / {} : {} HP".format(player_one, player_one_hp, player_two, player_two_hp))

if player_one_hp > player_two_hp:
	print("{} win the fight !".format(player_one))
elif player_one_hp < player_two_hp:
	print("{} win the fight !".format(player_two))
else:
	print("Draw !")

print("End of program")



