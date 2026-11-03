from abc import ABC, abstractmethod

# Classe abstrata
class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


# Cachorro
class Cachorro(Animal):
    def falar(self):
        return "Au au"

    def mover(self):
        return "corre"


# Gato
class Gato(Animal):
    def falar(self):
        return "Miau"

    def mover(self):
        return "pula"


# Vaca
class Vaca(Animal):
    def falar(self):
        return "Muuu"

    def mover(self):
        return "caminha"


# Habilidades
class Voador:
    def voar(self):
        return "voa"


class Nadador:
    def nadar(self):
        return "nada"


# Pato
class Pato(Animal, Voador, Nadador):
    def falar(self):
        return "Quack"

    def mover(self):
        return "anda"


# Jacaré
class Jacare(Animal, Nadador):
    def falar(self):
        return "Grrrr"

    def mover(self):
        return "anda"


# Funções polimórficas
def fazer_som(animal):
    print(animal.nome + ": " + animal.falar())


def fazer_movimento(animal):
    if isinstance(animal, Pato):
        print("Donald anda, Donald voa e Donald nada")
    elif isinstance(animal, Jacare):
        print("Jacaré anda, Jacaré nada")
    else:
        print(animal.nome + " " + animal.mover())


# Criando os animais
rex = Cachorro("Rex")
mimi = Gato("Mimi")
mimosa = Vaca("Mimosa")
donald = Pato("Donald")
jacare = Jacare("Jacaré")


# Executando o programa
for animal in [rex, mimi, mimosa, donald, jacare]:
    fazer_som(animal)
    fazer_movimento(animal)
