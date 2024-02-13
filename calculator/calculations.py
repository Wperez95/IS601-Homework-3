class Calculations:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation # Represents functions that are defined in operations folder

    def get_result(self):
        #This is saying run operation with a and b ex.) add (2,2)
        return self.operation(self.a, self.b)
    