from enum import Enum

# For readbilitys sake create an enum to map action numbers to words
class BoxingAction(Enum):
    NOOP = 0
    FIRE_STATIONARY = 1
    MOVE_UP = 2
    MOVE_RIGHT = 3
    MOVE_LEFT = 4
    MOVE_DOWN = 5
    MOVE_UP_RIGHT = 6
    MOVE_UP_LEFT = 7
    MOVE_DOWN_RIGHT = 8
    MOVE_DOWN_LEFT = 9
    FIRE_MOVE_UP = 10
    FIRE_MOVE_RIGHT = 11
    FIRE_MOVE_LEFT = 12
    FIRE_MOVE_DOWN = 13
    FIRE_MOVE_UP_RIGHT = 14
    FIRE_MOVE_UP_LEFT = 15
    FIRE_MOVE_DOWN_RIGHT = 16
    FIRE_MOVE_DOWN_LEFT = 17