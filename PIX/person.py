class Person:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando  = falando

        variavel_valida_dentro_do_init = True
        print(variavel_valida_dentro_do_init)
    
    def comer(self):
        print(f'{self.comendo} está comendo');
        self.comendo = True
        