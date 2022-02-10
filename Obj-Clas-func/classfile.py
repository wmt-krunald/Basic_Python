class Student:

    def __init__(self, name, roll, spi):
        self.name = name
        self.roll = roll
        self.spi = spi

    
    def distinction(self):
        if self.spi >= 7.5:
            return True
        else:
            return False
        
        