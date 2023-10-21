class Calculator:
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def Addition(self):
        add = self.num1 + self.num2
        print("El resultado de la suma es: ", add)

    def Substraction(self):
        sub = self.num1 - self.num2
        print("El resultado de la resta es: ", sub)

    def Multiplication(self):
        mul = self.num1 * self.num2
        print("El resultado de la multiplicación es: ", mul)

    def Division(self):
        div = self.num1 / self.num2
        print("El resultado de la división es: ", div)

num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

calculator = Calculator(num1, num2)
calculator.Addition()
calculator.Substraction()
calculator.Multiplication()
calculator.Division()