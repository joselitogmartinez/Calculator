class Calculator:
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

calculator = Calculator(num1, num2)