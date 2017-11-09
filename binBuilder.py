from .outcome import Outcome
import inspect

class binBuilder(object):
    '''class that generates the roulette bins
    and populates them with their corresponding
    outcomes.'''
    def __init__(self):
        pass
        
    def buildBins(self, wheel):
        '''Calls all the generator methods of the class object,
        using the standard library module inspect'''
        # using the inspect library to introspect the class object components 
        methods = inspect.getmembers(self, inspect.ismethod)
        for (name, func) in methods:
            if name.startswith('gen_'):
                func(wheel)
    
    def gen_straight_bets(self, wheel):
        '''generates straight bets.'''
        for i in range(1,37):
            outcome = Outcome(str(i), 35)
            wheel.addOutcome(i, outcome)
        wheel.addOutcome(0, Outcome('0', 35))
        wheel.addOutcome(37, Outcome('00', 35))

    def gen_split_bets(self, wheel):
        '''generates split bets.'''
        # center interior column
        for i in range(5,33,3):
            ou = Outcome('{},{}'.format(i-3, i), 17)
            od = Outcome('{},{}'.format(i, i+3), 17)
            od = Outcome('{},{}'.format(i, i+1), 17)
            og = Outcome('{},{}'.format(i-1, i), 17)
            wheel.addOutcome(i, ou)
            wheel.addOutcome(i, od)
            wheel.addOutcome(i, od)
            wheel.addOutcome(i, og)
        # edge corners
        wheel.addOutcome(1, Outcome('1,2', 17))
        wheel.addOutcome(1, Outcome('1,4', 17))
        wheel.addOutcome(3, Outcome('2,3', 17))
        wheel.addOutcome(3, Outcome('3,6', 17))
        wheel.addOutcome(34, Outcome('31,34', 17))
        wheel.addOutcome(34, Outcome('34,35', 17))
        wheel.addOutcome(36, Outcome('33,36', 17))
        wheel.addOutcome(36, Outcome('35,36', 17))
        # center col edge nums
        wheel.addOutcome(2, Outcome('1,2', 17))
        wheel.addOutcome(2, Outcome('2,3', 17))
        wheel.addOutcome(2, Outcome('2,5', 17))
        wheel.addOutcome(35, Outcome('34,35', 17))
        wheel.addOutcome(35, Outcome('35,36', 17))
        wheel.addOutcome(35, Outcome('32,35', 17))
            

    def gen_street_bets(self, wheel):
        '''generates street bets.'''
        # use the 1st column nums as reference for each row
        for i in range(1,35,3):
            outcome = Outcome('{},{},{}'.format(i, i+1, i+2), 11)
            wheel.addOutcome(i, outcome)
            wheel.addOutcome(i+1, outcome)
            wheel.addOutcome(i+2, outcome)
        

    def gen_corner_bets(self, wheel):
        '''generates corner bets.'''
        # center interior column
        for i in range(5,33,3):
            ul = Outcome('{},{},{},{}'.format(i-4, i-3, i-1, i), 8)
            ur = Outcome('{},{},{},{}'.format(i-3, i-2, i, i+1), 8)
            ll = Outcome('{},{},{},{}'.format(i-1, i, i+2, i+3), 8)
            lr = Outcome('{},{},{},{}'.format(i, i+1, i+3, i+4), 8)
            for j in [ul, ur, ll, lr]:
                wheel.addOutcome(i, j)
            
        # left interior column
        for i in range(4,32,3):
            up = Outcome('{},{},{},{}'.format(i-3, i-2, i, i+1), 8)
            lw = Outcome('{},{},{},{}'.format(i, i+1, i+3, i+4), 8)
            wheel.addOutcome(i, up)
            wheel.addOutcome(i, lw)
            
        # right interior column
        for i in range(6,34,3):
            ul = Outcome('{},{},{},{}'.format(i-4, i-3, i-1, i), 8)
            ll = Outcome('{},{},{},{}'.format(i-1, i, i+2, i+3), 8)
            wheel.addOutcome(i, ul)
            wheel.addOutcome(i, ll)
        
        # corners
        wheel.addOutcome(1, Outcome('1,2,4,5', 8))
        wheel.addOutcome(2, Outcome('1,2,4,5', 8))
        wheel.addOutcome(2, Outcome('2,3,5,6', 8))
        wheel.addOutcome(3, Outcome('2,3,5,6', 8))
        wheel.addOutcome(34, Outcome('31,32,34,35', 8))
        wheel.addOutcome(35, Outcome('31,32,34,35', 8))
        wheel.addOutcome(35, Outcome('32,33,35,36', 8))
        wheel.addOutcome(36, Outcome('32,33,35,36', 8))


            
        

    def gen_line_bets(self, wheel):
        '''generates line bets.'''
        # use left column numbers as anchors
        for i in range(1,32,3):
            line = list(range(i,i+6))
            outcome = Outcome(','.join([str(x)for x in line], 5))
            for j in line:
                wheel.addOutcome(j, outcome)


    def gen_dozen_bets(self, wheel):
        '''generates dozen bets.'''
        for i in range(3):
            outcome = Outcome('Dozen {}'.format(i+1), 2)
            for j in range(1,13):
                wheel.addOutcome(i*12 + j, outcome)

    def gen_column_bets(self, wheel):
        '''generates column bets.'''
        for i in range(3):
            outcome = Outcome('Column {}'.format(i+1), 2)
            for j in range(1+i, 35+i,3):
                wheel.addOutcome(j, outcome)



    def gen_even_money_bets(self, wheel):
        '''generates even money bets 
        (red, black, odd, even, high, low).'''
        reds = (1,3,5,7,9,
                12,14,16,18,19,
                21,23,25,27,
                30,32,34,36)

        red = Outcome('Red', 1)
        black = Outcome('Black', 1)
        even = Outcome('Even', 1)
        odd = Outcome('Odd', 1)
        high = Outcome('High', 1)
        low = Outcome('Low', 1)

        for i in range(1,37):
            if i < 19:
                wheel.addOutcome(i, low)
            else:
                wheel.addOutcome(i, high)
            if (i % 2) == 0 :
                wheel.addOutcome(i, even)
            else:
                wheel.addOutcome(i, odd)
            if i in reds:
                wheel.addOutcome(i, red)
            else:
                wheel.addOutcome(i, black)


    def gen_zeros_bets(self, wheel):
        '''generates the bets associated with
        the zero and double zero bins.'''
        wheel.addOutcome(0, Outcome('0',35))
        wheel.addOutcome(37, Outcome('00',35))
        wheel.addOutcome(0, Outcome('00-0-1-2-3',6))
        wheel.addOutcome(37, Outcome('00-0-1-2-3',6))

