class ProductCart:
    def __init__(self):
        self.__products = []

    def insert_product(self, product):
        self.__products.append(product)
    
    def show_products(self):
        for product in self.__products:
            print(product.name)
        
    def total_sum(self):
        total = 0
        for product in self.__products:
            total = total + product.price
        print(f"R$ {total}")
