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
    
    def log_records(self):
            """
        Log each dragon type and its combat statistics.

        This method iterates over the dragon records and prints
        each dragon type followed by its associated combat stats.

        :return: None
        :rtype: NoneType
        """
        
        for dragon_type, dragon_combat_stats in self:
            print(dragon_type)
            
            for stats in dragon_combat_stats:
                print('\t\t',str(stats))
                
    def average_combact_stats(self, print_to_stderr=None):
        
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
        
        average_combact = {}

        for dragon_type, dragon_combat_stats in self:    
            
            first_combact = dragon_combat_stats.pop()
            
            for stats in dragon_combat_stats:
                
                first_combact+= stats
                
                if print_to_stderr:
                    print('\t\t',str(stats))
        
            average_combact[dragon_type] = list(first_combact)
            
            print(average_combact, 'sadananda maharaj')