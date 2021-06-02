from collections import deque


class EstacionamentoQB:
    def __init__(self, k=0, n=0):
        if k < 1 or k > 10_000:
            raise ValueError('Tamanho deve ser entre 1 e 10.000')
        if n < 1 or n > 10_000:
            raise ValueError('Número de carros deve ser entre 1 e 10.000')
        self.tamanho_rua = k
        self.numero_carros = n
        self.entradas = {}
        self.contador_carros = 0

    def funcionando(self):
        return self.contador_carros < self.numero_carros

    def entrada_momento(self, momento):
        self.contador_carros += 1
        self.entradas[momento] = self.contador_carros

    def status(self, momento):
        q = deque(maxlen=self.tamanho_rua)
        for r in range(1, momento + 1):
            numero_carro = self.entradas.get(r, 0)
            q.appendleft(numero_carro)
        return list(q)


if __name__ == '__main__':
    K_N = input('Informe a quantidade de vagas e número de carros separados por espaço: ')
    K, N = K_N.split()
    estacionamento = EstacionamentoQB(int(K), int(N))
    while estacionamento.funcionando():
        momento = input('Instante (número do carro é sequencial): ')
        estacionamento.entrada_momento(int(momento))
    momento = input('Momento a consultar status: ')
    print(estacionamento.status(int(momento)))
