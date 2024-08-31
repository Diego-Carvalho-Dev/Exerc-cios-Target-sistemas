def calcula_percentuais(dados):
    total = sum(dados.values())
    percentuais = {estado: (valor / total) * 100 for estado, valor in dados.items()}
    return percentuais

# Dados de exemplo
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    # ...
}
percentuais = calcula_percentuais(faturamento_estados)
print(percentuais)
