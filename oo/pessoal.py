class Pessoa:
    def __init__(self, *filhos, nome= None, idade= 49):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return (f"Olá {id (self)}")

if __name__ == '__main__':
    filho1 = Pessoa(nome= "Fernanda")
    pai = Pessoa(filho1, nome= "Sidney")
    print(pai.cumprimentar())
    print(pai.idade)
    for filho in pai.filhos:
        print(filho)