import re

def format_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)  # remove qualquer caractere que não seja dígito
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

cpf = int(input("Digite seu Cpf: "))
print(format_cpf(cpf))  # saída: 123.456.789-09

# cpf = cpf.replace('.', '') 
#qual a função do replace? Substitui uma String por outra
def calcular_digito_verificador_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')  # Remova a pontuação
    cpf = [int(digito) for digito in cpf]  # Converta para lista de inteiros

    pesos = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_produtos = sum(digito * peso for digito, peso in zip(cpf, pesos))
    resto = soma_produtos % 11

    if resto < 2:
        return 0
    else:
        return 11 - resto

digito_verificador = calcular_digito_verificador_cpf(cpf)
print(f"O dígito de verificação é: {digito_verificador}")