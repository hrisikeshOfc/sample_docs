class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def multiply(self):
        return self.x * self.y

    def subtract(self): 
        return self.x - self.y

    def divide(self):
        return self.x / self.y


if __name__ == "__main__":
    cal = Calculator(34,5465)
    print(cal.add())