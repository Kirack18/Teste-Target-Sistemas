import json

with open('dados.json', 'r') as file:
    faturamento = json.load(file)

faturamento_filtrado = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)

media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

dias_acima_da_media = len([valor for valor in faturamento_filtrado if valor > media_mensal])

print(f"Menor valor de faturamento ocorrido em um dia do mês: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento ocorrido em um dia do mês: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_da_media}")