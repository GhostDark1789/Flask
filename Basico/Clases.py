class Operaciones:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def sumar(self):
        return self.num1+self.num2
    def restar(self):
        print(self.num1-self.num2)

Op = Operaciones(6,3)
print(Op.sumar())

Op.restar()
