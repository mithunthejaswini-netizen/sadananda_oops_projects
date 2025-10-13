import argparse

from controller.DragonArmyManager import DragonArmyBuilder

def build_argument_parse():

    parser = argparse.ArgumentParser(
                                    prog='Dragon Army',
                                    description='Create or update a Dragon Army unit with defined battle attributes.',
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter
                                    )
    parser.add_argument(
                        'army_type', 
                        metavar='army_type',
                        help='type of the dragon army (usually color name) : (str)'
                        )
                        
    parser.add_argument(
                        'name', 
                        metavar='name',
                        help='Name of the dragon army : (str)'
                        )
                        
    parser.add_argument(
                        'damage', 
                        type=int,
                        metavar='dmage',
                        help='dmage of the dragon army'
                        )
    parser.add_argument(
                        'health', 
                        type=int,
                        metavar='health',
                        help='health of the dragon army'
                        )
                        
    parser.add_argument(
                        'armor',
                        type=int,                    
                        metavar='armor',
                        help='armor of the dragon army'
                        )
    return parser
    
def main(*args):
                
    DragonArmyBuilder().update_dragon_army_record(*args)
    DragonArmyBuilder().display_strength()
 
if __name__=='__main__':  
         
    parser = build_argument_parse()
    args = parser.parse_args()
    try:
        main(args.army_type, args.name, args.damage, args.health, args.armor)
    except  TypeError as e:
        print(e)
        system.exit(-1)
    
    