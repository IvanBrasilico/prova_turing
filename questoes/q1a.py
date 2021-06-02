"""Funções necessárias para responder questão 1a"""
import sys
from typing import List


class Economizador():
    """Classe para economizar letras de uma lista de emails.

    Recebe uma lista de emails e a qtde a tratar. Provê diversos métodos para cortar
     letras e fazer estatísticas das economias.
    """

    def __init__(self, lista_emails: List[str] = None, qtde: int = None):
        """Inicializa o economizador.

        :param lista_emails: lista de emails (opcional, pode ser informado depois)
        :param qtde: Quantidade de emails a tratar (opcional, se omitido uso tudo)
        """
        self.qtde_emails = 0
        self.lista_emails = lista_emails
        if lista_emails and isinstance(lista_emails, list):
            self.qtde_emails = len(lista_emails)
        self.emails_economia = []

    def corta_coincidencias(self, str1: str, str2: str):
        """Compara duas strings e corta primeiras letras iguais.

        :param str1: String a ser cortada
        :param str2: String a comparar
        :return: String cortada
        """
        ind = 0
        while str1[ind] == str2[ind]:
            ind += 1
        return str1[ind:]

    def corta_letras_iniciais_emails(self):
        """Processa lista de emails e guarda em emails_economia"""
        if self.lista_emails is None or self.qtde_emails == 0 or \
                not isinstance(self.lista_emails, list) or len(self.lista_emails) == 0:
            raise ValueError('Não há lista de emails a ser processada.')
        if self.qtde_emails == 1:
            return self.lista_emails[:0]
        lista_economizada = [self.lista_emails[0]]
        emailanterior = self.lista_emails[0]
        for email in self.lista_emails[1: self.qtde_emails]:
            if email[0] == emailanterior[0]:
                email = self.corta_coincidencias(email, emailanterior)
            lista_economizada.append(email)
        self.emails_economia = lista_economizada

    def get_qtde_caracteres_economizados(self) -> int:
        """Compara a qtde de caracteres das listas original e processada e retorna diferença."""
        total_caracteres_original = len(''.join(self.lista_emails))
        total_caracteres_economia = len(''.join(self.emails_economia))
        return total_caracteres_original - total_caracteres_economia


def corrige_virus(emails_virus: List[str]) -> List[str]:
    """Corrige lista de emails afetadas pelo vírus.

    Segue especificações passados pela equipe de segurança para corrigir cada linha.
     Retorna ERRO se domínio for inválido
    """

    def inverte_string(s: str) -> str:
        result = ''
        ind = len(s)
        while ind > 0:
            ind -= 1
            result = result + s[ind]
        return result

    def corrige_linha(email):
        meio = len(email) // 2
        parte1 = email[:meio]
        parte2 = email[meio:]
        print(parte1)
        print(parte2)
        corrigido = inverte_string(parte1) + inverte_string(parte2)
        if not 'usp.br' in corrigido:
            return 'ERRO'
        return corrigido

    return [corrige_linha(email) for email in emails_virus]


if __name__ == '__main__':
    n = input('Informe a quantidade de emails: ')
    try:
        n = int(n)
        if n < 1 or n > 100:
            raise ValueError
    except ValueError:
        print('Informar um número inteiro entre 1 e 100.')
        sys.exit(1)
    lista_emails = []
    for r in range(1, n + 1):
        lista_emails.append(input(f'Informe o {r}o email: '))
    economizador = Economizador(lista_emails)
    economizador.corta_letras_iniciais_emails()
    print(economizador.get_qtde_caracteres_economizados())
