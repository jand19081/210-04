from game.casting.actor import Actor
import random
from constants import *

class Stone(Actor):
    """
    """

    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._points = 0

    def set_points(self, points):
        self._points = points

    def get_points(self):
        return self._points

    def create_stones(self, cast):
        """Creates the stones and gems for the game."""
        
        values = [1,-1]

        for n in range(10):
            points = random.choice(values)

            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS - 1)
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            # For the gems
            if points == 1:       
                gem = Stone()
                gem.set_text("*")
                gem.set_points(points)
                gem.set_font_size(FONT_SIZE)
                gem.set_color(GREEN)
                gem.set_position(position)
                gem.set_velocity(STONE_VELOCITY)
                cast.add_actor("stones", gem)
            
            # For the stones
            if points == -1:
                stone = Stone()
                stone.set_text("O")
                stone.set_points(points)
                stone.set_font_size(FONT_SIZE)
                stone.set_color(GREY)
                stone.set_position(position)
                stone.set_velocity(STONE_VELOCITY)
                cast.add_actor("stones", stone)