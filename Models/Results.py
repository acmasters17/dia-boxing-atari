from enum import Enum

# experiment can either result in win, draw or loss or unknwown if experiment still happening 
class Result(Enum):
    KOWIN = 2
    WIN = 1
    DRAW = 0
    LOSS = -1
    KOLOSS = -2
    UNKNOWN = 100
    
    