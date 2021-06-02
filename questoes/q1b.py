"""Funções necessárias para responder questão 1 b"""
import sys
from typing import List


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
        print('Informar um número inteiro entre 1 e 10_000.')
        sys.exit(1)
    emails_virus = []
    for r in range(1, n + 1):
        emails_virus.append(input(f'Informe o {r}o email: '))
    corrigido = corrige_virus(emails_virus)
    print(corrigido)
