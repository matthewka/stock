class RelativeStrengthIndex:
    def __init__(self, dataArray, len):
        self.dataLen = len(dataArray)
        self.len = len
        self.rs = self.calRS(dataArray)
        if self.dataLen <= 0:
            raise Exception("Data length is less than 0")

    def calRS(self, dataArray):
        rs = []
        for index in range(0, len(dataArray) -1):
            rs[index] = dataArray[index+1] - dataArray[index]

        return rs

    def calculate(self, len):
        for s in self.rs:
            ps = 0 # plus strength
            ms = 0 # minus strength
            ps_count = 0
            ms_count = 0

