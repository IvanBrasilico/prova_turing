from unittest import TestCase

from q1a import Economizador
from q1b import corrige_virus
from q2a import Estacionamento
from q2b import EstacionamentoQB


class Test1(TestCase):
    def setUp(self):
        # Dados teste q1a
        self.emails_original = ['camila.lobianco@usp.br',
                                'camilalala.topp@usp.br',
                                'azank.pistolado@usp.br']
        self.emails_saida = ['camila.lobianco@usp.br',
                             'lala.topp@usp.br',
                             'azank.pistolado@usp.br']
        # Dados teste q1b
        self.emails_virus = ['ibol.alimacrb.psu@ocna',
                             't.alalalimacrb.repsu@ppo',
                             '.orbmem_ovonrb.psu@gnirut']
        self.emails_corrigidos = ['camila.lobianco@usp.br',
                                  'ERRO',
                                  'novo_membro.turing@usp.br']
        # Dados teste q2a
        self.teste2a1 = {'K': 3, 'N': 6, 'entradas': [1, 2, -2, 3, -3, -1],
                         'possivel': True}
        self.teste2a2 = {'K': 3, 'N': 8, 'entradas': [1, 2, -2, 3, 5, -3, -1, -5],
                         'possivel': False}
        # Dados teste q2b
        self.teste2b1 = {'K': 4, 'N': 4, 'entradas': [1, 4, 6, 2], 'momento': 7,
                         'saida': [0, 3, 0, 2]}
        self.teste2b2 = {'K': 5, 'N': 7, 'entradas': [3, 6, 12, 9, 4, 15, 16], 'momento': 7,
                         'saida': [0, 2, 0, 5, 1]}


    def test_q1a_cortaletras(self):
        economizador = Economizador()
        caba = economizador.corta_coincidencias('jaboticaba', 'jaboti azul')
        assert caba == 'caba'

    def test_q1a(self):
        economizador = Economizador(self.emails_original)
        economizador.corta_letras_iniciais_emails()
        assert self.emails_saida == economizador.emails_economia
        assert economizador.get_qtde_caracteres_economizados() == 6

    def test_q1b(self):
        corrigido = corrige_virus(self.emails_virus)
        assert corrigido == self.emails_corrigidos

    def test_q2a(self):
        for teste in [self.teste2a1, self.teste2a2]:
            estacionamento = Estacionamento(teste['K'], teste['N'])
            estacionamento.entradas = teste['entradas']
            assert estacionamento.possivel == teste['possivel']

    def test_q2b(self):
        for teste in [self.teste2b1, self.teste2b2]:
            estacionamento = EstacionamentoQB(teste['K'], teste['N'])
            for momento in teste['entradas']:
                estacionamento.entrada_momento(momento)
            assert estacionamento.status(teste['momento']) == teste['saida']
