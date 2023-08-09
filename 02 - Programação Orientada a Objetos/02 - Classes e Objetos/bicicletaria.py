class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor=cor
        self.modelo=modelo
        self.ano=ano
        self.valor=valor
        self.aro=aro

    def buzinar(self):
        print("Bi bi")

    def parar(self):
        print("Parando Bicicleta....")
        print("Bicicleta parada!")

    def correr(self):
        print("Vruummmmm....")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "Caloi", 2023, 500)
b1.buzinar()
b1.correr()
b1.parar()

print(b1)