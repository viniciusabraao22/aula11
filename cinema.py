class Imgresso:
    def __init__(self, valor):
        self.valor = valor

    def ImgressoValor(self):
        print(f"O valor do ingresso é: R$ {self.valor:.2f}")


class Vip(Imgresso):
    def __init__(self, valor):
        # Aumenta 50% no valor do ingresso
        valor_vip = valor * 1.5
        super().__init__(valor_vip)

    def mostrar_valor_vip(self):
        print(f"O valor do ingresso VIP é: R$ {self.valor:.2f}")
