class Veiculo:
    def andar(self):
        print("Andei")

class Carro(Veiculo):
    def __init__(self):
        self.nrodas = 4

class Moto(Veiculo):
    def __init__(self):
        self.nrodas = 2 

class Monociclo(Veiculo):
    nrodas = 1

class Aviao:
    def voar(self):
        print("Voar")

class aerocarro(Veiculo, Aviao):
    pass


a = Carro()
b = Moto()
c = Monociclo()

print(a.nrodas)
print(b.nrodas)
print(a.andar())
print(b.andar())
print(c.andar())