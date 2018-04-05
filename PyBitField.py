class PyBitField:

    def __init__(self, size=32):
        self.intSize = int(size/32)
        if not((size % 32) == 0):
            self.intSize = self.intSize + 1
        self.intArray = [0] * self.intSize
        self.size = size

    def __getitem__(self, key):
        if not(isinstance(key, int) and (key >= 0) and (key < self.size)):
            raise TypeError("Invalid key, size of array is " + str(self.size))
        idx = int(key / 32)
        sub = key % 32
        mask = 1 << sub
        result = (self.intArray[idx] & mask) >> sub
        return(result)
        
    def __setitem__(self, key, value):
        if not(value in [0, 1]):
            raise ValueError("Assigned value must be 0 or 1.")
        if not(isinstance(key, int) and (key >= 0) and (key < self.size)):
            raise TypeError("Invalid key, size of array is " + str(self.size))
        idx = int(key / 32)
        sub = key % 32
        mask = 1 << sub
        if (value == 0):
            mask = ~mask
            self.intArray[idx] = self.intArray[idx] & mask
        if (value == 1):
            self.intArray[idx] = self.intArray[idx] | mask
        
        
    def __str__(self):
        strRep = ""
        for i in range(0,len(self.intArray)-1):
            strRep = strRep + "|" + "{:032b}".format(self.intArray[i])[::-1]
        extra = self.size % 32
        if (extra == 0):
            extra = 32
        shiftAmt = 32 - extra
        formatStr = "{:0" + str(extra) + "b}"
        strRep = strRep + "|" + formatStr.format(self.intArray[len(self.intArray)-1])[::-1]
        return(strRep+"|")
            
    def diagnostics(self):
        print("\tPyBitField")
        print("\tSize   :\t", self.size)
        print("\tintSize:\t", self.intSize)
        print(str(self))
