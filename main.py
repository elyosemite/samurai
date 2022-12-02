from PIX import (
    Person,
    User
)

from models import (
    Product,
    User
)

p1 = Person('Yuri', 24)
user = User()

p1.obter_ano_nascimento()
print(p1.ano_atual)
yuri = Person.person_factory('Yuri', 1984)

yuri.obter_ano_nascimento()
print(Person.gerar_id())
print(yuri.gerar_id())

computer = Product("iMAC", 2)
camisa = Product("Camisa", 3)

print(computer.name, computer.price)
print(camisa.name ,camisa.price)

# Trabalhando com atributo de classe

a1 = AnotherFile()
a2 = AnotherFile()

a1.algum_atributo_meu = 457454

print(a1.__dict__)
print(a2.__dict__)

print(a1.algum_atributo_meu)
print(a2.algum_atributo_meu)