# Number Guessing App

## Rules 
 - There are 02 roles: Player, and House(PC)
 - There is a deck, contains 52 playing cards. There are:
   + 4 Suites: Heart, Diamond, Club, Spade
   + 13 groups: A(Ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, J(Jack), Q(Queen), K(King)
   + 02 greatest cards: Black Joker, Red Joker
 - Each round, the Player and the House receive 01 card from the deck.
 - Player has to guess that his card is greater or less than the House's card.
 - Player starts with 60 points.
 - Reward for each winning round is 20 points.
 - Player must pay 25 points to join a single match
 - Game stages:
    + The House receives and shows his card first.
    + Player start guessing.
    + If the Player loses the round, he'll lose the reward.
    + If the Player wins the round, he can decide to continue or stop.
    + If the Player decides to stop, he can keep his current reward.
    + If the Player decides to continue, He does not receive the reward yet. But the reward will be doubled on the next round.
 - Game Win/Lose conditions:
    + Player will WIN the game if he has greater than or equal to 1000 points after any match.
    + Player will LOSE the game if he has less than 30 points after any match.

## Instructions Using Package
1. Download the package: Either clone the repository to a local machine with Python 3.6 or later already installed. 
2. Open Command Prompt or Terminal and navigate to the src folder.
3. Type in `python main.py` and let the program compile and interpreted itself.
4. To exit the game while in progress, hit Ctrl + C (or Command + C on Mac)
5. For more help, type `python main.py --help`

## Instructions Using Docker
1. Configure and install so that your docker system is operating properly. On how to install Docker, refer to [this instruction for Windows](https://docs.microsoft.com/en-us/windows/wsl/)
2. Image will be pulled automatically from Docker Hub after typing in `docker image pull minhphan0612/guessinggame`
3. Run image using command `docker run -it numberguesser"