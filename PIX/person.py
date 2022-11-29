class Person:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando  = falando

        variavel_valida_dentro_do_init = True
        print(variavel_valida_dentro_do_init)
    
    def comer(self):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        print(f'{self.comendo} está comendo');
        self.comendo = True
    
    def falar(self):
        print(f'Falando ...')

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} Não está comendo')
            return
        
        print(f'{self.nome} parou ded comer.')
        self.comendo = False