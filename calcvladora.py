class Calculadora:
    def __init__(self):
        print("Digite x:")
        self.x = int(input())

        print("Digite y:")
        self.y = int(input())

        print(f"Suma = {self.suma()}")
        print(f"Resta = {self.resta()}")

    def suma(self):
        return self.x + self.y

    def resta(self):
        return self.x - self.y

if __name__ == "__main__":
    Calculadora()