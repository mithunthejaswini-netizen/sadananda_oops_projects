class DragonArmyRecordLogs:
    """
    Manage and display records of dragon army combat statistics.

    This class is designed to iterate through collections of dragon types
    and their associated combat statistics, allowing you to print the
    records and calculate average combat values.

    It assumes that the class or its instances implement the iterator
    protocol (`__iter__` method) that yields tuples of
    (dragon_type, dragon_combat_stats).
    """
    
    @classmethod
    def log_records(cls, dragon_army_stats):
        """
        Log each dragon type and its combat statistics.

        This method iterates over the dragon records and prints
        each dragon type followed by its associated combat stats.
        
        :param dragon_army_stats: DragonArmyRecord which holds the records of all the armies based on the type as a key
        :type  dragon_army_stats: DragonArmyRecord
        :return: None
        :rtype: NoneType
        """
        for dragon_type, dragon_combat_stats in dragon_army_stats:
            
            average = dragon_army_stats.get_average_stats_by_type(dragon_type)
            
            print(f'{dragon_type}::({average[0]:.2f}/{average[1]:.2f}/{average[2]:.2f})'  )
            
            for stats in dragon_combat_stats:
                print('   ',str(stats))
            
            print('')
                
 
            
        
        

            
