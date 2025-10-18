# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 20:12:23 2025

@author: meetm
"""

from constants_utils.DragonArmyUtils import *
    
class  DragonArmyCombatStats:

    """
    
    Represents an individual dragon's combat statistics.

    This class encapsulates a dragon's name and key combat attributes,
    including damage, health, and armor. It supports equality checks,
    in-place addition for combining stats, iteration over numerical
    values, and readable string formatting.

    The class uses ``__slots__`` to minimize memory usage by preventing
    the dynamic creation of instance attributes.

    :param name: The name of the dragon.
    :type name: str
    :param damage: The damage value of the dragon. If not provided, a default
                   value from :class:`DragonArmyDefaultStatsEnum` is used.
    :type damage: int or float, optional
    :param health: The health value of the dragon. Defaults to a predefined
                   value if not specified.
    :type health: int or float, optional
    :param armor: The armor value of the dragon. Defaults to a predefined
                  value if not specified.
    :type armor: int or float, optional
    
    """
    
    __slots__ = ('_name', '_damage', '_health', '_armor')

    def __init__(self, name, damage=None, health=None, armor=None) -> None:
        self._name = name
        self._damage = damage
        self._health = health
        self._armor = armor
        
    @property
    def name(self):
        
        """
        Retrieve the dragon's name.

        :return: The name of the dragon.
        :rtype: str
        
        """
        
        return self._name
        
    def __eq__(self, other):
        
        """
        Compare two dragon combat records by name.

        :param other: Another instance of :class:`DragonArmyCombatStats`.
        :type other: DragonArmyCombatStats
        :return: ``True`` if both dragons have the same name, otherwise ``False``.
        :rtype: bool
        
        """
        
        return self._name==other._name
    
    def __hash__(self):
    
        """
        Compute a hash value based on the dragon's name.

        Enables this object to be used in hash-based collections like ``set`` or ``dict``.

        :return: Hash value of the dragon's name.
        :rtype: int
        
        """
        
        return hash(self._name)
    
    def __iadd__(self, comrade):
    
        """
        
        Add another dragon's combat stats to this one, in-place.

        Each corresponding stat (damage, health, armor) is incremented by
        the values from the ``comrade`` instance.

        :param comrade: Another dragon whose stats will be added.
        :type comrade: DragonArmyCombatStats
        :return: The updated instance with aggregated stats.
        :rtype: DragonArmyCombatStats
        
        """
    
        self._damage+= comrade.damage
        self._health+= comrade.health
        self._armor+= comrade.armor
        
        return self
    
    def __iter__(self):
               
        """
        Return an iterator over the dragon's numerical combat stats.

        :return: An iterator over [damage, health, armor].
        :rtype: iterator
        """
              
        return iter([self._damage, self._health, self._armor])
    
    def __str__(self):
        
        """
        Return a human-readable string representation of the dragon's stats.

        :return: A formatted string containing the dragon's name, damage,
                 health, and armor.
        :rtype: str
        """
        
        return f'-{self._name} -> damage : {self._damage}, health: {self._health}, armor: {self._armor}'

    
class DragonArmyRecord(metaclass=Singleton):
        
    __slots__ = ('army_type', 'average_stats')

    def __init__(self):
        
        self.army_type = {}        
        self.average_stats = dict()

    def __call__(self, _type, name, *combat_stats):
    
        """
        Add or update a dragon's combat record within the army data.

        This magic method allows the instance to be called like a function,
        simplifying the process of inserting or updating dragon combat statistics.
        If a dragon of the given type already exists, its record is updated;
        otherwise, a new entry is created and stored.

        Example usage::

            army = DragonArmyRecord()
            army("Fire", "Blazegon", 100, 2500, 30)

        :param _type: The dragon type or category (e.g., "Fire", "Ice").
        :type _type: str
        :param name: The name of the dragon whose record is to be added or updated.
        :type name: str
        :param combat_stats: Variable-length sequence of combat statistics
                             (e.g., damage, health, armor).
        :type combat_stats: tuple

        :return: None
        :rtype: NoneType
        """
        
        damage = DragonArmyDefaultStatsEnum.damage.value if not combat_stats[0] else combat_stats[0]
        health = DragonArmyDefaultStatsEnum.health.value if not combat_stats[1] else combat_stats[1]
        armor = DragonArmyDefaultStatsEnum.armor.value if not combat_stats[2] else combat_stats[2]
        
        if _type in self.army_type:
            
            combat_record = self.army_type[_type]
            new_record = DragonArmyCombatStats(name.capitalize(), damage, health, armor)
            
            if new_record in combat_record:
                combat_record.remove(new_record)
            combat_record.append(new_record)            
            self.army_type[_type] = combat_record
            
        else:
            _set = list()
            _set.append(DragonArmyCombatStats(name, damage, health, armor))
            self.army_type[_type] = _set
            
        self._sort_dragon_army_records()
            
    def _sort_dragon_army_records(self):
        """
        Sorts the dragon records in each army type by name.

        This method iterates over all army types stored in the ``self.army_type`` 
        dictionary and sorts the list of dragon objects associated with each type 
        alphabetically based on their ``name`` attribute.

        Notes
        -----
        - The method modifies ``self.army_type`` in place.
        - It assumes each element in the lists is an object with a ``name`` attribute.

        Example
        -------
        Suppose ``self.army_type`` is:
        {
            "RED": [Dragon(name="Zoltan"), Dragon(name="Arthas")],
            "BLUE": [Dragon(name="Mira"), Dragon(name="Balin")]
        }

        After calling this method:
        {
            "RED": [Dragon(name="Arthas"), Dragon(name="Zoltan")],
            "BLUE": [Dragon(name="Balin"), Dragon(name="Mira")]
        }
        """

        for key in self.army_type:
            l = self.army_type[key]
            self.army_type[key] = sorted(l, key=lambda x: x.name)

    def get_average_stats_by_type(self, _type):
    
        """
        Computes the average combat statistics for dragons of a given army type.

        Parameters
        ----------
        _type : str
            The type of dragon army for which average statistics are to be computed.
            Must be a valid key in ``self.army_type``.

        Returns
        -------
        list of float
            A list containing the average values of each combat statistic 
            (e.g., attack, defense, health). If there is only one or zero 
            dragons of the given type, the method returns their raw or zeroed stats.

        Notes
        -----
        - Each dragon in ``self.army_type[_type]`` is expected to be iterable 
          (e.g., a list or tuple) containing numerical stats.
        - The method sums corresponding indices across all dragons and divides 
          by the total number of dragons to compute averages.

        Example
        -------
        >>> self.army_type["RED"] = [
        ...     [100, 200, 300],
        ...     [150, 250, 350]
        ... ]
        >>> self.get_average_stats_by_type("RED")
        [125.0, 225.0, 325.0]
        """
        
        total_length = len(self.army_type[_type])
        
        army_combat = self.army_type[_type]
        average = [0] * 3

        for combats in army_combat:
            for index, stats in enumerate(combats):
                average[index]+= stats 
        
        average = average if total_length <= 1 else [stat/total_length for stat in average]
        return average        
            
    def __iter__(self):
    
        """
        Return an iterator object for traversing dragon army records.

        This is a mandatory magic method that enables the class to be iterable.
        It returns an instance of :class:`DragonArmyRecordIterator`, which handles
        the actual iteration logic over the dragon army data.

        Typically, you implement this method when defining a custom iterator
        class externally and need your container class to delegate iteration
        to that external iterator.

        :return: An iterator object capable of traversing the dragon army records.
        :rtype: DragonArmyRecordIterator
        """
    
        return DragonArmyRecord.DragonArmyRecordIterator(self.army_type)
        
    def display_strength(self):
    
        """
        This method actually displays the strength of the Army
            prints the total output of the army including the army type, name and combat stats
        
        :return: None
        :rtype: None
        
        """
    
        for dragon_type, dragon_combat_stats in self:
            print(dragon_type)
            
            for stats in dragon_combat_stats:
                print('\t\t',str(stats))
        
    class DragonArmyRecordIterator:

        """
        An iterator class for traversing dragon army records.

        This iterator sequentially yields each dragon type and its corresponding
        combat statistics from a given record (a dictionary-like structure).
        It maintains its own internal index to track iteration progress.

        :param army_record: A mapping of dragon types to their combat statistics.
        :type army_record: dict
        
        """        
        
        def __init__(self, army_record):
            self.army_record = army_record
            self._iterator_index = 0
        
        def __iter__(self):
            
            """
            
            It is an magic method used for iterator protocol
            :return: None
            :rtype: instance itself for iterator protocol
            
            """
            
            return self
        
        def __next__(self):
               
            """
            
            It is an magic method used for iterator protocol
            This will iterate over all the dictionary elements and return in key value pair
            :return: None
            :rtype: tuple (key, )
            
            """
                
            key = None
            if self._iterator_index < len(self.army_record):
                key = list(self.army_record.keys())[self._iterator_index]
                self._iterator_index+= 1
            else:
                raise StopIteration
    
            return key, self.army_record[key]