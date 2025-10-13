from model.DragonArmyRecord import *
from constants_utils.DragonArmyUtils import check_types

class DragonArmyBuilder:

    """
    A builder class responsible for managing and updating the Dragon Army records.

    This class acts as a high-level interface to interact with the `DragonArmyRecord`
    instance. It allows adding or updating dragon combat statistics and displaying
    the overall strength of the army.

    Attributes
    ----------
    dragon_army : DragonArmyRecord
        A shared instance of `DragonArmyRecord` used to store and manage dragon data.
    """
    

    dragon_army = DragonArmyRecord()
        
    @classmethod
    @check_types((str, str, int, int, int))
    def update_dragon_army_record(cls, *args):
    
        """
        Updates the dragon army record with a new or modified dragon entry.

        This method validates the argument types using the `check_types` decorator
        and delegates the update operation to the `DragonArmyRecord` instance.

        Parameters
        ----------
        *args : tuple
            A variable-length tuple containing:
            
            - `_type` (str): The dragon type (e.g., 'Red', 'Blue', etc.).
            - `name` (str): The dragon's name.
            - `combat_stats` (int, int, int): A sequence of three integers representing
              the dragon's damage, health, and armor respectively.

        Raises
        ------
        TypeError
            If argument types do not match the expected types specified in `check_types`.

        Examples
        --------
        >>> DragonArmyBuilder.update_dragon_army_record('Red', 'Inferno', 250, 3000, 50)
        """
        
    
        _type, name, *combat_stats = args
        DragonArmyBuilder.dragon_army(_type, name, *combat_stats)
        
    
    def display_strength(cls):
        """
        
        Displays the total strength or statistics of the dragon army.

        This method delegates the computation and output of army strength
        details to the `DragonArmyRecord.display_strength()` method.

        Returns
        -------
        None
            This method only displays information; it does not return a value.

        Examples
        --------
        >>> DragonArmyBuilder.display_strength()
        Red::Inferno(250,3000,50)
        Blue::Frostwing(180,2500,70)
        
        """
        
        DragonArmyBuilder.dragon_army.display_strength()
