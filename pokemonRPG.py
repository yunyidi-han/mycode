#!/usr/bin/python3
from random import randint 

# Yunyidi Han
# Making a pokemon battle game, objective is to level up enough to defeat the Gym Leader in Vermillion Gym

def showInstructions():
    #print a main menu and the commands
    print('''
Welcome to Pokemon!
========
Commands:
  go [direction]
  talk [item]
========
You're objective is to beat the
Vermillion Gym Leader!
========
Defeat Wild Pokemon, get items, level up!
''')

def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see ' + rooms[currentRoom]['item'])
    print("---------------------------")

#an inventory, which is initially empty
inventory = []

enemies = [{'Onyx':'ground'},{'Pigdy':'flying'},{'Bellsprout':'grass'},{'Growlith':'fire'},{'Psyduck':'water'}]


#combat script using methods, passed into it the player, enemy from above, and element for that enemy
def combat(player,enemy,element):
    enemyPokemon = Pokemon(randint(2,4),element)

    while enemyPokemon.get_hp > 0 and player.get_hp > 0:
        if player.get_hp > 0:
            playerTurn(player,enemyPokemon)
        else: 
            return False
        
        if enemyPokemon.get_hp > 0:
            enemy(turn)
        else:
            xp = randint(7,13)
            print(f"You defeated a level {enemyPokemon.get_level} {enemy} and gained {xp} exp!")
            player.get_exp(xp)
            return(True)


def playerTurn(player,enemyPokemon):
    action = input("Do you want to [attack] or use an [item]? >").lower()
    if action == 'attack':
        move = ''
        while move not in player.get_moveSet.keys(): #gotta validate this works
            move = input(f"What move do you want to use {player.get_moveSet}? >")
#left off around here... :< sad day        

def enemyTurn(player,enemyPokemon):
    pass


    
#bunch of classes and subclasses for player/enemies
#base player stats
class Pokemon():
    def __init__(self,name,level,element):
        self.name = name
        self.level = level
        self.element = element
        self.hp = self.level * 10
        self.experience = 0
        self.moveSet = [{'Tackle': 10}]
    
    def get_hp(self):
        return self.hp
    
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_element(self):
        return self.element
    
    def get_moveSet(self):
        return self.moveSet
        
    def use_nurse(self):
        self.hp = self.level * 10

    def use_potion(self):
        if 'potion' in inventory:
            inventory.remove('potion')
            self.hp += 20
            if self.hp > self.level*10:
                self.hp = self.level*10
            print(f"You used a potion and healed 20 HP! You're HP is now {self.hp}!")
       
    def use_fullHeal(self):
        if 'full heal' in inventory:
            inventory.remove('full heal')
            self.hp = self.level*10
            print(f"You used a full heal! You're HP is now {self.hp}!")
            
#next 3 subclasses are for players to pick
class Baulbasaur(Pokemon):
    def __init__(self):
        self.name = "Baulbasaur"
        self.element = 'grass'
        self.level = 5
        self.hp = self.level * 10
        self.experience = 0
        self.moveSet = [{'Tackle': 10}]
        self.damageUp = ['ground','water']
        self.damageDown = ['flying','fire']
                
    def get_exp(self, xp):
        self.experience += xp
        print(f"You gained {xp} experience! You have {xp}/20 experience!")
        if self.experience >= 20:
            self.level += 1
            print(f"You leveled up! You're now level {self.level}!")
            if self.level == 6:
                self.moveSet.append({"Vine whip", 20})
                print("You learned Vine whip: (20) damage!")

class Charmander(Pokemon):
    def __init__(self):
        self.name = "Charmander"
        self.element = 'fire'
        self.level = 5
        self.hp = self.level * 10
        self.experience = 0
        self.moveSet = [{'Tackle': 10}]
        self.damageUp = ['grass']
        self.damageDown = ['water','ground']
                
    def get_exp(self, xp):
        self.experience += xp
        print(f"You gained {xp} experience! You have {xp}/20 experience!")
        if self.experience >= 20:
            self.level += 1
            print(f"You leveled up! You're now level {self.level}!")
            if self.level == 6:
                self.moveSet.append({"Ember", 20})
                print("You learned Ember: (20) damage!")

class Squirtle(Pokemon):
    def __init__(self):
        self.name = "Squirtle"
        self.element = 'water'
        self.level = 5
        self.hp = self.level * 10
        self.experience = 0
        self.moveSet = [{'Tackle': 10}]
        self.damageUp = ['fire','ground']
        self.damageDown = ['grass']
                
    def get_exp(self, xp):
        self.experience += xp
        print(f"You gained {xp} experience! You have {xp}/20 experience!")
        if self.experience >= 20:
            self.level += 1
            print(f"You leveled up! You're now level {self.level}!")
            if self.level == 6:
                self.moveSet.append({"Bubble", 20})
                print("You learned Bubble: (20) damage!")
                
        

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Oak\'s Lab' : {
                  'south' : 'Poke Center',
                  'north'  : 'Short Grass',
                  'item'  : 'Prof Oak'
                },
            'Poke Center' : {
                  'north' : 'Oak\'s Lab',
                  'item'  : 'Nurse Joy',
                },
            'Short Grass' : {
                  'west' : 'Tall Grass',
                  'south': 'Oak\'s Lab',
                  'item' : 'Wild Pokemon',
                  'north' : 'Forest',
               },
            'Tall Grass' : {
                  'east' : 'Short Grass',
                  'item' : 'Rare Pokemon'
            },
            'Forest' : {
                  'north' : 'Vermillion Gym',
                  'south' : 'Short Grass',
                  'item' : 'Wild Pokemon'
               },
            'Vermillion Gym' : {
                  'south' : 'Forest',
                  'item' : 'Gym Leader Didi',
            }
         }

#start the player in the Hall


def pickPokemon():
    player1 = ''
    print("La la de da some text to introduce the game")
    starter = input("Which starter do you choose? [Baulbasaur, Charmander, Squirtle] > ").lower()
    if starter == 'charmander':
        return Charmander()
    elif starter == 'baulbasaur':
        return Baulbasaur()
    elif starter == 'squirtle':
        return Squirtle()



#loop forever
def main():
    global currentRoom 
    currentRoom = 'Oak\'s Lab'
    showInstructions()
    player = pickPokemon()
    while True:

        showStatus()
        
        win = 0

      #get the player's next 'move'
      #.split() breaks it up into an list array
      #eg typing 'go east' would give the list:
      #['go','east']
        move = ''
        while move == '':
            move = input('>')

      # split allows an items to have a space on them
      # get golden key is returned ["get", "golden key"]          
        move = move.lower().split(" ", 1)

      #if they type 'go' first
        if move[0] == 'go':
        #check that they are allowed wherever they want to go
            if move[1] in rooms[currentRoom]:
          #set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
            else:
                print('You can\'t go that way!')

      #if they type 'get' first
        if move[0] == 'talk' :
        #if the room contains an item, and the item is the one they want to get
            if move[1] in rooms[currentRoom]['item'].lower() and move[1] == 'prof oak':
                talkOak()
            elif move[1] in rooms[currentRoom]['item'].lower() and move[1] == 'nurse joy':
                talkJoy(player)
            elif move[1] in rooms[currentRoom]['item'].lower() and move[1] == 'wild pokemon':
                fightPokemon()
            elif move[1] in rooms[currentRoom]['item'].lower() and move[1] == 'rare pokemon':
                fightRare()
            elif move[1] in rooms[currentRoom]['item'].lower() and move[1] == 'gym leader didi':
                win = fightDidi()
            else:
          #tell them they can't get it
                print('Can\'t talk to ' + move[1] + '!')

def talkOak():
    print(f"Prof Oak seems kinda pissed he had to give you a free Pokemon, he doesn't want to talk")
    
def talkJoy(player):
    heal = input(f"Hey Pokemon Trainer! Want to heal your Pokemon to full? Y/N > ").lower()
    if heal == 'y':
        player.use_nurse
        print(f"{player.get_name} was healed to full! HP is {player.get_hp}")
    else:
        print("Why did you even come here... :[")
          
      
        
if __name__ == "__main__":
    main()
