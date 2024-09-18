INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(f"O valor final da variável SOMA é: {SOMA}")

def pertence_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or a == n

numero = int(input("Digite um número: "))
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

    import json

    dados_faturamento = '''
    [
        {"dia": 1, "valor": 200.0},
        {"dia": 2, "valor": 300.0},
        {"dia": 3, "valor": 0.0},
        {"dia": 4, "valor": 500.0},
        {"dia": 5, "valor": 0.0},
        {"dia": 6, "valor": 1000.0}
    ]
    '''

    # Carregar dados de faturamento do JSON
    faturamento = json.loads(dados_faturamento)

    # Filtrar apenas dias com faturamento
    faturamento_valido = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

    # Calcular menor, maior e média
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)

    # Número de dias com faturamento superior à média
    dias_acima_media = len([dia for dia in faturamento_valido if dia > media_mensal])


    #Percentual de faturamento por estado
    print(f"Menor faturamento: R${menor_faturamento}")
    print(f"Maior faturamento: R${maior_faturamento}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")

    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

faturamento_total = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
        percentual = (valor / faturamento_total) * 100
        print(f"{estado}: {percentual:.2f}% do faturamento total.")


#########percorre a string de trás para frente.
def inverter_string(s):
    string_invertida = ''
    for i in range(len(s)-1, -1, -1):
        string_invertida += s[i]
    return string_invertida

string_original = input("Digite uma string: ")
print(f"String invertida: {inverter_string(string_original)}")


