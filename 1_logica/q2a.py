class Estacionamento:
    def __init__(self, k=0, n=0):
        if k < 1 or k > 1000:
            raise ValueError('Tamanho deve ser entre 1 e 1.000')
        if n < 1 or n > 100_000:
            raise ValueError('Instantes deve ser entre 1 e 100.000')
        self.tamanho = k
        self.tempo = n
        self._fila = []
        # Possível é bool (True ou False) mas começa indefinido
        self._possivel: bool = None
        # A variável entradas serve para acumular histórico e testar tudo de uma vez.
        # Ou pode ser utilizada a função "entrada_saida_carro" iterativamente.
        self._entradas = []

    @property
    def entradas(self):
        return self._entradas

    @entradas.setter
    def entradas(self, pentradas):
        if len(pentradas) != self.tempo:
            raise ValueError(f'Tamanho das entradas definido como {self.tempo}')
        self._entradas = pentradas

    def entrada_saida_carro(self, carro):
        """Adiciona ou remove carros.

        Passar o número do carro. Se positivo, adiciona na fila. Se negativo, tenta retirar.
        Retorna exceção se tempo de monitoramento acabou e grava flag "possivel" como True.
        Retorna exceção se carro não está na fila, e grava flag "possivel" como Falso.
        Retorna exceção se não houverem mais vagas, e grava flag "possivel" como Falso.

        :param carro: inteiro com o número do carro
        :return: Raises exception ValueError
        """
        if abs(carro) < 1 or abs(carro) > 1_000:
            raise ValueError('Carro deve ser entre 1 e 1.000')
        if self.tempo == 1:
            self._possivel = True
            raise ValueError('Tempo de monitoramento acabou!')
        if carro < 0:
            ultimocarro = self._fila[len(self._fila) - 1]
            if ultimocarro != abs(carro):
                self._possivel = False
                raise ValueError('Carro não está na vaga!!!')
            self.tempo -= 1
            self._fila.pop()
        else:
            if len(self._fila) == self.tamanho:
                self._possivel = False
                raise ValueError('Não há mais vagas para adicionar carros!')
            self.tempo -= 1
            self._fila.append(carro)

    def processar_entradas(self):
        """Definir a property entradas e testar aqui."""
        try:
            for carro in self._entradas:
                self.entrada_saida_carro(carro)
        except ValueError as err:
            print(err)

    @property
    def possivel(self):
        self.processar_entradas()
        if self._possivel is None:
            raise ValueError('Teste inválido! Não foi possível determinar validade da fila')
        return self._possivel


if __name__ == '__main__':
    BOOLEAN_DICT = {True: 'sim', False: 'não', None: 'indefinido'}
    K_N = input('Informe a quantidade de vagas e número de instantes separados por espaço: ')
    K, N = K_N.split()
    estacionamento = Estacionamento(int(K), int(N))
    while True:
        carro = input('Número do carro (positivo para entrar, negativo para sair): ')
        try:
            estacionamento.entrada_saida_carro(int(carro))
        except ValueError as err:
            print(err)
            break
    print(BOOLEAN_DICT.get(estacionamento.possivel))
