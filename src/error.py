class Error(Exception):
    pass

class InvalidGuessChoice(Error):
    def __init__(self, guess) -> None:
        self.guess = guess
        self.message = "Type '>' or '<' instead."
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return f'{self.guess} is an invalid response. {self.message}'


class InvalidContinueChoice(Error):
    def __init__(self, choice) -> None:
        self.message = "Type 'Y' (Yes) or 'N' (No) to continue."
        self.choice = choice
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return f'{self.choice} is an invalid response. {self.message}'

class InvalidNameChoice(Error):
    def __init__(self, name) -> None:
        self.message = 'Name not allowed. Type again'
        self.name = name
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message