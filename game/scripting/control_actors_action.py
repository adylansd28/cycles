import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0 , -1 * constants.CELL_SIZE)
        self._direction_second = Point(0 , -1 * constants.CELL_SIZE)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        scores = cast.get_actors("scores")

        first_movement = False
        
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            first_movement = True
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
            first_movement = True
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            first_movement = True

        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            first_movement = True

        second_movement = False

        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction_second = Point(-constants.CELL_SIZE, 0)
            second_movement = True
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction_second = Point(constants.CELL_SIZE, 0)
            second_movement = True
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction_second = Point(0, -constants.CELL_SIZE)
            second_movement = True
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction_second = Point(0, constants.CELL_SIZE)
            second_movement = True
        
        cycles = cast.get_actors("cycles")

        if second_movement:
            cycles[1].grow_tail(1)
            cycles[1].turn_head(self._direction_second)
            scores[1].add_points(1)

        if first_movement:
            cycles[0].grow_tail(1)
            cycles[0].turn_head(self._direction)
            scores[0].add_points(1)

        counter = 0
                