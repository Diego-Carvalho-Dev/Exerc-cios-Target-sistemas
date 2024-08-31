import json

def analisa_faturamento(dados):
    faturamentos = [dado['valor'] for dado in dados if dado['valor'] > 0]
    if not faturamentos:
        return None, None, 0
    media = sum(faturamentos) / len(faturamentos)
    menor = min(faturamentos)
    maior = max(faturamentos)
    acima_media = sum(1 for valor in faturamentos if valor > media)
    return menor, maior, acima_media

# Assumindo que os dados estão em um arquivo JSON
with open('faturamento.json', 'r') as f:
    dados = json.load(f)
    menor, maior, dias_acima_media = analisa_faturamento(dados)
    print("Menor valor:", menor)
    print("Maior valor:", maior)
    print("Dias acima da média:", dias_acima_media)
