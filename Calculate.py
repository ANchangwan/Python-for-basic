class Calculate():
    def __init__(self,first,second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result

a = Calculate(3,4)

print(a.add())
print(a.mul())
print(a.sub())
print(float(a.div))


