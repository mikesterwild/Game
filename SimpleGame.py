import numpy as np
import time
import sys
from random import randint


room_list= ['Attic', 'Basement', 'Kitchen', 'Bedroom', 'Bathroom']
list_of_monsters = ['Big', 'Small']
gem_count = 100
health = 100


#welcome screen players see
def Welcome_screen():
    print """\nHello there %s, welcome to The House, the goal of the game is to find the dungeon and slay the etan that has been hiding there for years (you can leave the game at any time by simply typing "quit"). To start off you will be given 100 gems...""" % name
    print "heres the 100$ \n"
    time.sleep(.5)
    print "Bank: " + (str (gem_count) + "$")
    time.sleep(1)

def add_gems(x):
    global gem_count
    gem_count = gem_count + x
    print (str (gem_count) + "$")

def found_gems(x):
    global gem_count
    gem_count = gem_count + x
    print ("You found %s gems! You now have " + str (gem_count)) % x
def minus_gems(x):
    global gem_count
    gem_count = gem_count - x
    print (str(gem_count) + "$")

def lose_gems(x):
    global gem_count
    gem_count = gem_count - x
    print ("You lost %s gems! You now have " + str (gem_count) + "$") % x
def add_health(x):
    global health
    health = health + x
    print ("You've gained %s health, you now have " + str(health)) % x
def minus_health(x):
    global health
    health = health- x
    print ("you've lost %s health, you now have " + str(health)) % x
    if health <= 0:
        time.sleep(1)
        print "You have died"
        death()
good = [ found_gems, add_health ]
def death():
    print "What would you like to do next?"
    print "continue or quit?"
    user_choice = raw_input()
    if user_choice == "continue":
        Welcome_screen()
    else:
        sys.exit("hope you had fun")
bad = [minus_health, lose_gems ]

"""class Weapons(object):
    """"""
    def __init__(self, sowrds, bows, shields):
        self.sowrds = sowrds
        self.bows = bows
        self.shields = shields
    def hit_points(self):
        Sowrds = health - 75
        if user_hit_luck = 1:"""




def what_room():
    print "\n%s what room would you like to enter? Here are all the rooms: Attic, Bathroom, Basement, and the Kitchen ?\n" % (name)
    global user_room
    user_room = raw_input().strip().capitalize()

    if user_room == "Quit":
        sys.exit("Bye hope you had fun!")

    elif user_room not in room_list:
        time.sleep(0.5)
        print ("\nThats not a room try again.")
        time.sleep(0.5)
        what_room()

    else:
        time.sleep(1)
        print "\n..."
        time.sleep(1)
        print "You head towards the %s" % user_room
        time.sleep(2)
        print "..."
        time.sleep(1)

    what_chest()

def what_chest():
    print "\nAs you enter the %s you notice two chests, one to the left of you and one to the right. Which one will you open?\n" % user_room
    user_chest = raw_input().strip()
    if (user_chest == "Left" or user_chest == "left"):
        x = randint(0,16)
        time.sleep(1)
        print "\n..."
        time.sleep(1)
        print "Opening left chest"
        time.sleep(2)
        print "...\n"
        time.sleep(1)
        if (x==0):
            print "Sorry this chest is empty"
        else:
            print "You found %s gems!" % (x)
            add_gems(x)
            time.sleep(1)
    elif (user_chest == "Right" or user_chest == "right"):
        y = randint(0,16)
        print "Oh no a sipder came out and took %s gems!" %(y)
        minus_gems(y)
    elif user_chest == "quit":
        sys.exit("Bye hope you had fun!")
    else:
        print "That's not an option"
    time.sleep(1)
    hallway()

def hallway():
    print "\nYou see two seprate hallways one to your right and one to your left, which one do you enter?\n"
    user_hallway = raw_input().strip()
    if (user_hallway == "left" or user_hallway == "Left"):
        print "You enter the left hallway"
        time.sleep(1)
        bad[randint (0,1)](randint (0,11))
    elif (user_hallway == "Right" or user_hallway == "right"):
        print "You enter the right hallway"
        time.sleep(1)
        good[randint (0,1)](randint (0,11))
    elif user_hallway == "quit":
        sys.exit("Bye hope you had fun!")
    else:
        print "That's not an option %s" % (name)
    time.sleep(1)
    fighting(list_of_monsters[randint(0,1)])

def fighting(monster):
    #needs to subtract certain amount from user_health based on size of monster
    if monster == "Big":
        print "\nWow, a huge monster approaches"
        time.sleep(1)
        "It jumps towards you!"
        time.sleep(1)
        y = randint(24,51)
        if (y == 24):
            print "The huge monster missed!"
        else:
            minus_health(y)
    elif monster == "Small":
        print "\nWow a tiny monster approaches..."
        time.sleep(1)
        print "It attacks!"
        time.sleep(1)
        x = randint(0,16)
        if (x == 0):
            print "The tiny monster missed!"
        else:
            minus_health (x)
    game()

def hit_points():
    user_hit_luck = randint(1,10)
    if user_hit_luck == 1:
        minus_health(bigvalues[randint (0, 10)])
    elif user_hit_luck == (2,3,4,5,6):
        minus_health(smallvalues[randint (0, 23)])
    else:
        print "The enemy missed"

def game():
    while(gem_count<150):
        what_chest()
    print "You win!!!!!"

user= raw_input("\nBefore we start the game I would like to know your name\n")
name = user.capitalize()
name = name.strip()
Welcome_screen()
what_room()
