from constants import PLAYERS #imports PLAYERS List to this file
from constants import TEAMS #imports TEAMS List to this file

Players = PLAYERS.copy() #sets a copy of list to a new variable, Jamar Slade
Teams = TEAMS.copy()



def menu():
    print('BASKETBALL TEAM STATS TOOL\n')
    print('\n----MENU----')
    print("""
    Here are your choices :
    A) Display Team Stats
    B) Quit
        """)



def menu_option():
    print("""
    Here are your choices :
    A) Panthers
    B) Bandits
    C) Warriors
        """)



Panthers = []
Bandits = []
Warriors = []
experienced_players = []
new_players = [] 

def clean_data():# this portion works
    for player in Players:#Cody_academy google search
        #print (player['name'])
        #print (player['guardians'])
        if player['experience'] == 'YES':
            experienced_players.append(player['name'])
            player['experience'] = True
        else:
            new_players.append(player['name'])
            player['experience'] = False
        #print (player['experience'])#should be true or false
        height, unit = (player['height']).split(" ")#separates the digits and "inches from list"
        height = int(height)
        #print(height)
    #print("These are the experienced players: \n {}".format(experienced_players))
    #print("These are the new players: \n {}".format(new_players))



def balance_teams():
    max_Eplayers = len(experienced_players)/len(Teams)
    max_Nplayers = len(new_players)/len(Teams)+3 #This is because there are 3 players already
    for player in experienced_players: #So the experienced part works
        if len(Panthers) < max_Eplayers:
            Panthers.append(player)
            #print("These are the Panthers: {}".format(Panthers))
        elif len(Bandits) < max_Eplayers:
            Bandits.append(player)
           # print("These are the Bandits: {}".format(Bandits))
        else :
            Warriors.append(player)
            #print("Warriors: {}".format(Warriors))
    for player in new_players: #So the experienced part works
        if len(Panthers) < max_Nplayers:
            Panthers.append(player)
            #print("These are the Panthers: {}".format(Panthers))
        elif len(Bandits) < max_Nplayers:
            Bandits.append(player)
            #print("These are the Bandits: {}".format(Bandits))
        else :
            Warriors.append(player)
            #print("Warriors: {}".format(Warriors))


def Panther_Team():
    print("Team : Panthers Stats")
    print("----------------------")
    print("Total players: {}".format(len(Panthers)))
    print("\n PLayers on Team:")
    separator = ", "
    print(separator.join(Panthers))#To get rid of brackets when printing list



def Bandit_Team():
    print("Team : Bandits Stats")
    print("----------------------")
    print("Total players: {}".format(len(Bandits)))
    print("\n PLayers on Team:")
    separator = ", "
    print(separator.join(Bandits))



def Warrior_Team():
    print("Team : Warriors Stats")
    print("----------------------")
    print("Total players: {}".format(len(Warriors)))
    print("\n PLayers on Team:")
    separator = ", "
    print(separator.join(Warriors))



if __name__ == '__main__': #Checks if this is the local file being run
    clean_data()
    balance_teams()
    while True:
        try:
            menu()
            Choice = input("Enter option: ")
            if Choice != "A" and Choice != "B":
                raise ValueError ("Your choices are A or B")
        except ValueError as error:
            print("{}".format(error))
        else:
            if Choice == "B":
                break
            try:
                menu_option()
                Option = input("Enter option: ")
                if Option != "A" and Option != "B" and Option != "C":
                    raise ValueError ("Your choices are A or B or C")
            except ValueError as err:
                print("{}".format(err))
            else:
                if Option == "A":
                    Panther_Team()
                    break
                elif Option == "B":
                    Bandit_Team()
                    break
                else:
                    Warrior_Team()
                    break
