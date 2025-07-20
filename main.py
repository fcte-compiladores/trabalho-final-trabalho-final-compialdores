import re

TOKENS_REGEX = {
    "CPF": r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$",
    "CNPJ": r"^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$",
    "DATA": r"^\d{2}/\d{2}/\d{4}$",
    "EMAIL": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "TELEFONE": r"^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$"
}

def limpar_numero(s):
    return re.sub(r'\D', '', s)

def validar_cpf(cpf):
    cpf_original = cpf
    cpf = limpar_numero(cpf)
    print(f"🔍 Analisando CPF: {cpf_original}")
    if len(cpf) != 11:
        print("❌ CPF deve conter 11 dígitos numéricos.")
        print("Resultado final: ❌ CPF inválido.")
        return False

    if cpf == cpf[0] * 11:
        print("❌ CPF com todos os dígitos iguais não é válido.")
        print("Resultado final: ❌ CPF inválido.")
        return False

    def calc_digito(cpf, digito):
        peso = list(range(digito+1, 1, -1))
        soma = sum(int(cpf[i]) * peso[i] for i in range(digito))
        return soma

    soma1 = calc_digito(cpf, 9)
    digito1_esperado = 0 if (soma1 * 10) % 11 == 10 else (soma1 * 10) % 11
    digito1_real = int(cpf[9])
    print(f"🔢 Soma1: {soma1}, Dígito esperado: {digito1_esperado}, Dígito real: {digito1_real}")
    if digito1_esperado != digito1_real:
        print("❌ Primeiro dígito verificador inválido.")
        print("Resultado final: ❌ CPF inválido.")
        return False

    soma2 = calc_digito(cpf, 10)
    digito2_esperado = 0 if (soma2 * 10) % 11 == 10 else (soma2 * 10) % 11
    digito2_real = int(cpf[10])
    print(f"🔢 Soma2: {soma2}, Dígito esperado: {digito2_esperado}, Dígito real: {digito2_real}")
    if digito2_esperado != digito2_real:
        print("❌ Segundo dígito verificador inválido.")
        print("Resultado final: ❌ CPF inválido.")
        return False

    print("✅ CPF válido.")
    print("Resultado final: ✅ CPF válido!")
    return True

def validar_cnpj(cnpj):
    cnpj_original = cnpj
    cnpj = limpar_numero(cnpj)
    print(f"🔍 Analisando CNPJ: {cnpj_original}")
    if len(cnpj) != 14:
        print("❌ CNPJ deve conter 14 dígitos numéricos.")
        print("Resultado final: ❌ CNPJ inválido.")
        return False
    if cnpj == cnpj[0] * 14:
        print("❌ CNPJ com todos os dígitos iguais não é válido.")
        print("Resultado final: ❌ CNPJ inválido.")
        return False

    pesos1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    pesos2 = [6] + pesos1

    soma1 = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    resto1 = soma1 % 11
    digito1_esperado = 0 if resto1 < 2 else 11 - resto1
    digito1_real = int(cnpj[12])
    print(f"🔢 Soma1: {soma1}, Dígito esperado: {digito1_esperado}, Dígito real: {digito1_real}")
    if digito1_esperado != digito1_real:
        print("❌ Primeiro dígito verificador inválido.")
        print("Resultado final: ❌ CNPJ inválido.")
        return False

    soma2 = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
    resto2 = soma2 % 11
    digito2_esperado = 0 if resto2 < 2 else 11 - resto2
    digito2_real = int(cnpj[13])
    print(f"🔢 Soma2: {soma2}, Dígito esperado: {digito2_esperado}, Dígito real: {digito2_real}")
    if digito2_esperado != digito2_real:
        print("❌ Segundo dígito verificador inválido.")
        print("Resultado final: ❌ CNPJ inválido.")
        return False

    print("✅ CNPJ válido.")
    print("Resultado final: ✅ CNPJ válido!")
    return True

def validar_data(data):
    print(f"🔍 Analisando Data: {data}")
    if not re.match(TOKENS_REGEX["DATA"], data):
        print("❌ Formato inválido para data. Use DD/MM/AAAA.")
        print("Resultado final: ❌ Data inválida.")
        return False

    dia, mes, ano = map(int, data.split("/"))
    if not (1 <= dia <= 31):
        print(f"❌ Dia inválido: {dia}. Deve estar entre 1 e 31.")
        print("Resultado final: ❌ Data inválida.")
        return False
    if not (1 <= mes <= 12):
        print(f"❌ Mês inválido: {mes}. Deve estar entre 1 e 12.")
        print("Resultado final: ❌ Data inválida.")
        return False
    if ano < 1900 or ano > 2100:
        print(f"❌ Ano inválido: {ano}. Deve estar entre 1900 e 2100.")
        print("Resultado final: ❌ Data inválida.")
        return False

    meses_30_dias = [4, 6, 9, 11]
    if mes in meses_30_dias and dia > 30:
        print(f"❌ Mês {mes} tem no máximo 30 dias.")
        print("Resultado final: ❌ Data inválida.")
        return False

    if mes == 2:
        if dia > 29:
            print("❌ Fevereiro tem no máximo 29 dias.")
            print("Resultado final: ❌ Data inválida.")
            return False
        if dia == 29:
            bissexto = (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))
            if not bissexto:
                print(f"❌ {ano} não é ano bissexto, fevereiro não pode ter 29 dias.")
                print("Resultado final: ❌ Data inválida.")
                return False

    print("✅ Data válida.")
    print("Resultado final: ✅ Data válida!")
    return True

def validar_email(email):
    print(f"🔍 Analisando Email: {email}")
    if not re.match(TOKENS_REGEX["EMAIL"], email):
        print("❌ Formato inválido para email.")
        print("Resultado final: ❌ Email inválido.")
        return False
    print("✅ Email com formato válido.")
    print("Resultado final: ✅ Email válido!")
    return True

def validar_telefone(telefone):
    print(f"🔍 Analisando Telefone: {telefone}")
    if not re.match(TOKENS_REGEX["TELEFONE"], telefone):
        print("❌ Formato inválido para telefone. Exemplo válido: (61) 91234-5678.")
        print("Resultado final: ❌ Telefone inválido.")
        return False
    print("✅ Telefone com formato válido.")
    print("Resultado final: ✅ Telefone válido!")
    return True

def main():
    opcoes = ["CPF", "CNPJ", "DATA", "EMAIL", "TELEFONE"]

    print("Tipos disponíveis para validação:")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i} - {opcao}")
    print("6 - Sair") 

    while True:
        escolha = input("\nDigite o número da opção desejada:").strip()
        if escolha == '6':  
            print("Encerrando o programa. Até mais!")
            break

        if not escolha.isdigit() or not (1 <= int(escolha) <= len(opcoes)):
            print("Opção inválida. Digite um número válido.")
            continue

        tipo = opcoes[int(escolha) - 1]
        valor = input(f"Digite o valor para validar ({tipo}): ").strip()

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
            

if __name__ == "__main__":
    main()
