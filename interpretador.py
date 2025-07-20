from lark import Lark, Transformer
from main import validar_cpf, validar_cnpj, validar_data, validar_email, validar_telefone  # seu código atual

grammar = open("validador.lark").read()
parser = Lark(grammar, start="start")

class InterpretadorValidacao(Transformer):
    def valor(self, s):
        return s[0][1:-1]  # remove aspas

    def tipo(self, s):
        return s[0]

    def entrada(self, itens):
        tipo, valor = itens
        return (tipo, valor)

    def entradas(self, entradas):
        return entradas

    def start(self, tree):
        return tree[0]  # retorna a lista de entradas


def interpretar(texto):
    arvore = parser.parse(texto)
    interpretador = InterpretadorValidacao()
    dados = interpretador.transform(arvore)

    print("🔍 Resultados da validação:")
    for tipo, valor in dados:
        if tipo == "CPF":
            validar_cpf(valor)
        elif tipo == "CNPJ":
            validar_cnpj(valor)
        elif tipo == "DATA":
            validar_data(valor)
        elif tipo == "EMAIL":
            validar_email(valor)
        elif tipo == "TELEFONE":
            validar_telefone(valor)
        else:
            print(f"❓ Tipo desconhecido: {tipo}")


if __name__ == "__main__":
    entrada = """
    validar {
        CPF: "123.456.789-09",
        CNPJ: "12.345.678/0001-95",
        EMAIL: "exemplo@teste.com",
        DATA: "31/12/2024",
        TELEFONE: "(61) 91234-5678"
    }
    """
    interpretar(entrada)
