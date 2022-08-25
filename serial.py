"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    Accepts a starting number.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Sets the starting serial number for the generator"""
        self.start = start
        self.current = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.current}>"
    
    def generate(self):
        """Returns the current serial number and increments the counter"""
        num = self.current
        self.current +=1
        return num
    
    def reset(self):
        """Resets the serial generator to the original starting point"""
        self.current = self.start
    

