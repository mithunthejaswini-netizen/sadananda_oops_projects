import sys
from controller.DragonArmyManager import DragonArmyBuilder
        
sadananda = ['Azure D001 41 231 9',
'Verdant D002 42 232 10',
'Obsidian D003 43 233 11',
'Ivory D004 44 234 12',
'Crimson D005 45 235 13',
'Azure D006 46 236 14',
'Verdant D007 None 237 15',
'Obsidian D008 48 238 16',
'Ivory D009 49 239 17',
'Crimson D010 50 240 18',
'Azure D011 51 None 19',
'Verdant D012 52 242 8',
'Obsidian D013 53 243 None',
'Ivory D014 None 244 10',
'Crimson D015 55 245 11',
'Azure D016 56 246 12',
'Verdant D017 57 247 13',
'Obsidian D018 58 248 14',
'Ivory D019 59 249 15',
'Crimson D020 60 250 16',
'Azure D021 None 251 17',
'Verdant D022 62 None 18',
'Obsidian D023 63 253 19',
'Ivory D024 64 254 8',
'Crimson D025 65 255 9',
'Azure D026 66 256 None',
'Verdant D027 67 257 11',
'Obsidian D028 None 258 12',
'Ivory D029 69 259 13',
'Crimson D030 70 260 14',
'Azure D031 71 261 15',
'Verdant D032 72 262 16',
'Obsidian D033 73 None 17',
'Ivory D034 74 264 18',
'Crimson D035 None 265 19',
'Azure D036 76 266 8',
'Verdant D037 77 267 9',
'Obsidian D038 78 268 10',
'Ivory D039 79 269 None',
'Crimson D040 80 230 12',
'Azure D041 81 231 13',
'Verdant D042 None 232 14',
'Obsidian D043 83 233 15',
'Ivory D044 84 None 16',
'Crimson D045 85 235 17',
'Azure D046 86 236 18',
'Verdant D047 87 237 19',
'Obsidian D048 88 238 8',
'Ivory D049 None 239 9',
'Crimson D050 40 240 10',
'Azure D051 41 241 11',
'Verdant D052 42 242 None',
'Obsidian D053 43 243 13',
'Ivory D054 44 244 14',
'Crimson D055 45 None 15',
'Azure D056 None 246 16',
'Verdant D057 47 247 17',
'Obsidian D058 48 248 18',
'Ivory D059 49 249 19',
'Crimson D060 50 250 8',
'Azure D061 51 251 9',
'Verdant D062 52 252 10',
'Obsidian D063 None 253 11',
'Ivory D064 54 254 12',
'Crimson D065 55 255 None',
'Azure D066 56 None 14',
'Verdant D067 57 257 15',
'Obsidian D068 58 258 16',
'Ivory D069 59 259 17',
'Crimson D070 None 260 18',
'Azure D071 61 261 19',
'Verdant D072 62 262 8',
'Obsidian D073 63 263 9',
'Ivory D074 64 264 10',
'Crimson D075 65 265 11',
'Azure D076 66 266 12',
'Verdant D077 None None 13',
'Obsidian D078 68 268 None',
'Ivory D079 69 269 15',
'Crimson D080 70 230 16',
'Azure D081 71 231 17',
'Verdant D082 72 232 18',
'Obsidian D083 73 233 19',
'Ivory D084 None 234 8',
'Crimson D085 75 235 9',
'Azure D086 76 236 10',
'Verdant D087 77 237 11',
'Obsidian D088 78 None 12',
'Ivory D089 79 239 13',
'Crimson D090 80 240 14',
'Azure D091 None 241 None',
'Verdant D092 82 242 16',
'Obsidian D093 83 243 17',
'Ivory D094 84 244 18',
'Crimson D095 85 245 19',
'Azure D096 86 246 8',
'Verdant D097 87 247 9',
'Obsidian D098 None 248 10',
'Ivory D099 89 None 11',
'Crimson D100 40 250 12']        

def main(args):

    if len(args)==5: # Actual input with (type, name, damage, health, armor)
        try:
            args[2] = int(args[2]) if args[2] != 'None' else None # conver the army stats into integer value
            args[3] = int(args[3]) if args[3] != 'None' else None # conver the army stats into integer value
            args[4] = int(args[4]) if args[4] != 'None' else None # conver the army stats into integer value
        except:
            print('Type does not match')
                 
        _type, name, damage, health, armor = args[0], args[1], args[2], args[3], args[4]
        DragonArmyBuilder().update_dragon_army_record((_type, name, damage, health, armor))
        
    else:    
        if args[0].upper()=='EXIT': # this is to exit and print the average value
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
    
    try:
        for string in sadananda:
            main(string.split(' '))
            #army_details = input('')
    
        main(['exit'])
    except  TypeError as e:
        print(e)
        sys.exit(-1)
    
    