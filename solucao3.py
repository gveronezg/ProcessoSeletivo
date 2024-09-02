import json

# Exemplo de faturamento em formato JSON
faturamento_json = '''
{
    "faturamento_diario": [0, 123.45, 400.0, 0, 234.56, 350.2, 0, 540.3, 700.0, 0, 0, 300.0, 0]
}
'''

# Carregar o JSON para obter os dados
faturamento = json.loads(faturamento_json)["faturamento_diario"]

# Filtrar os dias com faturamento (ignorar valores 0)
faturamento_filtrado = [valor for valor in faturamento if valor > 0]

# Calcular o menor, maior e a média
menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)
media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

# Dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")