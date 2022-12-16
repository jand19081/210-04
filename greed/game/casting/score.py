
from game.casting.actor import Actor

class Score(Actor):
    """A number to store the player's score.
    
    Attributes:
        _score(int): The current score.
    """
    
    def __init__(self):
        """Constructs a new score."""
        super().__init__()
        self._score = 0

    def get_score(self):
        """Gets the current score."""
        return self._score

    def add_points(self, points):
        """Adds points to the current score."""
        self._score += points
