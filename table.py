''' Table

Responsibilities.
    A collection of bets placed on Outcomes by a Player. This isolates the set of possible bets and the management of the amounts currently at risk on each bet. 
    This also serves as the interface between the Player and the other elements of the game.

Collaborators.
    Collects the Outcomes; used by Player to place a bet amount on a specific Outcome; used by Game to compute the amount won from the amount that was bet.
'''

class Table(object):
    def __init__(self):
        pass
