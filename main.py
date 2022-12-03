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
    AnotherProduct,
    Customer,
    Address
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

# Composition

customer01 = Customer('Yuri')
customer02 = Customer('João')
customer03 = Customer('Beatriz')

customer01.insert_address('Maceió', 'AL')
customer01.insert_address('Batalha', 'AL')
customer01.insert_address('Belo Horizonte', 'MG')
customer01.show_address()

customer02.insert_address('Maceió', 'AL')
customer02.insert_address('São Paulo', 'SP')
customer02.show_address()

customer03.insert_address('Porto Alegre', 'RS')
customer03.insert_address('Curitiba', 'PR')
customer03.insert_address('Bauneário Camburiú', 'SC')
customer03.show_address()