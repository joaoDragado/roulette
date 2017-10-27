
''' Outcome

Responsibilities.
    A name for the bet and the payout odds. This isolates the
    calculation of the payout amount. Example: “Red”, “1:1”.

Collaborators.
    - Collected by Wheel into the bins that reflect the bets that win;
    - collected by Table into the available bets for the Player;
    - used by Game to compute the amount won from the amount that was
    bet.
'''
    
class Outcome(object):
    def __init__(self):
        pass
