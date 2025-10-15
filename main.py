import sys
from controller.DragonArmyManager import DragonArmyBuilder
        
def main(args):

    if len(args)==5:        
        try:
            args[2] = int(args[2]) if args[2] != 'None' else None
            args[3] = int(args[3]) if args[3] != 'None' else None
            args[4] = int(args[4]) if args[4] != 'None' else None
        except:
            print('Type does not match')
                 
        _type, name, damage, health, armor = args[0], args[1], args[2], args[3], args[4]
        DragonArmyBuilder().update_dragon_army_record((_type, name, damage, health, armor))
        
    else:    
        if args[0].upper()=='EXIT':
            print('')
            print('DRAGON ARMY COMBAT STATS')
            print('')
            DragonArmyBuilder().display_strength()
            sys.exit(1)
    
if __name__=='__main__':  

    print('')
    print('Enter the Dragon Army Details')
    print('ARMY TYPE -: ARMY NAME  |  DAMAGE  |  HEALTH | ARMOR')
    print('')
    
    while True:
        try:
            army_details = input('')
            main(army_details.split(' '))
        except  TypeError as e:
            print(e)
            sys.exit(-1)
    
    