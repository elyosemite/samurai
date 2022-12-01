from PIX import (
    Person,
    User
)

from models import Product

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
