from enum import IntEnum
from functools import wraps

class DragonArmyDefaultStatsEnum(IntEnum):
    
    """
    Enumeration defining the default combat statistics for dragons.

    Each member represents a standard base value used when
    creating or initializing dragon entities.

    :ivar damage: Default attack power value for a dragon.
    :vartype damage: int
    :ivar health: Default health points for a dragon.
    :vartype health: int
    :ivar armor: Default defense (armor) value for a dragon.
    :vartype armor: int

    **Example Usage**::

        base_health = DragonArmyDefaultStatsEnum.health
        print(f"Default dragon health: {base_health}")

    .. note::
        These values serve as standardized defaults. They may be overridden
        during dragon creation or gameplay logic.
    """
    
    damage = 45 
    health = 250
    armor = 10
    
class Singleton(type):

    """
    Metaclass implementing the Singleton design pattern.

    Ensures that only one instance of any class using this metaclass
    can ever exist. Subsequent instantiation attempts return
    the same object reference.

    **Example Usage**::

        class DragonManager(metaclass=Singleton):
            pass

        a = DragonManager()
        b = DragonManager()
        assert a is b  # ✅ True — both refer to the same instance

    """
    
    def __call__(cls,  *args, **kwargs):
        
        """
        Creates or returns the existing Singleton instance.

        :param args: Positional arguments to be passed to the class constructor.
        :type args: tuple
        :param kwargs: Keyword arguments to be passed to the class constructor.
        :type kwargs: dict
        :return: The single shared instance of the class.
        :rtype: object
        
        """
        
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*args, **kwargs)
            
        return cls._instance

def check_types(_types=(int,)):

    """
    Decorator factory for enforcing runtime type checks on method arguments.

    Ensures that the arguments passed to a method match the expected data types.
    This decorator is primarily intended for instance methods and automatically
    excludes the first parameter (`self`) during validation.

    :param _types: A tuple specifying the expected types of arguments.
                   Example: `(str, int)` means the first argument should
                   be a string and the second an integer.
    :type _types: tuple[type, ...]
    :return: A decorator function that validates argument types.
    :rtype: function

    :raises AssertionError: If the number of parameters does not match the expected types.
    :raises TypeError: If one or more arguments fail type validation.
    
    This decorator assumes the method signature pattern:
        `method(self, (<arg1>, <arg2>, ...))`.
        In other words, the arguments are passed as a **single iterable**
        (like a tuple or list) after `self`.
    """
    
    def _inner(func):
    
        @wraps(func)
        def _decorator(*args, **kwargs):
        
            """
            Validates argument types before executing the wrapped function.

            :param args: Positional arguments, with `self` as the first element.
            :type args: tuple
            :param kwargs: Keyword arguments (ignored in validation).
            :type kwargs: dict
            :return: Result of the wrapped function if validation passes.
            :rtype: Any
            :raises AssertionError: If argument count mismatches.
            :raises TypeError: If any argument type is invalid.
            
            """
            
            _args = args[1:][0] # To exclude first self i.e. instance 
            
            assert  len(_args)==len(_types),'Number of parameters does not match'

            for _type, _arg in zip(_types, _args):
                
                if not isinstance(_arg, _type):
                    raise TypeError(
                                    'Arguments passed does not match the type expected'
                    )
                    
            return func(*args, **kwargs)
        
        return _decorator
                
    return _inner