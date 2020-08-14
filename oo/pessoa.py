class Pessoa:
    def __init__(self, *filhos, nome= None, idade= 49):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return (f"Olá {self.nome}")

if __name__ == '__main__':
    filho1 = "Fernanda"
    pai = Pessoa(filho1, nome= "Sidney")
    print(pai.cumprimentar())
    print(pai.idade)
    print(pai.__dict__)
    for filho in pai.filhos:
        print(filho)
    pai.sobrenome = "Bailer" # Atributo dinamico não tem definido dentro da classe
    print(pai.sobrenome)