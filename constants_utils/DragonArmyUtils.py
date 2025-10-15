from enum import IntEnum
from functools import wraps

class DragonArmyDefaultStatsEnum(IntEnum):
    damage = 45 
    health = 250
    armor = 10
    
class Singleton(type):
    
    def __call__(cls,  *args, **kwargs):
        
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*args, **kwargs)
            
        return cls._instance

def check_types(_types=(int,)):

    def _inner(func):
    
        @wraps(func)
        def _decorator(*args, **kwargs):
        
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