"""
A module to define the exceptions and pre-defined messages
that may happen while the game is in progress.
"""
class Error(Exception):
    pass

class InvalidGuessChoice(Error):
    """
    Handles the exception when the player entered a wrong guess.
    """
    def __init__(self, guess) -> None:
        self.guess = guess
        self.message = "Type '>' or '<' instead."
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return f'{self.guess} is an invalid response. {self.message}'


class InvalidContinueChoice(Error):
    """
    Handles the exception when the player entered a wrong response
    whether to continue the match after winning a single round.
    """
    def __init__(self, choice) -> None:
        self.message = "Type 'Y' (Yes) or 'N' (No) to continue."
        self.choice = choice
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return f'{self.choice} is an invalid response. {self.message}'


class InvalidNameChoice(Error):
    """
    Handles the exception when the player entered an inappropriate name
    for the player object.
    """
    def __init__(self, name) -> None:
        self.message = 'Name not allowed. Type again'
        self.name = name
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message