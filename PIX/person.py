from datetime import datetime

class Person:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando  = falando

        variavel_valida_dentro_do_init = True
        print(variavel_valida_dentro_do_init)
    
    def comer(self, fruta):
        if self.comendo:
            print(f'{self.nome} já está comendo {fruta}')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print(f'{self.nome} está comendo');
        self.comendo = True
    
    def falar(self, mensagem):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando ... {mensagem}')
        self.falando =True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        
        print(f'{self.nome} parou de falar')
        self.falando = False

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} Não está comendo')
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False
    
    def obter_ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nascimento(cls):
        pass