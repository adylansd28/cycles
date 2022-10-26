import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():

    initial_vel = Point(0,-15)
    first_snake = Cycle(150, 150, initial_vel, constants.RED)
    second_snake = Cycle(600, 150, initial_vel, constants.GREEN)

    first_score = Score()
    first_score.set_position(Point(25,25))
    first_score.set_text("Score\nPlayer 1: ")
    first_score.set_color(constants.RED)

    second_score = Score()
    second_score.set_position(Point(775,25))
    second_score.set_text("Score\nPlayer 2: ")
    second_score.set_color(constants.GREEN)



    
    # create the cast
    cast = Cast()
    cast.add_actor("cycles", first_snake)
    cast.add_actor("cycles", second_snake)
    cast.add_actor("scores", first_score)
    cast.add_actor("scores", second_score)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()