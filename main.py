from pix import (
    Person,
    User
)

from models import (
    Product,
    User,
    Writer,
    Pen,
    WriteMachine,
    ProductCart,
    AnotherProduct
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

a1 = User()
a2 = User()

a1.algum_atributo_meu = 457454

# Association
writer_yuri = Writer("Yuri Melo")
my_pen = Pen("BIC")
my_write_machine = WriteMachine()

print(writer_yuri.name)
print(my_pen.brand)

writer_yuri.tool = my_write_machine
writer_yuri.tool.write()

writer_yuri.tool = my_pen
writer_yuri.tool.write()

# Aggregation

product01 = AnotherProduct("Camiseta Gucci", 9000)
product02 = AnotherProduct("iPhone 14 Pro Max", 14000)
product03 = AnotherProduct("Calça Louis Vuitton", 10000)

product_cart = ProductCart()
product_cart.insert_product(product01)
product_cart.insert_product(product02)
product_cart.insert_product(product03)

product_cart.show_products()
print("\n\nTotal a pagar: ")
product_cart.total_sum()