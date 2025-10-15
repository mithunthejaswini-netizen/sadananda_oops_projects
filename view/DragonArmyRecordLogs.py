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

        :return: None
        :rtype: NoneType
        """
        for dragon_type, dragon_combat_stats in dragon_army_stats:
            
            average = DragonArmyRecordLogs.get_average_combat_stats(dragon_combat_stats)
            
            print(f'{dragon_type}::({average[0]:.2f}/{average[1]:.2f}/{average[2]:.2f})'  )
            
            for stats in dragon_combat_stats:
                print('\t\t',str(stats))
            
            print('')
                
    @classmethod
    def get_average_combat_stats(cls, dragon_combat_stats):
        
        """
        Compute and optionally display the average combat statistics for each dragon type.

        The method aggregates all combat stats for each dragon type and stores
        their average in a dictionary. Optionally, it prints each stat to stderr
        (or standard output, depending on implementation) if ``print_to_stderr`` is True.

        :param print_to_stderr: If True, prints intermediate stats to stderr (or stdout).
        :type print_to_stderr: bool or None

        :return: A dictionary mapping each dragon type to its computed average combat statistics.
        :rtype: dict
        """
        
        t = ('damage', 'health', 'armor')
        
        average_combat = dict.fromkeys(t, 0.0)
        
        for _stats_obj in dragon_combat_stats:
            stats = list(_stats_obj)
            for name, value in zip(t, stats):
                average_combat[name]+= value
                
        total_length = len(dragon_combat_stats)
        average = (
                average_combat['damage']/total_length, 
                average_combat['health']/total_length, 
                average_combat['armor']/total_length, 
                )

        return average
            
        
        

            
