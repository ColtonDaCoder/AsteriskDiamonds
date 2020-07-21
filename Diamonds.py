class Diamonds:
    length = 0
    middle = 0
    oscillate = False
    switch = False
    def __init__(self, length):
        self.length = length
        print(round(length/2 + 0.01))
        self.middle = round(length*0.5 + 0.01)
    def space(self):
        print(' ', end = '')
    def asterisk(self):
        print('*', end = '')
    def line(self):
        print('')
    def inRange(self, num):
        return abs(num + 1 - self.middle)
    def outRange(self, num):
        if num + 1 > self.middle: 
            return abs(num + 1 - self.length) 
        else: 
            return num
    def run(self):
        for outer in range(0, self.length):
            properO = self.outRange(outer)
            for inner in range(0, self.length):
                properI = self.inRange(inner)
                if properI == properO:
                    self.asterisk()
                    if properO > 0:
                        #print('value')
                        if self.oscillate:
                            self.oscillate = False
                            self.switch = False
                        else:
                            self.oscillate = True
                elif self.oscillate and not(properI == properO):
                    if self.switch:
                        self.asterisk()
                        self.switch = False
                    else:
                        self.space()
                        self.switch = True
                else:
                    #print('second')
                    self.space()
            self.line() 
while True:
    num = int(input("input an odd number for the length of the diamond: "))
    if not (num % 2) == 0:
        drawing = Diamonds(num)
        drawing.run()
    else:
        print('ERROR: the input must be an odd number greater than 0')
